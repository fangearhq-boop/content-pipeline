"""Tests for compile-content-data.py tweet parsing — code-fence handling.

The module filename is hyphenated (not importable normally), so we load it by
path via importlib. Runs under pytest OR standalone: `python test_compile_content_data.py`.

Regression guard for the 2026-07-15 Cubs change where the drafting step began
wrapping each X post in a ``` fence under **Post N** labels. The label-parse
path passes raw text through, so without the fix the fence leaked into the
published tweet (and its extra chars could push a post over 280).
"""

import importlib.util
import os

_MOD_PATH = os.path.join(os.path.dirname(__file__), "compile-content-data.py")
_spec = importlib.util.spec_from_file_location("compile_content_data", _MOD_PATH)
ccd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ccd)


# ── _strip_code_fence unit cases ─────────────────────────────────────────

def test_strip_full_wrap():
    assert ccd._strip_code_fence("```\nHello world\n```") == "Hello world"

def test_strip_language_tagged_fence():
    assert ccd._strip_code_fence("```text\nHello world\n```") == "Hello world"

def test_strip_leading_only_fence():
    assert ccd._strip_code_fence("```\nHello world") == "Hello world"

def test_clean_text_untouched():
    clean = "6.0 WAR.\n\nThat's what PCA put up.\n\n#Cubs #GoCubs #MLB"
    assert ccd._strip_code_fence(clean) == clean

def test_empty_and_none():
    assert ccd._strip_code_fence("") == ""
    assert ccd._strip_code_fence(None) == ""


# ── End-to-end via parse_x_posts (the real bug path) ─────────────────────

# 2026-07-15 shape: **Post N** label + ``` fenced body + trailing [POSTING WINDOW].
X_MD_0715 = """# Cubs X Posts — 2026-07-15

### STORY 1: PCA All-Star Game — NL Shut Out 4-0

**Post 1**
```
1 hit out of the NL — and PCA had it.

AL shut out the NL 4-0. Crow-Armstrong entered in the 6th and singled in the 8th.

#Cubs #GoCubs #MLB
```
[POSTING WINDOW: 7:00 AM CT]

---
"""

# 2026-07-14 shape: STORY header + bare ``` block, [POSTING WINDOW] inside.
X_MD_0714 = """# X/Twitter Posts — 2026-07-14

### STORY 1A: Pete Crow-Armstrong — All-Star Tonight

```
[POSTING WINDOW: 7:00 AM CT]
6.0 WAR.

That's what Pete Crow-Armstrong put up in the FIRST HALF alone.

#Cubs #GoCubs #FlyTheW
```

---
"""


def _first_tweet(md):
    posts = ccd.parse_x_posts(md, brief_stories={})
    flat = [t for tweets in posts.values() for t in tweets]
    assert len(flat) == 1, f"expected 1 tweet, got {len(flat)}"
    return flat[0]


def test_0715_label_fence_is_stripped_end_to_end():
    t = _first_tweet(X_MD_0715)
    assert "```" not in t["text"], f"fence leaked: {t['text']!r}"
    assert t["text"].startswith("1 hit out of the NL")
    assert t["text"].endswith("#Cubs #GoCubs #MLB")
    assert t["posting_time"] == "7:00 AM CT"
    assert t["char_count"] == ccd.count_tweet_chars(t["text"])
    assert t["char_count"] <= 280

def test_0714_bare_block_still_clean_regression():
    t = _first_tweet(X_MD_0714)
    assert "```" not in t["text"]
    assert t["text"].startswith("6.0 WAR.")
    assert t["text"].endswith("#Cubs #GoCubs #FlyTheW")
    assert t["posting_time"] == "7:00 AM CT"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
        print(f"PASS  {fn.__name__}")
    print(f"\nAll {len(fns)} tests passed.")
