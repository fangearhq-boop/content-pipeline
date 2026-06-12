# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-06-12 |
| Writing | Complete (all steps) | 2026-06-12 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 36 claims, 87 HIGH; image warnings cosmetic/expected for imagn) | 2026-06-12 |
| Compile | Complete (07-content-data.json — 5 stories, 8 X posts, 0 FB posts, 5 articles, 7 images) | 2026-06-12 |
| Dashboard | Complete (review-dashboard.html, 23 items) | 2026-06-12 |
| PostPlanner Export | Complete (standard 8 posts + TOBI 8 posts) | 2026-06-12 |
| WordPress Publish | Attempted — proxy blocks WordPress API (same as all previous runs) | 2026-06-12 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-06-12 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-06-12 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-12.xlsx (8 posts), tfr-postplanner-tobi-2026-06-12.xlsx (8 TOBI posts)
- **Coverage:** Stuttgart BOSS Open QF day (Mpetshi Perricard 49 aces vs Bublik No. 3 seed, first grass meeting; Lehecka vs Tiafoe; Shelton top seed + Fritz defending champ; SF Saturday); Queen's Club WTA Day 5 catch-up (rain washout Day 4 compressed 5 R16s into Friday; Rybakina No. 1 vs reigning champ; Raducanu vs Cirstea rematch; Boulter "brilliant"; Jovic/Anisimova in QF; Wimbledon 17 days); Sinner confirms Hurlingham Giorgio Armani Tennis Classic June 23-27 (no official grass events; Cobolli+Darderi+Norrie; BNP Paribas new sponsor; Wimbledon draw June 26); FAA def. Fucsovics 6-3, 6-4 into Libema Open QF vs Majchrzak (zero BPs faced; career-high No. 4; quote "three guys ahead of me"); Wimbledon 17 days countdown (Alcaraz out wrist injury; Sinner defends 2025 title; Swiatek defends women's; draw June 26)
- **Notes:**
  - verify-facts.py: 1 run — passed; 36 claims, 87 HIGH; image warnings cosmetic (imagn source, all not_started)
  - compile: 5 stories, 8 X posts, 0 FB posts, 5 articles, 7 images; posting window warnings cosmetic
  - dashboard: 23 items
  - PostPlanner exports: both standard (8) and TOBI (8) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-11 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 9 X posts + 10 FB posts (5 long-form + 5 captions) = 19 total
- **Articles:** 5 (bylines: Ryan Calloway x2 [S1, S5], Elena Voss x2 [S2, S4], Marcus Cole x1 [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-11.xlsx (9 posts), tfr-postplanner-tobi-2026-06-11.xlsx (9 TOBI posts)
- **Coverage:** Shimabukuro stuns Kyrgios 6-4, 6-2 Stuttgart R16 (comeback halted; first career meeting; Shimabukuro into QF); Serena Williams Queen's Club comeback ends (Mboko knee injury vs Pliskova forces QF withdrawal vs Fernandez/Siegemund; comeback lasts one match, one win); Sinner hospital all-clear (San Raffaele Milan, 4h tests cardiac MRI+Holter+stress ECG, no pathology, skipping Halle+QC, Wimbledon June 29 sole target); Stuttgart R16 round-up (Shelton def. Giron 7-6(3) 7-5; Hijikata def. Tiafoe 6-7 7-6 6-3; Duckworth def. Lehecka 6-4 6-3); Queen's Club WTA midweek (Raducanu faces Cirstea R16; Boulter through; Wimbledon 18 days out; Rybakina top seed)
- **Notes:**
  - verify-facts.py: 2 runs required — first run flagged 2 char violations (S2 tweet A: 295, S4 tweet A: 288). Fixed by shortening both posts. Second run passed.
  - compile: 5 stories, 9 X posts, 0 FB posts, 5 articles, 9 images; posting window warnings cosmetic
  - dashboard: 24 items
  - PostPlanner exports: both standard (9) and TOBI (9) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-10 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Ryan Calloway x2 [S1, S4], Elena Voss x2 [S2, S5], Marcus Cole x1 [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-10.xlsx (7 posts), tfr-postplanner-tobi-2026-06-10.xlsx (7 TOBI posts)
- **Coverage:** Serena Williams/Mboko WIN doubles opener at Queen's Club (def. No. 3 seeds Melichar-Martinez/Routliffe 7-6(2), 6-2; QF next vs Fernandez/Siegemund); Kyrgios def. Moutet 6-3, 6-4 in Stuttgart (8 aces, 84% first serve, zero BPs for Moutet; first singles grass win since 2022 Wimbledon final; quote "I'm very thrilled to be back"; Tiafoe def. Altmaier Day 2); Queen's Club WTA Day 2 (Raducanu def. Blinkova 6-0, 6-3; Boulter def. No. 8 Fernandez 3-6, 7-6(4), 7-5; both British women through); Libema Open Day 2 (Mannarino def. defending champ Diallo 6-4, 3-6, 7-5; Cilic def. Shapovalov; Damm vs FAA next); Grass season Week 1 snapshot (Wimbledon 21 days, 3 simultaneous events, no clear favourite)
- **Notes:**
  - verify-facts.py: passed; 25 claims; image warnings cosmetic (imagn source, all not_started)
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-09 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Elena Voss x2 [S1, S4], Marcus Cole x2 [S2, S5], Ryan Calloway x1 [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-09.xlsx (7 posts), tfr-postplanner-tobi-2026-06-09.xlsx (7 TOBI posts)
- **Coverage:** Serena Williams returns to competitive tennis at Queen's Club in doubles with Victoria Mboko (world No. 9) vs No. 3 seeds Melichar-Martinez/Routliffe (4-year absence since 2022 US Open); Stuttgart BOSS Open Day 1 main draw (Kyrgios first grass match in ~3 years vs Moutet; Fritz defending, Shelton top seed have byes; Tiafoe vs Altmaier); HSBC Championships Queen's Club WTA Day 1 (Cristian def. Zheng No. 5 seed 6-4, 7-6(4); Dart def. Samsonova 5-7, 6-4, 6-3; Boulter-Fernandez rain-delayed); Libema Open 's-Hertogenbosch (FAA top seed career-high No. 4; Medvedev No. 2; de Minaur defending 2024; Griekspoor vs Van de Zandschulp all-Dutch R1); WTA grass season overview (zero days between Roland Garros and Queen's Club; Andreeva champion no points to defend; Wimbledon July 1)
- **Notes:**
  - verify-facts.py: passed; 34 claims; image warnings cosmetic (imagn source, all not_started)
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-08 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 10 FB posts (5 long-form + 5 captions) = 16 total
- **Articles:** 5 (bylines: Elena Voss x2 [S1, S4], Marcus Cole x2 [S2, S5], Ryan Calloway x1 [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-08.xlsx (6 posts), tfr-postplanner-tobi-2026-06-08.xlsx (6 TOBI posts)
- **Coverage:** Zverev wins Roland Garros 2026 (def. Cobolli 6-1, 4-6, 6-4, 6-7(5), 6-1; first GS title; first German men's GS since Becker 1996; 0-3 in finals before; 25th career title; 125th career GS win); Roland Garros controversies — physio visit during play + line-call error at 5-5 (last GS with human line judges); Post-Roland Garros rankings (Zverev ↑ No. 3, Cobolli career-high No. 10, Arnaldi +70, Andreeva ↑ No. 6, Chwalinska +93); Stuttgart BOSS Open opens today (Kyrgios vs Moutet — first grass in ~3 years; Fritz defending; Zverev/Cobolli/Mensik withdrew); Cobolli feature (Italy's first GS finalist since Panatta 1976; career-high No. 10)
- **Notes:**
  - verify-facts.py: passed; 31 claims; image warnings cosmetic (imagn source, all not_started)
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-07 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 9 X posts + 10 FB posts (5 long-form + 5 captions) = 19 total
- **Articles:** 5 (bylines: Elena Voss x2 [S1, S4], Marcus Cole x2 [S2, S5], Ryan Calloway x1 [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-07.xlsx (9 posts), tfr-postplanner-tobi-2026-06-07.xlsx (9 TOBI posts)
- **Coverage:** Men's Final match day preview Zverev vs Cobolli (TODAY, 3 PM Paris / 9 AM ET; Zverev 0-3 in GS finals, Cobolli first GS final, H2H 3-1 Zverev, guaranteed first-time champion); Andreeva wins women's title 6-3, 6-3 over Chwalinska (youngest RG champion since Seles 1992, first Russian women's RG title since Sharapova 2014, trailed 2-3 then won 10 straight, coached by Martinez); RG 2026 tournament record-books wrap-up (Chwalinska first qualifier in RG final history, Cobolli first Italian GS finalist since Panatta 1976, 4th Open Era GS SF walkover); Grass court season preview Stuttgart June 8-14 (Fritz, Berrettini, Kyrgios, Mensik); Andreeva feature (coaching by Martinez, Russian tennis legacy, what winning at 19 means)
- **Notes:**
  - verify-facts.py: 1 run — passed; 26 claims; consistency warnings cosmetic (story title partial match); image warnings cosmetic (imagn source, all not_started)
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-06 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 9 X posts + 10 FB posts (5 long-form + 5 captions) = 19 total
- **Articles:** 5 (bylines: Elena Voss x2 [S1, S4], Marcus Cole x2 [S2, S5], Ryan Calloway x1 [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-06.xlsx (9 posts), tfr-postplanner-tobi-2026-06-06.xlsx (9 TOBI posts)
- **Coverage:** Women's Final day-of preview (Andreeva vs Chwalinska, 3 PM Paris, both first GS final, Chwalinska first qualifier in RG final history); Zverev def. Mensik 7-5, 6-2, 3-6, 6-3 (3h01m, 4th GS final for Zverev, Mensik medical timeout set 3); Arnaldi viral illness withdrawal → Cobolli walkover into first GS final (4th walkover in Open Era GS SF history, Italy's first men's GS finalist since Panatta 1976); Men's Final preview Zverev vs Cobolli Sunday (Zverev 0-3 in GS finals, H2H 3-1 Zverev, first first-time champion since Sinner AO 2024); Roland Garros 2026 historic moments meta-story
- **Notes:**
  - verify-facts.py: 1 run — passed after fixing 1 char violation (Story 5 tweet A from 298 to 275 chars); 33 claims
  - image manifest warnings cosmetic (expected for imagn source, all not_started)
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-05 — Full Pipeline Run
- **Steps completed:** All 15
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 8 X posts + 10 FB posts = 18 total
- **Articles:** 5 (bylines: Elena Voss x2 [S1, S4], Marcus Cole x2 [S2, S5], Ryan Calloway x1 [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-05.xlsx (8 posts), tfr-postplanner-tobi-2026-06-05.xlsx (8 TOBI posts)
- **Coverage:** Andreeva def. Kostyuk 6-1, 6-3 Women's SF; Chwalinska def. Shnaider 7-6(4), 6-4 (first qualifier ever in RG final); Zverev vs Mensik men's SF preview; Cobolli vs Arnaldi first all-Italian GS SF preview; Women's final preview Andreeva vs Chwalinska June 6
- **Notes:** verify-facts.py passed; WordPress proxy error; Dashboard push failed (same as all prior runs)
