---
name: fact-check
description: >
  **Universal Fact-Check Engine**: Verifies factual claims in any FanGear HQ content
  using web search. Works across all content types — daily brief pipeline claims,
  trivia database entries, historical content batches, and any new niche or format.

  Use this skill whenever you need to: fact-check content before publication, verify
  a batch of trivia/historical entries, run the verification step of the daily pipeline
  (Step 10), validate claims extracted by verify-facts.py, or check any content where
  factual accuracy matters. Also use when generating content that will later need
  verification — the skill defines the correction format that downstream scripts expect.

  This skill replaces ad-hoc fact-checking prompts. If you're about to write a custom
  prompt telling an agent to "check these entries and write corrections," use this
  skill instead — it standardizes the process and prevents the format mismatches that
  cause correction pipelines to break.
---

# FanGear HQ — Universal Fact-Check Engine

## Why This Skill Exists

Fact-checking is the single biggest quality bottleneck across all FanGear HQ content.
In production, we've seen:

- ~21% error rate in AI-generated historical sports content
- Completely fabricated entries that passed initial generation (e.g., a Kirby Puckett
  trade that never happened)
- Date errors as the most common failure mode (wrong month, day, or year)
- Correction format inconsistencies that broke automated pipelines — agents returning
  compound fields like `"field": "month, day, year"` instead of one correction per field

This skill standardizes how verification works so it's consistent whether you're
checking 3 entries or 3,000, across any niche or content type.

---

## Core Principles

**1. One correction per field, always.**
Never combine multiple field changes into a single correction. If month, day, and year
are all wrong, that's three separate corrections (or more likely, a removal — see below).

**2. Context determines the right action.**
A wrong date in a trivia entry doesn't mean "fix the date." If the entry was supposed
to fill a specific calendar slot (like "On This Day" for March 15), changing the date
to March 22 defeats the purpose. The right action is `"action": "remove"` so a new
entry can be generated for the correct date. The skill handles this distinction
through verification modes.

**3. Verify before you assert.**
Every claim must be checked against a web source before marking it correct or incorrect.
"This looks right to me" is not verification. Search for it.

**4. Track what you checked.**
The output always includes how many entries were verified, how many errors were found,
and the error rate. This data shapes future quality decisions.

---

## Verification Modes

The skill operates in three modes depending on what you're checking. Pick the right
mode before starting — it changes how corrections are handled.

### Mode 1: Bulk Content Verification

**When:** Checking a batch of trivia entries, historical content, database records.
**Input:** A Python file or list of entry dicts.
**Key behavior:** Entries with wrong dates in date-anchored content (On This Day,
calendar-specific entries) get `"action": "remove"` rather than date corrections,
because the entry exists to fill a specific calendar slot.

### Mode 2: Daily Pipeline Verification

**When:** Running Step 10 of the daily content pipeline, verifying claims extracted
by `verify-facts.py`.
**Input:** A `06-fact-check-log.md` file with extracted claims, or raw content files.
**Key behavior:** Claims are verified in priority order (Priority 1 first). Corrections
are written back into the fact-check log with source URLs.

### Mode 3: Single-Entry Spot Check

**When:** Verifying a specific claim or small number of entries interactively.
**Input:** The claim text directly in conversation.
**Key behavior:** Returns verdict inline with source. No correction file needed.

---

## The Correction Format

This is the contract. Every automated consumer of fact-check output depends on this
exact format. Do not deviate from it.

### Field-level correction

```python
{
    "index": 42,           # 0-based position in the source list
    "field": "year",       # EXACTLY ONE field name — never compound
    "old_value": 1987,     # Current value (for verification)
    "new_value": 1990,     # Corrected value
    "reason": "Jordan's 69-point game was March 28, 1990, not 1987"
}
```

**Rules:**
- `field` must be a single key that exists in the entry dict (e.g., `"year"`, `"content"`, `"title"`, `"day"`, `"month"`, `"tags"`, `"subcategory"`)
- Never use compound fields like `"month, day, year"` or `"title and content"`
- If multiple fields need fixing on the same entry, write multiple corrections
- `old_value` must match the current value — this prevents applying stale corrections

### Removal

```python
{
    "index": 8,
    "action": "remove",
    "reason": "Carlton Fisk never hit 500 HR; he hit 376. Entry is fabricated."
}
```

**When to remove instead of correct:**
- The event never happened at all (fabricated)
- The date correction would move a date-anchored entry off its assigned date
- Multiple fields are wrong and the entry is unsalvageable
- The claim is so misleading that rewording would change its identity

### Output file structure

Write corrections to a Python file defining a single list:

```python
# /tmp/{league}_{batch}_corrections.py
corrections = [
    {"index": 3, "field": "day", "old_value": 4, "new_value": 26, "reason": "..."},
    {"index": 8, "action": "remove", "reason": "..."},
    {"index": 12, "field": "content", "old_value": "...", "new_value": "...", "reason": "..."},
]
```

Also write a human-readable summary to a text file:

```
# /tmp/{league}_{batch}_factcheck.txt
=== FACT-CHECK: {description} ===
Entries checked: 83
Errors found: 22
Error rate: 26.5%

CORRECTIONS:
[1] Index 3 (1/4): Day should be 26, not 4. Prince Fielder signed Jan 26, 2012.
[2] Index 8 (2/29): REMOVE — Fabricated. Carlton Fisk hit 376 HR, not 500.
...
```

---

## Verification Procedure

For each entry or claim, follow this sequence:

### Step 1: Identify the core claims

What facts does this entry assert? Typically:
- A specific event happened
- On a specific date (month/day/year)
- Involving specific people, teams, or organizations
- With specific stats, scores, or outcomes

### Step 2: Search for verification

Use web search with targeted queries:
- `"[person/team] [event type] [year]"` — e.g., "Nolan Ryan strikeout record 1983"
- `"[sport] [month] [day] history"` — e.g., "MLB April 8 history"
- `"[specific claim]"` — e.g., "Kirby Puckett trade Mets" (this would reveal no results, confirming fabrication)

Search at least once per entry. For entries where the first search raises doubts,
do a second search with different terms.

### Step 3: Compare and judge

- **Correct:** Search results confirm all key claims. No correction needed.
- **Minor error:** One field is wrong (e.g., year off by one). Write a field correction.
- **Major error:** Multiple fields wrong or event misrepresented. Assess whether
  corrections can salvage it or if removal is cleaner.
- **Fabricated:** No evidence the event happened. Write a removal.
- **Unverifiable:** Can't find sources either way. Flag in the summary but don't
  correct — absence of evidence isn't evidence of absence.

### Step 4: Write corrections

Follow the correction format exactly. One correction per field. Include the reason
so a human reviewer can understand the change without re-searching.

---

## Dispatching Verification Agents

When checking large batches (50+ entries), dispatch parallel subagents. Here's the
standard prompt template — adapt the specifics but keep the correction format
instructions verbatim:

```
You are a fact-checker for {content_type} content. Read the file {input_file}
which contains {count} entries in a list called `{variable_name}`.

For EVERY entry, verify using web search:
1. The event/claim actually happened
2. Key dates (month, day, year) are correct
3. Names, teams, stats, and outcomes are accurate
4. Content doesn't overstate or misrepresent what happened

You MUST check ALL entries — do not skip any.

Write your results to TWO files:

1. `{summary_file}` — Plain text report:
   - Total entries checked
   - Total errors found
   - Error rate percentage
   - For each error: index, what's wrong, correct information

2. `{corrections_file}` — Python file defining a list called `{corrections_var}`:

   CRITICAL FORMAT RULES:
   - One correction per field. NEVER use compound field names.
   - BAD:  {"index": 0, "field": "month, day, year", ...}
   - GOOD: {"index": 0, "field": "month", ...}, {"index": 0, "field": "day", ...}

   For field corrections:
   {"index": N, "field": "fieldname", "old_value": "...", "new_value": "...", "reason": "..."}

   For fabricated/unsalvageable entries:
   {"index": N, "action": "remove", "reason": "..."}

   {MODE_SPECIFIC_INSTRUCTION}

If no errors found, write empty list and 0 errors.
```

**Mode-specific instructions to insert:**

For date-anchored content (On This Day entries):
```
IMPORTANT: If a date correction would change the month or day to a DIFFERENT
calendar date than what's assigned, use "action": "remove" instead. These entries
exist to fill specific calendar slots — moving them defeats the purpose.
```

For daily pipeline content:
```
Include the source URL where you verified or disproved each claim.
```

---

## Applying Corrections

Read `references/apply-corrections.md` for the standard correction-application script.
The key steps:

1. Load the source entries and correction list
2. Process removals first (collect indices to remove)
3. Apply field corrections to non-removed entries (verify old_value matches)
4. Filter out removed entries
5. Report: entries corrected, entries removed, entries unchanged
6. Save the corrected dataset

---

## Batch Size Guidelines

Based on production experience:

- **Subagent batch size:** 80-100 entries per agent works well. Larger batches lead to
  agents skipping entries or losing focus toward the end.
- **Parallel agents:** 2-4 concurrent agents is the sweet spot. More than that tends to
  hit rate limits on web search.
- **Verification depth:** For initial fact-check, sample-based is acceptable (check
  every entry but accept that some searches won't find definitive sources). For
  corrections that failed the first round, verify exhaustively — these are the
  entries most likely to be fabricated.

---

## Integration with Existing Systems

### With verify-facts.py (Daily Pipeline)

The existing `verify-facts.py` script extracts claims and generates `06-fact-check-log.md`.
This skill picks up where that script leaves off — actually verifying the extracted claims
against web sources. The workflow:

1. Run `verify-facts.py` → produces claim list with priorities
2. Use this skill (Mode 2) to verify claims in priority order
3. Write corrections back into the fact-check log

### With Trivia Database generation

When generating new batches of trivia/historical content:

1. Generate entries using the content skill
2. Use this skill (Mode 1) to verify the batch
3. Apply corrections using the standard script
4. For removed entries (date-anchored), regenerate replacements for those specific dates
5. Verify replacements (they have a higher fabrication rate than originals — ~25% vs ~21%)
6. Repeat until all slots are filled with verified content

### With claim-patterns.py (Niche-Specific Claims)

The niche claim-patterns.py files (Softball scores, Parenting prices/locations) define
what to extract. This skill defines how to verify what's been extracted. They're
complementary — claim-patterns finds the needles, this skill checks if they're real.

---

## Reference Files

- `references/apply-corrections.md` — Standard script for applying corrections to datasets
- `references/correction-examples.md` — Real examples of good and bad corrections from production
- `references/error-taxonomy.md` — Common error types by content category with search strategies
