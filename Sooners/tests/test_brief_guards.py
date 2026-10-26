"""Offline guards and one fixture day. Network stays in the dry-run."""

from __future__ import annotations

import io
import subprocess
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date, datetime
from http.client import IncompleteRead
from pathlib import Path

NICHE = Path(__file__).resolve().parents[1]
if str(NICHE) not in sys.path:
    sys.path.insert(0, str(NICHE))

from sooners_brief.contract import (  # noqa: E402
    COLLEGE_SLOTS,
    Hold,
    has_number,
    host_class,
    numbers_in,
    verify_brief,
    x_length,
)
from sooners_brief.generate import _fresh, build_drafts, recently_used, render_day  # noqa: E402
from sooners_brief.sources import (  # noqa: E402
    SourceFetchError,
    SourceItem,
    _parse_when,
    fetch_text,
    football_season_year,
    require_publishable_source,
)

ON = date(2026, 10, 26)
ROOT = NICHE.parent


def item(sport, title, url, text, published):
    return SourceItem(sport=sport, title=title, url=url, text=text, published=published)


def fixture_bundle():
    return {
        "football": [
            item(
                "football",
                "Heinecke Named SEC Defensive Player of the Week",
                "https://soonersports.com/news/2026/10/26/football-heinecke",
                "Heinecke Named SEC Defensive Player of the Week. "
                "University of Oklahoma linebacker Owen Heinecke was named the SEC "
                "Defensive Player of the Week after he recorded 10 tackles and forced "
                "a fumble in OU's 23-15 road win at Mississippi State on Saturday.",
                datetime(2026, 10, 26, 10, 49),
            )
        ],
        "basketball": [
            item(
                "womens-basketball",
                "Sooners Cruise to Exhibition Win Over Southern Nazarene",
                "https://soonersports.com/news/2026/10/25/womens-basketball-exhibition",
                "Sooners Cruise to Exhibition Win Over Southern Nazarene. "
                "Oklahoma scored on its first possession and never trailed as it "
                "defeated Southern Nazarene, 124-39, in an exhibition game Sunday "
                "afternoon at Lloyd Noble Center.",
                datetime(2026, 10, 25, 17, 13),
            )
        ],
        "softball": [
            item(
                "softball",
                "Patty Gasso Inducted to Oklahoma Women's Hall of Fame",
                "https://soonersports.com/news/2026/10/16/softball-patty-gasso",
                "Patty Gasso Inducted to Oklahoma Women's Hall of Fame. "
                "Oklahoma Softball head coach Patty Gasso was inducted to the "
                "Oklahoma Women's Hall of Fame as formally announced during an "
                "induction ceremony at the Skirvin Hilton Hotel in Oklahoma City "
                "Friday, Oct. 16.",
                datetime(2026, 10, 16, 18, 5),
            )
        ],
        "baseball": [
            item(
                "baseball",
                "Oklahoma Baseball Announces Complete 2027 Schedule",
                "https://soonersports.com/news/2026/10/21/baseball-2027-schedule",
                "Oklahoma Baseball Announces Complete 2027 Schedule. "
                "head coach Skip Johnson announced the team's full 2027 season "
                "schedule Wednesday, a slate consisting of 54 games, highlighted by "
                "27 home games at Kimrey Family Stadium.",
                datetime(2026, 10, 21, 13, 16),
            )
        ],
        "recruiting": [
            item(
                "recruiting",
                "Making the case for OU safety Peyton Bowen to be a Jim Thorpe Award finalist",
                "https://www.on3.com/teams/oklahoma-sooners/news/peyton-bowen-thorpe/",
                "Making the case for OU safety Peyton Bowen to be a Jim Thorpe Award "
                "finalist. Peyton Bowen has been so good for OU this season that he "
                "should be considered for one of college football's most prestigious "
                "individual awards.",
                datetime(2026, 10, 26, 11, 0),
            )
        ],
        "next_game": item(
            "football-schedule",
            "Oklahoma versus South Carolina",
            "https://soonersports.com/sports/football/schedule/2026",
            "Upcoming Event: Football versus South Carolina on October 31, 2026 at 3:15 p.m. CT",
            None,
        ),
    }


class GuardTests(unittest.TestCase):
    def test_allowlist_and_banned_hosts(self):
        self.assertEqual(host_class("https://www.espn.com/college-football/story/1"), "allow")
        self.assertEqual(host_class("https://www.soonersports.com/news/1"), "allow")
        self.assertEqual(host_class("https://www.on3.com/teams/oklahoma-sooners/feed/"), "allow")
        self.assertEqual(host_class("https://www.mlb.com/news/1"), "banned")
        self.assertEqual(host_class("https://statsapi.mlb.com/api/v1/schedule"), "banned")
        self.assertEqual(host_class("https://www.baseball-reference.com/teams/"), "banned")
        self.assertEqual(host_class("https://notespn.com/story"), "other")

    def test_denver_pairs_match_the_six_chicago_slots(self):
        self.assertEqual(
            [spec["ct"] for spec in COLLEGE_SLOTS],
            ["9:00 AM CT", "10:30 AM CT", "12:30 PM CT", "3:00 PM CT", "6:00 PM CT", "8:30 PM CT"],
        )
        self.assertEqual(
            [spec["denver"] for spec in COLLEGE_SLOTS],
            ["8:00 AM MT", "9:30 AM MT", "11:30 AM MT", "2:00 PM MT", "5:00 PM MT", "7:30 PM MT"],
        )

    def test_fixture_day_is_acceptable_for_social(self):
        drafts = build_drafts(fixture_bundle(), ON)
        posts, facts = render_day(ON, drafts)
        hold = verify_brief(posts, facts)
        self.assertTrue(hold.ok, hold.summary())
        self.assertIn("Acceptable for social", facts)
        for spec in COLLEGE_SLOTS:
            self.assertIn(spec["ct"], posts)
        self.assertIn("#Sooners", posts)
        self.assertNotIn("mlb.com", facts)
        self.assertNotIn("baseball-reference.com", facts)
        self.assertNotIn("statsapi.mlb.com", facts)
        self.assertIn("10 tackles", posts)
        self.assertIn("124-39", posts)
        self.assertIn("Never trailed", posts)
        self.assertIn("3:15 p.m. CT", posts)
        self.assertIn("Oklahoma City", posts)
        self.assertNotIn("plaque", posts.lower())
        self.assertNotIn("Peyton", posts)
        self.assertNotIn("Thorpe", posts)
        self.assertNotIn("Norman stays in the mix", posts)

    def test_empty_day_keeps_only_the_posting_date(self):
        drafts = build_drafts({}, ON)
        self.assertEqual(len(drafts), 6)
        for draft in drafts:
            self.assertEqual(numbers_in(draft.text), ["2026", "10", "26"])
            self.assertIn("#Sooners", draft.text)
            self.assertNotIn("Not inventing", draft.text)
        posts, facts = render_day(ON, drafts)
        self.assertTrue(verify_brief(posts, facts).ok, verify_brief(posts, facts).summary())

    def test_decommit_headline_and_spelled_number_are_not_posted(self):
        bundle = fixture_bundle()
        bundle["recruiting"] = [
            item(
                "recruiting",
                "Five-star decommits from Oklahoma",
                "https://www.on3.com/teams/oklahoma-sooners/news/five-star-decommits/",
                "Five-star decommits from Oklahoma. A five-star prospect is gone. Norman stays in the mix.",
                datetime(2026, 10, 26, 18, 0),
            )
        ]
        drafts = build_drafts(bundle, ON)
        text = drafts[3].text
        lowered = text.casefold()
        self.assertNotIn("decommit", lowered)
        self.assertNotIn("five", lowered)
        self.assertNotIn("norman stays in the mix", lowered)
        self.assertNotIn("peyton", lowered)
        self.assertNotIn("thorpe", lowered)
        self.assertIn("2026-10-26", text)
        posts, facts = render_day(ON, drafts)
        self.assertTrue(verify_brief(posts, facts).ok, verify_brief(posts, facts).summary())

    def test_reused_news_url_does_not_repeat_the_number(self):
        bundle = fixture_bundle()
        history = [(date(2026, 10, 25), bundle["football"][0].url)]
        drafts = build_drafts(bundle, ON, history)
        self.assertNotIn("23-15", drafts[0].text)
        posts, facts = render_day(ON, drafts)
        self.assertTrue(verify_brief(posts, facts).ok, verify_brief(posts, facts).summary())

    def test_reversed_exhibition_does_not_flip_the_winner(self):
        bundle = fixture_bundle()
        bundle["basketball"] = [
            item(
                "womens-basketball",
                "Texas exhibition",
                "https://soonersports.com/news/reversed",
                "Texas defeated Oklahoma, 80-70, in an exhibition and never trailed.",
                datetime(2026, 10, 26, 12, 0),
            )
        ]
        drafts = build_drafts(bundle, ON)
        self.assertNotIn("80-70", drafts[2].text)
        self.assertNotIn("defeated Oklahoma", drafts[2].text)
        self.assertNotIn("Never trailed", drafts[2].text)
        self.assertNotIn("Oklahoma defeated Oklahoma", drafts[2].text)

        bundle["basketball"] = [
            item(
                "mens-basketball",
                "Sooners exhibition",
                "https://soonersports.com/news/sooners-win",
                "The Sooners defeated Kansas, 90-80, in an exhibition. Kansas never trailed until late.",
                datetime(2026, 10, 26, 12, 0),
            )
        ]
        won = build_drafts(bundle, ON)
        self.assertIn("Sooners defeated Kansas 90-80", won[2].text)
        self.assertNotIn("Never trailed", won[2].text)

        bundle["basketball"] = [
            item(
                "mens-basketball",
                "Oklahoma State exhibition",
                "https://soonersports.com/news/okstate",
                "Oklahoma State defeated Texas, 81-70, in an exhibition.",
                datetime(2026, 10, 26, 12, 0),
            )
        ]
        state = build_drafts(bundle, ON)
        self.assertNotIn("81-70", state[2].text)
        self.assertNotIn("defeated Texas", state[2].text)

    def test_softball_city_is_copied_only_from_the_claim(self):
        bundle = fixture_bundle()
        bundle["softball"] = [
            item(
                "softball",
                "Patty Gasso Inducted to Oklahoma Women's Hall of Fame",
                "https://soonersports.com/news/gasso-no-city",
                "Patty Gasso was inducted to the Oklahoma Women's Hall of Fame on Friday, Oct. 16.",
                datetime(2026, 10, 16, 18, 5),
            )
        ]
        drafts = build_drafts(bundle, ON)
        self.assertIn("Oct. 16", drafts[4].text)
        self.assertNotIn("Oklahoma City", drafts[4].text)
        self.assertNotIn("plaque", drafts[4].text.lower())

    def test_kickoff_and_quiet_text_change_each_day(self):
        monday = build_drafts(fixture_bundle(), date(2026, 10, 26))
        tuesday = build_drafts(fixture_bundle(), date(2026, 10, 27))
        self.assertNotEqual(monday[1].text, tuesday[1].text)
        self.assertIn("3:15 p.m. CT", monday[1].text)
        self.assertIn("3:15 p.m. CT", tuesday[1].text)
        self.assertIn("2026-10-26", monday[1].text)
        self.assertIn("2026-10-27", tuesday[1].text)
        quiet_monday = build_drafts({}, date(2026, 10, 26))
        quiet_tuesday = build_drafts({}, date(2026, 10, 27))
        self.assertNotEqual(quiet_monday[0].text, quiet_tuesday[0].text)
        self.assertNotEqual(quiet_monday[3].text, quiet_tuesday[3].text)
        self.assertNotEqual(quiet_monday[0].text, quiet_monday[1].text)

    def test_freshness_window_and_unknown_timestamp(self):
        fresh = item("football", "t", "https://soonersports.com/a", "t", datetime(2026, 10, 22, 8, 0))
        stale = item("football", "t", "https://soonersports.com/b", "t", datetime(2026, 10, 21, 8, 0))
        unknown = item("football", "t", "https://soonersports.com/c", "t", None)
        self.assertTrue(_fresh(fresh, ON, "football"))
        self.assertFalse(_fresh(stale, ON, "football"))
        self.assertFalse(_fresh(unknown, ON, "football"))
        self.assertIsNotNone(_parse_when("2026-10-26T17:13:00.5Z"))
        self.assertIsNotNone(_parse_when("2026-10-26T17:13:00Z"))
        self.assertIsNotNone(_parse_when("2026-10-26T17:13:00.123456"))
        self.assertIsNone(_parse_when("not-a-timestamp"))
        parsed = item(
            "football",
            "t",
            "https://soonersports.com/d",
            "t",
            _parse_when("2026-10-26T17:13:00.5Z"),
        )
        self.assertTrue(_fresh(parsed, ON, "football"))

    def test_reuse_gap_boundary(self):
        url = "https://soonersports.com/news/boundary"
        self.assertTrue(recently_used([(date(2026, 10, 5), url)], url, ON))
        self.assertFalse(recently_used([(date(2026, 10, 4), url)], url, ON))
        self.assertFalse(recently_used([(ON, url)], url, ON))

    def test_clock_fragment_and_other_rows_do_not_back_a_number(self):
        self.assertFalse(has_number("Kickoff at 3:15 p.m. CT", "3"))
        self.assertFalse(has_number("Kickoff at 3:15 p.m. CT", "15"))
        self.assertTrue(has_number("Kickoff at 3:15 p.m. CT", "3:15"))
        self.assertEqual(numbers_in("Oklahoma vs South Carolina. October 31. 3:15 p.m. CT."), ["31", "3:15"])
        posts = """### STORY 1: A

**Post 1** — 9:00 AM CT | Football morning recap

```
TAKE 3.

#Sooners #BoomerSooner
```

### STORY 2: B

**Post 2** — 10:30 AM CT | Football next look

```
NEXT.

#Sooners #BoomerSooner
```

### STORY 3: C

**Post 3** — 12:30 PM CT | Basketball

```
HOOPS.

#Sooners #BoomerSooner
```

### STORY 4: D

**Post 4** — 3:00 PM CT | Recruiting

```
BOARD.

#Sooners #BoomerSooner
```

### STORY 5: E

**Post 5** — 6:00 PM CT | Softball

```
SOFTBALL.

#Sooners #BoomerSooner
```

### STORY 6: F

**Post 6** — 8:30 PM CT | Baseball

```
BASEBALL.

#Sooners #BoomerSooner
```
"""
        facts = """Acceptable for social

| Claim | Source | Confidence | Slot | Status |
|-------|--------|------------|------|--------|
| Kickoff at 3:15 p.m. CT | https://soonersports.com/schedule | HIGH | 10:30 AM CT | VERIFIED |
| 10 tackles | https://soonersports.com/news/hoops | HIGH | 12:30 PM CT | VERIFIED |
"""
        hold = verify_brief(posts, facts)
        self.assertFalse(hold.ok)
        self.assertEqual(hold.code, "unbacked_number")
        self.assertIn("9:00 AM CT number 3", hold.summary())

    def test_emoji_counts_as_two_characters(self):
        self.assertEqual(x_length("A"), 1)
        self.assertEqual(x_length("🏈"), 2)
        self.assertEqual(x_length("⚾"), 2)
        self.assertEqual(x_length("A" * 278 + "🏈"), 280)
        self.assertGreater(x_length("A" * 279 + "🏈"), 280)

    def test_schedule_year_follows_the_date(self):
        self.assertEqual(football_season_year(date(2026, 10, 26)), 2026)
        self.assertEqual(football_season_year(date(2027, 1, 15)), 2026)
        self.assertEqual(football_season_year(date(2027, 8, 1)), 2027)

    def test_fetch_retries_and_empty_bundle_fails(self):
        sleeps = []
        calls = {"n": 0}

        class Body:
            def read(self):
                return b"ok"

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

        def opener(request, timeout):
            calls["n"] += 1
            if calls["n"] < 3:
                raise IncompleteRead(b"partial")
            return Body()

        text = fetch_text("https://soonersports.com/x", opener=opener, sleeper=sleeps.append)
        self.assertEqual(text, "ok")
        self.assertEqual(calls["n"], 3)
        self.assertEqual(sleeps, [1, 2])

        def always_fail(request, timeout):
            raise IncompleteRead(b"partial")

        with self.assertLogs("sooners_brief.sources", level="WARNING") as logs:
            with self.assertRaises(SourceFetchError):
                fetch_text("https://soonersports.com/down", opener=always_fail, sleeper=lambda _seconds: None, attempts=3)
        self.assertTrue(any("attempt 3/3" in line for line in logs.output))

        with self.assertRaises(SourceFetchError):
            require_publishable_source(
                {
                    "football": [],
                    "basketball": [],
                    "softball": [],
                    "baseball": [],
                    "recruiting": [item("recruiting", "t", "https://www.on3.com/x", "t", None)],
                    "next_game": None,
                }
            )

    def test_dry_run_prints_the_hold_from_verify_brief(self):
        import generate_daily

        real = generate_daily.verify_brief

        def wrapped(posts, facts):
            hold = real(posts, facts)
            return Hold(hold.ok, hold.code, ["from-the-check"])

        generate_daily.verify_brief = wrapped
        try:
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                code = generate_daily.run(ON, True, loader=lambda _on_date: fixture_bundle())
        finally:
            generate_daily.verify_brief = real
        self.assertEqual(code, 0)
        self.assertIn("from-the-check", stdout.getvalue())

        def explode(_on_date):
            raise SourceFetchError("every Sooners source came back empty")

        stderr = io.StringIO()
        with redirect_stderr(stderr):
            failed = generate_daily.run(ON, True, loader=explode)
        self.assertEqual(failed, 1)
        self.assertIn("every Sooners source came back empty", stderr.getvalue())

    def test_workflows_keep_the_review_guards(self):
        daily = (ROOT / ".github/workflows/sooners-daily.yml").read_text(encoding="utf-8")
        ci = (ROOT / ".github/workflows/sooners-brief-ci.yml").read_text(encoding="utf-8")
        self.assertIn("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", daily)
        self.assertIn('"$hour" != "07"', daily)
        self.assertIn('"$hour" != "08"', daily)
        self.assertIn("paths:", ci)
        self.assertIn("Sooners/**", ci)
        self.assertIn("branches:", ci)
        self.assertIn("- main", ci)
        self.assertNotRegex(ci, r"^on:\n\s+push:\n\s*$")

    def test_prove_accuracy_red_script(self):
        script = NICHE / "scripts" / "prove_accuracy_red.py"
        completed = subprocess.run([sys.executable, str(script)], check=False, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("RED missing_fact_check_log", completed.stdout)
        self.assertIn("RED unbacked_number", completed.stdout)
        self.assertIn("RED banned_host", completed.stdout)
        self.assertIn("RED unlisted_host", completed.stdout)
        self.assertIn("RED too_long", completed.stdout)
        self.assertIn("RED freshness_window", completed.stdout)
        self.assertIn("RED reuse_boundary", completed.stdout)
        self.assertIn("RED reversed_result", completed.stdout)
        self.assertIn("RED empty_fetch", completed.stdout)
        self.assertIn("guards_fired=", completed.stdout)


if __name__ == "__main__":
    unittest.main()
