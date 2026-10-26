"""Offline guards and one fixture day. Network stays in the dry-run."""

from __future__ import annotations

import subprocess
import sys
import unittest
from datetime import date, datetime
from pathlib import Path

NICHE = Path(__file__).resolve().parents[1]
if str(NICHE) not in sys.path:
    sys.path.insert(0, str(NICHE))

from sooners_brief.contract import (  # noqa: E402
    COLLEGE_SLOTS,
    host_class,
    numbers_in,
    verify_brief,
)
from sooners_brief.generate import build_drafts, render_day  # noqa: E402
from sooners_brief.sources import SourceItem  # noqa: E402

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
        self.assertEqual(numbers_in(drafts[3].text), [])
        self.assertIn("on3.com", drafts[3].url)
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
        self.assertIn("3:15 p.m. CT", posts)
        self.assertIn("Peyton Bowen", posts)
        self.assertIn("https://www.on3.com/", facts)
        self.assertNotIn("RECRUITING SLOT STAYS CLEAN", posts)
        self.assertNotIn("Not inventing", posts)

    def test_empty_day_stays_number_free(self):
        drafts = build_drafts({}, ON)
        self.assertEqual(len(drafts), 6)
        for draft in drafts:
            self.assertEqual(numbers_in(draft.text), [])
            self.assertIn("#Sooners", draft.text)
            self.assertNotIn("Not inventing", draft.text)
        posts, facts = render_day(ON, drafts)
        self.assertTrue(verify_brief(posts, facts).ok, verify_brief(posts, facts).summary())

    def test_mailbag_does_not_crowd_out_the_thorpe_note(self):
        bundle = fixture_bundle()
        mailbag = item(
            "recruiting",
            "OU mailbag: Predicting the rest of Oklahoma's schedule",
            "https://www.on3.com/teams/oklahoma-sooners/news/ou-mailbag/",
            "OU mailbag: Predicting the rest of Oklahoma's schedule. "
            "Every week, answers about all things OU athletics.",
            datetime(2026, 10, 26, 18, 0),
        )
        bundle["recruiting"] = [mailbag, *bundle["recruiting"]]
        drafts = build_drafts(bundle, ON)
        self.assertIn("PEYTON BOWEN", drafts[3].text)
        self.assertNotIn("mailbag", drafts[3].text.lower())

    def test_reused_news_url_does_not_repeat_the_number(self):
        bundle = fixture_bundle()
        history = [(date(2026, 10, 25), bundle["football"][0].url)]
        drafts = build_drafts(bundle, ON, history)
        self.assertNotIn("23-15", drafts[0].text)
        posts, facts = render_day(ON, drafts)
        self.assertTrue(verify_brief(posts, facts).ok, verify_brief(posts, facts).summary())

    def test_prove_accuracy_red_script(self):
        script = NICHE / "scripts" / "prove_accuracy_red.py"
        completed = subprocess.run([sys.executable, str(script)], check=False, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("RED missing_fact_check_log", completed.stdout)
        self.assertIn("RED unbacked_number", completed.stdout)
        self.assertIn("RED banned_host", completed.stdout)
        self.assertIn("guards_fired=6", completed.stdout)


if __name__ == "__main__":
    unittest.main()
