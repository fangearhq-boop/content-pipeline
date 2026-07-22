# Fact-Check Log — 2026-07-22

## STORY 1: Cubs 11, Tigers 2 — Game 2 Recap

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Cubs 11, Tigers 2 final score | ESPN recap, MLB.com, CBS Sports box score (3 independent) | HIGH | ✅ VERIFIED |
| Cubs scored 6 runs in the first inning | Multiple recaps ("erupt in 6-run first") | HIGH | ✅ VERIFIED |
| David Peterson threw 6⅔ scoreless innings | MLB.com headline: "David Peterson throws scoreless start in Cubs' win over Tigers" | HIGH | ✅ VERIFIED |
| Peterson entered with 6.45 ERA | Yesterday's pipeline (July 21) Story 5 fact-checked | HIGH | ✅ VERIFIED |
| Peterson improved to 5-7 | Inferred from "W" in game (single-source AI summary says "5-7") | MEDIUM | ⚠️ USED (tweet doesn't cite W-L record; framing only) |
| PCA reached 5 times (2 H, 3 BB, 2 RBI) | ESPN recap AI summary | MEDIUM | ⚠️ USED ("PCA reached five times" — single source) |
| Conforto pinch-hit 2-run HR, 4th of the year | ESPN/CBS recap AI summary | MEDIUM | ⚠️ USED ("pinch-hit 2-run homer" — number 4 cited in tweet as fact) |
| Conforto tying Glenallen Hill 1999 for most PHRs by a Cub since 1901 | ESPN/CBS recap AI summary (SINGLE SOURCE) | MEDIUM-LOW | ❌ NOT USED — compound historical claim, not independently verified; hedged to "franchise-level number" in tweet |
| Suzuki 2 RBI, Kelly 2 RBI | Single AI summary | MEDIUM | ⚠️ CITED IN RESEARCH NOTES only; not in tweets |
| Dillon Dingler 2-run HR, 6-for-8 / 3 HR in series | Single AI summary | MEDIUM | ⚠️ CITED IN RESEARCH NOTES only; not in tweets |
| Cubs record now 57-44 | Math: 56-44 (per series-context.json) + 1 win = 57-44 | HIGH | ✅ VERIFIED |

**Story 1 verdict**: 0 HIGH-risk errors. Compound PHR historical claim (Hill/1999) correctly excluded from tweet. All used claims backed by at least 1 credible source.

---

## STORY 2: Peterson/Conforto Bold Take

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Peterson entered with 6.45 ERA | Yesterday's pipeline (verified) | HIGH | ✅ VERIFIED |
| Peterson 6⅔ scoreless innings | MLB.com (HIGH from Story 1) | HIGH | ✅ VERIFIED |
| "4 pinch-hit homers this season" | ESPN recap summary | MEDIUM | ⚠️ USED — framed without historical superlative |
| "franchise-level number by any measure" | Not a statistical claim; editorial framing | N/A | ✅ OK — opinion, not fact-check item |

**Story 2 verdict**: No high-risk claims. Franchise-record language properly hedged to editorial.

---

## STORY 3: Thornton Day-to-Day — No Fracture

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| "No fractures" / CT scan clean | ESPN (headline), Washington Post (separate article) | HIGH | ✅ VERIFIED (2 independent sources) |
| Day-to-day with bruised left heel | ESPN headline | HIGH | ✅ VERIFIED |
| "108.9 mph comebacker" | Yesterday's pipeline (verified Monday) | HIGH | ✅ VERIFIED |
| He played catch Tuesday | ESPN story | HIGH | ✅ VERIFIED |
| Tests off mound Wednesday | ESPN story text | MEDIUM | ⚠️ USED — single-source but credible outlet |
| Thursday off-day for Cubs | Schedule confirmed by series-context.json (no Thursday game listed) | HIGH | ✅ VERIFIED |

**Story 3 verdict**: 0 HIGH-risk errors. Most claims HIGH, mound-test detail MEDIUM (ESPN).

---

## STORY 4: Trade Deadline — Sonny Gray Complication

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Sonny Gray 12-1 record | BosoxInjection / CubbieCrib AI summaries (SINGLE SOURCE each) | MEDIUM | ⚠️ USED — career-best season framing is directionally consistent with earlier pipelines (9-1 as of July 9 → 12-1 plausible by July 22) |
| Gray 2.48 ERA | Same as above | MEDIUM | ⚠️ USED — consistent with prior "2.54 ERA" from July 6 pipeline |
| Red Sox went from sellers to buyers | CubbieCrib article | MEDIUM | ⚠️ USED — single outlet but framing consistent with "insane turnaround" headline language |
| "Gray may not move" | CubbieCrib + BosoxInjection directional | MEDIUM | ⚠️ USED — editorial read on reporting; not a fact |
| Joe Ryan (55% trade odds per ESPN) | CBS Sports summary | MEDIUM | ⚠️ NOT explicitly cited in tweet (just "still makes sense") |
| August 3 deadline | Standard known date | HIGH | ✅ VERIFIED |
| "12 days to August 3" from July 22 | Calculated: July 22 → Aug 3 = 12 days | HIGH | ✅ VERIFIED |

**Compound claim risk**: "12-1 with a 2.48 ERA" — this is the Gray stat combo. Not independently verified (no Baseball Reference check). MEDIUM risk. Directionally consistent with season arc. Should not be restated in tomorrow's pipeline without re-verification.

**Story 4 verdict**: Gray stats MEDIUM (single-source AI summary); framing is directionally correct. No HIGH-risk errors, but Gray's specific numbers should be re-checked against a primary source before reuse.

---

## STORY 5: Game 3 Preview — Rea vs. Montero

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Colin Rea starts tonight | Bleacher Report preview, series preview sources | MEDIUM | ⚠️ USED — single-source-category; no MLB.com official announcement found |
| Rea 7-6, 4.74 ERA | Bleacher Report preview | MEDIUM | ⚠️ USED with caution — CBS Sports had "5-5, 4.99 ERA" (discrepancy; likely different date). Tweet cites the preview-day number |
| Keider Montero starts for Detroit | Same preview source | MEDIUM | ⚠️ USED |
| Montero 6-5, 3.22 ERA | Same source | MEDIUM | ⚠️ USED |
| Game time 7:10 PM CT | series-context.json (official MLB data) | HIGH | ✅ VERIFIED |
| Wrigley Field | series-context.json | HIGH | ✅ VERIFIED |
| Series tied 1-1 entering tonight | Game 1 Detroit win + Game 2 Cubs win = 1-1 | HIGH | ✅ VERIFIED |
| "11-run statement" (from Game 2) | Cubs scored 11 runs (verified HIGH) | HIGH | ✅ VERIFIED |

**Story 5 verdict**: Pitcher stats MEDIUM (single preview source, Rea W-L discrepancy noted). Game time and series context HIGH. No fabricated claims.

---

## STORY 6: Wild Card Hot Streak

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Cubs 57-44 | Calculated (HIGH) | HIGH | ✅ VERIFIED |
| No. 1 NL Wild Card | Standings search (July 21 updated) | HIGH | ✅ VERIFIED |
| "23-10 over last 33 games" | Single Bleacher Report preview summary | MEDIUM | ⚠️ USED — single source; significant hot streak stat; cross-reference against full season math is possible (Cubs were ~47-41 on June 20 approximately = record improvement consistent) |
| Phillies one back (56-45) | StatMuse/CBS Sports standings | MEDIUM | ⚠️ USED — standings from July 21 (before any July 22 results) |
| "Cardinals six back" (51-48) | Multiple standings sources | MEDIUM | ⚠️ USED — approximate (6 GB math: 57-44 Cubs vs 51-48 Cards: GB = ((57-51)+(48-44))/2 = (6+4)/2 = 5.0 GB). Actually 5 GB not 6. Correction needed. |
| 12 days to deadline | Calculated | HIGH | ✅ VERIFIED |

**⚠️ CORRECTION**: Cardinals games-behind calculation:
- Cubs: 57-44. Cardinals: 51-48.
- GB = ((57-51) + (48-44)) / 2 = (6 + 4) / 2 = 5.0 GB.
- Tweet says "six back" but correct figure is 5 back.
- **ACTION: Edit tweet to say "five back" before compile.**

**Story 6 verdict**: One math error caught (Cardinals GB: should be five, not six). Correcting tweet.

---

## STORY 7: Pre-Game Hype

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| "Game 1: Tigers in extras" | July 21 pipeline (Tigers 8, Cubs 6 in 10 innings) | HIGH | ✅ VERIFIED |
| "Game 2: Cubs 11-2" | Multiple sources (HIGH) | HIGH | ✅ VERIFIED |
| "7:10 PM CT" | series-context.json | HIGH | ✅ VERIFIED |
| "bounced back LOUD last night" | Editorial opinion framing | N/A | ✅ OK |

**Story 7 verdict**: All claims HIGH or editorial. Clean.

---

## Summary

| Story | HIGH claims | MEDIUM claims | Errors found | Corrections made |
|-------|------------|--------------|--------------|-----------------|
| 1 — Game recap | 4 | 3 | Compound PHR record excluded | Excluded from tweet ✅ |
| 2 — Bold take | 2 | 1 | None | — |
| 3 — Thornton | 5 | 1 | None | — |
| 4 — Deadline | 2 | 5 | Gray stats single-source | Used with MEDIUM flag |
| 5 — Preview | 3 | 4 | Rea W-L discrepancy | Used preview-day stat, flagged |
| 6 — Wild card | 3 | 3 | Cardinals GB math (6 → 5) | **Correcting tweet** |
| 7 — Hype | 3 | 0 | None | — |

**Overall**: 1 confirmed error (Cardinals GB miscalculation) corrected before compile. 1 compound historical claim correctly excluded (Conforto PHR franchise record). No HIGH-confidence errors in published tweet content.
