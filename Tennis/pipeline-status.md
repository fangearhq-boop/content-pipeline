# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-08-09 |
| Writing | Complete (all steps) | 2026-08-09 |
| Fact-check | Complete (verify-facts.py run — 5 stories, 34 claims) | 2026-08-09 |
| Compile | Complete (07-content-data.json — 5 stories, 7 X posts, 5 articles, 22 items) | 2026-08-09 |
| Dashboard | Complete (review-dashboard.html, 22 items) | 2026-08-09 |
| PostPlanner Export | Complete (standard 7 posts 13:03–20:39 ET; TOBI 7 posts) | 2026-08-09 |
| WordPress Publish | Attempted — proxy blocks write to WordPress API (same as all prior runs) | 2026-08-09 |
| Dashboard Push | Not attempted (proxy blocks; same as all prior runs) | 2026-08-09 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-08-09 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-09.xlsx (7 posts 13:03–20:39 ET), tfr-postplanner-tobi-2026-08-09.xlsx (7 TOBI posts)
- **Key stories:** Alexandrova stuns No. 1 Sabalenka 7-6(3), 4-6, 6-4 in Toronto R16 (H2H levels 5-5, title defense over, 2h29m); Swiatek exorcises RG ghost — def. Kostyuk 3-6, 6-1, 6-2 (wins 12/15 games after first set, "I'm in a different place for sure"); FAA withdraws Montreal with back injury (No. 2 seed, home event, can't serve); Montreal QF picture (VdZ def. Hurkacz, Tien def. Paul, Mensik def. Atmane — wide-open generational draw); US Open injury watch (Tomljanovic season over, Paolini Toronto withdrawal, Raducanu out, Alcaraz follow-up)
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON — known issue); image manifest all not_started (expected for imagn source); posting window warnings cosmetic; WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

### 2026-08-06 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-06.xlsx (7 posts 13:07–20:43 ET), tfr-postplanner-tobi-2026-08-06.xlsx (7 TOBI posts)
- **Key stories:** Griekspoor stuns No. 1 Zverev in Montreal R2 (6-7(3), 6-2, 6-4; 8th top-10 win; first NBO top-seed opener upset since 2022); Montreal chaos day — VdZ stuns Medvedev (6-3, 7-6(5)), Tirante ousts Fritz (7-5, 6-3); Fonseca beats Tsitsipas (7-6(3), 7-5; first Brazilian R3 at Canadian Masters since Kuerten); WTA Toronto R3 — Sabalenka (13-match HC streak) vs. Zhang Shuai; Montreal R3 preview (FAA, de Minaur, Fils, Shelton)
- **Issues:** FB posts not picked up by compile script (0 FB posts — known issue); image manifest 5 warnings (not_started — cosmetic); posting window warnings cosmetic; WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

### 2026-08-04 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-04.xlsx (7 posts), tfr-postplanner-tobi-2026-08-04.xlsx (7 TOBI posts)
- **Key stories:** Eala wins WTA DC Open (historic — first Filipino WTA champion; corrects Aug 3 brief prediction); Fritz wins DC Open ATP (11th title); Montreal Day 1 opens; WTA Toronto Day 1 results; Alcaraz Cincinnati return preview
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON); WordPress blocked by proxy; dashboard push blocked by proxy; verify-facts image manifest parsing noted 5 image warnings (status: not_started, expected)
- **Story history:** Updated with all 5 stories

### 2026-08-03 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-03.xlsx (7 posts, 13:02–20:38 ET), tfr-postplanner-tobi-2026-08-03.xlsx (7 TOBI posts)
- **Key stories:** Aug 3 brief predicted Pegula wins WTA final — INCORRECT; actual result was Eala won 4-6, 6-4, 6-0 (covered correctly on Aug 4); Fritz vs. Jódar ATP final preview (result covered Aug 4); WTA Toronto Day 1; Montreal draw preview; hard court swing overview
- **Issues:** WP credentials not found at run time; proxy blocked dashboard push
- **Story history:** NOT updated (no Aug 3 entries in story-history.md; Aug 4 run caught up)

### 2026-08-05 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 2 Tier 2, 1 Tier 3)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-05.xlsx (7 posts, 13:05–20:41 ET), tfr-postplanner-tobi-2026-08-05.xlsx (7 TOBI posts)
- **Key stories:** Draper in tears Montreal R1 loss (Atmane 6-3, 2-6, 6-2 — emotional injury story); Navone saves 11/12 BPs to beat Berrettini (career-best 19th win 2026); Sabalenka opens Toronto 6-3, 6-3 (24/25 hard courts); Swiatek bagels Bejlek 6-0, 6-3 in Toronto R1; Cincinnati preview (Sinner/Alcaraz/Zverev)
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON — known issue); WordPress blocked by proxy; dashboard push blocked by proxy; image manifest all not_started (expected)
- **Story history:** Updated with all 5 stories

### 2026-08-08 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2], Elena Voss [S3, S5])
- **PostPlanner exports:** tfr-postplanner-2026-08-08.xlsx (7 posts 12:57–20:39 ET), tfr-postplanner-tobi-2026-08-08.xlsx (7 TOBI posts)
- **Key stories:** Fonseca (19) beats Ruud to set up Shelton R16 showdown (2 teens in Montreal R16 first since Shapovalov/Tsitsipas 2018); Fernandez stuns Roland Garros champion Andreeva 6-1, 6-4 in Toronto (biggest win since 2021 USO final); Montreal R16 set — Shelton only top-10 remaining (Zverev/Medvedev/Fritz/Hurkacz/Ruud/Paul all eliminated); Kostyuk vs. Swiatek Toronto R16 rematch after Roland Garros upset; Alcaraz withdraws from Cincinnati — US Open title defence in doubt (tenosynovitis, last match April)
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON — known issue); image manifest all not_started (expected for imagn source); WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories
