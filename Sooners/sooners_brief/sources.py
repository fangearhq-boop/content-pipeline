"""Allowlisted Sooners sources. No MLB hosts, no API keys."""

from __future__ import annotations

import html
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from sooners_brief.contract import normalize

USER_AGENT = "FanHQ-SoonersPipeline/1.0"
SOONERSPORTS = "https://soonersports.com"
ON3_FEED = "https://www.on3.com/teams/oklahoma-sooners/feed/"
FOOTBALL_SCHEDULE = f"{SOONERSPORTS}/sports/football/schedule/2026"

SPORT_IDS = {
    "football": 2,
    "mens-basketball": 4,
    "softball": 10,
    "womens-basketball": 11,
    "baseball": 1,
}


@dataclass
class SourceItem:
    sport: str
    title: str
    url: str
    text: str
    published: datetime | None = None


def fetch_text(url: str, timeout: int = 25) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json, application/xml, text/html, */*"})
    with urlopen(request, timeout=timeout) as response:
        raw = response.read()
    return raw.decode("utf-8", "replace")


def plain(fragment: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", fragment or "")
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return normalize(html.unescape(text))


def _parse_when(value: str | None) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    # API timestamps are naive local times. Drop a trailing timezone abbreviation.
    trimmed = re.sub(r"\s+[A-Z]{2,4}$", "", value)
    for fmt in ("%a, %d %b %Y %H:%M:%S", "%a, %d %b %Y %H:%M", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(trimmed, fmt)
        except ValueError:
            continue
    return None


def _safe(url: str) -> str:
    try:
        return fetch_text(url)
    except (HTTPError, URLError, TimeoutError, OSError):
        return ""


def stories_for(sport: str, sport_id: int, count: int = 6) -> list[SourceItem]:
    import json

    raw = _safe(f"{SOONERSPORTS}/api/v2/stories?sportId={sport_id}&count={count}")
    if not raw:
        return []
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return []
    items = []
    for entry in payload.get("items") or []:
        path = entry.get("contentUrl") or ""
        url = path if path.startswith("http") else SOONERSPORTS + path
        title = plain(entry.get("title") or entry.get("contentTitle") or "")
        teaser = plain(entry.get("teaser") or "")
        items.append(
            SourceItem(
                sport=sport,
                title=title,
                url=url,
                text=normalize(f"{title}. {teaser}"),
                published=_parse_when(entry.get("contentDate")),
            )
        )
    return items


def on3_items() -> list[SourceItem]:
    raw = _safe(ON3_FEED)
    if not raw:
        return []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return []
    items = []
    for node in root.findall(".//item"):
        title = plain(node.findtext("title") or "")
        link = (node.findtext("link") or "").strip()
        description = plain(node.findtext("description") or "")
        items.append(
            SourceItem(
                sport="recruiting",
                title=title,
                url=link,
                text=normalize(f"{title}. {description}"),
                published=_parse_when(node.findtext("pubDate")),
            )
        )
    return items


_NEXT_GAME = re.compile(
    r"Upcoming Event: Football (versus|at) (.+?) on "
    r"([A-Z][a-z]+ \d{1,2}, \d{4}) at "
    r"(\d{1,2}:\d{2}(?:-\d{1,2}:\d{2})? p\.m\. CT)"
)


def next_football_game() -> SourceItem | None:
    page = plain(_safe(FOOTBALL_SCHEDULE))
    match = _NEXT_GAME.search(page)
    if not match:
        return None
    sentence = match.group(0)
    return SourceItem(
        sport="football-schedule",
        title=f"Oklahoma {match.group(1)} {match.group(2)}",
        url=FOOTBALL_SCHEDULE,
        text=sentence,
        published=None,
    )


def load_bundle() -> dict:
    basketball = stories_for("womens-basketball", SPORT_IDS["womens-basketball"])
    basketball += stories_for("mens-basketball", SPORT_IDS["mens-basketball"])
    basketball.sort(key=lambda item: item.published or datetime.min, reverse=True)
    return {
        "football": stories_for("football", SPORT_IDS["football"]),
        "basketball": basketball,
        "softball": stories_for("softball", SPORT_IDS["softball"]),
        "baseball": stories_for("baseball", SPORT_IDS["baseball"]),
        "recruiting": on3_items(),
        "next_game": next_football_game(),
    }
