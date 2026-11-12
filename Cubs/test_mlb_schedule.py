"""Official-schedule conversion and the Oct 2026 time/venue regressions.

Run: python Cubs/test_mlb_schedule.py

These tests do not call the network. They use the Stats API gameDate values
confirmed for the games that shipped wrong.
"""

import importlib.util
import os
import sys
import tempfile

_MOD_PATH = os.path.join(os.path.dirname(__file__), "mlb_schedule.py")
_spec = importlib.util.spec_from_file_location("mlb_schedule", _MOD_PATH)
sched = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = sched
_spec.loader.exec_module(sched)


def _game(game_date, away, home, venue, game_pk, series="NL Division Series", number=2, tbd=False, abstract="Final"):
    return {
        "gamePk": game_pk,
        "gameDate": game_date,
        "seriesDescription": series,
        "seriesGameNumber": number,
        "venue": {"id": 1, "name": venue},
        "teams": {
            "away": {"team": {"id": 1, "name": away}},
            "home": {"team": {"id": 2, "name": home}},
        },
        "status": {
            "abstractGameState": abstract,
            "startTimeTBD": tbd,
        },
    }


def _payload(*games):
    return {"dates": [{"date": "2026-10-04", "games": list(games)}]}


# Confirmed from statsapi.mlb.com for 2026-10-04 and 2026-10-06.
OCT4 = _payload(
    _game(
        "2026-10-04T20:00:00Z",
        "San Diego Padres",
        "Milwaukee Brewers",
        "American Family Field",
        849825,
        number=2,
    ),
    _game(
        "2026-10-05T00:00:00Z",
        "Atlanta Braves",
        "Los Angeles Dodgers",
        "UNIQLO Field at Dodger Stadium",
        849826,
        number=2,
    ),
)
OCT6 = _payload(
    _game(
        "2026-10-07T01:30:00Z",
        "Milwaukee Brewers",
        "San Diego Padres",
        "Petco Park",
        849900,
        number=3,
    ),
    _game(
        "2026-10-06T22:00:00Z",
        "Los Angeles Dodgers",
        "Atlanta Braves",
        "Truist Park",
        849901,
        number=3,
    ),
)

OCT4_TWEET = (
    "Both Game 2s today — Brewers/Padres at 4:00 PM CT, Dodgers/Braves at 8:00 PM CT."
)
OCT4_TWEET_FIXED = (
    "Both Game 2s today — Brewers/Padres at 3:00 PM CT, Dodgers/Braves at 7:00 PM CT."
)
OCT6_TWEET = (
    "The team that swept us plays at our rival's house tonight.\n\n"
    "Padres vs. Brewers NLDS Game 3 at American Family Field, tonight on FOX."
)
OCT6_TWEET_FIXED = (
    "Brewers at Padres, NLDS Game 3, Petco Park, 8:30 PM CT."
)


def test_october_game_dates_are_central_daylight_not_the_eastern_listing():
    # 20:00Z is 3:00 PM CDT (UTC-5). A fixed UTC-6 conversion would say 2:00 PM.
    # CBS/Yahoo printed 4:00 PM, which is the Eastern clock.
    assert sched.format_ct("2026-10-04T20:00:00Z") == "3:00 PM CT"
    assert sched.format_ct("2026-10-04T20:00:00Z") != "4:00 PM CT"
    assert sched.format_ct("2026-10-05T00:00:00Z") == "7:00 PM CT"
    assert sched.format_ct("2026-10-05T00:00:00Z") != "8:00 PM CT"
    # The late game is still the evening of Oct 4 in Chicago, not Oct 5.
    local = sched.game_date_to_chicago("2026-10-05T00:00:00Z")
    assert local.strftime("%Y-%m-%d") == "2026-10-04"
    assert local.tzname() == "CDT"


def test_november_standard_time_is_not_a_fixed_five_hour_offset():
    # First Sunday of November 2026 is Nov 1, so Nov 4 is CST (UTC-6).
    # 01:00Z Nov 5 is 7:00 PM CST on Nov 4. UTC-5 would wrongly say 8:00 PM.
    assert sched.format_ct("2026-11-05T01:00:00Z") == "7:00 PM CT"
    local = sched.game_date_to_chicago("2026-11-05T01:00:00Z")
    assert local.strftime("%Y-%m-%d") == "2026-11-04"
    assert local.tzname() == "CST"


def test_spring_forward_uses_chicago_not_a_fixed_offset():
    # 2026-03-08 is the DST start. 18:05Z is 1:05 PM CDT, after the jump.
    assert sched.format_ct("2026-03-08T18:05:00Z") == "1:05 PM CT"
    assert sched.game_date_to_chicago("2026-03-08T18:05:00Z").tzname() == "CDT"
    # The night before is still CST: 01:05Z on March 8 is 7:05 PM on March 7.
    assert sched.format_ct("2026-03-08T01:05:00Z") == "7:05 PM CT"
    before = sched.game_date_to_chicago("2026-03-08T01:05:00Z")
    assert before.strftime("%Y-%m-%d") == "2026-03-07"
    assert before.tzname() == "CST"


def test_fractional_utc_game_date_and_naive_clock_rejected():
    assert sched.format_ct("2026-10-04T20:00:00.000Z") == "3:00 PM CT"
    try:
        sched.format_ct("2026-10-04T20:00:00")
    except ValueError as exc:
        assert "no timezone" in str(exc)
    else:
        raise AssertionError("naive gameDate was accepted")
    try:
        sched.format_ct("4:00 PM")
    except ValueError:
        pass
    else:
        raise AssertionError("a national-listing clock was accepted as a gameDate")


def test_payload_uses_venue_name_and_chicago_clock():
    games = sched.games_from_payload(OCT4)
    assert len(games) == 2
    brewers = games[0]
    assert brewers.first_pitch_ct == "3:00 PM CT"
    assert brewers.venue == "American Family Field"
    assert brewers.away == "San Diego Padres"
    assert brewers.home == "Milwaukee Brewers"
    dodgers = games[1]
    assert dodgers.first_pitch_ct == "7:00 PM CT"
    assert dodgers.venue == "UNIQLO Field at Dodger Stadium"


def test_dodger_stadium_alias_matches_official_venue_name():
    games = sched.games_from_payload(OCT4)
    issues = sched.check_items(
        [("03-social-posts-x.md", "Braves at Dodgers, 7:00 PM CT, Dodger Stadium.")],
        games,
    )
    assert issues == []


def test_oct4_published_times_are_rejected():
    games = sched.games_from_payload(OCT4)
    issues = sched.check_items([("03-social-posts-x.md", OCT4_TWEET)], games)
    text = "\n".join(issues)
    assert "4:00 PM CT" in text
    assert "3:00 PM CT" in text
    assert "American Family Field" in text
    assert "8:00 PM CT" in text
    assert "7:00 PM CT" in text
    assert "Dodger Stadium" in text
    assert "national listing" in text


def test_oct4_corrected_times_pass():
    games = sched.games_from_payload(OCT4)
    assert sched.check_items([("03-social-posts-x.md", OCT4_TWEET_FIXED)], games) == []


def test_quoting_the_bad_listing_next_to_the_official_clock_is_allowed():
    games = sched.games_from_payload(OCT4)
    same_sentence = (
        "CBS and Yahoo listed Padres at Brewers at 4:00 PM CT; "
        "the official gameDate is 3:00 PM CT at American Family Field."
    )
    assert sched.check_items([("01-research-notes.md", same_sentence)], games) == []
    # A sentence that only states the national clock is still the Oct 4 failure.
    wrong_only = "CBS and Yahoo listed Padres at Brewers, 4:00 PM CT."
    issues = sched.check_items([("01-research-notes.md", wrong_only)], games)
    assert len(issues) == 1
    assert "3:00 PM CT" in issues[0]


def test_two_sites_worth_of_eastern_time_still_fails_without_the_ct_clock():
    games = sched.games_from_payload(OCT4)
    note = "CBS Sports and Yahoo Sports both say Padres at Brewers, 4:00 PM ET."
    issues = sched.check_items([("01-research-notes.md", note)], games)
    assert len(issues) == 1
    assert "4:00 PM ET" in issues[0]
    assert "3:00 PM CT" in issues[0]


def test_oct6_wrong_park_is_rejected_and_petco_passes():
    games = sched.games_from_payload(OCT6)
    issues = sched.check_items([("03-social-posts-x.md", OCT6_TWEET)], games)
    assert len(issues) == 1
    assert "American Family Field" in issues[0]
    assert "Petco Park" in issues[0]
    assert "Milwaukee Brewers at San Diego Padres" in issues[0]
    assert sched.check_items([("03-social-posts-x.md", OCT6_TWEET_FIXED)], games) == []


def test_historical_wrigley_mention_on_a_day_the_cubs_are_idle_is_not_a_venue_claim():
    games = sched.games_from_payload(OCT6)
    text = "The Cubs watched October from home. Wrigley Field will be loud again in April."
    assert sched.check_items([("03-social-posts-x.md", text)], games) == []


def test_posting_slots_do_not_inherit_clubs_from_the_previous_line():
    games = sched.games_from_payload(OCT4)
    text = "\n".join([
        "Padres at Brewers tonight.",
        "- **Slot:** 7:00 AM CT",
        "Story 4 (NLDS Game 2 tonight) placed at 6:30 PM CT",
        "Moved the fan-engagement story (NLDS Game 1 tonight) to 6:30 PM CT — winning window.",
        "### STORY 4: NLDS Game 2 Tonight — Braves at Dodgers, 8:00 PM CT",
    ])
    issues = sched.check_items(
        [("02-story-analysis.md", text)], games, schedule_date="2026-10-04"
    )
    assert len(issues) == 1
    assert "8:00 PM CT" in issues[0]
    assert "7:00 AM" not in issues[0]
    assert "6:30 PM" not in issues[0]


def test_earlier_games_in_a_series_are_not_judged_as_today():
    games = sched.games_from_payload(OCT6)
    text = "\n".join([
        "### Brewers/Padres NLDS",
        "- **Schedule:**",
        "- Game 1: Oct 3 (Sat), 7:30 PM CT at American Family Field",
        "- Game 2: Oct 4 (Sun), 3:00 PM CT at American Family Field",
        "- **Game 3: Oct 6 (Tue, TONIGHT) at American Family Field, on FOX/FS1**",
    ])
    issues = sched.check_items(
        [("00-research.md", text)], games, schedule_date="2026-10-06"
    )
    assert len(issues) == 1
    assert "Petco Park" in issues[0]
    assert "7:30" not in issues[0]
    assert "3:00" not in issues[0]


def test_semicolon_splits_two_first_pitches_in_one_line():
    games = sched.games_from_payload(OCT4)
    line = "Braves @ Dodgers 8 PM CT; Padres @ Brewers 4 PM CT."
    issues = sched.check_items([("00-daily-brief.md", line)], games, schedule_date="2026-10-04")
    text = "\n".join(issues)
    assert "8:00 PM CT" in text
    assert "4:00 PM CT" in text
    assert "more than one official game" not in text


def test_posting_windows_are_not_first_pitches():
    games = sched.games_from_payload(OCT4)
    brief = "\n".join([
        "### STORY 1: Overnight recap",
        "- **Posting window:** 7:00 AM CT",
        "Finding: Story 4 placed in 6:30 PM CT evening slot.",
        "Brewers and Padres play at 3:00 PM CT. Braves at Dodgers, 7:00 PM CT.",
    ])
    assert sched.check_items([("00-daily-brief.md", brief)], games) == []


def test_tbd_start_cannot_be_filled_in_from_a_listing():
    payload = _payload(_game(
        "2026-10-04T20:00:00Z",
        "San Diego Padres",
        "Milwaukee Brewers",
        "American Family Field",
        1,
        tbd=True,
    ))
    games = sched.games_from_payload(payload)
    assert games[0].first_pitch_ct is None
    issues = sched.check_items(
        [("03-social-posts-x.md", "Padres at Brewers, 4:00 PM CT.")],
        games,
    )
    assert issues
    assert "TBD" in issues[0]


def test_white_sox_alias_does_not_bind_the_red_sox():
    payload = _payload(
        _game("2026-07-04T23:10:00Z", "Boston Red Sox", "New York Yankees", "Yankee Stadium", 1, series="Regular Season", number=1),
        _game("2026-07-04T23:10:00Z", "Chicago White Sox", "Chicago Cubs", "Wrigley Field", 2, series="Regular Season", number=1),
    )
    # Same UTC instant is fine for alias isolation; clocks are not the point.
    games = sched.games_from_payload(payload)
    issues = sched.check_items(
        [("03-social-posts-x.md", "White Sox at Wrigley Field, 6:10 PM CT.")],
        games,
    )
    # 23:10Z on July 4 is 6:10 PM CDT. Venue Wrigley matches the White Sox game.
    assert issues == []
    swapped = sched.check_items(
        [("03-social-posts-x.md", "White Sox at Yankee Stadium, 6:10 PM CT.")],
        games,
    )
    assert swapped
    assert "Wrigley Field" in swapped[0]


def test_content_folder_check_flags_oct4_without_network():
    games_payload = OCT4

    def fetch(_date):
        return games_payload

    with tempfile.TemporaryDirectory() as folder:
        with open(os.path.join(folder, "03-social-posts-x.md"), "w", encoding="utf-8") as handle:
            handle.write(OCT4_TWEET + "\n")
        report = sched.check_content_folder(folder, "2026-10-04", fetch=fetch)
    assert report["blocking"] is True
    assert "4:00 PM CT" in report["markdown"]
    assert "Result: FAIL" in report["markdown"]


def test_fetch_failure_blocks_only_when_a_schedule_claim_is_present():
    def fetch(_date):
        raise OSError("network down")

    with tempfile.TemporaryDirectory() as folder:
        with open(os.path.join(folder, "03-social-posts-x.md"), "w", encoding="utf-8") as handle:
            handle.write("Padres at Brewers, first pitch 4:00 PM CT.\n")
        blocked = sched.check_content_folder(folder, "2026-10-04", fetch=fetch)
        with open(os.path.join(folder, "03-social-posts-x.md"), "w", encoding="utf-8") as handle:
            handle.write("The rotation is gone. Hoyer is building from scratch.\n")
        clear = sched.check_content_folder(folder, "2026-10-04", fetch=fetch)
    assert blocked["blocking"] is True
    assert "secondary listing" in blocked["markdown"]
    assert clear["blocking"] is False


def test_content_data_post_text_is_checked_and_posting_time_is_not():
    payload = {
        "stories": [
            {
                "story_num": 1,
                "title": "NLDS Game 2",
                "angle": "Braves at Dodgers, 8:00 PM CT.",
                "posting_window": "7:00 AM CT",
                "x_posts": [
                    {
                        "text": "Braves at Dodgers, 7:00 PM CT.",
                        "posting_time": "6:30 PM CT",
                    }
                ],
            }
        ]
    }
    items = sched._items_from_content_data(payload)
    blob = "\n".join(text for _label, text in items)
    assert "posting_time" not in blob
    assert "6:30 PM CT" not in blob
    games = sched.games_from_payload(OCT4)
    issues = sched.check_items(items, games)
    assert any("8:00 PM CT" in issue for issue in issues)
    assert not any("6:30 PM CT" in issue for issue in issues)


def test_fact_check_log_includes_the_official_schedule_section():
    engine_scripts = os.path.join(os.path.dirname(__file__), "..", "_engine", "scripts")
    path = os.path.join(engine_scripts, "verify-facts.py")
    spec = importlib.util.spec_from_file_location("verify_facts", path)
    verify = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = verify
    spec.loader.exec_module(verify)
    log, count = verify.generate_fact_check_log(
        "October 04, 2026",
        "Chicago Cubs Fan HQ",
        {},
        [],
        [],
        {},
        "## Official MLB Schedule (2026-10-04)\n\n**Result: FAIL.**",
    )
    assert count == 0
    assert "## Official MLB Schedule (2026-10-04)" in log
    assert "**Result: FAIL.**" in log
    assert log.index("Official MLB Schedule") < log.index("Verification Priority Guide")


def main():
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print("PASS", test.__name__)
    print(f"{len(tests)} passed")


if __name__ == "__main__":
    main()
