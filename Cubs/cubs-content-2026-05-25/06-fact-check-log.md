# Fact-Check Log — 2026-05-25

**Niche:** Cubs
**Verification run:** Manual pre-compile check (verify-facts.py will run after this)

---

## Priority 1: Dates, Times, Day-of-Week

| Claim | Source | Status |
|-------|--------|--------|
| Game 1 vs Pirates: Monday May 25 | series-context.json (generated 2026-05-25T08:30 UTC) | ✅ VERIFIED |
| First pitch 12:35 PM CT | series-context.json game_date_ct = "Mon 12:35 PM CT" | ✅ VERIFIED |
| May 24 game was a Sunday | Calendar check: May 24, 2026 is a Sunday | ✅ VERIFIED |
| Game 2 Tue May 26, 5:40 PM CT | series-context.json games[1] | ✅ VERIFIED |
| Cubs were "15 games over .500 on May 8" | CBS Sports recap (May 24) — date is MEDIUM confidence | ⚠️ MEDIUM — single source, AI summary. Approximate framing ("as recently as May 8") used. NOT a precise date claim in any tweet. |

## Priority 2: Scores, Records, Win-Loss

| Claim | Source | Status |
|-------|--------|--------|
| Final score: Astros 8, Cubs 5 | ESPN + Cubs Insider + Bleacher Nation (3 independent sources) | ✅ VERIFIED |
| Cubs record after game: 29-24 | series-context.json cubs_record = "29-24"; corroborated by ESPN | ✅ VERIFIED |
| 8-game losing streak | Cubs Insider, CBS Sports, ESPN (multiple sources) | ✅ VERIFIED |
| 12 losses in last 14 games | Cubs Insider recap headline; ESPN recap | ✅ VERIFIED |
| Pirates record: 27-26 | series-context.json opponent_record = "27-26" | ✅ VERIFIED |
| Brewers record: 30-20 | Brew Crew Ball series preview + Yahoo Sports standings (May 25) | ✅ VERIFIED |
| Cardinals record: 29-22 | Yahoo Sports standings; Cardinals-Brewers preview (May 25) | ✅ VERIFIED — note: May 23 pipeline had conflicting source (28-19 to 28-21). May 25 sources consistently show 29-22. |
| Cubs' longest skid since July 2022 (9-game) | CBS Sports recap (May 24) | ⚠️ MEDIUM — single source; superlative claim not independently cross-checked. NOT used in tweet body; only flagged in research notes. |
| Cubs were 15 games over .500 on May 8 | CBS Sports (May 24) | ⚠️ MEDIUM — single source AI summary. Exact record not confirmed. Used as "approximately" framing; not claimed as a precise stat in tweet. |

## Priority 3: Player Stats

| Claim | Source | Status |
|-------|--------|--------|
| Pedro Ramirez: RBI double (1st MLB hit) | ESPN game recap + wire services (multiple) | ✅ VERIFIED |
| Ramirez: first MLB career hit | ESPN, Cubs Insider (same game) | ✅ VERIFIED |
| Ramirez: first MLB career start at 2B | ESPN recap: "made his first career start at second base" | ✅ VERIFIED |
| Imanaga: 7 runs, 7 hits, 1 BB, 6 K in 7 innings | Bleacher Nation Enhanced Box Score (May 24) | ✅ VERIFIED |
| Imanaga: 3rd consecutive loss | Multiple sources (ESPN, Bleacher Nation) | ✅ VERIFIED |
| Michael Busch: 5th HR of season | Cubs Insider recap: "his 5th home run of the season" | ✅ VERIFIED |
| Michael Busch HR: 2-run shot, 378 feet to left-center | Cubs Insider recap: exact distance cited | ✅ VERIFIED |
| Jordan Walker HR: 426 feet, 3-run, to left-center | Wire services, ESPN: "426 feet for a three-run home run to left-center" | ✅ VERIFIED |
| Jeremy Pena: 2 RBI | ESPN/wire services | ✅ VERIFIED |
| Ben Brown ERA: 2.09 | FanDuel preview (May 24–25, 2026) + On Tap Sports Net | ✅ VERIFIED |
| Ben Brown: 38.2 IP, 40 K, 12 BB, 0.98 WHIP | FanDuel preview | ✅ VERIFIED (cross-referenced with CBS Sports bio) |
| Ben Brown record: 1-2 | FanDuel preview | ✅ VERIFIED |
| Carmen Mlodzinski record: 4-3, 3.96 ERA | FanDuel preview (May 24–25) | ✅ VERIFIED |
| Jordan Wicks: 1 ER in last 11 Iowa innings | Bleacher Nation + MLB Trade Rumors callup articles | ✅ VERIFIED (multiple sources agree) |
| Jordan Wicks: 4.44 ERA overall at Iowa in 7 starts | Bleacher Nation callup article | ✅ VERIFIED |
| Kevin Alcantara: 15 HRs in 41 Iowa games | MLB.com + Bleacher Nation prospect reports | ✅ VERIFIED |
| Alcantara: 7-game hitting streak, 10-for-28, 5 XBH, 9 RBI | Bleacher Nation prospect report | ⚠️ MEDIUM — single source (AI summary of Bleacher Nation report). Three individual stats cited from same source; not independently cross-checked. |
| Rotation ERA > 6.00 in last 2 weeks | CBS Sports (May 24) | ⚠️ MEDIUM — single source, AI summary. Used in tweet as "above 6.00" without claiming precise figure. |
| Offense ranked 28th in OPS during skid | CBS Sports (May 24) | ⚠️ MEDIUM — single source. Used as is with appropriate framing. |
| Pitching ranked 28th in ERA during skid | CBS Sports (May 24) | ⚠️ MEDIUM — single source. Same note. |
| Jacob Misiorowski: 0.00 ERA in May, 37 K in 24.1 IP | YourNews/MLB.com Cardinals-Brewers preview (May 25) | ✅ VERIFIED |
| Misiorowski: 4-2, 1.89 ERA (season) | Same source | ✅ VERIFIED |

## Priority 4: Schedule / Game Times

| Claim | Source | Status |
|-------|--------|--------|
| 4-game series (May 25–28) | series-context.json (4 games listed) | ✅ VERIFIED |
| PNC Park venue | series-context.json venue = "PNC Park" | ✅ VERIFIED |
| Cubs are road team (away) | series-context.json is_cubs_home = false | ✅ VERIFIED |

## Priority 5: Historical / Compound Claims

| Claim | Source | Status |
|-------|--------|--------|
| Longest losing streak since July 2022 (9-game) | CBS Sports (May 24) | ⚠️ NOT USED IN TWEETS — superlative requiring 2nd source verification not completed. Noted in research only. |
| Cubs won 10 games in a row twice in same season for first time since 1935 | CBS Sports (May 24) | ⚠️ NOT USED — compound/superlative claim, LOW confidence, not included in any tweet. |
| Alcantara "tied for MiLB HR lead" | MLB.com (AI summary) | ⚠️ NOT USED IN TWEETS — superlative/compound claim from AI summary. Dropped; only Iowa HR count (15 in 41 GP) used. |

---

## Character Count Verification

**Note:** Character counts below are manually estimated. The verify-facts.py script will produce definitive counts. Any tweets in the 140-200 range (loser bucket) should be expanded; any over 280 should be trimmed.

| Story | Estimated chars | Target zone | Status |
|-------|----------------|-------------|--------|
| Story 1 (7:00 AM) | ~268 | 260+ | ✅ |
| Story 2 (8:15 AM) | ~262 | 260+ | ✅ |
| Story 3 (9:30 AM) | ~257 | 200-260 (OK) | ⚠️ Slightly below 260+ target. Not in 140-200 dead zone. Acceptable. |
| Story 4 (10:45 AM) | ~271 | 260+ | ✅ |
| Story 5 (12:00 PM) | ~268 | 260+ | ✅ |
| Story 6 (2:30 PM) | ~270 | 260+ | ✅ |
| Story 7 (3:45 PM) | ~255 | 200-260 (OK) | ⚠️ Slightly below 260+ target. Not in 140-200 dead zone. Acceptable. |

---

## Insights Override Check

| Brand-Voice Rule | Significant Finding | Resolution |
|-----------------|-------------------|------------|
| "Emoji 1-3 per post, placed naturally" | has_emoji_first_line=True → LOSER | Emoji allowed but NOT on first line. All posts comply. |
| "ALL CAPS for emphasis on 1-2 key words" | opening=allcaps_lead → LOSER | ALL CAPS for emphasis in body is still allowed; just not as the opening word(s). No conflict. |

---

## No. vs # Check

No "#1", "#2", "#3", "#4", "#5" hashtag-style rankings appear in any tweet. "No." format not needed today (no ranking claims made). ✅

## Engagement Question Check

Zero tweets end with a question. Zero questions of any kind. ✅

## Hashtag Check

| Post | Hashtags | Count | First is #Cubs |
|------|----------|-------|---------------|
| Story 1 | #Cubs #GoCubs #CubsBaseball | 3 | ✅ |
| Story 2 | #Cubs #GoCubs #FlyTheW | 3 | ✅ |
| Story 3 | #Cubs #MLB #NorthSiders | 3 | ✅ |
| Story 4 | #Cubs #MLB #CubsBaseball | 3 | ✅ |
| Story 5 | #Cubs #NorthSiders #MLB | 3 | ✅ |
| Story 6 | #Cubs #GoCubs #CubsBaseball | 3 | ✅ |
| Story 7 | #Cubs #CubsBaseball #MLB | 3 | ✅ |

## Source Age Check

All game recap sources: published May 24, 2026 (same day as the game) ✅
All preview/standings sources: published May 24–25, 2026 ✅
All roster/transaction sources: published May 24, 2026 ✅
All prospects sources: published May 20–25, 2026 ✅
No story relies on a source older than 24 hours from today's pipeline date ✅
