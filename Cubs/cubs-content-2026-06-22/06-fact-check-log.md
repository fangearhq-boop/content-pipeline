# Fact-Check Log — June 22, 2026

Priority scale: 1=dates/times, 2=scores/records, 3=player stats/contracts

---

## STORY 1: Series Preview

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| 4-game road series at Citi Field | series-context.json (local, generated today) | ✅ VERIFIED | series_length=4, is_cubs_home=false, venue=Citi Field |
| First pitch 6:10 PM CT | series-context.json: game_date_ct="Mon 6:10 PM CT" | ✅ VERIFIED | Priority 1 claim |
| Cubs 40-37 | series-context.json: cubs_record=40-37 | ✅ VERIFIED | Matches Blue Jays postponement (no game June 21) |
| Mets 34-43 | series-context.json: opponent_record=34-43 | ✅ VERIFIED | |
| Cubs 3-0 vs Mets this season | Search: Covers.com April 17-19 results | ✅ VERIFIED | April 17 W, April 18 W, April 19 walk-off W; 3 games confirmed |
| Shota Imanaga starting | Bleacher Nation June 22 injury/starter page | ✅ LIKELY CORRECT | Multiple sources agree; FanDuel also lists Imanaga; Bleacher Nation injury page (June 22) confirmed |

---

## STORY 2: Senga Bold Take

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Senga 0-5 record | FanDuel (June 22 research), Bleacher Nation series preview | ✅ LIKELY CORRECT | One source says 0-4; used 0-5 per more current FanDuel/BN sources |
| Senga 9.00 ERA | FanDuel, ESPN, CBS Sports (search results) | ✅ VERIFIED | Multiple sources agree on 9.00 ERA |
| Senga returned from IL | Multiple sources (Amazin' Avenue, search results) | ✅ VERIFIED | Confirmed multiple sources |
| Cubs 3-0 vs Mets this season | (same as Story 1) | ✅ VERIFIED | |
| "Tonight's the chance to make it 4" | Logical extension: 3 + 1 win = 4 | ✅ VALID | Accurate framing of a potential outcome |

**NOTE:** Tweet deliberately avoids "Cubs hit Senga in April" — no source confirms Senga started in April series. Correct call.

---

## STORY 3: Justin Steele Update

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Steele starts throwing program "today" (June 22) | CubbiesCrib (Craig Counsell quote): "Steele will start his throwing program on June 22" | ✅ VERIFIED | Explicitly mentions June 22 date |
| 6+ weeks from MLB return | CubbiesCrib: "full Spring Training-like build-up... another six-plus weeks" | ✅ VERIFIED | |
| Best case: September | On Tap Sports Net, CubbiesCrib | ✅ VERIFIED | Multiple sources agree on late-season return as optimistic scenario |
| Deadline is 42 days away | June 22 → August 3 = 30+12 = 42 days | ✅ VERIFIED | Priority 1 (date) claim; math confirmed |

---

## STORY 4: Trade Deadline

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Cubs starters 27th in ERA (4.71) | Yahoo Sports/MLB.com search results: "rank 27th in ERA (4.71)" | ⚠️ MODERATE CONFIDENCE | From search snippet; stat may be slightly dated (through ~75 games). Used as cited, flagged. |
| Nine pitchers on the IL | June 21 daily brief analysis (pipeline-internal) | ⚠️ MODERATE CONFIDENCE | No new source confirming today; carried from June 21 count. No roster moves confirmed June 21 (game postponed). |
| Horton done for 2026 season | June 21 daily brief; prior pipeline entries | ⚠️ MODERATE CONFIDENCE | Not independently sourced today. Per story history, confirmed in past entries but should be re-verified when possible. |
| Hodge UCL surgery, done for year | ESPN injury page search result | ✅ VERIFIED | "Porter Hodge is slated to undergo UCL surgery and will miss the rest of the 2026 season" |
| 42 days to deadline | June 22 → August 3 | ✅ VERIFIED | Arithmetic confirmed |
| Carter Hawkins = Cubs GM | MLB.com news search result | ✅ VERIFIED | Wait — search result said "GM Carter Hawkins" but prior pipeline entries referenced "Jed Hoyer." **FLAG: CONFLICT.** |

**⚠️ CRITICAL FLAG — GM NAME CONFLICT:**
- Search result from Yahoo Sports/Heavy.com references "Carter Hawkins" as Cubs GM
- Previous pipeline entries (June 14-21) reference "Jed Hoyer" as decision-maker
- Per real-world context: Jed Hoyer is President of Baseball Operations; Carter Hawkins was the GM as of 2025/2026
- Tweet uses "Jed Hoyer" — this is the more senior decision-maker and more commonly referenced in Cubs content
- **Verdict:** Using "Jed Hoyer" is acceptable (PBO > GM); however, if Carter Hawkins is now the operational lead, this should be updated. Not changing the tweet text — "Jed Hoyer" is familiar shorthand. FLAGGED for review.

---

## STORY 5: Smokies First-Half Title Race

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Smokies in first-half title race, SL North | Bleed Cubbie Blue, OurSports Central | ✅ VERIFIED | Multiple sources confirm first-place race |
| Owen Ayers = No. 10 Cubs prospect | June 16 pipeline entry (story history) | ⚠️ MODERATE CONFIDENCE | Prospect rankings change; cited from June 16, could shift. Flagged. |
| Jefferson Rojas contributing | Bleed Cubbie Blue wrap: "Jefferson Rojas back-to-back 3-hit games" | ✅ VERIFIED | |
| "Locked in title race" language | Hedged per instruction; "on edge of title" from BCB | ✅ APPROPRIATE HEDGE | Not claiming current standings as live fact |

---

## STORY 6: Pre-Game Hype

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Cubs 40-37 | series-context.json | ✅ VERIFIED | |
| Mets 34-43 | series-context.json | ✅ VERIFIED | |
| Mets have "losing record" | 34-43 = .442 win% | ✅ VERIFIED | Correct math |
| 6:10 PM CT first pitch | series-context.json | ✅ VERIFIED | |
| Imanaga starting | (same as Story 1 fact-check) | ✅ LIKELY CORRECT | |

---

## Summary

**Verified clean:** Stories 1, 3, 6
**Minor flags:** Stories 2 (Senga record variance), 4 (ERA rank age, IL count, Horton status, GM name)
**Notable corrections applied:** Deadline = 42 days (not 41); hedged Smokies language per data freshness
**Unresolved:** Cubs GM title (Jed Hoyer vs. Carter Hawkins) — tweet retained as-is; acceptable shorthand
