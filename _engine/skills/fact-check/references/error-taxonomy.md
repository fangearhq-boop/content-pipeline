# Error Taxonomy — Common Errors by Content Type

Based on production data across 2,100+ trivia entries and multiple daily pipeline runs.
Use this to prioritize what to search for and how to search for it.

---

## Sports Historical Content (Trivia Database)

### Error rates by category (from production)

| Category | Error Rate | Most Common Error |
|----------|-----------|-------------------|
| On This Day (MLB) | 26.5% | Wrong date (off by days to months) |
| On This Day (NBA) | 10.6% | Wrong date, wrong opponent |
| Record Book | ~15% | Wrong stat value, wrong holder |
| Player Milestones | ~20% | Wrong date of achievement |
| Legendary Games | ~12% | Wrong opponent, wrong score |
| Traded Away Too Soon | ~10% | Misleading trade framing |
| Draft History | ~8% | Wrong pick number, wrong year |

### Error types ranked by frequency

1. **Date errors (40% of all errors)**
   - Wrong year (most common): event happened in 1990, entry says 1987
   - Wrong month: confusing when event happened vs when it was announced
   - Wrong day: off by 1-3 days, especially for multi-day events
   - Search strategy: `"[player] [event] [year]"` — verify year first, then month/day

2. **Stat errors (20% of all errors)**
   - Wrong number: "500 home runs" when actual is 376
   - Wrong ranking: "first to achieve" when actually second or third
   - Wrong opponent: right game, wrong team listed
   - Search strategy: `"[player] career stats"` or `"[player] [specific stat]"`

3. **Fabrication (5% of all errors but highest severity)**
   - Event never happened at all
   - Player never played for that team
   - Trade never occurred
   - Search strategy: search for the specific claim. If nothing comes up AND the claim
     seems specific enough that it should have coverage, suspect fabrication. Cross-check
     with `"[player] career"` or `"[player] transactions"`.

4. **Misleading framing (15% of all errors)**
   - "First ever" when actually first in a specific context
   - "Legendary" game that was actually routine
   - Overstated significance
   - Search strategy: search for the superlative claim specifically

5. **Wrong context (10% of all errors)**
   - Right event, wrong surrounding details
   - Correct trade but wrong package details
   - Correct milestone but wrong game context
   - Search strategy: read the full source, not just the headline

---

## Daily Pipeline Content (Niche Launches)

### By claim priority

**Priority 1 claims (dates, times, locations, prices) — ~8% error rate**
- Times wrong because of timezone confusion (ET vs CT vs MT)
- Event dates off by one day
- Prices from outdated sources
- Addresses with wrong street numbers
- Search strategy: go to the official source (team website, event page, school district site)

**Priority 2 claims (scores, records, statistics) — ~12% error rate**
- Scores transcribed incorrectly from sources
- Records listed as "program record" without verification
- Win-loss records not updated after recent games
- Search strategy: check the official box score or standings page

**Priority 3 claims (rankings, org references) — ~3% error rate**
- Rankings from previous week, not current
- Organization names slightly wrong
- Search strategy: check the current week's poll/ranking

### By content file

| File | Risk Level | What to check |
|------|-----------|---------------|
| 00-daily-brief.md | High | Story dates, tier assignments, scheduling |
| 03-social-posts-x.md | Medium | Character count (≤280), claim accuracy, hashtags |
| 04-social-posts-facebook.md | Medium | Claim accuracy, event details |
| articles/*.html | High | All factual claims, especially in leads and headlines |
| 05-image-concepts.md | Low | Photo search terms (wrong player name = wrong photo) |

---

## Search Strategies by Error Type

### For date verification
```
Best:  "[player full name] [event] [year]"
       "[team] [event type] [month] [year]"
Also:  "[sport] history [month] [day]"
       "on this day [sport] [month] [day]"
```

### For stat verification
```
Best:  "[player] career statistics baseball-reference"
       "[player] career stats basketball-reference"
Also:  "[player] [specific stat] all-time"
       "[team] all-time [stat category] leaders"
```

### For event verification (did it happen?)
```
Best:  "[specific event claim]" (in quotes for exact match)
       "[player] [team] trade [year]"
Also:  "[player] career timeline"
       "[player] transactions history"
```

### For daily pipeline claims
```
Best:  [official source URL directly] (team site, school district, event page)
       "[event name] [city] [date]"
Also:  "[venue name] events [month] [year]"
       "[organization] [announcement type] [year]"
```

---

## Red Flags That Suggest Fabrication

Watch for these patterns — they strongly predict fabricated entries:

- **Round-number milestones that seem too clean**: "500th home run" for a player
  who actually hit 376. AI tends to invent round-number milestones.
- **Famous player + unlikely event**: Kirby Puckett traded to the Mets (never
  happened — he played his entire career with the Twins).
- **Duplicate fabrication**: The same false claim appearing multiple times in a batch
  (we saw the Fisk 500 HR claim twice in one MLB batch).
- **Offseason events in peak season dates**: A January signing listed as happening
  in July, or a trade deadline event listed in February.
- **Highly specific details with no source**: "Scored 47 points on 18-of-23 shooting"
  — if these exact details can't be found, the specificity itself is a red flag.
- **Events described with AI-typical phrasing**: "cementing his legacy", "etched in
  history", "in a game that would go down as" — these suggest generated content
  rather than sourced facts.
