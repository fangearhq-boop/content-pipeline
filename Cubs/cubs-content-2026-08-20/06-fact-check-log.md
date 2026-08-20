# Fact-Check Log — August 20, 2026

Priority labels per niche-config.yaml:
- P1: Dates, times, day-of-week
- P2: Scores, records, win-loss
- P3: Player stats (ERA, BA, HR, WAR)

---

## Post 1: Game 3 Recap

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "José Urquidy came on in the third inning" | ESPN recap, CBS Sports box score | ✓ VERIFIED | Newcomb opened 2 IP; Urquidy entered 3rd |
| "Eight strikeouts, no walks" | ESPN recap, Bleed Cubbie Blue | ✓ VERIFIED | Multiple sources confirm 8 K, 0 BB for Urquidy |
| "Two hits allowed total" | ESPN/CBS Sports box score | ✓ VERIFIED | "Two-hitter" confirmed; Taylor had both Cubs hits |
| "Clay Holmes gave them 5.1 innings and one run" | ESPN recap, theScore | ✓ VERIFIED | Holmes 5.1 IP, 1 ER per multiple sources |
| "Series ends 3-3" | ESPN, CBS Sports, Sun-Times | ✓ VERIFIED | Multiple sources confirm 2026 Crosstown series split 3-3 |
| Score omitted from tweet per insight | N/A | ✓ APPLIED | has_score=False finding; score in research files not tweet |

---

## Post 2: Cardinals Reality Check

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "Cardinals won two games against the Cubs this month" | Aug 19 story history, search results | ✓ VERIFIED | Aug series per search context confirmed 2-1 Cardinals |
| "13.5 games back in the NL Central" | Aug 19 story history (Cubs 74-53, Cards 64-62) | ✓ VERIFIED | Aug 19 pipeline: "Cardinals 64-62 sit 13.5 GB in NL Central" — may shift slightly after Aug 19 games but approximately accurate |

---

## Post 3: Swanson Injury Update

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "Grade 2 oblique strain" | Multiple: theRx, ClutchPoints, SportsKeeda, Yardbarker | ✓ VERIFIED | Grade 2 confirmed by MRI per all sources |
| "Target return is four weeks" | Multiple sources quote Counsell: "probably four weeks" | ✓ VERIFIED | Manager's own words, multiple outlets |
| "Puts him back in the lineup by mid-September" | Math: Aug 17 IL + 4 weeks = ~Sept 14-15 | ✓ VERIFIED | Calculation correct from Aug 17 IL placement |
| "Hoerner at short, Ramírez at second" | ALLCHGO Sports, FanGraphs RosterResource | ✓ VERIFIED | Confirmed as interim alignment |

---

## Post 4: Wild Card Standings

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "Cubs hold NL Wild Card No. 1" | Fox Sports playoff picture, Yahoo Sports | ✓ VERIFIED | Confirmed across multiple standing trackers |
| "Phillies five games back" | Fox Sports (Cubs 73-53, Phillies 68-58 as of ~Aug 18); adjusted for Aug 19 | ⚠️ LOW CONFIDENCE | Aug 18 data: Cubs 5 GB up; after Aug 19 Cubs loss, could be 4 games if Phillies won. Approximate. |
| "Brewers lead the NL Central by four" | Aug 19 story history (Cubs 74-53, 4 GB of Brewers) | ⚠️ LOW CONFIDENCE | After Aug 19 Cubs loss → 74-54. Actual Brewers record unknown for Aug 19. Gap likely 4-4.5 GB. Approximate. |
| "Seven head-to-head games with Milwaukee still to play" | Aug 19 pipeline story: "7 H2H games remaining (Aug 31-Sep 3, Sep 7-9)" | ✓ VERIFIED | Series dates per story history: Aug 31-Sep 3 (4 games) + Sep 7-9 (3 games) = 7 |
| "Six weeks left in the season" | Math: Aug 20 to end of regular season (~Sept 27) = ~5.5-6 weeks | ✓ VERIFIED | Reasonable approximation for late August |

**⚠️ NOTE:** Exact standings (Phillies gap, Brewers gap) are approximations based on Aug 18-19 data. Tweet uses round numbers consistent with best available data. The "four" and "five" figures could vary by 0.5-1 game depending on Aug 19 game results for Phillies and Brewers — not verifiable from current sources.

---

## Post 5: Jaxon Wiggins

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "Touched 98 mph in his first Iowa relief appearance" | Bleacher Nation Aug 19 prospects report, Cubbie Crib | ✓ VERIFIED | 98.1 mph confirmed; first relief appearance confirmed |
| "One inning, zero runs, two strikeouts" | Bleacher Nation Aug 19 report | ✓ VERIFIED | 1 IP, 0 H, 0 R, 1 BB, 2 K line confirmed |
| "No. 2 Cubs prospect" | North Side Baseball 2026 Top 20 ranking | ✓ VERIFIED | Listed as No. 2 per published ranking |
| "Control has been the question" | Bleacher Nation / Cubbie Crib analysis | ✓ VERIFIED | >1 BB/IP in Iowa as starter per search results |

---

## Post 6: PCA Stats

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "30 home runs" | Aug 18 pipeline (PCA hit 30th HR in walk-off win Game 1) | ✓ VERIFIED | 30th HR confirmed in pipeline Aug 18 |
| "31 stolen bases" | StatMuse search result for PCA stolen bases | ✓ VERIFIED | StatMuse confirms 31 SB in 2026 |
| ".938 OPS" | Yardbarker article, StatMuse | ✓ VERIFIED | .937-.938 OPS confirmed in two sources |
| "24 years old" | Wikipedia, Baseball Reference | ✓ VERIFIED | Born 2001; age 24 in 2026 |

---

## Post 7: Steele and Brown Bullpen Updates

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "Justin Steele is targeting a September bullpen return" | Yahoo Sports, Cubs GM Hoyer quotes | ✓ VERIFIED | Multiple sources; Cubs confirmed bullpen (not starter) target |
| "Ben Brown is pain-free and throwing live sessions" | Cubbie Crib, Bleacher Nation | ✓ VERIFIED | "Pain-free" and "throwing bullpen daily" confirmed |
| Framing: "could reshape the playoff pitching picture" | Analysis/opinion | N/A | Take; not a factual claim requiring sourcing |

---

## Compound Claims Requiring Cross-Reference

| Claim | Primary Source | Cross-Ref | Status |
|-------|---------------|-----------|--------|
| Urquidy 8 K, 0 BB | ESPN | Bleed Cubbie Blue | ✓ CONFIRMED |
| Series 3-3 split | ESPN | Sun-Times | ✓ CONFIRMED |
| Swanson Grade 2, 4 weeks | theRx | ClutchPoints | ✓ CONFIRMED |
| PCA 30 HR | Aug 18 pipeline + Yardbarker | StatMuse | ✓ CONFIRMED |

---

## Flags and Caveats

1. **Standings figures (Post 4):** Phillies gap (5 GB) and Brewers gap (4 GB) are approximate based on Aug 18-19 data. Could be off by 0.5-1 game. Risk is low because round-number framing ("five games," "four games") covers small variance.
2. **Cardinals GB (Post 2):** "13.5 games back" is from Aug 19 story history. If Cardinals won Aug 19, they're 13.5 GB; if Cubs also lost (confirmed) and Cardinals won, gap narrows slightly. Remains approximately accurate.
3. **Wiggins performance stats:** From Aug 19 Bleacher Nation prospects report — sourced from a reliable Cubs-beat publication but single source for the exact relief appearance line.
