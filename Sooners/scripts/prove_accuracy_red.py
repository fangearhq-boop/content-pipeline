#!/usr/bin/env python3
"""Prove the Sooners brief guards go red.

Exits 0 only when each guard rejects a bad day. A guard that stays green is a
failure of this proof, not a pass.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

NICHE = Path(__file__).resolve().parents[1]
if str(NICHE) not in sys.path:
    sys.path.insert(0, str(NICHE))

from sooners_brief.contract import FACT_NAME, POSTS_NAME, verify_brief, verify_day  # noqa: E402

CLEAN_POSTS = """# Sooners X/Twitter Posts — 2026-10-26

### STORY 1: Sample

**Post 1** — 9:00 AM CT | Football morning recap

```
SEC WEEK.

Oklahoma won 23-15.

#Sooners #BoomerSooner
```

### STORY 2: Next

**Post 2** — 10:30 AM CT | Football next look

```
NEXT.

Saturday is the next one.

#Sooners #BoomerSooner
```

### STORY 3: Hoops

**Post 3** — 12:30 PM CT | Basketball

```
HOOPS.

Exhibition week in Norman.

#Sooners #BoomerSooner
```

### STORY 4: Recruiting

**Post 4** — 3:00 PM CT | Recruiting

```
RECRUITING.

Norman stays on the trail.

#Sooners #BoomerSooner
```

### STORY 5: Softball

**Post 5** — 6:00 PM CT | Softball

```
SOFTBALL.

The standard in Norman holds.

#Sooners #BoomerSooner
```

### STORY 6: Baseball

**Post 6** — 8:30 PM CT | Baseball

```
BASEBALL.

The slate is already public.

#Sooners #BoomerSooner
```
"""

CLEAN_FACTS = """# Sooners Fact-Check Log — 2026-10-26

**Verdict:** Acceptable for social

Acceptable for social

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Oklahoma won 23-15 | https://soonersports.com/news/sample | HIGH | VERIFIED |
"""


def expect_red(code: str, hold, label: str) -> str | None:
    if hold.ok or hold.code != code:
        return f"{label} did not go red as {code}: {hold.summary()}"
    print(f"RED {hold.code}: {hold.messages[0]}")
    return None


def main() -> int:
    failures = []

    missing = verify_brief(CLEAN_POSTS, None)
    failures.append(expect_red("missing_fact_check_log", missing, "missing log"))

    with tempfile.TemporaryDirectory() as tmp:
        day = Path(tmp) / "sooners-content-2026-10-26"
        day.mkdir()
        (day / POSTS_NAME).write_text(CLEAN_POSTS, encoding="utf-8")
        folder_hold = verify_day(day)
        failures.append(expect_red("missing_fact_check_log", folder_hold, "missing file"))

    unbacked_posts = CLEAN_POSTS.replace("Oklahoma won 23-15.", "Oklahoma won 99-1.")
    unbacked = verify_brief(unbacked_posts, CLEAN_FACTS)
    failures.append(expect_red("unbacked_number", unbacked, "unbacked number"))

    for host, sample in (
        ("mlb.com", "https://www.mlb.com/news/sample"),
        ("statsapi.mlb.com", "https://statsapi.mlb.com/api/v1/schedule"),
        ("baseball-reference.com", "https://www.baseball-reference.com/teams/OKL/2026.shtml"),
    ):
        facts = CLEAN_FACTS.replace("https://soonersports.com/news/sample", sample)
        hold = verify_brief(CLEAN_POSTS, facts)
        failures.append(expect_red("banned_host", hold, host))

    problems = [item for item in failures if item]
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    fired = sum(1 for item in failures if item is None)
    print(f"guards_fired={fired}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
