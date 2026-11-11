"""Tests for stories[].sources[] harvesting (story_sources.py + compiler wiring).

Offline only: every test builds a temporary content folder. Runs under pytest
OR standalone: `python test_story_sources.py`.

Contract (springs-daily PR #338 parenting ingest):
  stories[].sources = [{"name": str, "url": "http(s)://...", "official": bool}, ...]
Extra keys are allowed (ingest ignores them). URLs must come from the material;
nothing is invented. Evergreen stories may have an empty list.
"""

import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile
import unittest

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import story_sources as ss  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "compile_content_data", os.path.join(_HERE, "compile-content-data.py"))
ccd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ccd)


BRIEF = """# Daily Brief

### STORY 1: CPSC Recalls Nursing Pillows
- **Tier:** 1
- **Posting window:** 8:00 AM MT

### STORY 2: 10 Ways to Make Bedtime Easier
- **Tier:** 3
- **Posting window:** 12:00 PM MT

### STORY 3: AAP Flu Shot Guidance
- **Tier:** 2
- **Posting window:** 3:00 PM MT

## Publishing Schedule
| Time | Description | Type |
|------|-------------|------|
| 8:00 AM | Story 1 | X |
"""

# Mixed header styles on purpose ("## Story", "### STORY") as seen in Parenting.
RESEARCH = """# Research Notes

## Story 1: CPSC Recalls Nursing Pillows

**Sources:**
- Denver7: "Nursing pillows recalled" — https://www.denver7.com/news/nursing-pillows-recalled
- CPSC.gov recall listing: https://www.cpsc.gov/Recalls/2027/Kikea-Nursing-Pillows.
- CPSC.gov: Baby Brezza sterilizer recall (no URL captured)
- Duplicate: http://cpsc.gov/Recalls/2027/Kikea-Nursing-Pillows/

## Story 2: 10 Ways to Make Bedtime Easier

**Sources:**
- General parenting knowledge (no link)

### STORY 3: AAP Flu Shot Guidance

**Sources:**
- [AAP policy statement](https://publications.aap.org/pediatrics/article/doi/10.1542/peds.2026-078778)
- Pikes Peak Pediatrics clinic schedule [OFFICIAL]: https://www.pikespeakpeds.example.com/flu-clinic

## Appendix
- Unrelated link https://www.example.com/not-a-story-source
"""

ARTICLE_1 = """<article><header><h1>CPSC Recalls Nursing Pillows</h1></header>
<p>See the <a href="https://www.cpsc.gov/Recalls/2027/Kikea-Nursing-Pillows">CPSC recall notice</a>
and our <a href="https://springsdaily.com/events/this-weekend">weekend list</a>.</p>
<p>Also covered by <a href="https://www.koaa.com/news/pillows">KOAA</a>.</p>
</article>"""


class _FolderCase(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="story-sources-")
        os.makedirs(os.path.join(self.dir, "articles"))
        self._write("00-daily-brief.md", BRIEF)
        self._write("01-research-notes.md", RESEARCH)
        self._write("articles/article-01-cpsc-recalls-nursing-pillows.html", ARTICLE_1)

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def _write(self, rel, text):
        with open(os.path.join(self.dir, rel), "w", encoding="utf-8") as f:
            f.write(text)

    def harvest(self, **kw):
        return ss.harvest_story_sources(self.dir, ss.parse_host_list("springsdaily.com"), **kw)


class PayloadShapeTests(_FolderCase):
    def test_every_source_has_name_url_official(self):
        for num, sources in self.harvest().items():
            for s in sources:
                self.assertIsInstance(s["name"], str)
                self.assertTrue(s["name"].strip(), s)
                self.assertRegex(s["url"], r"^https?://")
                self.assertIsInstance(s["official"], bool)

    def test_extra_fields_are_plain_json(self):
        # Extra keys (found_in/title/publisher) are allowed and must serialize.
        json.dumps(self.harvest())

    def test_compiled_json_has_sources_list_on_every_story(self):
        brief_stories, schedule = ccd.parse_daily_brief(BRIEF)
        source_map = self.harvest()
        data = ccd.assemble_json({"platforms": ["x"]}, "2026-11-11", brief_stories, schedule,
                                 {}, {}, {}, {}, {}, {}, source_map)
        by_num = {s["story_num"]: s for s in data["stories"]}
        self.assertEqual(set(by_num), {1, 2, 3})
        for s in data["stories"]:
            self.assertIsInstance(s["sources"], list)
        self.assertTrue(by_num[1]["sources"])
        self.assertEqual(by_num[2]["sources"], [])

    def test_assemble_without_source_map_is_backward_compatible(self):
        brief_stories, schedule = ccd.parse_daily_brief(BRIEF)
        data = ccd.assemble_json({"platforms": ["x"]}, "2026-11-11", brief_stories, schedule,
                                 {}, {}, {}, {}, {})
        self.assertTrue(all(s["sources"] == [] for s in data["stories"]))


class OfficialPreferenceTests(_FolderCase):
    def test_official_first_then_news(self):
        s1 = self.harvest()[1]
        flags = [s["official"] for s in s1]
        self.assertEqual(flags, sorted(flags, reverse=True), s1)
        self.assertEqual(ss.host_of(s1[0]["url"]), "cpsc.gov")
        self.assertIn("denver7.com", [ss.host_of(s["url"]) for s in s1])

    def test_dedupe_by_url_merges_origins(self):
        s1 = self.harvest()[1]
        cpsc = [s for s in s1 if ss.host_of(s["url"]) == "cpsc.gov"]
        self.assertEqual(len(cpsc), 1, cpsc)
        self.assertIn("01-research-notes.md", cpsc[0]["found_in"])
        self.assertTrue(any(o.startswith("articles/") for o in cpsc[0]["found_in"]))

    def test_trailing_punctuation_trimmed_not_rewritten(self):
        urls = [s["url"] for s in self.harvest()[1]]
        self.assertIn("https://www.cpsc.gov/Recalls/2027/Kikea-Nursing-Pillows", urls)

    def test_official_host_rules(self):
        yes = ["https://www.cdc.gov/flu", "https://army.mil/x", "https://uccs.edu/a",
               "https://co.us/x", "https://www.d11.org/bond", "https://asd20.org",
               "https://www.elpasoco.com/x", "https://elpasocountyhealth.org/flu",
               "https://ppld.org", "https://www.csu.org/", "https://publications.aap.org/x",
               "https://www.healthychildren.org/x", "https://www.who.int/x",
               "https://coloradosprings.gov/news/x"]
        no = ["https://www.denver7.com/x", "https://gazette.com/x", "https://notd11.org/x",
              "https://d11.org.evil.com/x", "https://cpsc.gov.example.com/x"]
        for u in yes:
            self.assertTrue(ss.is_official_host(u), u)
        for u in no:
            self.assertFalse(ss.is_official_host(u), u)

    def test_official_marker_vouches_for_unlisted_host(self):
        s3 = self.harvest()[3]
        clinic = [s for s in s3 if "pikespeakpeds" in s["url"]][0]
        self.assertTrue(clinic["official"])
        self.assertNotIn("OFFICIAL", clinic["name"])

    def test_markdown_link_label_used_as_name(self):
        s3 = self.harvest()[3]
        aap = [s for s in s3 if "publications.aap.org" in s["url"]][0]
        self.assertEqual(aap["name"], "AAP policy statement")
        self.assertTrue(aap["official"])

    def test_cap(self):
        self.assertLessEqual(len(self.harvest(max_sources=2)[1]), 2)
        cands = [ss._make("https://news%d.example.com/a" % i, "", "", "", "x", False)
                 for i in range(20)]
        cands.append(ss._make("https://www.cpsc.gov/Recalls/a", "", "", "", "x", False))
        out = ss.rank_and_cap(cands, max_sources=5)
        self.assertEqual(len(out), 5)
        self.assertTrue(out[0]["official"])


class NeverInventTests(_FolderCase):
    def _all_material(self):
        text = ""
        for root, _, files in os.walk(self.dir):
            for f in files:
                with open(os.path.join(root, f), encoding="utf-8") as fh:
                    text += fh.read()
        return text

    def test_every_url_is_literally_in_the_material(self):
        material = self._all_material()
        for sources in self.harvest().values():
            for s in sources:
                self.assertIn(s["url"], material, s)

    def test_bare_domain_mention_produces_no_url(self):
        # "CPSC.gov: Baby Brezza ..." has no http(s) URL -> nothing for it.
        urls = [s["url"] for s in self.harvest()[1]]
        self.assertFalse(any("brezza" in u.lower() for u in urls))
        self.assertNotIn("https://cpsc.gov", urls)
        self.assertNotIn("https://www.cpsc.gov", urls)

    def test_no_material_no_sources(self):
        empty = tempfile.mkdtemp(prefix="story-sources-empty-")
        try:
            with open(os.path.join(empty, "01-research-notes.md"), "w", encoding="utf-8") as f:
                f.write("## Story 1: Recall\n\n**Sources:**\n- CPSC.gov recall listing\n- cdc.gov\n")
            self.assertTrue(all(v == [] for v in ss.harvest_story_sources(empty).values()))
        finally:
            shutil.rmtree(empty, ignore_errors=True)

    def test_evergreen_story_stays_empty(self):
        self.assertEqual(self.harvest().get(2, []), [])

    def test_self_links_excluded(self):
        for sources in self.harvest().values():
            for s in sources:
                self.assertNotIn("springsdaily.com", s["url"])

    def test_non_story_sections_not_attributed(self):
        for sources in self.harvest().values():
            for s in sources:
                self.assertNotIn("not-a-story-source", s["url"])


class ConfigTests(unittest.TestCase):
    def test_exclude_hosts_from_config(self):
        hosts = ss.exclude_hosts_from_config({
            "source_exclude_hosts": "springsdaily.com, www.other.example",
            "github_pages_url": "https://fangearhq-boop.github.io/cos-parenting",
        })
        self.assertEqual(hosts, {"springsdaily.com", "other.example", "fangearhq-boop.github.io"})

    def test_parenting_config_excludes_springsdaily(self):
        root = os.path.dirname(os.path.dirname(_HERE))
        cfg = ccd.load_niche_config(os.path.join(root, "Parenting"))
        self.assertIn("springsdaily.com", ss.exclude_hosts_from_config(cfg))

    def test_header_styles(self):
        text = ("## Story 1: a\nhttps://a.gov/1\n### STORY 2: b\nhttps://b.gov/2\n"
                "### Story 3 — c\nhttps://c.gov/3\n## STORY 4A: d\nhttps://d.gov/4\n")
        parts = ss.split_by_story(text)
        self.assertEqual(sorted(parts), [1, 2, 3, 4])
        for n, part in parts.items():
            self.assertEqual(len(re.findall(r"https://", part)), 1, (n, part))


if __name__ == "__main__":
    unittest.main(verbosity=2)
