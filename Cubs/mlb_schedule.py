#!/usr/bin/env python3
"""Official MLB first-pitch times and ballparks for the Cubs brief.

Stats API ``gameDate`` is UTC. Convert it with ``zoneinfo`` ``America/Chicago``
so daylight time and standard time both come out right. Do not take a clock
off CBS, Yahoo, ESPN, Fox, or a TV listing and append "CT".

Research:

    python Cubs/mlb_schedule.py --date YYYY-MM-DD

Fact-check (also invoked by ``verify-facts.py`` for the Cubs niche):

    python Cubs/mlb_schedule.py --date YYYY-MM-DD --check Cubs/cubs-content-YYYY-MM-DD

Exit 2 means the brief or a post disagrees with the official schedule.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

CHICAGO = ZoneInfo("America/Chicago")
UTC = ZoneInfo("UTC")

SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"
BOXSCORE_URL = "https://statsapi.mlb.com/api/v1/game/{game_pk}/boxscore"

# Publishable copy. The fact-check log and the dashboard quote this copy;
# scanning them would flag the record of a bad claim instead of the claim.
PUBLISHABLE_FILES = (
    "00-daily-brief.md",
    "00-research.md",
    "01-research-notes.md",
    "02-story-analysis.md",
    "03-social-posts-x.md",
    "04-social-posts-facebook.md",
)

CENTRAL_ZONES = {"CT", "CDT", "CST"}
CLOCK_RE = re.compile(
    r"\b(?P<hour>\d{1,2})(?::(?P<minute>\d{2}))?\s*"
    r"(?P<ampm>a\.?m\.?|p\.?m\.?)\s*"
    r"(?P<zone>ET|CT|MT|PT|EST|CST|MST|PST|EDT|CDT|MDT|PDT)\b",
    re.IGNORECASE,
)
VENUE_RE = re.compile(
    r"\b([A-Z][\w'’.\-]*(?:\s+[A-Z][\w'’.\-]*){0,6}\s"
    r"(?:Field|Park|Stadium|Coliseum|Centre|Center))\b"
)
POSTING_PREFIX_RE = re.compile(
    r"(?:posting[_\s-]*window|posting[_\s-]*time|evening slot|posting slot|"
    r"\bslot\s*:|placed in|placed at|tweet posts at|posts at)\W*$",
    re.IGNORECASE,
)
POSTING_SUFFIX_RE = re.compile(r"^\s*(?:[—–-]\s*)?\(?\s*(?:slot|window)\b", re.IGNORECASE)
MONTH_DAY_RE = re.compile(
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|"
    r"Dec(?:ember)?)\.?\s+(\d{1,2})\b",
    re.IGNORECASE,
)
MONTH_NUMBERS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}
START_SIGNAL_RE = re.compile(r"\bfirst pitch\b|\bGame\s+\d\b", re.IGNORECASE)
SKIP_ABSTRACT = {"Postponed", "Cancelled"}


@dataclass(frozen=True)
class OfficialGame:
    game_pk: int | None
    game_date_utc: str
    first_pitch_ct: str | None
    venue: str
    away: str
    home: str
    series: str
    series_game_number: int | None
    start_note: str | None
    aliases: tuple[str, ...]

    def matchup(self) -> str:
        return f"{self.away} at {self.home}"

    def summary(self) -> str:
        series = self.series or "Game"
        if self.series_game_number:
            series = f"{series} Game {self.series_game_number}"
        when = self.first_pitch_ct or self.start_note or "time unavailable"
        pk = f"gamePk {self.game_pk}" if self.game_pk else "gamePk unknown"
        return (
            f"{self.matchup()} — {series} — {when} — {self.venue} — "
            f"gameDate {self.game_date_utc} — {pk}"
        )


def parse_utc_game_date(game_date: str) -> datetime:
    """Parse a Stats API gameDate. Naive clocks are rejected.

    There is no helper that stamps CT onto a bare "4:00 PM". That is the
    failure mode this module exists to prevent.
    """
    text = (game_date or "").strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"Unparseable gameDate {game_date!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError(
            f"gameDate {game_date!r} has no timezone. The Stats API value is UTC. "
            "Refusing to guess a zone or label a national-listing clock as CT."
        )
    return parsed.astimezone(UTC)


def game_date_to_chicago(game_date: str) -> datetime:
    """UTC gameDate → aware America/Chicago datetime. DST follows the IANA zone."""
    return parse_utc_game_date(game_date).astimezone(CHICAGO)


def format_ct(game_date: str) -> str:
    """'3:00 PM CT'. The zone label is always CT; the offset comes from Chicago."""
    local = game_date_to_chicago(game_date)
    raw = local.strftime("%I:%M %p")
    clock = raw[1:] if raw.startswith("0") else raw
    return f"{clock} CT"


def clock_only(ct_label: str | None) -> str | None:
    if not ct_label:
        return None
    return ct_label[: -len(" CT")] if ct_label.endswith(" CT") else ct_label


def team_aliases(team_name: str) -> tuple[str, ...]:
    parts = (team_name or "").split()
    if not parts:
        return ()
    # Bare "Sox" matches both Red Sox and White Sox. Require the city word.
    if parts[-1] == "Sox" and len(parts) >= 2:
        aliases = [f"{parts[-2]} {parts[-1]}"]
    else:
        aliases = [parts[-1]]
        if parts[-1] == "Jays" and len(parts) >= 2:
            aliases.append(f"{parts[-2]} {parts[-1]}")
    if parts[-1] == "Diamondbacks":
        aliases.extend(["D-backs", "Dbacks"])
    ordered = sorted(set(aliases), key=len, reverse=True)
    return tuple(ordered)


def official_game_from_api(raw: dict) -> OfficialGame | None:
    if not isinstance(raw, dict):
        return None
    game_date = raw.get("gameDate")
    if not game_date:
        return None
    teams = raw.get("teams") or {}
    away = ((teams.get("away") or {}).get("team") or {}).get("name") or ""
    home = ((teams.get("home") or {}).get("team") or {}).get("name") or ""
    if not away or not home:
        return None
    status = raw.get("status") or {}
    abstract = status.get("abstractGameState") or ""
    tbd = bool(status.get("startTimeTBD"))
    start_note = None
    first_pitch = None
    if tbd:
        start_note = "first pitch TBD — do not publish a clock time"
    elif abstract in SKIP_ABSTRACT:
        start_note = f"{abstract} — do not publish a clock time"
    else:
        first_pitch = format_ct(game_date)
    venue = ((raw.get("venue") or {}).get("name")) or ""
    aliases: list[str] = []
    for name in (away, home):
        aliases.extend(team_aliases(name))
    series_number = raw.get("seriesGameNumber")
    try:
        series_number = int(series_number) if series_number is not None else None
    except (TypeError, ValueError):
        series_number = None
    game_pk = raw.get("gamePk")
    try:
        game_pk = int(game_pk) if game_pk is not None else None
    except (TypeError, ValueError):
        game_pk = None
    return OfficialGame(
        game_pk=game_pk,
        game_date_utc=str(game_date),
        first_pitch_ct=first_pitch,
        venue=venue,
        away=away,
        home=home,
        series=raw.get("seriesDescription") or "",
        series_game_number=series_number,
        start_note=start_note,
        aliases=tuple(dict.fromkeys(aliases)),
    )


def games_from_payload(payload: dict) -> list[OfficialGame]:
    if not isinstance(payload, dict):
        raise ValueError("schedule payload was not a JSON object")
    games: list[OfficialGame] = []
    for date_block in payload.get("dates") or []:
        if not isinstance(date_block, dict):
            continue
        for raw in date_block.get("games") or []:
            game = official_game_from_api(raw)
            if game:
                games.append(game)
    games.sort(key=lambda game: game.game_date_utc)
    return games


def fetch_schedule_payload(date_str: str, timeout: float = 20.0) -> dict:
    """GET the public Stats API schedule. No auth, no posting."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str or ""):
        raise ValueError(f"date must be YYYY-MM-DD, got {date_str!r}")
    url = f"{SCHEDULE_URL}?sportId=1&date={date_str}&hydrate=team,venue"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "CubsContentPipeline/1.0 (schedule check)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise OSError(f"Stats API request failed: {exc}") from exc
    return json.loads(body)


def _line_start(text: str, index: int) -> int:
    return text.rfind("\n", 0, index) + 1


def _line_end(text: str, index: int) -> int:
    end = text.find("\n", index)
    return len(text) if end < 0 else end


def is_posting_clock(text: str, match_start: int, match_end: int) -> bool:
    """True for a posting-window clock, not a first pitch."""
    line_start = _line_start(text, match_start)
    prefix = text[max(line_start, match_start - 60):match_start]
    if POSTING_PREFIX_RE.search(prefix):
        return True
    suffix = text[match_end:_line_end(text, match_end)]
    if POSTING_SUFFIX_RE.search(suffix[:32]):
        return True
    line = text[line_start:_line_end(text, match_start)]
    # "moved Story 5 to 6:30 PM CT — in the winning window"
    if re.search(r"\bto\s+$", prefix) and re.search(r"\b(window|slot|posting)\b", line, re.IGNORECASE):
        return True
    return False


def _month_days(sentence: str) -> list[tuple[int, int]]:
    found = []
    for match in MONTH_DAY_RE.finditer(sentence):
        month = MONTH_NUMBERS[match.group(0)[:3].lower()]
        found.append((month, int(match.group(1))))
    for match in re.finditer(r"\b(\d{4})-(\d{2})-(\d{2})\b", sentence):
        found.append((int(match.group(2)), int(match.group(3))))
    return found


def _about_some_other_day(sentence: str, schedule_date: str | None) -> bool:
    """True when the sentence names a calendar day and it is not ``schedule_date``.

    Series recaps list Game 1's real first pitch on a later morning. That clock
    is not a claim about today's official slate.
    """
    if not schedule_date:
        return False
    month, day = (int(part) for part in schedule_date.split("-")[1:])
    found = _month_days(sentence)
    if not found:
        return False
    return not any(item == (month, day) for item in found)


def _sentence_span(text: str, index: int) -> tuple[int, int]:
    start = 0
    for cursor in range(index, -1, -1):
        if text[cursor] in ".!?\n":
            start = cursor + 1
            break
    end = len(text)
    for cursor in range(index, len(text)):
        if text[cursor] in ".!?\n":
            end = cursor + 1
            break
    return start, end


def _find_games(window: str, games: list[OfficialGame]) -> list[OfficialGame]:
    """Team nicknames in ``window``, longest alias first so 'Blue Jays' wins over 'Jays'."""
    aliases: list[tuple[str, int]] = []
    for index, game in enumerate(games):
        for alias in game.aliases:
            aliases.append((alias, index))
    aliases.sort(key=lambda item: len(item[0]), reverse=True)
    masked = window
    hits: list[int] = []
    for alias, index in aliases:
        pattern = re.compile(rf"\b{re.escape(alias)}\b")
        if pattern.search(masked):
            if index not in hits:
                hits.append(index)
            masked = pattern.sub(" " * len(alias), masked)
    return [games[index] for index in hits]


def _bind_game(hits: list[OfficialGame]) -> OfficialGame | None:
    if not hits:
        return None
    if len(hits) == 1:
        return hits[0]
    # Prefer the game whose two clubs both appear when the window named a pair
    # plus a stray nickname. ``hits`` is already the games touched; if more
    # than one game was touched, the caller treats it as ambiguous.
    return None


def _normalize_clock(match: re.Match) -> str | None:
    hour = int(match.group("hour"))
    minute = int(match.group("minute") or "0")
    if not (1 <= hour <= 12 and 0 <= minute <= 59):
        return None
    ampm = re.sub(r"[^A-Za-z]", "", match.group("ampm")).upper()
    if ampm not in {"AM", "PM"}:
        return None
    return f"{hour}:{minute:02d} {ampm}"


def _zone(match: re.Match) -> str:
    zone = match.group("zone").upper()
    if zone in {"EST", "EDT"}:
        return "ET"
    if zone in {"PST", "PDT"}:
        return "PT"
    if zone in {"MST", "MDT"}:
        return "MT"
    return zone


def _official_times(games: list[OfficialGame]) -> str:
    clocks = [game.first_pitch_ct for game in games if game.first_pitch_ct]
    if not clocks:
        notes = [f"{game.matchup()} ({game.start_note})" for game in games if game.start_note]
        return "; ".join(notes) if notes else "none on the official schedule"
    return "; ".join(clocks)


def check_items(
    items: list[tuple[str, str]],
    games: list[OfficialGame],
    schedule_date: str | None = None,
) -> list[str]:
    """Compare publishable copy to official games. Returns blocking issue strings."""
    issues: list[str] = []
    seen: set[str] = set()

    def add(issue: str) -> None:
        if issue not in seen:
            seen.add(issue)
            issues.append(issue)

    for label, text in items:
        previous_clock_end = 0
        for match in CLOCK_RE.finditer(text):
            if is_posting_clock(text, match.start(), match.end()):
                previous_clock_end = match.end()
                continue
            claimed = _normalize_clock(match)
            if not claimed:
                previous_clock_end = match.end()
                continue
            zone = _zone(match)
            sentence_start, sentence_end = _sentence_span(text, match.start())
            sentence = text[sentence_start:sentence_end]
            if _about_some_other_day(sentence, schedule_date):
                previous_clock_end = match.end()
                continue
            # Stay on this line so a posting slot does not inherit the previous
            # paragraph's club names. Also stop at the previous clock.
            left = max(previous_clock_end, _line_start(text, match.start()), match.start() - 80)
            # Teams usually precede the clock ("Padres at Brewers, 7:30 PM CT").
            # A comma right after the clock starts the next game's clause
            # ("4:00 PM CT, Dodgers/Braves at 8:00 PM CT") and must not bind both.
            after = text[match.end():match.end() + 48]
            if after.lstrip()[:1] in ",;":
                after = ""
            else:
                after = re.split(r"[,.;\n]", after, maxsplit=1)[0]
            window = text[left:match.start()] + " " + after
            hits = _find_games(window, games)
            bound = _bind_game(hits)
            signal = bool(START_SIGNAL_RE.search(window)) or bool(hits)
            claimed_label = f"{claimed} {zone}"

            if not signal:
                previous_clock_end = match.end()
                continue

            if len(hits) > 1 and bound is None:
                names = "; ".join(game.summary() for game in hits)
                add(
                    f"{label}: {claimed_label} sits next to more than one official game "
                    f"({names}). Split them and use each game's own first pitch."
                )
                previous_clock_end = match.end()
                continue

            if zone not in CENTRAL_ZONES:
                official = bound.first_pitch_ct if bound else None
                if official and official in sentence:
                    previous_clock_end = match.end()
                    continue
                if bound:
                    add(
                        f"{label}: {claimed_label} is a national-listing zone, not Central. "
                        f"Official first pitch for {bound.matchup()} is {bound.first_pitch_ct} "
                        f"at {bound.venue} (gameDate {bound.game_date_utc}, "
                        f"gamePk {bound.game_pk})."
                    )
                else:
                    add(
                        f"{label}: {claimed_label} is not Central. Publish the America/Chicago "
                        f"clock from the Stats API. Official times: {_official_times(games)}."
                    )
                previous_clock_end = match.end()
                continue

            if bound is None:
                official_clocks = {clock_only(game.first_pitch_ct) for game in games}
                if claimed not in official_clocks:
                    add(
                        f"{label}: {claimed_label} is not an official first pitch. "
                        f"Official times: {_official_times(games)}."
                    )
                previous_clock_end = match.end()
                continue

            if bound.first_pitch_ct is None:
                if bound.start_note and bound.start_note in sentence:
                    previous_clock_end = match.end()
                    continue
                add(
                    f"{label}: {claimed_label} is not a publishable first pitch for "
                    f"{bound.matchup()}. Official schedule: {bound.start_note} "
                    f"(gameDate {bound.game_date_utc}, gamePk {bound.game_pk})."
                )
                previous_clock_end = match.end()
                continue

            official_clock = clock_only(bound.first_pitch_ct)
            if claimed != official_clock:
                if bound.first_pitch_ct and bound.first_pitch_ct in sentence:
                    previous_clock_end = match.end()
                    continue
                add(
                    f"{label}: {claimed_label} is not the first pitch for {bound.matchup()}. "
                    f"Official: {bound.first_pitch_ct} at {bound.venue} "
                    f"(gameDate {bound.game_date_utc}, gamePk {bound.game_pk}). "
                    f"Do not relabel a national listing as CT."
                )
            previous_clock_end = match.end()

        for match in VENUE_RE.finditer(text):
            mentioned = match.group(1)
            span = _sentence_span(text, match.start())
            sentence = text[span[0]:span[1]]
            if _about_some_other_day(sentence, schedule_date):
                continue
            line = text[_line_start(text, match.start()):_line_end(text, match.start())]
            hits = _find_games(line, games)
            if len(hits) != 1:
                # "Game 3 at American Family Field" often sits under a
                # "Brewers/Padres" header rather than repeating the clubs.
                section_at = text.rfind("\n###", 0, match.start())
                left = section_at if section_at >= 0 else max(0, match.start() - 400)
                left = max(left, match.start() - 500)
                hits = _find_games(text[left:match.end() + 40], games)
            bound = _bind_game(hits)
            if bound is None:
                continue
            if not bound.venue:
                continue
            if _venue_matches(mentioned, bound.venue):
                continue
            if bound.venue in sentence:
                continue
            add(
                f"{label}: {mentioned} is not the ballpark for {bound.matchup()}. "
                f"Official venue: {bound.venue} "
                f"(gameDate {bound.game_date_utc}, gamePk {bound.game_pk})."
            )
    return issues


def _venue_matches(mentioned: str, official: str) -> bool:
    left = mentioned.casefold()
    right = official.casefold()
    return left == right or left in right or right in left


def schedule_claims_present(items: list[tuple[str, str]]) -> bool:
    for _label, text in items:
        for match in CLOCK_RE.finditer(text):
            if is_posting_clock(text, match.start(), match.end()):
                continue
            window = text[max(0, match.start() - 80):match.end() + 24]
            if START_SIGNAL_RE.search(window) or CLOCK_RE.search(window):
                # A zoned clock that is not a posting slot can be a first pitch.
                # Team binding happens after the schedule is known; until then,
                # treat it as a claim so a failed fetch cannot be skipped.
                return True
        if VENUE_RE.search(text):
            return True
    return False


def load_publishable_items(content_folder: str) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for name in PUBLISHABLE_FILES:
        path = os.path.join(content_folder, name)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        if text.strip():
            items.append((name, text))
    articles = os.path.join(content_folder, "articles")
    if os.path.isdir(articles):
        for name in sorted(os.listdir(articles)):
            if not name.endswith(".html"):
                continue
            path = os.path.join(articles, name)
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            if text.strip():
                items.append((f"articles/{name}", text))
    data_path = os.path.join(content_folder, "07-content-data.json")
    if os.path.isfile(data_path):
        with open(data_path, encoding="utf-8") as handle:
            payload = json.load(handle)
        items.extend(_items_from_content_data(payload))
    return items


def _items_from_content_data(payload: dict) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    if not isinstance(payload, dict):
        return items
    for story in payload.get("stories") or []:
        if not isinstance(story, dict):
            continue
        number = story.get("story_num", "?")
        for field in ("title", "angle"):
            value = story.get(field)
            if isinstance(value, str) and value.strip():
                items.append((f"07-content-data.json story {number} {field}", value))
        for post in story.get("x_posts") or []:
            if isinstance(post, dict) and isinstance(post.get("text"), str):
                items.append((f"07-content-data.json story {number} post", post["text"]))
    return items


def render_report(
    date_str: str,
    games: list[OfficialGame],
    issues: list[str],
    fetch_error: str | None,
    claims_present: bool,
) -> dict:
    lines = [
        f"## Official MLB Schedule ({date_str})",
        "",
        "First pitch is the Stats API `gameDate` (UTC) converted to America/Chicago. "
        "The ballpark is `venue.name` on that same game. CBS, Yahoo, ESPN, Fox, and TV "
        "listings are not sources for a time, a ballpark, or a game stat, even when two "
        "of them agree. Box score: `https://statsapi.mlb.com/api/v1/game/{gamePk}/boxscore`.",
        "",
    ]
    if fetch_error and not issues:
        lines.append(f"- {fetch_error}")
    elif not games and not fetch_error:
        lines.append(f"- No MLB games on the official schedule for {date_str}.")
    else:
        for game in games:
            lines.append(f"- {game.summary()}")
    lines.append("")
    if issues:
        lines.append("**Result: FAIL.** Fix the brief and the posts before this fact-check can pass.")
        lines.append("")
        for issue in issues:
            lines.append(f"- {issue}")
    else:
        lines.append("**Result: no first-pitch or ballpark mismatches.**")
        lines.append("")
        if fetch_error and not claims_present:
            lines.append("The schedule fetch failed, and this copy states no first pitch or ballpark.")
        else:
            lines.append(
                "Scores, inning lines, and player stats are not cleared by this clock and "
                "ballpark check. Use the Stats API box score for the gamePk. Two news sites "
                "agreeing is not verification."
            )
    return {"markdown": "\n".join(lines), "blocking": bool(issues), "issues": list(issues)}


def check_content_folder(content_folder: str, date_str: str, fetch=None) -> dict:
    """Fact-check hook. ``fetch`` defaults to the live Stats API and may be injected."""
    try:
        items = load_publishable_items(content_folder)
    except (OSError, json.JSONDecodeError) as exc:
        message = f"Could not read the brief folder {content_folder}: {exc}"
        return render_report(date_str, [], [message], message, True)
    present = schedule_claims_present(items)
    fetcher = fetch or fetch_schedule_payload
    fetch_error = None
    games: list[OfficialGame] = []
    try:
        payload = fetcher(date_str)
        games = games_from_payload(payload)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        fetch_error = (
            f"Could not read the MLB Stats API schedule for {date_str}: {exc}. "
            "Do not verify first-pitch times, ballparks, or game stats from CBS, Yahoo, "
            "ESPN, Fox, or any other secondary listing."
        )
    if fetch_error:
        issues = [fetch_error] if present else []
    else:
        issues = check_items(items, games, schedule_date=date_str)
    return render_report(date_str, games, issues, fetch_error, present)


def format_schedule(date_str: str, games: list[OfficialGame]) -> str:
    lines = [
        f"Official MLB schedule for {date_str}",
        "Source: Stats API gameDate (UTC) converted to America/Chicago; venue.name",
        f"Endpoint: {SCHEDULE_URL}?sportId=1&date={date_str}&hydrate=team,venue",
        "",
    ]
    if not games:
        lines.append(f"No MLB games on the official schedule for {date_str}.")
    else:
        for game in games:
            lines.append(f"- {game.summary()}")
            if game.game_pk:
                lines.append(f"  boxscore: {BOXSCORE_URL.format(game_pk=game.game_pk)}")
    lines.append("")
    lines.append(
        "Copy first-pitch clocks and ballpark names from this list only. "
        "Do not relabel a CBS, Yahoo, ESPN, or Fox listing as CT."
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="Official schedule date, YYYY-MM-DD")
    parser.add_argument(
        "--check",
        metavar="CONTENT_FOLDER",
        help="Compare that brief folder to the official schedule",
    )
    args = parser.parse_args(argv)
    try:
        if args.check:
            report = check_content_folder(args.check, args.date)
            print(report["markdown"])
            return 2 if report["blocking"] else 0
        payload = fetch_schedule_payload(args.date)
        games = games_from_payload(payload)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print(
            "Do not fall back to a national listing for first pitch or ballpark.",
            file=sys.stderr,
        )
        return 1
    print(format_schedule(args.date, games))
    return 0


if __name__ == "__main__":
    sys.exit(main())
