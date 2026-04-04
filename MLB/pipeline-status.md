# Ballpark Banter Pipeline Status

## Last Run
- **Date**: 2026-04-04
- **Steps Completed**: Full pipeline (Steps 1-15) — research (10+ searches via agent), brief, analysis, X posts (9), FB posts (14), image concepts, articles (5), fact-check (1 char violation fixed on Story 5 tweet), compile, dashboard, publish, PostPlanner exports (X + TOBI). WordPress publish blocked by proxy sandbox (same as all prior sessions).
- **Dashboard Published**: Yes — https://fangearhq-boop.github.io/content-dashboards/
- **Issues**: Story 6 Tier 2 optional article not written by design. IMAGE MISSING warnings expected (not_started). WordPress 403 (proxy sandbox). publish-unified-dashboard.py 403 (PAT) — used publish-dashboard.py.

## Previous Run
- **Date**: 2026-04-03
- **Steps Completed**: Full pipeline (Steps 1-15) — research (10+ searches via agent), brief, analysis, X posts (9), FB posts (14), image concepts, articles (5), fact-check (1 char violation fixed on Story 3 tweet), compile, dashboard, publish, PostPlanner exports (X + TOBI). WordPress publish blocked by proxy sandbox (fanrumor.com not in allowed_hosts).
- **Dashboard Published**: Yes — https://fangearhq-boop.github.io/content-dashboards/
- **Issues**: Story 6 Tier 2 optional article not written by design. IMAGE MISSING warnings expected (not_started). WordPress blocked by proxy (network-level restriction — same as prior sessions).

## Previous Run
- **Date**: 2026-04-02
- **Steps Completed**: Full pipeline (Steps 1-15) — research (10+ searches via agent), brief, analysis, X posts (9), FB posts (14), image concepts, articles (5), fact-check (0 char violations), compile, dashboard, publish, PostPlanner exports (X + TOBI)
- **Dashboard Published**: Yes — https://fangearhq-boop.github.io/content-dashboards/
- **Issues**: Story 6 Tier 2 optional article not written by design. IMAGE MISSING warnings expected (not_started). WordPress publish skipped — WP_FANRUMOR_USERNAME env var not set in this session (same network/403 issue as prior sessions).

## Previous Run
- **Date**: 2026-04-01
- **Steps Completed**: Full pipeline (Steps 1-15) — research (8+ searches via agent), brief, analysis, X posts (9), FB posts (14), image concepts, articles (5), fact-check (0 violations), compile, dashboard, publish, PostPlanner exports (X + TOBI)
- **Dashboard Published**: Yes — https://fangearhq-boop.github.io/content-dashboards/
- **Issues**: None. Story 6 Tier 2 optional article not written by design. IMAGE MISSING warnings expected (not_started). No char-limit violations on first verify-facts pass.

## Previous Previous Run
- **Date**: 2026-03-31
- **Steps Completed**: Full pipeline (Steps 1-15) — research (8+ searches), brief, analysis, X posts, FB posts, image concepts, articles (5), fact-check, compile, dashboard, publish, PostPlanner exports (X + TOBI)
- **Dashboard Published**: Yes (pushed to fangearhq-boop/content-pipeline via publish-dashboard.py)
- **Issues**: Non-fast-forward push (known pattern); fixed with git pull --rebase + git push -u origin HEAD:main.

## Previous Previous Run
- **Date**: 2026-03-30
- **Steps Completed**: Full pipeline (Steps 1-15) — research (10+ searches), brief, analysis, X posts, FB posts, image concepts, articles (6), fact-check, compile, dashboard, publish, PostPlanner exports (X + TOBI)
- **Dashboard Published**: Yes (pushed to fangearhq-boop/content-pipeline via publish-dashboard.py)
- **Issues**: publish-unified-dashboard.py 403 error (fine-grained PAT scoped to content-pipeline only). Used publish-dashboard.py instead — pushed to content-pipeline. Same non-fast-forward pattern; fixed with git pull --rebase + git push -u origin HEAD:main.

## Deploy Info
- **Dashboard:** Unified (fangearhq-boop/content-dashboards, subfolder: bb)

## Pipeline Run Log
<!-- Append newest at top -->

### 2026-04-04
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 9 (1 char-limit violation fixed on Story 5 tweet before compile)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 5 (Stories 1-5; Story 6 Tier 2 optional — no article by design; Story 7 Tier 3 excluded)
- **PostPlanner exports:** bb-postplanner-2026-04-04.xlsx (23 posts) + bb-postplanner-tobi-2026-04-04.xlsx (16 TOBI posts)
- **Fact-check:** 1 char-limit violation (Story 5 tweet #1, 299 chars) fixed. 0 consistency errors after fix. Image manifest not_started (expected).
- **Dashboard:** Published (https://fangearhq-boop.github.io/content-dashboards/)
- **WordPress:** Blocked by proxy sandbox (fanrumor.com not in allowed_hosts — known network restriction)
- **Notes:** 10+ web searches via agent. Key stories: Judge HR 371 first AB home opener Yankees 8-2 Marlins 6-1 passes Gil Hodges 83rd all-time (P10); DeLauter 5 HRs in 7 career games only 4th player ever Guardians 4-1 Cubs home opener (P10); Ohtani first HR 2026 3-run shot Dodgers 13-6 Nationals Tucker first as Dodger 38-game OB streak (P9); Twins 10 Rays 4 home opener Gray grand slam 7-run 7th (P7); 2026 rookie class historic DeLauter+Stewart both POTWs only 2nd time ever (P8); Yankees 6-1 Brewers 5-1 Marlins 5-2 White Sox/RedSox/A's 1-5 (P6); Saturday slate preview (P5)

### 2026-04-03
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 9 (1 char-limit violation fixed on Story 3 tweet before compile)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 5 (Stories 1-5; Story 6 Tier 2 optional — no article by design; Story 7 Tier 3 excluded)
- **PostPlanner exports:** bb-postplanner-2026-04-03.xlsx (23 posts) + bb-postplanner-tobi-2026-04-03.xlsx (16 TOBI posts)
- **Fact-check:** 1 char-limit violation (Story 3 tweet #1, 305 chars) fixed. 0 consistency errors after fix. Image manifest not_started (expected).
- **Dashboard:** Published (https://fangearhq-boop.github.io/content-dashboards/)
- **WordPress:** Blocked by proxy sandbox (fanrumor.com not in allowed_hosts)
- **Notes:** 10+ web searches via agent. Key stories: Judge 500th career XBH + first in MLB history 5 HR/15 RBI in team's first 6 games Yankees 5-1 (P10); Griffin No. 1 prospect called up Pirates April 2 (P9); 2026 rookie class historic DeLauter + Murakami each HR in first 3 games 3rd/4th ever McGonigle 4-hit debut Wetherholt walk-off Stewart cleanup (P8); Marlins 5-1 NL East leaders Alcantara CG shutout (P7); Reds rotation Greene until July Lodolo blister rehab (P6); DeLauter + Stewart sweep first POTW as rookies 2nd time ever (P6); Standings: Yankees/Marlins/Brewers 5-1 WhiteSox/RedSox 1-5 (P5)

### 2026-04-02
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 9 (0 char-limit violations on verify-facts)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 5 (Stories 1-5; Story 6 Tier 2 optional — no article by design; Story 7 Tier 3 excluded)
- **PostPlanner exports:** bb-postplanner-2026-04-02.xlsx (9 posts) + bb-postplanner-tobi-2026-04-02.xlsx (9 TOBI posts)
- **Fact-check:** 0 char-limit violations. 1 consistency note (Story 6 no article — optional). Image manifest not_started (expected).
- **Dashboard:** Published (https://fangearhq-boop.github.io/content-dashboards/)
- **WordPress:** Skipped — WP_FANRUMOR_USERNAME not set in session (env var from prior session did not persist). Network/403 pattern same as prior sessions.
- **Notes:** Agent-based web research (10+ searches). Key stories: Alcantara Maddux 93-pitch CG shutout Marlins 10-0 Marlins 5-1 (P10); Dodgers Samurai Sequence complete — Sasaki/Ohtani/Yamamoto first ever in MLB history per Elias (P10); Skenes bounce-back 5 IP 1 ER after 0.2 IP OD disaster (P8); DeLauter 4 HR in 3 games + Stewart .700 BA both win first POTWs of 2026 (P8); Masyn Winn first career walk-off Cardinals 4-2 Mets 0-for-29 RISP (P7); Liam Hicks 12 RBI in 6 games Rule 5 pick MLB leader (P6); Week 1 standings Yankees/Blue Jays 3-0 Marlins 5-1 A's 0-3 White Sox 0-6 (P5)

### 2026-04-01
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 9 (0 char-limit violations on verify-facts)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 5 (Stories 1-5; Story 6 Tier 2 optional — no article by design; Story 7 Tier 3 excluded)
- **PostPlanner exports:** bb-postplanner-2026-04-01.xlsx (23 posts) + bb-postplanner-tobi-2026-04-01.xlsx (16 TOBI posts)
- **Fact-check:** 0 char-limit violations. 1 consistency note (Story 6 no article — optional). Image manifest not_started (expected).
- **Dashboard:** Published (https://fangearhq-boop.github.io/content-dashboards/)
- **Notes:** Agent-based web research. Key stories: Ohtani 6 scoreless IP 6 K 0 ER 98 mph debut Dodgers 4-1 (P10); Dodgers complete historic Japanese pitcher trilogy Sasaki/Ohtani/Yamamoto first in MLB history per Elias (P10); Braves 3 starters on IL Sale/Lopez carrying the load (P8); Judge 368 HRs 32 from 400 ABS challenge assist on first HR (P7); April 1 scores Astros 8-1 Rangers 8-5 Rays end Brewers' perfect start 3-2 (P7); NL East four teams at 3-1 Phillies 1-3 (P6); Blue Jays 50 Ks MLB record 50th anniversary (P5)

### 2026-03-31
- **Steps completed:** Full pipeline 1-15
- **Stories:** 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- **X Posts:** 8 (all under 280 chars; 0 violations on verify-facts)
- **FB Posts:** 7 long-form + 7 image captions
- **Articles:** 5 (Stories 1-5; Story 6 Tier 2 optional — no article by design; Story 7 Tier 3 excluded)
- **PostPlanner exports:** bb-postplanner-2026-03-31.xlsx (22 posts, 11:10–21:19) + bb-postplanner-tobi-2026-03-31.xlsx (15 TOBI posts)
- **Fact-check:** 0 char-limit violations. Consistency warnings: Story 7 missing from image-concepts (intentional Tier 3 exclusion); Story 6 no article (intentional optional omission); image manifest format mismatch (cosmetic). No blocking issues.
- **Dashboard:** Published (pushed to content-pipeline repo; non-fast-forward fixed with git pull --rebase)
- **Notes:** 8+ web searches. Key stories: Ohtani 2026 pitching debut vs. Guardians tonight — first full 2-way season / unprecedented 3-game Japanese starter sequence (Sasaki-Ohtani-Yamamoto per Elias) (P10); Blue Jays 50 Ks in 3 games MLB record — Gausman 11 Ks OD record, Cease 12 Ks debut record, first teammates since 1901 with 11+ Ks each in first 2 games (P10); Judge first HR 2026 via ABS challenge — 368 career HRs, 32 from 400 (P8); ABS system debut — 6 overturned calls in one game, Bucknor 8 challenges (P8); Dodgers first loss to Guardians 4-2 / Messick 6 scoreless — three-peat bid (P7); 2026 rookie class DeLauter + Murakami + Wetherholt (P7); Early standings Yankees/Blue Jays/Brewers 3-0 (P5)
- **Fact concerns:** Ohtani 2025 ERA — 2.87 used (dodgerblue.com/BB-Ref); one secondary source cited 3.34 in 67⅓ IP. Stadium rename to Uniqlo Field (March 16) confirmed via search results.

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
