"""Allowlisted Sooners sources. No MLB hosts, no API keys."""

from __future__ import annotations

import html
import logging
import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime
from http.client import IncompleteRead, RemoteDisconnected
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from sooners_brief.contract import normalize

log = logging.getLogger("sooners_brief.sources")

USER_AGENT = "FanHQ-SoonersPipeline/1.0"
SOONERSPORTS = "https://soonersports.com"
ON3_FEED = "https://www.on3.com/teams/oklahoma-sooners/feed/"
FETCH_ATTEMPTS = 3

SPORT_IDS = {
    "football": 2,
    "mens-basketball": 4,
    "softball": 10,
    "womens-basketball": 11,
    "baseball": 1,
}

_RETRYABLE = (HTTPError, URLError, TimeoutError, IncompleteRead, RemoteDisconnected, OSError)


class SourceFetchError(RuntimeError):
    """Raised when the brief has nothing it is allowed to publish from."""


@dataclass
class SourceItem:
    sport: str
    title: str
    url: str
    text: str
    published: datetime | None = None


def football_season_year(on_date: date) -> int:
    """January is still the previous season's schedule page."""
    if on_date.month == 1:
        return on_date.year - 1
    return on_date.year


def schedule_url(on_date: date) -> str:
    return f"{SOONERSPORTS}/sports/football/schedule/{football_season_year(on_date)}"


def fetch_text(url: str, timeout: int = 25, opener=None, sleeper=None, attempts: int = FETCH_ATTEMPTS) -> str:
    opener = opener or urlopen
    sleeper = sleeper or time.sleep
    last = None
    for attempt in range(1, attempts + 1):
        try:
            request = Request(
                url,
                headers={"User-Agent": USER_AGENT, "Accept": "application/json, application/xml, text/html, */*"},
            )
            with opener(request, timeout=timeout) as response:
                raw = response.read()
            return raw.decode("utf-8", "replace")
        except _RETRYABLE as exc:
            last = exc
            log.warning("fetch failed %s attempt %s/%s: %s", url, attempt, attempts, exc)
            if attempt == attempts:
                break
            sleeper(2 ** (attempt - 1))
    raise SourceFetchError(f"{url}: {last}")


def plain(fragment: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", fragment or "")
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return normalize(html.unescape(text))


def _parse_when(value: str | None) -> datetime | None:
    if value is None:
        return None
    raw = str(value).strip()
    if not raw:
        return None
    candidates = [raw]
    if raw.endswith("Z"):
        candidates.append(raw[:-1] + "+00:00")
    for candidate in candidates:
        try:
            return datetime.fromisoformat(candidate)
        except ValueError:
            continue
    trimmed = re.sub(r"\s+[A-Z]{2,4}$", "", raw)
    for candidate in (raw, trimmed):
        for fmt in (
            "%a, %d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S %Z",
            "%a, %d %b %Y %H:%M:%S",
            "%a, %d %b %Y %H:%M",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
        ):
            try:
                return datetime.strptime(candidate, fmt)
            except ValueError:
                continue
    return None


def _safe(url: str, opener=None, sleeper=None) -> str:
    try:
        return fetch_text(url, opener=opener, sleeper=sleeper)
    except SourceFetchError as exc:
        log.error("source unavailable: %s", exc)
        return ""


def stories_for(sport: str, sport_id: int, count: int = 6, opener=None, sleeper=None) -> list[SourceItem]:
    import json

    raw = _safe(f"{SOONERSPORTS}/api/v2/stories?sportId={sport_id}&count={count}", opener=opener, sleeper=sleeper)
    if not raw:
        return []
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        log.error("stories payload was not JSON for %s", sport)
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


def on3_items(opener=None, sleeper=None) -> list[SourceItem]:
    raw = _safe(ON3_FEED, opener=opener, sleeper=sleeper)
    if not raw:
        return []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        log.error("On3 feed was not XML")
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


def next_football_game(on_date: date, opener=None, sleeper=None) -> SourceItem | None:
    url = schedule_url(on_date)
    page = plain(_safe(url, opener=opener, sleeper=sleeper))
    match = _NEXT_GAME.search(page)
    if not match:
        return None
    return SourceItem(
        sport="football-schedule",
        title=f"Oklahoma {match.group(1)} {match.group(2)}",
        url=url,
        text=match.group(0),
        published=None,
    )


def require_publishable_source(bundle: dict) -> None:
    """Recruiting headlines are not publishable. An unused feed cannot save the day."""
    if bundle.get("next_game") is not None:
        return
    for key in ("football", "basketball", "softball", "baseball"):
        if bundle.get(key):
            return
    raise SourceFetchError("every Sooners source came back empty")


def load_bundle(on_date: date, opener=None, sleeper=None) -> dict:
    basketball = stories_for("womens-basketball", SPORT_IDS["womens-basketball"], opener=opener, sleeper=sleeper)
    basketball += stories_for("mens-basketball", SPORT_IDS["mens-basketball"], opener=opener, sleeper=sleeper)
    basketball.sort(key=lambda item: item.published or datetime.min, reverse=True)
    bundle = {
        "football": stories_for("football", SPORT_IDS["football"], opener=opener, sleeper=sleeper),
        "basketball": basketball,
        "softball": stories_for("softball", SPORT_IDS["softball"], opener=opener, sleeper=sleeper),
        "baseball": stories_for("baseball", SPORT_IDS["baseball"], opener=opener, sleeper=sleeper),
        "recruiting": on3_items(opener=opener, sleeper=sleeper),
        "next_game": next_football_game(on_date, opener=opener, sleeper=sleeper),
    }
    require_publishable_source(bundle)
    return bundle
