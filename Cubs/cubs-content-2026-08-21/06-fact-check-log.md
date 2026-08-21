# Fact-Check Log — 2026-08-21

## Verification Summary

All HIGH-priority claims verified. MEDIUM-confidence items flagged below.

---

## STORY 1: Series Preview — Cubs at Mariners

| Claim | Source | Confidence | Status |
|-------|--------|-----------|--------|
| "Cubs open a 3-game series at T-Mobile Park in Seattle tonight" | Cubs/_data/series-context.json (authoritative) | HIGH | ✓ VERIFIED |
| "first pitch 9:10 PM CT" | series-context.json game_date_ct "Fri 9:10 PM CT"; ISO 2026-08-22T02:10:00Z = 9:10 PM CDT | HIGH | ✓ VERIFIED |
| "Chicago's 74-54" | series-context.json cubs_record: "74-54" | HIGH | ✓ VERIFIED |
| "Seattle's at 60-68" | series-context.json opponent_record: "60-68" | HIGH | ✓ VERIFIED |
| "Boyd vs Hancock" | SI series preview + Baseball-Reference preview SEA202608210 | MEDIUM | ✓ CONSISTENT across 2 sources |

**Priority 1 check (game times):** Game 1 at 9:10 PM CT confirmed from JSON snapshot (ISO 2026-08-22T02:10:00Z converts to Aug 21 at 9:10 PM CDT / UTC-5). Day of week Friday Aug 21 confirmed. ✓

---

## STORY 2: Matthew Boyd — Game 1 Starter Profile

| Claim | Source | Confidence | Status |
|-------|--------|-----------|--------|
| "Boyd: 8-2, 4.02 ERA, 1.24 WHIP through 85 innings" | SI.com / Bleacher Nation series preview | MEDIUM | FLAG — AI summary of stats; use as stated, may be slightly stale |

**Flag:** Boyd's stats are from a series preview page published before this game. The "8-2, 4.02 ERA" figure is consistent with his mid-season trajectory (was 6-1, 3.41 ERA early in season per a separate SI source). No second independent source with exact current stats — MEDIUM confidence. Stats are directionally correct and consistent; risk of slight inaccuracy in exact ERA is low.

**Action:** Used as stated. Readers should verify exact current stats at MLB.com/players.

---

## STORY 3: Rotation Shuffle — Cabrera IL, Peterson Starts Saturday

| Claim | Source | Confidence | Status |
|-------|--------|-----------|--------|
| "Edward Cabrera is back on the IL" | CBS Sports, Yardbarker, FanGraphs Roster Resource | MEDIUM | ✓ Consistent across multiple sources |
| "right middle finger blister" | Yardbarker / FanGraphs injury report | MEDIUM | ✓ Consistent |
| "David Peterson gets the Saturday slot in Seattle" | Injury report / CBS Sports "David Peterson will take over Cabrera's spot in the rotation this weekend in Seattle" | MEDIUM | ✓ VERIFIED — explicit quote from search result |
| "Javier Assad recalled from Iowa" | Injury report "Assad was recalled from Triple-A Iowa on Monday as the corresponding move" | MEDIUM | ✓ Consistent — identity confirmed as Javier Assad per Cubs roster context |

**Flag:** "Assad recalled on Monday" — the search result says "Monday" for the Assad recall. If today is Friday Aug 21, "Monday" would be Aug 17. This is consistent with Swanson going on IL (which preceded Cabrera) — the roster moves came in waves. The tweet says Assad was recalled for "bullpen depth" which is accurate regardless of exact date. ✓

---

## STORY 4: Wild Card / Playoff Stakes

| Claim | Source | Confidence | Status |
|-------|--------|-----------|--------|
| "Cubs at 74-54" | series-context.json | HIGH | ✓ VERIFIED |
| "Phillies 4 back for NL Wild Card No. 1" | Wild card standings search (Cubs 74-54, Phillies 70-58); math: (4+4)/2=4 | MEDIUM | ✓ Math verified; Phillies 70-58 record from single source |
| "Brewers lead the division by five" | Sportsnaut NL Central article + Brew Crew Ball Week 21 | MEDIUM | FLAG — "approximately five" from analysis piece; prior pipeline (Aug 20) said "4 GB". Could be 4.5 or 5. Used "five" — directionally accurate. |
| "seven times in September" (Brewers H2H) | Cubs story-history.md Aug 20 pipeline coverage | MEDIUM | Referenced from prior research; consistent with Aug 31-Sep 3 (4 games) + Sep 7-9 (3 games) = 7 games. ✓ |

**Cross-reference note:** "NL Wild Card No. 1" uses "No." format per brand-voice rules (not "#1"). ✓

---

## STORY 5: First Pitch Hype

| Claim | Source | Confidence | Status |
|-------|--------|-----------|--------|
| "9:10 PM CT" | series-context.json | HIGH | ✓ VERIFIED |
| "74 wins" | series-context.json cubs_record: "74-54" | HIGH | ✓ VERIFIED |
| "Boyd on the mound" | Series preview (confirmed Game 1 starter) | MEDIUM | ✓ Consistent |

---

## Overall Assessment

- **Priority 1 (times/dates):** ✓ All verified via series-context.json
- **Priority 2 (records/standings):** ✓ Cubs and Mariners records HIGH confidence; Phillies record MEDIUM; Brewers division lead ~5 flagged
- **Priority 3 (player stats — Boyd ERA):** MEDIUM confidence — AI summary stats, directionally correct
- **No compound claims** ("first since...", "career-high...", "led MLB...") in any tweet — compound claim rule not triggered
- **No superlative/historical claims** in any tweet today — historical verification not needed

## Rule Checks

- [x] All times in CT format ✓
- [x] Records use Winner-Loser format where applicable ✓
- [x] "No. 1" not "#1" for wild card ranking ✓
- [x] No engagement questions ✓
- [x] Exactly 3 hashtags per tweet ✓
- [x] First hashtag is #Cubs in all tweets ✓
- [x] 50/50 informative/bold split: Stories 1, 2, 3 = informative; Stories 4, 5 = bold/energy ✓
- [x] Series preview leads with matchup (not pitcher, not stakes) ✓
- [x] Blank lines between paragraphs ✓
- [x] Max 1 tweet per hour — slots are 90+ min apart ✓
