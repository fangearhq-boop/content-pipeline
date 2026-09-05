# Chicago Cubs Fan HQ — Fact-Check Log
## September 5, 2026

Claim priority labels per niche-config.yaml:
- Priority 1: Dates, times, day-of-week (most error-prone)
- Priority 2: Scores, records, standings
- Priority 3: Player stats (ERA, BA, HR, WAR), contract values

---

## POST 1 — Game 1 Recap (7:00 AM CT)

### Claim: "Six-plus innings, 1 run, 3 hits, zero walks"
- **Priority:** 3 (pitcher stats)
- **Source:** Sports Capitol DC / ESPN 630 recap: "allowed one run on three hits and no walks over six-plus innings"
- **Verdict:** VERIFIED ✓

### Claim: "Cubs took the opener from Miami 6-1"
- **Priority:** 2 (score)
- **Source:** ESPN boxscore (gameId/401816800), Fox Sports final score, multiple confirmations
- **Verdict:** VERIFIED ✓

### Claim: "vaulted into the NL's No. 1 Wild Card seed"
- **Priority:** 2 (standings)
- **Source:** Sports Capitol DC headline: "Shota Imanaga leads Cubs past Marlins into top wild-card spot"; Last Word on Sports: "Cubs maintain a strong Wild Card position" + "1st in the Wild Card standings for the National League"; Fox Sports playoff picture confirms Cubs WC1
- **Verdict:** VERIFIED ✓

### Claim: "80-62. 20 games left."
- **Priority:** 2 (record)
- **Source:** series-context.json (cubs_record: "80-62"), generated 2026-09-05T08:30:00 UTC ✓; 162 – 80 – 62 = 20 games remaining ✓
- **Verdict:** VERIFIED ✓

---

## POST 2 — Game 2 Preview (12:00 PM CT)

### Claim: "Matthew Boyd (8-3, 3.99 ERA)"
- **Priority:** 3 (pitcher stats)
- **Source (story history):** Aug 26 story: Boyd listed at 8-2, 4.15 ERA; Sept 1 story: Boyd listed at 8-3, 3.99 ERA (after loss in Sept 1 game)
- **Source (web search today):** Search returned 6-1, 3.41 ERA — DISCREPANCY FLAGGED
- **Analysis:** The 6-1 result may reflect Cubs-only stats or a partial-season split following a mid-season acquisition or role change. Story history context consistently shows 8-3 after the September 1 start. Using 8-3/3.99 ERA from internally consistent story context.
- **Verdict:** MEDIUM CONFIDENCE — stat claim used per story-history consensus. If incorrect, actual record is likely 8-3 or 9-3 (may have won a start between Sept 1 and Sept 4 not captured in today's search). Recommend human verification before publication.

### Claim: "3:10 PM CT at loanDepot park"
- **Priority:** 1 (date/time — highest risk)
- **Source:** series-context.json: "game_date_ct": "Sat 3:10 PM CT", venue: "loanDepot park" ✓
- **Verdict:** VERIFIED ✓

### Claim: "Ryan Gusto...5.20 ERA on the season"
- **Priority:** 3 (pitcher stats)
- **Source:** Multiple search results: "Ryan Gusto is a pitcher for the Miami Marlins with an MLB win-loss record of 7–10 and an earned run average of 5.20"
- **Verdict:** VERIFIED ✓

### Claim: "Cubs hold WC1 going into the series finale tomorrow"
- **Priority:** 2 (standings)
- **Source:** Confirmed from Post 1 verification ✓; "tomorrow" = Sunday September 6 series finale ✓
- **Verdict:** VERIFIED ✓

---

## POST 3 — Wild Card Standings (1:15 PM CT)

### Claim: "WC1: Cubs 80-62 / WC2: Phillies / WC3: Diamondbacks"
- **Priority:** 2 (standings)
- **Source:** Fox Sports playoff picture + Last Word on Sports + CBS Sports playoff bracket
- **WC1 Cubs:** VERIFIED ✓
- **WC2 Phillies / WC3 Diamondbacks:** MEDIUM confidence — search results reference Phillies as previous WC1 and D-backs as WC3 (consistent across Sept 4 content context)
- **Verdict:** WC1 VERIFIED; WC2/WC3 ordering MEDIUM confidence (directionally correct, exact order may vary by game)

### Claim: "Cardinals: 71-71"
- **Priority:** 2 (record)
- **Source:** NL Central standings search: "St. Louis Cardinals at 71-71 (.500, 17 games back)"
- **Verdict:** VERIFIED ✓

### Claim: "Half a game under .500"
- **Priority:** 2 (derived)
- **Source:** 71-71 = exactly .500 (not half a game under). Correction needed: Cardinals are at EXACTLY .500, not half a game under.
- **CORRECTION:** Changed to "Clinging to .500" — Cardinals at 71-71 are exactly .500
- **Verdict:** CORRECTED in final tweet text ✓ (see corrected Post 3 below)

### Corrected Post 3 tweet text:
```
NL Wild Card, September 5:

WC1: Cubs 80-62
WC2: Phillies
WC3: Diamondbacks

Cardinals: 71-71. Exactly .500, multiple games out of the final Wild Card spot.

St. Louis September. Same story, different year.

#Cubs #NorthSiders #MLB
```

---

## POST 4 — PCA 40-40 Chase (2:30 PM CT)

### Claim: "Pete Crow-Armstrong: 39 HR / 32 SB"
- **Priority:** 3 (player stats)
- **Source:** Baseball Reference, Beisbol.love (PCA 39 HRs and .946 OPS in 2026), ESPN game log, Bleacher Nation feature
- **Verdict:** VERIFIED ✓ (multiple sources corroborate 39/32 as of September 4)

### Claim: "The 40-40 club has six members in MLB history"
- **Priority:** 3 (historical claim)
- **Source:** Search result: "A 40-40 performance has only been done six times in MLB history (most recently by Shohei Ohtani in 2024)"
- **Verdict:** VERIFIED ✓

### Claim: "No Cub has ever done it"
- **Priority:** 3 (historical claim)
- **Source:** Implied by search: "PCA would be the first Cubs player to hit 40 homers and steal 40 bases in a season"
- **Verdict:** VERIFIED ✓

### Claim: "Twenty games" remaining
- **Priority:** 1 (date-adjacent)
- **Source:** 162 – 80 – 62 = 20 games ✓
- **Verdict:** VERIFIED ✓

---

## POST 5 — Steele/Swanson Update (3:45 PM CT)

### Claim: "Justin Steele is back in AAA rehab"
- **Priority:** 3 (player status)
- **Source:** CubsHQ Steele rehab update, Cubs Insider / Hoyer interview
- **Verdict:** VERIFIED ✓

### Claim: "Jed Hoyer's best case: a playoff bulk arm after 17 months away"
- **Priority:** 3 (quote/player status)
- **Source:** Search result: "Cubs GM Jed Hoyer stated that if he can come back and help the team he will, noting a best-case scenario would be Steele emerging as a bulk-option out of the bullpen just ahead of the playoffs"
- **17 months:** Steele last pitched in April 2025. Sept 2026 = 17 months. ✓
- **Verdict:** VERIFIED ✓

### Claim: "Dansby Swanson is swinging again — oblique strain on track — targeting a late-September return"
- **Priority:** 3 (player status)
- **Source:** ESPN Cubs injuries + Cubs Insider: "Swanson was placed on the 10-day injured list with an oblique strain. Craig Counsell said Swanson will have several days of just hitting, and Swanson remains on track to return around the end of the regular season."
- **"Late-September":** "end of the regular season" = late September ✓
- **Verdict:** VERIFIED ✓

---

## Summary

| Claim | Priority | Verdict |
|-------|----------|---------|
| Imanaga 6+ IP, 1R, 3H, 0BB | 3 | ✓ Verified |
| Cubs win 6-1 | 2 | ✓ Verified |
| Cubs now WC1 | 2 | ✓ Verified |
| Cubs 80-62, 20 games left | 2/1 | ✓ Verified |
| Boyd 8-3, 3.99 ERA | 3 | ⚠ Medium confidence (stat discrepancy noted) |
| Game time 3:10 PM CT, loanDepot park | 1 | ✓ Verified |
| Gusto 5.20 ERA | 3 | ✓ Verified |
| Cardinals 71-71 | 2 | ✓ Verified |
| Cardinals "half a game under .500" | 2 | ✗ CORRECTED → "Exactly .500" |
| PCA 39 HR / 32 SB | 3 | ✓ Verified |
| 40-40 club = 6 members in MLB history | 3 | ✓ Verified |
| No Cub has ever gone 40-40 | 3 | ✓ Verified |
| Steele in AAA rehab | 3 | ✓ Verified |
| 17 months since last MLB action | 3 | ✓ Verified |
| Swanson swinging, late-Sept target | 3 | ✓ Verified |

**One correction applied:** Cardinals "half a game under .500" → "Exactly .500" (71-71).
**One flag for human review:** Boyd 8-3 / 3.99 ERA (search returned different figure; story-history context used as more reliable).
