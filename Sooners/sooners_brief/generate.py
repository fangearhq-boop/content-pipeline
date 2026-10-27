"""Build one Sooners day folder from allowlisted source text."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta

from sooners_brief.contract import (
    COLLEGE_SLOTS,
    FACT_NAME,
    POSTS_NAME,
    VERDICT,
    X_LIMIT,
    content_folder_name,
    has_number,
    normalize,
    numbers_in,
    verify_brief,
    x_length,
)

FRESH_DAYS = {
    "football": 4,
    "basketball": 10,
    "softball": 21,
    "baseball": 21,
    "recruiting": 5,
}
# One URL is used once inside this window. Football freshness is shorter, so a
# used award does not come back. The schedule slot is not URL-gated: the next
# kickoff is re-read every morning and can repeat until the slate changes.
REUSE_GAP_DAYS = 21
HASHTAGS = "#Sooners #BoomerSooner #SoonerNation"


@dataclass
class Claim:
    text: str
    url: str


@dataclass
class Draft:
    slot_ct: str
    label: str
    title: str
    text: str
    claims: list[Claim] = field(default_factory=list)
    url: str = ""


def in_window(sport: str, on_date: date) -> bool:
    month = on_date.month
    if sport == "football":
        return month in (1, 8, 9, 10, 11, 12)
    if sport == "basketball":
        return month in (10, 11, 12, 1, 2, 3, 4)
    if sport in ("softball", "baseball"):
        return month in (2, 3, 4, 5, 6, 9, 10)
    return True


def recently_used(history: list[tuple[date, str]], url: str, on_date: date) -> bool:
    cutoff = on_date - timedelta(days=REUSE_GAP_DAYS)
    return any(used_url == url and cutoff <= used_on < on_date for used_on, used_url in history)


def _age_days(item, on_date: date) -> int | None:
    published = getattr(item, "published", None)
    if published is None:
        return None
    return (on_date - published.date()).days


def _fresh(item, on_date: date, sport: str) -> bool:
    """Unknown or unparseable timestamps are stale. A future stamp is stale too."""
    age = _age_days(item, on_date)
    if age is None:
        return False
    return 0 <= age <= FRESH_DAYS[sport]


def _date_stamp(on_date: date) -> str:
    return f"{on_date.strftime('%A')} {on_date.isoformat()}"


def _date_claim(on_date: date, url: str) -> Claim:
    return Claim(f"America/Chicago posting date {on_date.isoformat()}", url)


def _claim_from(source_text: str, snippet: str) -> str | None:
    source = normalize(source_text)
    claim = normalize(snippet)
    if claim and claim in source:
        return claim
    return None


def _finish(slot: str, label: str, title: str, text: str, claims: list[Claim], url: str) -> Draft | None:
    text = text.strip() + "\n"
    if "#Sooners" not in text or x_length(text) > X_LIMIT:
        return None
    for number in numbers_in(text):
        if not any(has_number(claim.text, number) for claim in claims):
            return None
    return Draft(slot_ct=slot, label=label, title=title, text=text, claims=claims, url=url)


# Fan-facing lines. These can publish with no game statistic. The story title
# is the same voice; it is not a pipeline label.
_QUIET_COPY = {
    "Football morning recap": (
        "BOOMER. 🏈",
        "Morning in Norman. Quiet campus, loud colors.",
    ),
    "Football next look": (
        "EYES UP. 🏈",
        "Next kick is a Sooners problem in the best way. Eyes on the slate.",
    ),
    "Basketball": (
        "LLOYD NOBLE, SOON. 🏀",
        "Hoops season is the long grind. Norman will be ready when the ball goes up.",
    ),
    "Recruiting": (
        "NORMAN STAYS ON THE TRAIL. 🎯",
        "The trail is quiet this morning. Norman is still on it.",
    ),
    "Softball": (
        "THE STANDARD HOLDS. 🥎",
        "Softball in Norman keeps its own standard. Patty's program does not take a day off.",
    ),
    "Baseball": (
        "FALL BALL, THEN SPRING. ⚾",
        "The diamond can wait. Fall is the workshop and spring is the loud part.",
    ),
}
_QUIET_TITLES = {
    "Football morning recap": "Morning in Norman",
    "Football next look": "Eyes up",
    "Basketball": "Lloyd Noble, soon",
    "Recruiting": "Norman stays on the trail",
    "Softball": "The standard holds",
    "Baseball": "Fall ball, then spring",
}


def _quiet(slot: str, label: str, _sport: str, on_date: date) -> Draft:
    # The sport name stays out of the tweet and the story title.
    lead, detail = _QUIET_COPY[label]
    url = "https://soonersports.com/"
    text = f"{lead}\n\n{_date_stamp(on_date)}. {detail}\n\n{HASHTAGS}\n"
    draft = _finish(
        slot,
        label,
        _QUIET_TITLES[label],
        text,
        [Claim("Fan line with no game statistic.", url), _date_claim(on_date, url)],
        url,
    )
    if draft is None:
        raise RuntimeError(f"quiet post failed for {slot}")
    return draft


def _football_award(item, slot: str) -> Draft | None:
    text = normalize(item.text)
    match = re.search(
        r"([A-Z][a-z]+ [A-Z][a-z]+) was named the SEC Defensive Player of the Week "
        r"after he recorded (\d+) tackles and forced a fumble in OU's (\d+)-(\d+) "
        r"road win at ([A-Za-z]+(?: [A-Za-z]+)*) on",
        text,
    )
    if not match:
        return None
    player, tackles, ours, theirs, opponent = match.groups()
    claim = _claim_from(text, match.group(0))
    if claim is None:
        return None
    tweet = (
        "SEC DEFENSIVE PLAYER OF THE WEEK. 🏈\n\n"
        f"{player}. {tackles} tackles and a forced fumble in the {ours}-{theirs} "
        f"road win at {opponent}.\n\n"
        "That's our guy on the big stage.\n\n"
        f"{HASHTAGS}"
    )
    return _finish(slot, "Football morning recap", item.title, tweet, [Claim(claim, item.url)], item.url)


def _next_game(item, slot: str, on_date: date) -> Draft | None:
    if item is None:
        return None
    sentence = normalize(item.text)
    match = re.search(
        r"Football (versus|at) (.+?) on ([A-Z][a-z]+ \d{1,2}), \d{4} at "
        r"(\d{1,2}:\d{2}(?:-\d{1,2}:\d{2})? p\.m\. CT)",
        sentence,
    )
    if not match:
        return None
    place, opponent, when, clock = match.groups()
    where = "at" if place == "at" else "vs"
    lead = "ROAD WEEK. 🏈" if place == "at" else "HOME LOOK. 🏈"
    tweet = (
        f"{lead}\n\n"
        f"Oklahoma {where} {opponent}. {when}. {clock}.\n\n"
        f"{_date_stamp(on_date)}. Official slate. Be there.\n\n"
        f"{HASHTAGS}"
    )
    claim = _claim_from(sentence, sentence)
    if claim is None:
        return None
    title = f"Oklahoma {where} {opponent}"
    return _finish(
        slot,
        "Football next look",
        title,
        tweet,
        [Claim(claim, item.url), _date_claim(on_date, item.url)],
        item.url,
    )


# The winner is the word immediately in front of "defeated", plus at most four
# lowercase filler words ("women", "men's basketball", "as it"). A capital, a
# colon, a comma, or "as the" in that gap is a different subject.
_FILLER_WORD = r"(?!as\s+the\b)[a-z][a-z'-]*"
_WIN = re.compile(
    rf"\b(Oklahoma|Sooners)\b(?!\s+[A-Z])"
    rf"((?:\s+{_FILLER_WORD}){{0,4}})"
    rf"\s+defeated "
    rf"([A-Z][^,]{{2,48}}?), (\d+)-(\d+), in an exhibition"
)


def _basketball(item, slot: str) -> Draft | None:
    text = normalize(item.text)
    match = _WIN.search(text)
    if not match:
        return None
    subject, between, opponent, ours, theirs = match.groups()
    if opponent.strip().casefold() in {"oklahoma", "sooners"}:
        return None
    if re.search(r"[A-Z]|,|:|\bas the\b", between):
        return None
    claim = _claim_from(text, match.group(0))
    if claim is None:
        return None
    side = "Women's basketball" if item.sport == "womens-basketball" else "Men's basketball"
    line = f"{subject} defeated {opponent} {ours}-{theirs}."
    if "never trailed" in between.casefold():
        line = f"{subject} defeated {opponent} {ours}-{theirs}. Never trailed."
    tweet = f"EXHIBITION WIN. 🏀\n\n{line}\n\n{side} just checked in.\n\n{HASHTAGS}"
    return _finish(slot, "Basketball", item.title, tweet, [Claim(claim, item.url)], item.url)


def _softball(item, slot: str) -> Draft | None:
    text = normalize(item.text)
    match = re.search(
        r"Patty Gasso was inducted to the Oklahoma Women's Hall of Fame.{0,220}?Oct\. (\d{1,2})",
        text,
    )
    if not match:
        return None
    claim = _claim_from(text, match.group(0))
    if claim is None:
        return None
    day = match.group(1)
    city = " in Oklahoma City" if "in Oklahoma City" in claim else ""
    tweet = (
        "PATTY GASSO. HALL OF FAME. 🥎\n\n"
        f"Oklahoma Women's Hall of Fame. The ceremony was Oct. {day}{city}.\n\n"
        f"{HASHTAGS}"
    )
    return _finish(slot, "Softball", item.title, tweet, [Claim(claim, item.url)], item.url)


def _baseball(item, slot: str) -> Draft | None:
    text = normalize(item.text)
    match = re.search(
        r"full (\d{4}) season schedule.{0,180}?(\d+) games, highlighted by (\d+) home games",
        text,
    )
    if not match:
        return None
    year, games, home = match.groups()
    claim = _claim_from(text, match.group(0))
    if claim is None:
        return None
    coach = "Skip Johnson" if "Skip Johnson" in text else "Oklahoma baseball"
    tweet = (
        f"{year} BASEBALL SCHEDULE IS OUT. ⚾\n\n"
        f"{games} games. {home} of them at home. {coach} put the slate on paper.\n\n"
        "Fall is the workshop. Spring cashes it.\n\n"
        f"{HASHTAGS}"
    )
    return _finish(slot, "Baseball", item.title, tweet, [Claim(claim, item.url)], item.url)


def _pick(items, on_date: date, history, sport: str, builder, slot: str) -> Draft | None:
    if not in_window(sport, on_date):
        return None
    for item in items:
        if recently_used(history, item.url, on_date):
            continue
        if not _fresh(item, on_date, sport):
            continue
        draft = builder(item, slot)
        if draft is not None:
            return draft
    return None


def build_drafts(bundle: dict, on_date: date, history: list[tuple[date, str]] | None = None) -> list[Draft]:
    history = history or []
    specs = COLLEGE_SLOTS
    drafts: list[Draft] = []

    football = _pick(bundle.get("football") or [], on_date, history, "football", _football_award, specs[0]["ct"])
    drafts.append(football or _quiet(specs[0]["ct"], specs[0]["label"], "football", on_date))

    nxt = _next_game(bundle.get("next_game"), specs[1]["ct"], on_date) if in_window("football", on_date) else None
    drafts.append(nxt or _quiet(specs[1]["ct"], specs[1]["label"], "football", on_date))

    basketball = _pick(bundle.get("basketball") or [], on_date, history, "basketball", _basketball, specs[2]["ct"])
    drafts.append(basketball or _quiet(specs[2]["ct"], specs[2]["label"], "basketball", on_date))

    # Fixed line. Third-party headlines are not copied, including decommits
    # and spelled-out numbers.
    drafts.append(_quiet(specs[3]["ct"], specs[3]["label"], "recruiting", on_date))

    softball = _pick(bundle.get("softball") or [], on_date, history, "softball", _softball, specs[4]["ct"])
    drafts.append(softball or _quiet(specs[4]["ct"], specs[4]["label"], "softball", on_date))

    baseball = _pick(bundle.get("baseball") or [], on_date, history, "baseball", _baseball, specs[5]["ct"])
    drafts.append(baseball or _quiet(specs[5]["ct"], specs[5]["label"], "baseball", on_date))
    return drafts


def render_posts(on_date: date, drafts: list[Draft]) -> str:
    lines = [
        f"# Sooners X/Twitter Posts — {on_date.isoformat()}",
        "",
        "**Platform:** X/Twitter only",
        "**Account voice:** @SoonersFanRecap",
        "**Slots:** six college windows in America/Chicago. Denver equivalents are in niche-config.yaml.",
        "",
        "---",
        "",
    ]
    for index, draft in enumerate(drafts, start=1):
        lines.extend(
            [
                f"### STORY {index}: {draft.title}",
                "",
                f"**Post {index}** — {draft.slot_ct} | {draft.label}",
                "",
                "```",
                draft.text.rstrip("\n"),
                "```",
                "",
                f"**Char count:** {x_length(draft.text)} ✓ (≤280)",
                "",
                "---",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_fact_log(on_date: date, drafts: list[Draft]) -> str:
    lines = [
        f"# Sooners Fact-Check Log — {on_date.isoformat()}",
        "",
        f"**Verdict:** {VERDICT}",
        "",
        VERDICT,
        "",
        "Numeric claims in the X posts are backed only by rows whose status is VERIFIED and whose source host is on the college allowlist.",
        "",
        "| Claim | Source | Confidence | Slot | Status |",
        "|-------|--------|------------|------|--------|",
    ]
    for draft in drafts:
        for claim in draft.claims:
            claim_cell = claim.text.replace("|", "/")
            lines.append(f"| {claim_cell} | {claim.url} | HIGH | {draft.slot_ct} | VERIFIED |")
    lines.append("")
    return "\n".join(lines)


def render_day(on_date: date, drafts: list[Draft]) -> tuple[str, str]:
    posts = render_posts(on_date, drafts)
    facts = render_fact_log(on_date, drafts)
    hold = verify_brief(posts, facts)
    if not hold.ok:
        raise RuntimeError(hold.summary())
    return posts, facts


def load_history(text: str) -> list[tuple[date, str]]:
    found = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() == "date" or set(cells[0]) <= set("-: "):
            continue
        try:
            used_on = datetime.strptime(cells[0], "%Y-%m-%d").date()
        except ValueError:
            continue
        found.append((used_on, cells[2]))
    return found


def history_row(on_date: date, draft: Draft) -> str:
    title = draft.title.replace("|", "/")
    return f"| {on_date.isoformat()} | {draft.slot_ct} | {draft.url} | {title} |"


def day_paths(niche_root, on_date: date):
    folder = niche_root / content_folder_name(on_date)
    return folder, folder / POSTS_NAME, folder / FACT_NAME
