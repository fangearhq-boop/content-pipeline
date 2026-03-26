"""
FanGear HQ Softball Niche — Claim Pattern Extraction

This module is dynamically loaded by the universal verify-facts.py script.
It extracts softball-specific factual claims beyond the universal date/time checks.

Exported function:
    extract_niche_claims(text, claim_list, story_num)

Claim dict format (must match universal engine expectations):
    {'type': str, 'value': str, 'context': str, 'story': str, 'priority': int}

Handles:
- Scores (beat/won/lost N-N) — Priority 2
- Records (W-L patterns with context filtering) — Priority 2
- Rankings (#N, No. N, ranked Nth) — Priority 3
- Player stats (.450 BA, 12 HRs, ERA, etc.) — Priority 3
- Historical claims (first time since, program record, career-high) — Priority 2

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
    Extract softball-specific factual claims from text.

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

    # 0. PLAYER AGES: "N years old", "N-year-old", "age N" — Priority 1 (HIGH)
    # LLMs frequently get ages wrong. Always verify from a source.
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

    # 1. SCORES: beat/won/lost N-N — Priority 2
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

    # 2. RECORDS: W-L patterns with context filtering — Priority 2
    for match in re.finditer(r'\b(\d{1,2})-(\d{1,2})\b', text):
        w, l = int(match.group(1)), int(match.group(2))
        # Plausible game counts only
        if w + l < 2 or w + l > 60:
            continue
        # Filter out date ranges and page/section refs
        if is_date_range(text, match.start(), match.end()):
            continue
        if is_page_or_section_ref(text, match.start(), match.end()):
            continue
        # Must be near team/record context (within 60 chars before)
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

    # 3. RANKINGS: #N, No. N, ranked Nth — Priority 3
    for match in re.finditer(r'(?:#|No\.\s*)(\d{1,2})\b', text):
        claim_list.append({
            'type': 'Ranking',
            'value': match.group(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })

    # 4. PLAYER STATS: .450 BA, 12 HRs, 0.95 ERA, etc. — Priority 3
    for match in re.finditer(
        r'(?:\d+\.)?\d+\s*(?:BA|ERA|HRs?|RBIs?|SO|BB|AVG|OBP|SLG|OPS|Ks?|SB|IP)\b',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Stat',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 3
        })

    # 5. HISTORICAL CLAIMS: first time since, program record, career-high — Priority 2
    for match in re.finditer(
        r'(?:first\s+time\s+since|program\s+record|career[- ]high|all[- ]time|'
        r'best\s+start\s+since|longest\s+streak|school\s+record|'
        r'NCAA\s+record|consecutive)',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Historical',
            'value': match.group().strip(),
            'context': get_context(match, 50),
            'story': story_num,
            'priority': 2
        })
