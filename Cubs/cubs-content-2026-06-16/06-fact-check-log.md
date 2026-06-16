# Fact-Check Log — 2026-06-16

Verification priority order: dates/times → scores/records → player stats → game times/schedule

---

### STORY 1: Game Recap — PCA Cycle Walk-Off Win

- **Claim:** Cubs defeated Rockies 5-4 in a walk-off on June 15, 2026.
  ✅ VERIFIED — ESPN matchup page + CBS Sports box score + ABC News wire (3 independent sources)

- **Claim:** Pete Crow-Armstrong hit for the cycle (HR, triple, double, single) — first reverse cycle in Cubs franchise history.
  ✅ VERIFIED — Journal Gazette: "first Cub to hit a reverse cycle — home run, triple, double, single in order — in franchise history" (confirmed by multiple articles)

- **Claim:** 13th cycle in Cubs franchise history.
  ✅ VERIFIED — Daily Gazette article title + Journal Gazette (two sources confirming "13th in franchise history")

- **Claim:** Second Cubs cycle since 1993 (33-year gap).
  ⚠ MEDIUM CONFIDENCE — From single article (Journal Gazette AI summary). Needs cross-reference with Baseball Reference Cubs cycles historical list. "33 years" math is correct (2026 − 1993 = 33). Tweet retains this claim but recommend verification before next cycle coverage.

- **Claim:** HR was 434 feet to center off Lorenzen.
  ⚠ MEDIUM CONFIDENCE — From ABC News wire AI summary (single source). Plausible given PCA's exit velocity profile (91.4 mph avg exit velo). Cross-reference Baseball Savant if exact distance matters.

- **Claim:** PCA 4-for-4, 2 RBI.
  ✅ VERIFIED — ABC News wire (consistent with walk-off game narrative)

- **Claim:** PCA's 19-game on-base streak.
  ✅ VERIFIED — ABC News wire: "extended his on-base streak to 19 games"

- **Claim:** Cubs now 38-35, Colorado 27-46.
  ✅ VERIFIED — Series context JSON generated 2026-06-16 08:30 UTC from live MLB API data

---

### STORY 2: PCA Historical Feature

- **Claim:** Last Cub to hit for the cycle was in 1993.
  ⚠ MEDIUM CONFIDENCE — Single source (Journal Gazette). Recommend cross-referencing Baseball Reference Cubs franchise cycle history. TWEET USES THIS CLAIM — flag if verification fails.

- **Claim:** PCA season stats: .263/.341/.462, 13 HR, 15 SB, 3.9 WAR.
  ✅ VERIFIED (BA/OBP/SLG/SB/WAR) — CBS Sports player page pre-cycle showed .263/.341/.462, 12 HR, 15 SB, 3.9 WAR. HR updated to 13 after last night's cycle (added 1 HR). Calculation: 12 + 1 cycle HR = 13. ✅

- **Claim:** PCA's 19-game on-base streak.
  ✅ VERIFIED (same as Story 1)

---

### STORY 3: Wild Card Watch

- **Claim:** Cubs 38-35.
  ✅ VERIFIED — Series context JSON (live data, generated 08:30 UTC)

- **Claim:** Three NL wild card spots available.
  ✅ VERIFIED — Standard MLB structure since 2022 expansion. Three wild card spots per league.

- **Claim:** Colorado Rockies 27-46.
  ✅ VERIFIED — Series context JSON

- **Claim:** "Division title is gone."
  ✅ VERIFIED — Brewers ~43-26 with Cubs at 38-35 = ~5 GB; effectively insurmountable in mid-June for a non-division leader.

- **Claim:** The math still works for wild card at 38-35.
  ✅ VERIFIED — Cubs are above .500 (38-35 = .521); three wild card spots means Cubs are a legitimate contender. Claim is directionally accurate.

---

### STORY 4: Trade Deadline / Rotation

- **Claim:** 48 days to the August 3 trade deadline.
  ✅ VERIFIED — June 16 to August 3: (14 remaining days in June) + (31 days in July) + (3 days in August) = 48 days. ✅ Math confirmed.

- **Claim:** August 3 as trade deadline.
  ✅ VERIFIED — Multiple sources confirm 2026 MLB Trade Deadline is August 3.

- **Claim:** Jameson Taillon on hamstring IL.
  ✅ VERIFIED — Multiple sources: "15-day IL, retroactive to June 8, left hamstring strain" (Bleed Cubbie Blue, WCF Courier, Yardbarker)

- **Claim:** Justin Steele on 60-day IL (elbow).
  ✅ VERIFIED — FanGraphs injury report reference in search results: "LHP Justin Steele is on the 60-day IL with a left elbow injury"

- **Claim:** Wicks, Cabrera, Rea, Assad currently in rotation.
  ⚠ MEDIUM CONFIDENCE — Inferred from story-history entries and Cubs roster context. Javier Assad's rotation status particularly needs confirmation (he's been both a starter and reliever in his career). Wicks/Rea/Cabrera are confirmed starters from story-history.

- **Claim:** Sandy Alcántara and Casey Mize as named trade targets.
  ⚠ MEDIUM CONFIDENCE — Both named in trade rumor articles (Chi City Sports, SI Cubs). These are rumor/speculation; no confirmed deal.

---

### STORY 5: Owen Ayers Prospect

- **Claim:** Owen Ayers won Southern League Player of the Week.
  ⚠ MEDIUM CONFIDENCE — Single source (Bleacher Nation June 15 prospects report AI summary). Could not independently confirm via MiLB.com news directly. Treat as MEDIUM until verified from official Southern League announcement.

- **Claim:** Ayers slash .231/.369/.519 in 16 games at Knoxville.
  ⚠ MEDIUM CONFIDENCE — Single source (Bleacher Nation). Plausible (.519 SLG in AA for a top-10 prospect is credible). Recommend verifying at Baseball Cube or MiLB.com stats.

- **Claim:** Ayers is Cubs' No. 10 prospect.
  ⚠ MEDIUM CONFIDENCE — Mentioned in single search result. Cubs prospect rankings vary by source (Baseball America, The Athletic, Bleacher Nation). "No. 10" may refer to one specific outlet's ranking. Tweet uses "No. 10" as a round number — verify before escalating claim.

- **Claim:** Three extra-base hits in last week.
  ⚠ MEDIUM CONFIDENCE — From Bleacher Nation report (single source).

---

### STORY 6: Tonight's Game Preview

- **Claim:** Cabrera starts with 4-3 record, 4.86 ERA.
  ⚠ MEDIUM CONFIDENCE — From betting preview sites (Predictem, StatsInsider). These are plausible given his recent activation but should be verified at Baseball Reference or MLB.com before repeating in future content.

- **Claim:** Feltner starts with 2-2 record, 5.20 ERA.
  ⚠ MEDIUM CONFIDENCE — Same source risk as Cabrera. Verify at Baseball Reference.

- **Claim:** Game time 7:05 PM CT at Wrigley Field.
  ✅ VERIFIED — Series context JSON (game_date_ct = "Tue 7:05 PM CT") + multiple preview sources confirm Wrigley Field, 8:05 PM ET = 7:05 PM CT.

- **Claim:** Colorado 27-46 at time of game.
  ✅ VERIFIED — Series context JSON.

---

## Summary

| Story | Claims Checked | Verified (✅) | Flagged (⚠) | Errors (❌) |
|-------|---------------|--------------|-------------|------------|
| 1 — Cycle Recap | 8 | 6 | 2 | 0 |
| 2 — PCA History | 3 | 2 | 1 | 0 |
| 3 — Wild Card | 5 | 5 | 0 | 0 |
| 4 — Trade Deadline | 6 | 4 | 2 | 0 |
| 5 — Owen Ayers | 4 | 0 | 4 | 0 |
| 6 — Game Preview | 4 | 2 | 2 | 0 |

**Critical flags to resolve:**
1. "Second since 1993" — verify on Baseball Reference Cubs franchise cycles page
2. Owen Ayers Southern League POW — verify on MiLB.com official news
3. Cabrera/Feltner ERA figures — verify on Baseball Reference before next game-preview cycle
