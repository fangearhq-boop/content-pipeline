"""Parse and hold Sooners briefs the way sooners-x-bot does.

sooners-x-bot reads America/Chicago
`Sooners/sooners-content-YYYY-MM-DD/03-social-posts-x.md` and
`06-fact-check-log.md`. Numeric claims in a post are publishable only when a
fact-check row is exactly VERIFIED and its source host is allowlisted. The day
verdict the bot accepts is the phrase "Acceptable for social".

mlb.com, statsapi.mlb.com, and baseball-reference.com are never valid sources.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

CHICAGO = ZoneInfo("America/Chicago")
DENVER = ZoneInfo("America/Denver")

POSTS_NAME = "03-social-posts-x.md"
FACT_NAME = "06-fact-check-log.md"
VERDICT = "Acceptable for social"
X_LIMIT = 280

# Six college slots. Chicago is what the bot schedules. Denver is the same
# instant, one hour earlier while both zones are on daylight time, and still
# one hour earlier in standard time.
COLLEGE_SLOTS = (
    {"ct": "9:00 AM CT", "denver": "8:00 AM MT", "label": "Football morning recap"},
    {"ct": "10:30 AM CT", "denver": "9:30 AM MT", "label": "Football next look"},
    {"ct": "12:30 PM CT", "denver": "11:30 AM MT", "label": "Basketball"},
    {"ct": "3:00 PM CT", "denver": "2:00 PM MT", "label": "Recruiting"},
    {"ct": "6:00 PM CT", "denver": "5:00 PM MT", "label": "Softball"},
    {"ct": "8:30 PM CT", "denver": "7:30 PM MT", "label": "Baseball"},
)

ALLOWLIST = (
    "soonersports.com",
    "espn.com",
    "ncaa.com",
    "ncaa.org",
    "oudaily.com",
    "secsports.com",
    "on3.com",
    "247sports.com",
    "crimsonandcreammachine.com",
)

BANNED = (
    "mlb.com",
    "statsapi.mlb.com",
    "baseball-reference.com",
)

# A clock is one token. "3" must not satisfy, or be satisfied by, "3:15".
_NUMBER = re.compile(r"\d{1,2}:\d{2}|\d+(?:\.\d+)?")
_URL = re.compile(r"https?://\S+")
_STORY = re.compile(r"^### STORY\s+(\d+)\s*:", re.M)
_FENCE = re.compile(r"```(?:[^\n]*)\n(.*?)```", re.S)


@dataclass
class FactRow:
    claim: str
    source: str
    status: str
    slot: str = ""

    @property
    def verified(self) -> bool:
        return self.status.strip() == "VERIFIED"


@dataclass
class BriefPost:
    story: str
    slot: str
    text: str


@dataclass
class Hold:
    ok: bool
    code: str
    messages: list[str] = field(default_factory=list)

    def summary(self) -> str:
        head = "PASS" if self.ok else "RED"
        detail = "; ".join(self.messages) if self.messages else self.code
        return f"{head} {self.code}: {detail}"


def chicago_today():
    return datetime.now(CHICAGO).date()


def content_folder_name(on_date) -> str:
    return f"sooners-content-{on_date.isoformat()}"


def normalize(text: str) -> str:
    text = (
        text.replace("\u2019", "'")
        .replace("\u2018", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\xa0", " ")
    )
    return re.sub(r"\s+", " ", text).strip()


def numbers_in(text: str) -> list[str]:
    seen = []
    for match in _NUMBER.findall(text):
        if match not in seen:
            seen.append(match)
    return seen


def has_number(text: str, number: str) -> bool:
    if re.fullmatch(r"\d{1,2}:\d{2}", number):
        return re.search(rf"(?<!\d){re.escape(number)}(?!\d)", text) is not None
    # A colon is a clock boundary, so the "3" in "3:15" is not a bare 3.
    return re.search(rf"(?<![\d:]){re.escape(number)}(?![\d:])", text) is not None


def _is_emoji(char: str) -> bool:
    code = ord(char)
    return (
        0x1F300 <= code <= 0x1FAFF
        or 0x1F1E6 <= code <= 0x1F1FF
        or 0x2600 <= code <= 0x27BF
        or 0x2300 <= code <= 0x23FF
        or code == 0xFE0F
        or code == 0x200D
    )


def x_length(text: str) -> int:
    """X weighted length. URLs count as 23. Emoji count as 2."""
    weighted = _URL.sub("x" * 23, text)
    total = 0
    for char in weighted:
        if ord(char) in (0xFE0F, 0x200D):
            continue
        total += 2 if _is_emoji(char) else 1
    return total


def host_of(url: str) -> str:
    try:
        host = urlparse(url.strip()).hostname or ""
    except ValueError:
        return ""
    host = host.lower().rstrip(".")
    if host.startswith("www."):
        host = host[4:]
    return host


def _matches_host(host: str, root: str) -> bool:
    return host == root or host.endswith("." + root)


def host_class(url: str) -> str:
    host = host_of(url)
    if not host:
        return "other"
    for banned in BANNED:
        if _matches_host(host, banned):
            return "banned"
    for allowed in ALLOWLIST:
        if _matches_host(host, allowed):
            return "allow"
    return "other"


def parse_fact_rows(fact_md: str) -> list[FactRow]:
    rows = []
    for line in fact_md.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[0].lower() == "claim" or set(cells[0]) <= set("-: "):
            continue
        slot = cells[3] if len(cells) >= 5 else ""
        rows.append(FactRow(claim=cells[0], source=cells[1], status=cells[-1], slot=slot))
    return rows


def parse_posts(posts_md: str) -> list[BriefPost]:
    parts = re.split(r"(?=^### STORY\s+\d+\s*:)", posts_md, flags=re.M)
    posts = []
    for part in parts:
        if not part.startswith("### STORY"):
            continue
        story = _STORY.search(part)
        fences = _FENCE.findall(part)
        slot = ""
        for spec in COLLEGE_SLOTS:
            if spec["ct"] in part:
                slot = spec["ct"]
                break
        text = fences[0].strip("\n") if fences else ""
        posts.append(BriefPost(story=story.group(1) if story else "", slot=slot, text=text))
    return posts


def verify_brief(posts_md: str, fact_md: str | None) -> Hold:
    """Return a hold. `ok` is False when the bot must skip or hold the day."""
    messages: list[str] = []
    if fact_md is None or not fact_md.strip():
        return Hold(False, "missing_fact_check_log", ["06-fact-check-log.md is missing or empty"])

    posts = parse_posts(posts_md or "")
    expected = [spec["ct"] for spec in COLLEGE_SLOTS]
    found = [post.slot for post in posts]
    if found != expected:
        messages.append(f"slots were {found or ['none']}, expected {expected}")

    for post in posts:
        if not post.text:
            messages.append(f"{post.slot or 'story'} has no fenced tweet")
            continue
        if "#Sooners" not in post.text:
            messages.append(f"{post.slot} tweet is missing #Sooners")
        if x_length(post.text) > X_LIMIT:
            messages.append(f"{post.slot} tweet is {x_length(post.text)} characters")

    rows = parse_fact_rows(fact_md)
    backing: list[FactRow] = []
    for row in rows:
        if not row.verified:
            continue
        kind = host_class(row.source)
        if kind == "banned":
            messages.append(f"banned source cited as VERIFIED: {row.source}")
        elif kind != "allow":
            messages.append(f"VERIFIED source is not allowlisted: {row.source}")
        else:
            backing.append(row)

    for post in posts:
        pool = _rows_for(post, backing)
        for number in numbers_in(post.text):
            if not any(has_number(row.claim, number) for row in pool):
                messages.append(
                    f"{post.slot} number {number} has no VERIFIED allowlisted row"
                )

    if VERDICT not in fact_md:
        messages.append(f'missing verdict phrase "{VERDICT}"')

    if messages:
        code = _primary_code(messages)
        return Hold(False, code, messages)
    return Hold(True, "acceptable", [VERDICT])


def verify_day(day_dir: Path) -> Hold:
    fact_path = day_dir / FACT_NAME
    posts_path = day_dir / POSTS_NAME
    if not posts_path.is_file():
        return Hold(False, "missing_posts", [f"{POSTS_NAME} is missing"])
    fact_md = fact_path.read_text(encoding="utf-8") if fact_path.is_file() else None
    return verify_brief(posts_path.read_text(encoding="utf-8"), fact_md)


def _rows_for(post: BriefPost, backing: list[FactRow]) -> list[FactRow]:
    """A digit has to be on that post's row. Untagged logs stay global."""
    if any(row.slot for row in backing):
        return [row for row in backing if row.slot == post.slot]
    return list(backing)


def _primary_code(messages: list[str]) -> str:
    blob = " ".join(messages)
    if "missing or empty" in blob:
        return "missing_fact_check_log"
    if "banned source" in blob:
        return "banned_host"
    if "not allowlisted" in blob:
        return "unlisted_host"
    if "has no VERIFIED allowlisted row" in blob:
        return "unbacked_number"
    if "slots were" in blob:
        return "bad_slots"
    if "missing #Sooners" in blob:
        return "missing_sooners_hashtag"
    if "tweet is" in blob and "characters" in blob:
        return "too_long"
    if "verdict phrase" in blob:
        return "missing_verdict"
    return "hold"
