# Fact-Check Log — September 4, 2026

## Verification Summary

| Priority | Claim | Confidence | Source | Status |
|----------|-------|------------|--------|--------|
| 1 | Final score: Cubs 2, Brewers 1 | HIGH | FOX6 Milwaukee, WTMJ, mlb.com/cubs/news headline ("Kevin Gausman strikes out 9 in 7 innings") | ✅ VERIFIED |
| 1 | Gausman: 7 IP, 1 ER, 9 K | HIGH | MLB.com headline + FOX6/WMTV recap articles | ✅ VERIFIED |
| 1 | PCA HR No. 39 (2-run, 3rd inning) | HIGH | Multiple game recap sources (FOX6, WMTV, mlb.com) | ✅ VERIFIED |
| 1 | Cubs split the 4-game Brewers series | HIGH | WTMJ article states "salvaged a split" | ✅ VERIFIED |
| 1 | Cubs 8 games behind Brewers in NL Central | HIGH | WTMJ search result text: "eight games behind in the division standings" | ✅ VERIFIED |
| 2 | Cubs record: 79-62 | HIGH | series-context.json (official MLB data, generated same morning) | ✅ VERIFIED |
| 2 | Marlins record: 71-70 | HIGH | series-context.json | ✅ VERIFIED |
| 2 | 3-game series at loanDepot park | HIGH | series-context.json (game_pk confirmed 3 games Sept 4-6) | ✅ VERIFIED |
| 2 | Game 1 time: 6:10 PM CT | HIGH | series-context.json game_date_ct="Fri 6:10 PM CT" | ✅ VERIFIED |
| 2 | 21 games remaining | HIGH | Math: 79+62=141 played; 162-141=21 | ✅ VERIFIED |
| 2 | PCA HR total: 39 | HIGH | Multiple game recap sources | ✅ VERIFIED |
| 2 | PCA SB total: 32 (needs 8 more) | MEDIUM | pipeline-status.md from Sept 3 states "32 SB"; no direct Sept 4 source found | ⚠️ MEDIUM — tweet states "8 steals"; acceptable if 32 SB confirmed |
| 2 | NL WC: Phillies WC1, Cubs WC2, AZ WC3 | MEDIUM | CBS Sports/Bleacher Report playoff picture articles (AI summaries — not direct page reads) | ⚠️ MEDIUM — framing used is categorical ("holding No. 2 spot") not specific GB numbers |
| 2 | Cardinals 3+ games out of WC3 | MEDIUM | Search result: "St. Louis is 3.5 games back" (of WC3, i.e., AZ) | ⚠️ MEDIUM — tweet says "three-plus games out with a month left" (editorial framing, defensible) |
| 3 | Gausman 60% whiff rate on splitter | MEDIUM | Yahoo Sports/FOX sports search result summaries | ⚠️ MEDIUM — cited in tweet; not verified from primary stat page |
| 3 | Steele: 1.2 IP, 1 ER, 90.3 mph avg fastball | MEDIUM | SI.com and Bleacher Nation article summaries | ⚠️ MEDIUM — not verified from primary box score |
| 3 | Steele last competitive outing: April 2025 (~17 months ago) | MEDIUM | Search result: "last taking the mound on April 7, 2025" | ⚠️ MEDIUM — confirmed by multiple sources, reasonable |
| 3 | Swanson resumed swinging Aug. 31 | MEDIUM | CBS Sports / ESPN injury report (AI summary) | ⚠️ MEDIUM — consistent across multiple sources |
| 3 | Wiggins: 4 scoreless, 7 K in 16 batters, 96-98 mph | MEDIUM | cubbiescrib article summary; consistent with pipeline-status.md | ⚠️ MEDIUM — exact figures from one primary article |
| 3 | 32 HRs since June 1 (PCA) | MEDIUM | lastwordonsports.com AI search summary | ⚠️ MEDIUM — not cross-referenced; used in tweet |
| 3 | Cubs have 198 HR (league-leading) | MEDIUM | Search result summary | ⚠️ MEDIUM — NOT used in tweets (only mentioned in research files) |

---

## Claims Excluded (LOW Confidence)

| Claim | Reason Excluded | Action |
|-------|----------------|--------|
| "No Cubs player has ever had a 40-40 season" | LOW — from AI search summary only; not verified from Baseball Reference or MLB Records | EXCLUDED from tweet copy. PCA tweet does not include this claim. |
| "40-40 accomplished only 6 times in MLB history" | LOW — AI summary only | EXCLUDED from tweet copy |
| Gausman's Win-Loss record | Slight source discrepancy noted in pipeline-status.md from Sept 3 | NOT included in tweets |

---

## Cross-Reference Checks (Compound Claims)

**"Cubs took the series finale 2-1 and split with the NL-leading Brewers":**
- Score "2-1": HIGH (multiple sources)
- "Split": HIGH (WTMJ confirmed)
- "NL-leading Brewers": Brewers have the best record in NL (87-53 entering Sept 3, won the series 3-1); MEDIUM — not directly cited but consistent with prior pipeline entries
→ ✅ PASS (no compound claim crossing entities)

**"Needs 1 more HR and 8 steals over 21 games to join the 40-40 club":**
- 1 HR needed: HIGH (39 confirmed, needs 40)
- 8 steals needed: MEDIUM (32 SB from pipeline, needs 40)
- 21 games: HIGH (math verified)
→ ⚠️ MEDIUM PASS — conditional on 32 SB being accurate

---

## Format Compliance

| Rule | Status |
|------|--------|
| Each tweet ≤ 280 chars | ✅ All 7 tweets checked and under 280 |
| Exactly 3 hashtags per tweet on one line | ✅ Confirmed all 7 |
| First hashtag is #Cubs | ✅ Confirmed all 7 |
| No "#1" or "#2" (use "No. 1", "No. 2") | ✅ Confirmed — "No. 2" used; "No. 39" for PCA HR count |
| No engagement questions | ✅ No questions asked in any tweet |
| Score format: winner first | ✅ "Cubs took the series finale 2-1" / "Cubs won 2-1" |
| Time format: "H:MM AM/PM CT" | ✅ "6:10 PM CT" used |
| Blank line before hashtags | ✅ Confirmed all 7 |
| Blank line between sections | ✅ Confirmed all 7 |
| No filler content | ✅ All 7 tweets anchored to specific news/stats |
| opening=statement avoided | ✅ All tweets open with fragment, number, label, or stat line |
| has_stat in every tweet | ✅ All 7 tweets contain ≥1 numeric stat |

---

## Character Counts (Verified)

| Tweet | Approx Char Count | Status |
|-------|------------------|--------|
| Story 1 (Series Preview) | 251 | ✅ |
| Story 2 (Gausman Recap) | 265 | ✅ |
| Story 3 (PCA 40-40) | 205 | ✅ |
| Story 4 (Wild Card) | 260 | ✅ |
| Story 5 (Steele/Swanson) | 252 | ✅ |
| Story 6 (Wiggins) | 248 | ✅ |
| Story 7 (Game Hype) | 229 | ✅ |
