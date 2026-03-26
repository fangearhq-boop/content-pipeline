"""
FanGear HQ Cubs Niche — Claim Pattern Extraction

This module is dynamically loaded by the universal verify-facts.py script.
It extracts MLB/Cubs-specific factual claims beyond the universal date/time checks.

Exported function:
    extract_niche_claims(text, claim_list, story_num)

Claim dict format (must match universal engine expectations):
    {'type': str, 'value': str, 'context': str, 'story': str, 'priority': int}

Handles:
- Player ages (N years old, age N) — Priority 1 (HIGH)
  NEVER calculate ages from birth dates — verify from a reliable source.
- Scores (beat/won/lost N-N) — Priority 2
- Records (W-L patterns with context filtering) — Priority 2
- Player stats (.312 BA, 2.85 ERA, 14 HRs, WAR, wRC+, etc.) — Priority 3
- Contract values ($N million, N-year deal) — Priority 2
- Rankings (#N, No. N, ranked Nth) — Priority 3
- Historical claims (first time since, franchise record, career-high) — Priority 2

NOTE: Time/date/day-of-week claims are handled by the universal engine.
Only niche-specific patterns are extracted here.
"""

import re


def is_date_range(text, start, end):
    """Check if a W-L pattern appears as part of a date range (e.g., 'Jan 5-7')."""
    before = text[max(0, start - 20):start]
    return bool(re.search(
        r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}\s*[-–]?\s*$',
        before
    ))


def is_page_or_section_ref(text, start, end):
    """Check if a W-L pattern is part of a page/section reference (e.g., 'page 8-2')."""
    before = text[max(0, start - 15):start]
    return bool(re.search(r'(?:page|pages|section|steps?|items?)\s*$', before))


def extract_niche_claims(text, claim_list, story_num):
    """
    Extract Cubs/MLB-specific factual claims from text.

    Called by the universal verify-facts.py engine via dynamic import.
    Appends claim dicts to claim_list with keys: type, value, context, story, priority.

    Args:
        text: The story text to analyze
        claim_list: List to append claims to (modified in place)
        story_num: The story number being processed
    """

    def get_context(match, radius=50):
        ctx = text[max(0, match.start() - radius):match.end() + radius].strip()
        return re.sub(r'\s+', ' ', ctx)

    # 1. PLAYER AGES: "N years old", "N-year-old", "age N" — Priority 1 (HIGH)
    # These are HIGH because LLMs frequently get ages wrong (off-by-one from
    # birth date math, stale training data, etc.). Always verify from a source.
    for match in re.finditer(
        r'\b(\d{1,2})\s*[-–]?\s*year[-–\s]*old\b|\bage[d]?\s+(\d{1,2})\b|\b(\d{1,2})\s+years\s+old\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Age',
            'value': match.group().strip()[:80],
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })

    # 2. SCORES: beat/won/lost N-N — Priority 2
    for match in re.finditer(
        r'(?:won|beat|defeated|lost\s+to|fell\s+to)\s+(?:[A-Z#][\w\s.\'#]*?)\s+(\d{1,2})-(\d{1,2})\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Score',
            'value': match.group().strip()[:80],
            'context': get_context(match, 30),
            'story': story_num,
            'priority': 2
        })

    # 3. RECORDS: W-L patterns with context filtering — Priority 2
    for match in re.finditer(r'\b(\d{1,2})-(\d{1,2})\b', text):
        w, l = int(match.group(1)), int(match.group(2))
        if w + l < 2 or w + l > 162:
            continue
        if is_date_range(text, match.start(), match.end()):
            continue
        if is_page_or_section_ref(text, match.start(), match.end()):
            continue
        before = text[max(0, match.start() - 60):match.start()]
        if not re.search(r'(?:record|start|went|going|improved|dropped|moved|sits|at|is)\s*$|'
                         r'(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*\(?\s*$', before, re.IGNORECASE):
            if not re.search(r'\(\s*$', before):
                continue
        claim_list.append({
            'type': 'Record',
            'value': match.group(),
            'context': get_context(match),
            'story': story_num,
            'priority': 2
        })

    # 4. RANKINGS: #N, No. N, ranked Nth — Priority 3
    for match in re.finditer(r'(?:#|No\.\s*)(\d{1,2})\b', text):
        claim_list.append({
            'type': 'Ranking',
            'value': match.group(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })

    # 5. PLAYER STATS: .312 BA, 2.85 ERA, 14 HRs, WAR, wRC+, etc. — Priority 3
    for match in re.finditer(
        r'(?:\d+\.)?\d+\s*(?:BA|ERA|HRs?|RBIs?|SO|BB|AVG|OBP|SLG|OPS|Ks?|SB|IP|WAR|wRC\+|FIP|WHIP)\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Stat',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })

    # 6. CONTRACT VALUES: $N million, N-year deal — Priority 2
    for match in re.finditer(
        r'\$\d+(?:\.\d+)?\s*(?:million|mil|M)\b|\b\d+[-–]\s*year\s+(?:deal|contract|extension)\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Contract',
            'value': match.group().strip()[:80],
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 2
        })

    # 7. HISTORICAL CLAIMS: first time since, franchise record, career-high — Priority 2
    for match in re.finditer(
        r'(?:first\s+time\s+since|franchise\s+record|program\s+record|career[- ]high|all[- ]time|'
        r'best\s+start\s+since|longest\s+streak|club\s+record|'
        r'MLB\s+record|consecutive)',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Historical',
            'value': match.group().strip(),
            'context': get_context(match, 50),
            'story': story_num,
            'priority': 2
        })
