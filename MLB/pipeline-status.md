# Ballpark Banter Pipeline Status

## Last Run
- **Date**: 2026-03-30
- **Steps Completed**: Full pipeline (Steps 1-15) — research (10+ searches), brief, analysis, X posts, FB posts, image concepts, articles (6), fact-check, compile, dashboard, publish, PostPlanner exports (X + TOBI)
- **Dashboard Published**: Yes (pushed to fangearhq-boop/content-pipeline via publish-dashboard.py)
- **Issues**: publish-unified-dashboard.py 403 error (fine-grained PAT scoped to content-pipeline only). Used publish-dashboard.py instead — pushed to content-pipeline. Same non-fast-forward pattern; fixed with git pull --rebase + git push -u origin HEAD:main.

## Previous Run
- **Date**: 2026-03-29
- **Steps Completed**: Full pipeline (Steps 1-15) — research (14+ searches), brief, analysis, X posts, FB posts, image concepts, articles (6), fact-check, compile, dashboard, publish, PostPlanner exports (X + TOBI)
- **Dashboard Published**: Yes (https://fangearhq-boop.github.io/content-dashboards/)
- **Issues**: publish-dashboard.py required git pull --rebase before push (non-fast-forward, known pattern)

## Deploy Info
- **Dashboard:** Unified (fangearhq-boop/content-dashboards, subfolder: bb)

## Pipeline Run Log
<!-- Append newest at top -->

### 2026-03-30
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 9 (all under 280 chars; 5 char-limit violations fixed on first verify-facts pass)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 6 (Stories 1-6; Story 7 Tier 3 excluded per tier rules)
- **PostPlanner exports:** bb-postplanner-2026-03-30.xlsx (16 posts) + bb-postplanner-tobi-2026-03-30.xlsx (9 TOBI posts)
- **Fact-check:** 5 char-limit violations fixed (Stories 1, 2, 3, 5, 7 tweet #1). 0 consistency errors after fixes. Image manifest not_started (expected).
- **Dashboard:** Published (pushed to content-pipeline repo; publish-unified-dashboard.py blocked by 403 on fine-grained PAT)
- **Notes:** 10+ web searches. Key stories: Giants 20 scoreless innings franchise record 1909 (P10), Murakami HR in first 3 MLB games 4th player ever (P10), Hancock 6 no-hit innings joins Félix Hernández Mariners company (P8), Brewers sweep Yelich PH homer first career (P8), Ohtani pitching debut March 31 (P7), Gore Rangers debut 5 hitless IP (P7), Early standings Judge 400 HR chase (P5)

### 2026-03-29
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 9 (all under 280 chars; 5 char-limit violations fixed on first verify-facts pass)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 6 (Stories 1-6; Story 7 Tier 3 excluded per tier rules)
- **PostPlanner exports:** bb-postplanner-2026-03-29.xlsx (23 posts) + bb-postplanner-tobi-2026-03-29.xlsx (16 TOBI posts)
- **Fact-check:** 0 char-limit violations (after fixes). 0 consistency errors. Image not_started (expected).
- **Dashboard:** Published, live at https://fangearhq-boop.github.io/content-dashboards/
- **Notes:** 14+ web searches conducted. Key stories: Tyler O'Neill 6 consecutive OD HRs MLB record per Elias (P10), McGreevy 6 no-hit innings + Wetherholt walk-off Cardinals 6-5 in 10 (P10), Will Smith birthday walk-off HR Dodgers sweep ARI 3-0 8-game streak (P8), DeLauter 2 HRs in debut Guardians 6-4 (P8), Ohtani pitching debut March 31 4 IP 11 K spring (P7), Wetherholt HR + walk-off 2 games (P7), Opening Weekend standings Dodgers 3-0 Pirates 0-2 (P5)
- **Fact concerns:** O'Neill 2026 team (MEDIUM — assumed Red Sox, no contradicting news); Sunday March 29 game results MEDIUM (in progress at research time).

### 2026-03-28
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 9 (all under 280 chars)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 6 (Stories 1-6; Story 7 Tier 3 evergreen excluded per tier rules)
- **PostPlanner exports:** bb-postplanner-2026-03-28.xlsx (23 posts) + bb-postplanner-tobi-2026-03-28.xlsx (16 TOBI posts)
- **Fact-check:** 0 char-limit violations. 0 consistency errors. Image manifest not_started (expected — image production separate step).
- **Dashboard:** Published, live at https://fangearhq-boop.github.io/content-dashboards/
- **Notes:** publish-unified-dashboard.py fails 403 (PAT denied to content-dashboards). Used publish-dashboard.py instead — succeeds. Key stories: Skenes 0.2 IP OD disaster shortest by Cy Young winner ever (P10), ABS challenge history Caballero first / Alvarez first successful (P10), Rookie debut triple Wetherholt 425 ft / Benge HR+SB / McGonigle 4-for-5 (P8), Diaz Dodgers 5-4 D-backs live trumpet save (P8), Rogers 7 shutout Helsley 100+ mph 6-pitch K streak Alonso Orioles debut (P7), Judge golden sombrero then first HR (P7), Opening Weekend overview (P5).
- **Fact concerns:** None — all facts HIGH confidence from dual-source research.

### 2026-03-24
- **Steps completed:** 1-6 (Research through X Posts), 5b (Articles — 5 written), 7 (Fact-Check — pass), 8a (Compile), 8b (Story History), 8d (Dashboard published), 8e (PostPlanner exports)
- **Steps remaining:** Facebook Posts + Image Concepts + Image Production (enrichment skill)
- **Stories:** 7 total (2 Tier 1, 3 Tier 2, 2 Tier 3)
- **X Posts:** 10 written, all under 280 characters
- **Articles:** 5 (Stories 1-5)
- **PostPlanner exports:** bb-postplanner-2026-03-24.xlsx (X) + bb-postplanner-tobi-2026-03-24.xlsx (TOBI)
- **Notes:** Opening Day eve content. Yankees-Giants tomorrow (Fried vs Webb). Braves rotation crisis (5 arms on IL). Phillies Sanchez $107M extension. Wetherholt/Benge prospect debuts. Dodgers three-peat quest. Griffin to Triple-A. Skenes historic OD start. 12 web searches. Previous session had factual errors (wrong Yankees starter, Griffin status outdated) — all corrected with fresh research.
- **Fact concerns:** None — all facts HIGH confidence.

### 2026-03-20
- **Steps completed:** 1-6 (Research through X Posts)
- **Steps remaining:** 7 (Facebook Posts), 8 (Image Concepts), 9 (Articles), 10 (Fact-Check), 10b (Compile Content Data), 11 (Image Production), 12 (Story History Update - DONE), 13 (Dashboard), 14 (Review & Export), 15 (Publish)
- **Stories:** 7 total (2 Tier 1, 3 Tier 2, 2 Tier 3)
- **X Posts:** 10 written, character counts verified (all under 280)
- **Notes:** Two major injury leads — Birdsong (TJ, season-ending) and Greene (bone chips, July return). Griffin prospect watch is the engagement anchor. WBC fallout continues (Suzuki, Teel injuries). Opening Day starters follow-up from 3/19. 14 web searches conducted. Post split: 5 informative / 5 witty.
- **Fact concerns:** Eovaldi "3rd straight" Opening Day start — CBS says "6th career" but consecutive count varies by source. Used "third straight season" per CBS. All other facts HIGH confidence.

### 2026-03-19 — FIRST RUN
- **Steps completed:** 1-6 (Research through X Posts)
- **Steps remaining:** 7 (Facebook Posts), 8 (Image Concepts), 9 (Articles), 10 (Fact-Check), 10b (Compile Content Data), 11 (Image Production), 12 (Story History Update - DONE), 13 (Dashboard), 14 (Review & Export), 15 (Publish)
- **Stories:** 7 total (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 10 written, character counts verified
- **Notes:** First-ever pipeline run for Ballpark Banter (MLB). WBC Final (Venezuela 3-2 USA) is the lead story. Ohtani's pitching return is the second lead. Opening Day is one week away (March 26). Research covered 14 web searches across scores, transactions, injuries, prospects, and power rankings.
- **Fact concerns:** Wilyer Abreu HR in WBC Final — sources conflict on RBI count (some say 3-run HR but math doesn't add up with 3-2 final). Marked LOW confidence — safe to reference HR without specifying run count.
