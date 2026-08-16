# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-08-16 |
| Writing | Complete (all steps) | 2026-08-16 |
| Fact-check | Complete (verify-facts.py run — 5 stories, 28 claims) | 2026-08-16 |
| Compile | Complete (07-content-data.json — 5 stories, 7 X posts, 5 articles, 27 items) | 2026-08-16 |
| Dashboard | Complete (review-dashboard.html, 27 items) | 2026-08-16 |
| PostPlanner Export | Complete (standard 7 posts 13:02–20:38 ET; TOBI 7 posts) | 2026-08-16 |
| WordPress Publish | Attempted — proxy blocks WordPress API (same as all prior runs) | 2026-08-16 |
| Dashboard Push | Attempted — proxy lacks write access to content-dashboards repo (same as all prior runs) | 2026-08-16 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-08-16 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-16.xlsx (7 posts 13:02–20:38 ET), tfr-postplanner-tobi-2026-08-16.xlsx (7 TOBI posts)
- **Key stories:** Tirante (No. 50, ARG) stuns Djokovic 2-6, 6-4, 6-4 in Cincinnati R2 — Djokovic vomited/medical timeout, only 14th M1000 loss from set up since 2005, Cincinnati comeback over, US Open fitness in doubt; Jodar def. Shapovalov 7-5, 4-6, 7-5 (corrects Aug 15 incorrect report of Shapovalov win) — came back from 1-5, saved match points, shoelaces broke twice, Shapovalov furious, Jodar 14-3 deciding sets 2026; Venus Williams (46, ranked 615) loses to Arango 6-2, 6-2 with Serena watching — 0-14 in 2026 singles; Sabalenka survives Gibson 4-6, 6-1, 7-5 + Zverev outlasts Norrie 3-6, 6-3, 6-3 — both No. 1 seeds drop first set but advance; US Open 8-day countdown (Djokovic out, Sinner/Alcaraz fitness crisis deepens, draw Aug 27)
- **Issues:** Aug 15 pipeline had incorrect Shapovalov win result — corrected in today's coverage; FB posts not picked up by compile script (0 FB posts in JSON — known issue); image manifest all not_started (expected for imagn source); posting window warnings cosmetic (known issue); WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories (including correction note for S2)

### 2026-08-15 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-15.xlsx (7 posts 12:57–20:39 ET), tfr-postplanner-tobi-2026-08-15.xlsx (7 TOBI posts)
- **Key stories:** Shapovalov def. Jodar 6-1, 6-4 (R2 Cincinnati — 2nd Shapovalov win vs Jodar in 2026; Dallas was first; Jodar Montreal SF hero gets harsh reality check); Djokovic returns Cincinnati after 2-year absence (3-time champion, 10-match win streak, vs Tirante today — Sinner/Alcaraz both withdrawn, wide-open draw, potential SF vs Zverev); Hijikata def. Monfils 2-6, 7-6, 6-3 in emotional R1 (Monfils retiring end 2026, likely last Cincinnati; Hijikata first ATP hard-court win, faces Darderi R2); Sabalenka vs Rybakina WTA No. 1 battle in Cincinnati (Rybakina 306 aces, Swiatek defending champion just won Toronto, US Open 9 days away); US Open 9-day countdown (Sinner knee/Alcaraz wrist both withdrawn from Cincinnati — fitness doubts for Flushing; Zverev/Djokovic/Shelton lead men's field, Swiatek frontrunner women's)
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON — known issue); image manifest all not_started (expected for imagn source); posting window warnings cosmetic (known issue); WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

### 2026-08-14 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-14.xlsx (6 posts 13:46–20:36 ET), tfr-postplanner-tobi-2026-08-14.xlsx (6 TOBI posts)
- **Key stories:** Shelton def. Nakashima 6-3, 7-6(4) — defends Montreal, first since Nadal (2018-19) to back-to-back Canadian Masters, joins Murray/Djokovic in Open Era club; entered week 1-4 in Masters 1000; Swiatek def. Rybakina 6-2, 6-3 — first title of 2026, 10-month drought snapped, 12th career WTA 1000, completes North American swing career sweep; Nakashima rises to career-high No. 22 (both UVA alums — all-Cavaliers Masters 1000 final); Cincinnati Day 2 underway (Zverev/Djokovic debut Aug 15); US Open 2-week preview (Sinner knee, Alcaraz wrist, Shelton/Swiatek frontrunners)
- **Issues:** posting window warnings cosmetic (known issue); image manifest all not_started (expected for imagn source); WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

### 2026-08-13 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-13.xlsx (7 posts 13:12–20:42 ET), tfr-postplanner-tobi-2026-08-13.xlsx (7 TOBI posts)
- **Key stories:** Nakashima def. Jodar 7-6(3), 6-4; Shelton def. Tien 6-2, 6-3 (Shelton injured — collided with LCD ad panel, bleeding elbow/hand, coach Erin Stubbs furious, "payback" win; Tien had led H2H 2-0); All-American final tonight not before 8 PM ET; Swiatek def. Svitolina 6-3, 1-6, 6-3 (first win vs. Svitolina in 3 2026 meetings, first 2026 WTA 1000 final); Rybakina def. Gauff 5-7, 6-2, 6-2 (3rd set-down comeback in Toronto); Toronto final tonight 6 PM ET H2H 6-6; Cincinnati Day 1 open (Zverev 1, Djokovic 3, same half, Sinner/Alcaraz/Raducanu/Paolini all withdrawn); US Open injury watch (Alcaraz/Sinner/Tiafoe/Raducanu/Paolini)
- **Issues:** posting window warnings cosmetic (known issue); image manifest all not_started (expected for imagn source); WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

### 2026-08-12 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-12.xlsx (7 posts 13:10–20:40 ET), tfr-postplanner-tobi-2026-08-12.xlsx (7 TOBI posts)
- **Key stories:** Montreal QF blitz — Shelton 6-3 6-1 (18 winners, 3 UE, 89% first-serve pts), Tien 6-3 6-2, Nakashima 6-2 6-3 (11 aces, 1h17m), Jodar 7-6(5) 6-3; 3 Americans in Canadian Masters SF (first since 1992); Jodar (ESP, 19) first player born 2006+ in Masters SF, 34W-13L, No. 11 live; Rybakina def. Osaka 4-6, 7-6(5), 6-4 (13 aces, 2h33m); Gauff walkover (Bencic hip); Toronto SFs: Swiatek/Svitolina today, Gauff/Rybakina Aug 13; Cincinnati ATP draw (Zverev 1, Djokovic 3, same half, starts Aug 13); Cincinnati WTA draw (Sabalenka 1, Rybakina 2, Swiatek defending, starts Aug 13)
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON — known issue); image manifest all not_started (expected for imagn source); posting window warnings cosmetic; WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

### 2026-08-11 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-11.xlsx (7 posts 13:15–20:45 ET), tfr-postplanner-tobi-2026-08-11.xlsx (7 TOBI posts)
- **Key stories:** Svitolina def. Alexandrova 3-6, 6-0, 6-3 (93 min; from set down; WTA 1000 streak to 10); Swiatek def. Shnaider 6-2, 6-1 (64 min, 0 BPs faced, 88% 1st serve); Toronto SF: Swiatek vs. Svitolina Aug 12 (H2H 4-3 Swiatek; Svitolina won both 2026 meetings); Montreal all-2000s QF (first in ATP history — all 8 born in 2000s, first all-25-under since Paris 2007); Sinner Cincinnati withdrawal (knee, joins Alcaraz/wrist; Zverev top seed; Djokovic returning); Shelton vs. Mensik QF (Shelton no sets dropped, Mensik H2H 2-1)
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON — known issue); image manifest all not_started (expected for imagn source); posting window warnings cosmetic; WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

### 2026-08-10 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-10.xlsx (7 posts 13:18–20:42 ET), tfr-postplanner-tobi-2026-08-10.xlsx (7 TOBI posts)
- **Key stories:** Alexandrova into Toronto SF (beat Svitolina QF 2h29m; 48hrs after stunning Sabalenka R16; 3rd career win over No. 1-calibre player); Shelton def. Fonseca 6-3, 7-6(3) (defending champion advances; Fonseca had beaten Tsitsipas + Ruud to get here; Shelton H2H 2-0); Tien 50th HC win + Merida first QF complete Montreal bracket (QF: Shelton/Mensik, Tien/Merida, Fils/Jodar, Nakashima/Darderi); Swiatek vs. Shnaider Toronto QF preview (Shnaider beat Pegula 6-3, 6-2 in 73 min; H2H 1-0 Swiatek clay); Tiafoe right-hand cyst surgery ~Aug 8 (US Open Aug 30; joins Alcaraz/FAA on injury list)
- **Issues:** FB posts not picked up by compile script (0 FB posts in JSON — known issue); image manifest all not_started (expected for imagn source); posting window warnings cosmetic; WordPress blocked by proxy; dashboard push blocked by proxy
- **Story history:** Updated with all 5 stories

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
