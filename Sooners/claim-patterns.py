"""College claim patterns for the Sooners niche.

The daily brief does not use this module to decide what posts. sooners_brief
binds every tweet digit to a verbatim allowlisted span. This module exists so
the shared engine can import the niche the same way it imports the others.
"""

import re

CLAIM_TYPES = {
    "Score": 2,
    "Counting stat": 3,
    "Ranking": 3,
    "Clock": 1,
}


def extract_niche_claims(text, claim_list, story_num):
    """Append college claims. No pro-baseball stat families."""

    def add(kind, match, priority):
        claim_list.append(
            {
                "type": kind,
                "value": match.group().strip()[:80],
                "context": re.sub(r"\s+", " ", text[max(0, match.start() - 40): match.end() + 40]).strip(),
                "story": story_num,
                "priority": priority,
            }
        )

    for match in re.finditer(r"\b\d{1,3}\s*-\s*\d{1,3}\b", text):
        add("Score", match, 2)
    for match in re.finditer(
        r"\b\d+\s+tackles?\b|\b\d+\s+sacks?\b|\b\d+\s+points?\b|\b\d+\s+rebounds?\b",
        text,
        re.IGNORECASE,
    ):
        add("Counting stat", match, 3)
    for match in re.finditer(r"\b(?:No\.|ranked)\s*#?\d+\b", text, re.IGNORECASE):
        add("Ranking", match, 3)
    for match in re.finditer(r"\b\d{1,2}:\d{2}\s*p\.m\.\s*CT\b", text, re.IGNORECASE):
        add("Clock", match, 1)
