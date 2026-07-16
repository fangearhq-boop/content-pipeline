# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-07-16 |
| Writing | Complete (all steps) | 2026-07-16 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 33 claims, 106 HIGH; image not_started warnings cosmetic/expected for imagn) | 2026-07-16 |
| Compile | Complete (07-content-data.json — 5 stories, 7 X posts, 5 FB posts, 5 articles, 10 images; 27 dashboard items) | 2026-07-16 |
| Dashboard | Complete (review-dashboard.html, 27 items) | 2026-07-16 |
| PostPlanner Export | Complete (standard 7 posts 12:50–20:38 ET; TOBI 7 posts) | 2026-07-16 |
| WordPress Publish | Attempted — proxy blocks WordPress API (same as all previous runs) | 2026-07-16 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-07-16 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-07-16 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB long-form + 5 FB captions = 17 total (PostPlanner xlsx: 7 posts 12:50–20:38 ET, 7 TOBI)
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-16.xlsx (7 posts), tfr-postplanner-tobi-2026-07-16.xlsx (7 TOBI posts)
- **Coverage:** Burruchaga (ARG, No. 67) def. Cobolli [1] (No. 9) 6-2, 6-4 Umag R2 — first Top-10 win of career; ATP Tour "one of the best matches of the year"; 78% first-serve pts, 4/7 BPs; all 13 wins on clay; Cobolli first match since Wimbledon QF; Umag QFs July 16: ADF/Molcan, Arnaldi/Dzumhur, Droguet/Merida Aguilar. Alcaraz Cincinnati return: on Cincinnati entry list (Aug 13-23); wrist "completely healed" (Dr. Ruiz-Cotorro); next 2 weeks crucial; defending champion Cincinnati + US Open (Aug 31–Sep 13); missed RG/Wimbledon/Canada from April 14 Barcelona tenosynovitis; No. 3. Bastad QFs: Borges def. Dimitrov 6-4, 6-2 (4th QF 2026); Vallejo (PAR) def. van de Zandschulp 4-6, 6-3, 7-6(4) — first Paraguayan ATP QF since Ramon Delgado Mumbai 2006 (2h57m); Travaglia def. Navone [4] 6-4, 6-2; Rublev into QF; Thursday Centre Court: Rublev/Baez/Tabilo/Basilashvili; Iasi QFs: Putintseva/Zidansek/Burel/Marcinko. WTA Athens R2: Sakkari def. Dart 6-1, 6-2 (3 games total in 2 Athens matches); Parks def. Hontama 6-7(4), 6-2, 7-5; Zheng def. Micic 6-4, 6-1; QFs Friday July 17: Parks vs Sakkari (Parks 2-0 H2H). Gstaad Day 4: Bublik (defending champion) vs Halys; Ruud (former champion) vs Faria (who beat Wawrinka R1); Tsitsipas def. Buse [5] 6-4, 6-4 now vs Kym (Swiss WC).
- **Notes:**
  - verify-facts.py: passed; 33 claims, 106 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 7 X posts, 5 FB posts, 5 articles, 10 images; 27 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (7 posts) and TOBI (7 posts) generated successfully; 12:50–20:38 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3] (rotating from July 15: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])

### 2026-07-15 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 5 FB long-form + 5 FB captions = 16 total (PostPlanner xlsx: 6 posts 13:01–20:26 ET, 6 TOBI)
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-15.xlsx (6 posts), tfr-postplanner-tobi-2026-07-15.xlsx (6 TOBI posts)
- **Coverage:** Stan Wawrinka farewell at Gstaad: lost R1 to Jaime Faria 6-7(8), 6-4, 6-4; on-court ceremony with Swiss Davis Cup teammates; tournament gifted custom skis (The Man + 2015 RG geometric print); debut at Gstaad 2003; 41yo; farewell tour through end of 2026. Canadian Open entry list: 71 of 72 top ATP players confirmed; Sinner [1], Djokovic, Zverev [2], FAA (9th home appearance) all in; Alcaraz absent (tenosynovitis since April 14 Barcelona — missed RG, Wimbledon, Canada); wild cards: Monfils + Diallo; Shapovalov direct entry; WTA Toronto 72/75; draws July 29-30. Clay Courts Day 3 — Droguet def. Blockx [5] 3-6, 6-2, 6-0 (drop shots + 77% 1st-serve pts); Dimitrov def. Svrcina 7-6(5), 1-6, 6-4 (Bastad); Rublev [1] def. Pellegrino 6-3, 6-2 (Bastad); Tsitsipas def. Buse [5] 6-4, 6-4 (Gstaad); Cerundolo [6] def. Kolar 4-6, 6-3, 6-4 (Gstaad); Wed: Bublik vs Halys (Gstaad), Tsitsipas vs Kym (Gstaad), Dimitrov vs Borges (Bastad), Cobolli [1] vs Burruchaga (Umag). WTA Athens inaugural: first WTA event in Athens in 35 years; Sakkari 6-0, 7-6(1) vs Kudermetova Day 1; Krejcikova def. Tomova 6-3, 6-3; Tauson def. Hibino 7-5, 6-4; Zheng def. Bouzas Maneiro [6] 7-5, 6-1 (upset); runs Jul 13-19. Alcaraz wrist update: absent from Canadian Open list; team has not issued return timeline; video hitting at academy; growing concern from Tennis365 2026 season may be over; US Open August 24.
- **Notes:**
  - verify-facts.py: Story 3 tweet fixed 282→278 chars; Story 5 tweet fixed 297→277 chars; 32 claims, 74 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully; 13:01–20:26 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3] (rotating from July 14: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])

### 2026-07-14 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (1 Tier 1, 4 Tier 2)
- **Posts:** 6 X posts + 5 FB long-form + 5 FB captions = 16 total (PostPlanner xlsx: 6 posts 12:51–20:21 ET, 6 TOBI)
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-14.xlsx (6 posts), tfr-postplanner-tobi-2026-07-14.xlsx (6 TOBI posts)
- **Coverage:** Post-Wimbledon ATP/WTA rankings: Sinner leads by 4,970 pts; Zverev overtook Alcaraz for No. 2 (first time); Alcaraz drops to No. 3; Fery rockets from No. 114 to No. 36 (+78 spots, career high, new British No. 1); Noskova rises to career-high No. 7 (was No. 12); Swiatek fell No. 3 to No. 8; Gauff up to No. 4; Muchova career-high No. 6. Noskova viral moment: post-Wimbledon presser quote "Let me get drunk" — 21-year-old champion, no media training, widely shared. Sinner post-Wimbledon plans: Canadian Open + Cincinnati targeted, no clay events; Coach Cahill quote: "The M1000 events are incredibly important." ATP clay swing underway: Bastad (Nordea Open, July 13-19) — Passaro [4] def. by qualifier Krumich 6-4, 6-3; Rublev top seed with R2 bye; Gstaad (Bublik defending) + Umag (Cobolli top seed) also began simultaneously. Berrettini chronic hip pain: withdrew from Gstaad AND Kitzbühel; eyes on Canadian Open August + US Open.
- **Notes:**
  - verify-facts.py: passed; 26 claims, 64 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully; 12:51–20:21 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3] (rotating from July 13: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])
  - Story 3 tweet shortened to fix 290-char violation; re-verified passed

### 2026-07-13 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB long-form + 5 FB captions = 17 total (PostPlanner xlsx: 7 posts 12:55–20:37 ET, 7 TOBI)
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-13.xlsx (7 posts), tfr-postplanner-tobi-2026-07-13.xlsx (7 TOBI posts)
- **Coverage:** Sinner def. Zverev 6-7(7), 7-6(2), 6-3, 6-4 in 3h46m — 5th Grand Slam, 2nd Wimbledon, 10th man to defend title; came from set down; won 2nd-set TB 7-2 decisive; 80% 1st-serve pts won; quote: "There is no failure if you don't win a Grand Slam. These are very, very rare days." Djokovic post-Wimbledon: not retiring; wants one more Wimbledon; targeting US Open; on Sinner: "just a level or more better"; acknowledged grass sharpness lacking after only 13 matches in 2026. Finals Day doubles: Heliövaara/Patten def. Arévalo/Pavić 7-6(4), 7-6(3) — Patten first British man to win Wimbledon doubles twice in Open Era; Guo/Mladenovic def. Dabrowski/Stefani 6-3, 7-5 (first major together); Cruz Hewitt (son of Lleyton Hewitt) runner-up in boys' singles, lost to Jordan Lee (USA) 6-4, 4-6, 7-5. Wimbledon 2026 records: Sinner 100 career GS wins; Djokovic 108 all-time Wimbledon wins (passes Federer); Noskova 10th straight different women's champion; Fery first unseeded British player in Open Era men's SF. Post-Wimbledon: ATP clay season (Bastad, Gstaad, Umag, Iasi all begin July 13).
- **Notes:**
  - verify-facts.py: passed; 21 claims, 52 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 7 X posts, 0 FB posts (parser compatibility), 5 articles, 7 images; 22 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (7 posts) and TOBI (7 posts) generated successfully; 12:55–20:37 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3] (rotating from July 12: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
  - Cruz Hewitt boys' final result confirmed: lost to Jordan Lee (USA) 6-4, 4-6, 7-5 (was TBD in July 12 pipeline)

### 2026-07-12 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 5 FB long-form + 5 FB captions = 18 total (PostPlanner xlsx: 8 posts standard 12:54–20:50 ET, 8 TOBI)
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-12.xlsx (8 posts), tfr-postplanner-tobi-2026-07-12.xlsx (8 TOBI posts)
- **Coverage:** Noskova (No. 9, CZE, 21) def. Muchova (No. 10, CZE) 6-2, 5-7, 6-3 — first all-Czech Grand Slam final in history; Muchova saved 5 match points from 5-2 down in set 2; youngest Wimbledon women's champion since Kvitova 2011; Czech women 3 of last 4 Wimbledon titles. Noskova dedicates title to late mother (died 2024): "I definitely would not be standing here without her"; Muchova on-court: "I'll start with Linda, my ex-friend" (both from Přerov, pop. 43,000). Men's final preview: Sinner (No. 1, defending champion) vs Zverev (No. 2, Roland Garros 2026 champion) — 15th career meeting, first on grass; Sinner leads H2H 10-4; Zverev chasing Channel Slam (CORRECTION: last done Alcaraz 2024, not Federer 2009 as July 11 pipeline stated). Channel Slam history explainer (Open Era completions: Laver, Borg ×3, Nadal, Federer, Djokovic, Alcaraz 2024). Finals Day: Cruz Hewitt (son of Lleyton) in boys' singles final (result TBD); Ostapenko/Arevalo def. Hunter/Polmans 4-6, 7-5, 6-2 in mixed doubles (July 9); Arevalo first player from El Salvador to win Wimbledon title.
- **Notes:**
  - CORRECTION APPLIED: July 11 pipeline stated "Channel Slam last done Federer 2009" — corrected to "last done Carlos Alcaraz 2024" per ATP Tour source. Applied throughout all today's content.
  - verify-facts.py: passed; 22 claims, 53 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 5 FB posts, 5 articles, 8 images; 28 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:54–20:50 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3] (rotating from July 11: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3])
  - Cruz Hewitt boys' final result TBD at pipeline run time — noted in article and social posts

### 2026-07-11 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 8 X posts + 5 FB long-form + 5 FB captions = 18 total (PostPlanner xlsx: 8 posts standard 12:50–20:46 ET, 8 TOBI)
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-11.xlsx (8 posts), tfr-postplanner-tobi-2026-07-11.xlsx (8 TOBI posts)
- **Coverage:** Sinner def. Djokovic 6-4, 6-4, 6-4 — zero break points faced, 88% first-serve pts won, 16 aces; Djokovic playing injured ankle/calf, 48h after 5h15m QF epic; Sinner into final as defending champion, chasing first Wimbledon title defense since Federer 2009. Zverev def. Fery 7-6(0), 6-2, 6-4 — swept opening TB 7-0; 44 winners; Fery career transformed: No. 114 → No. 36 (career high), new British No. 1, ~$1.2M prize money vs $884K career earnings before tournament; only 2nd WC to reach Wimbledon men's SF in Open Era (Ivanisevic 2001). Women's final preview: Muchova (No. 10, 29, Přerov) vs Noskova (No. 9, 21, Přerov) — first all-Czech women's GS final in history; first same-nationality women's GS final since Venus-Serena Wimbledon 2009; not before 4 PM BST / 11 AM ET Saturday. Men's final preview: Sinner vs Zverev Sunday July 12, not before 4 PM BST / 11 AM ET; first ATP No. 1 vs No. 2 in Wimbledon final (Open Era); Zverev chasing Channel Slam (last done Federer 2009). Fery career feature: 23yo WC story — No. 114 → No. 36, doubled career earnings in one tournament, 2nd-ever WC in Wimbledon men's SF.
- **Notes:**
  - verify-facts.py: passed; 26 claims, 60 HIGH; image not_started warnings cosmetic (expected for imagn source — same as all prior runs)
  - compile: 5 stories, 8 X posts, 5 FB posts, 5 articles, 8 images; 28 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:50–20:46 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3] (rotating from July 10: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
  - Women's final happening TODAY — covered as preview; result for follow-up Sunday
  - Men's final Sunday July 12 — preview covered; result for follow-up Monday

### 2026-07-10 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 9 X posts + 5 FB long-form + 5 FB captions = 19 total (PostPlanner xlsx: 9 posts standard, 9 TOBI)
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-10.xlsx (9 posts), tfr-postplanner-tobi-2026-07-10.xlsx (9 TOBI posts)
- **Coverage:** Women's SF results (Day 11, July 9): Muchova def. Gauff 6-2, 1-6, 7-6(10) in 2h35m — match point saved at 9-8 in TB; Noskova def. Kostyuk 6-4, 6-4 in 79 min. First all-Czech women's Wimbledon final in history; first same-nationality women's Slam final since Williams sisters 2017 US Open. Women's final preview: Muchova (29, 2nd Slam final) vs Noskova (21, 1st Slam final), both from Přerov, Czech Republic. Men's SFs TODAY (July 10): Fery (No. 114 wildcard) vs Zverev (RG champion chasing Channel Slam — only 5 men in Open Era: Laver, Borg, Federer, Nadal, Djokovic). Sinner (defending champ, 12 straight sets) vs Djokovic (39yo, ankle/calf injury, longest men's QF in Wimbledon history). Czech dynasty feature: 12 Wimbledon titles, Navratilova to Noskova.
- **Notes:**
  - verify-facts.py: passed; 24 claims, 47 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 9 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; 24 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (9 posts) and TOBI (9 posts) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Story history updated: added July 9 entries (from daily brief) and July 10 entries

### 2026-07-09 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 9 X posts + 5 FB long-form + 5 FB captions = 19 total (PostPlanner xlsx: 9 posts standard, 9 TOBI)
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-09.xlsx (9 posts, 12:51–20:59 ET), tfr-postplanner-tobi-2026-07-09.xlsx (9 TOBI posts)
- **Coverage:** Fery (British wildcard, No. 114) def. Cobolli (No. 9) 6-4, 7-6(4), 6-0 — 2nd men's wildcard Wimbledon SF in Open Era (Ivanisevic 2001 was first; he won the title); 5th British man in Wimbledon SF in Open Era; lowest-ranked SF since Ivanisevic. Zverev (No. 2) def. Fritz (No. 6) 6-4, 6-4, 6-2 in 1h59m — first-ever Wimbledon SF; ended 0-7 losing streak vs Fritz; now 5th active player with all-4-Slam SFs; Paris-London double (RG + Wimbledon) now possible — last done by Nadal 2008; Fritz had knee injury timeout in 2nd set. Women's Day 10: Kostyuk def. Paolini 6-3, 6-2 (69 min); Noskova def. Mertens 6-3, 7-5 (30 winners, 79% first-serve pts). Day 11: women's SFs today — Gauff vs Muchova (CC), Kostyuk vs Noskova; guaranteed first-time women's champion (10th straight year). Men's SFs Friday: Fery vs Zverev (CC), Sinner vs Djokovic (Court 1).
- **Notes:**
  - verify-facts.py: passed; 24 claims, 39 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 9 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; 24 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (9 posts) and TOBI (9 posts) generated successfully; 12:51–20:59 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3] (rotating from July 8: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3])

### 2026-07-08 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 9 X posts + 5 FB long-form + 5 FB captions = 19 total (PostPlanner xlsx: 9 posts standard, 9 TOBI)
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-08.xlsx (9 posts, 13:01–20:53 ET), tfr-postplanner-tobi-2026-07-08.xlsx (9 TOBI posts)
- **Coverage:** Djokovic def. No. 3 FAA 7-6(10), 3-6, 6-3, 6-7(4), 7-6(4) in 5h15m — longest QF in Wimbledon history; 8th consecutive Wimbledon SF; ankle/calf injury; survived 3 match points in 5th-set TB; won 22-point first-set TB. Sinner def. Struff 7-5, 7-6(4), 6-3 — 16 aces, 3/3 BPs, no sets dropped all tournament; Struff oldest Open Era first-time Grand Slam QF (36yo, 47th major, surpassed Santoro). Women's Day 9: Gauff def. Pegula 4-6, 6-3, 6-3 (first Wimbledon SF, 5/5 BPs, hadn't won on grass in 2 years; youngest to SF all 4 slams since Sharapova 2007); Muchova def. Osaka 7-6(4), 6-4 (4th Czech woman to SF all 4 slams Open Era). Day 10 preview: Fery (British wildcard) vs Cobolli (No. 9) on Centre Court; Fritz (No. 7) vs Zverev (No. 2, first Wimbledon QF) on Court 1 — Fritz leads H2H 10-5, 7 consecutive; Paolini (No. 13) vs Kostyuk (20-of-21); Noskova (No. 9) vs Mertens (No. 25). Sinner vs Djokovic SF preview — 3rd time in 4 years at this stage; 2025: Sinner won SF straight sets + title; Djokovic arrives injured from 5h15m epic.
- **Notes:**
  - CORRECTION NOTE: July 7 pipeline reported Fritz "7-0 all-time vs Zverev" — verified corrected to Fritz leads H2H 10-5 overall with 7 consecutive wins
  - verify-facts.py: passed; 25 claims, 52 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 9 X posts, 5 FB posts, 5 articles, 5 images; 29 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (9 posts) and TOBI (9 posts) generated successfully; 13:01–20:53 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3] (rotating from July 7: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])

### 2026-07-07 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 5 FB long-form + 5 FB captions = 18 total (PostPlanner xlsx: 8 posts standard, 8 TOBI)
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-07.xlsx (8 posts, 13:10–20:52 ET), tfr-postplanner-tobi-2026-07-07.xlsx (8 TOBI posts)
- **Coverage:** Fery def. Dimitrov 7-5, 3-6, 4-6, 6-4, 7-6(10-7) — CORRECTION of July 6 pipeline error; first British wildcard Grand Slam QF in Open Era; 23yo, outside top 100; first WC men's QF Wimbledon since Kyrgios 2014; next vs No. 9 Cobolli. Cobolli (No. 9) def. de Minaur (No. 5) 7-5, 7-6(4), 6-3 — biggest Day 8 men's upset; 2nd consecutive Wimbledon QF; Fritz def. Bublik 7-6(1), 6-4, 6-4 (3rd straight QF, 7-0 all-time vs Zverev); Zverev leads Lehecka 6-4, 7-5, 3-3 (suspended curfew, resumes Day 9). Paolini def. Eala 6-4, 4-6, 6-3 (ends historic Filipino run); Noskova def. Keys 6-4, 7-6(2); Mertens def. Bouzkova 6-4, 6-4; Kostyuk def. Krueger 6-4, 6-4; Wimbledon 2026 guaranteed first-time women's champion. Day 9 QF preview: Gauff(7) vs Pegula(4) [first all-American Wimbledon ladies' QF top-10 seeds since 2009 Serena-Venus final]; FAA(3) vs Djokovic(7) [first grass meeting, H2H 1-1, Djokovic chasing 25th/8th Wimbledon]; Sinner(1) vs Struff; Osaka(14) vs Muchova(10) [Bad Homburg rematch]; scheduling controversy. FAA calls medical timeout rule "a disgrace of a rule" after ADF called physio at 5-4 in 4th set; proposed fix; Roddick support.
- **Notes:**
  - verify-facts.py: passed; 13 claims, 24 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 5 FB posts, 5 articles, 5 images; 28 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 13:10–20:52 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3] (rotating from July 6: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])

### 2026-07-06 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 5 FB long-form + 5 FB captions = 18 total (PostPlanner xlsx: 8 posts standard, 8 TOBI)
- **Articles:** 3 (bylines: Marcus Cole [S1, S4], Elena Voss [S2/S5 analysis], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-06.xlsx (8 posts, 12:52–20:48 ET), tfr-postplanner-tobi-2026-07-06.xlsx (8 TOBI posts)
- **Coverage:** Djokovic def. Safiullin 7-6(4), 6-3, 3-6, 6-3 — 106th Wimbledon win (sole record past Federer's 105); 39yo, 17th QF, quote "A win is a win, even if you win ugly"; next vs FAA. Osaka def. Sabalenka (No. 1) 6-2, 7-6(2) in 88 min — first career Wimbledon QF; first win vs Sabalenka since 2018 US Open (8 years); ended Sabalenka's 21-match Open Era GS tiebreak winning streak; Osaka 8-1 on grass 2026, was 0-13 on non-hard vs top-10; "She overpowered me" — Sabalenka. Day 8 round-up: Zverev def. Lehecka (4 sets); Dimitrov def. Fery (4 sets); Struff def. Hurkacz 3-6, 6-7, 7-6, 7-5, 4-2 ret. (back/abdomen) — 36yo, 47th major, first GS QF, oldest maiden major QF Open Era. QF preview: Sinner (0 sets dropped) vs Struff; FAA vs Djokovic (record-holder). Women's QF: Osaka in; Gauff vs Pegula all-American; Muchova def. Krejcikova 7-5, 5-7, 6-3; Eala vs Paolini + Mertens vs Bouzkova pending.
- **Notes:**
  - verify-facts.py: passed; 14 claims, 33 HIGH; Tier 2 missing article warnings cosmetic (expected); image not_started warnings cosmetic (imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility), 3 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:52–20:48 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3] (rotating from July 5: Ryan Calloway [S1, S4])

### 2026-07-05 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 5 FB long-form + 5 FB captions = 18 total (PostPlanner xlsx: 18 posts standard, 13 TOBI)
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-05.xlsx (18 posts, 12:53–21:23 ET), tfr-postplanner-tobi-2026-07-05.xlsx (13 TOBI posts)
- **Coverage:** Eala stuns Swiatek 7-6(9), 6-2 — first Filipino player in Grand Slam second week (Open Era); quotes: "Being here is a blessing" + "little girls with ruffled socks and chubby cheeks"; 24 winners, 5/7 BPs, 68% on Swiatek 2nd serve; next Paolini R4 Day 8. Mertens (No. 25) def. Rybakina (No. 2) 7-6(4), 6-1 — 96 min; first grass top-10 win for Mertens; only 2nd win in 9 meetings vs Rybakina; Day 6 eliminated both No. 2 and No. 3 seeds. Bublik def. Tiafoe 4-6, 7-6(5), 7-6(13-11), 4-6, 6-3 — 48 aces, saved 9 set points in 13-11 TB; Zverev def. Giron 6-2, 7-6, 6-4; Keys def. Anisimova 3-6, 6-2, 6-3. Day 7 Preview: Djokovic (105 wins=Federer) vs Safiullin for sole record at 106; H2H 3-0 Djokovic, first grass meeting; Sabalenka vs Osaka R4 first grass meeting, H2H 8-4 Sabalenka, Osaka first-ever Wimbledon R4; Sinner vs Mochizuki; Gauff vs Bencic; Pegula vs Jovic; FAA vs DAF. Open Women's draw: Swiatek + Rybakina both gone Day 6; Sabalenka frontrunner; Eala vs Paolini Day 8.
- **Notes:**
  - verify-facts.py: passed; 21 claims, 45 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 23 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (18 posts) and TOBI (13 posts) generated successfully; 12:53–21:23 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3] (rotating from July 4: Elena Voss [S1, S4])

### 2026-07-04 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB long-form + 5 FB captions = 17 total (PostPlanner xlsx: 17 posts standard, 12 TOBI)
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-04.xlsx (17 posts, 12:54–21:26 ET), tfr-postplanner-tobi-2026-07-04.xlsx (12 TOBI posts)
- **Coverage:** Djokovic equals Federer all-time Wimbledon men's record at 105 wins (def. Rinderknech 7-5, 6-4, 1-6, 7-6(4); faces Safiullin R4 Sunday, H2H 3-0; sole record possible with 1 more win); Struff (No. 74) upsets No. 8 Medvedev 7-6(4), 7-6(5), 7-5 (Medvedev led by break in all 3 sets incl. 5-2 3rd set; Struff won all 3 TBs; 4/12 BPs converted; first Wimbledon R4 for Struff); Women's Day 5 sweep (Sabalenka def. Ostapenko 6-4, 6-4; Osaka def. Kasatkina 6-1, 6-3 — first-ever Wimbledon R4; Gauff def. Liu 6-3, 6-7(5), 6-2; Sabalenka Open Era record 21 consecutive GS tiebreak wins); Day 6 — Swiatek vs Eala Centre Court (first grass meeting, H2H 1-1); Rybakina, Zverev, Tiafoe, Keys also in action; Day 7 preview (Djokovic vs Safiullin record chase; Sinner vs Mochizuki; Sabalenka vs Osaka R4 marquee; Alcaraz absent wrist injury)
- **Notes:**
  - verify-facts.py: passed; 17 claims, 38 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 7 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 8 images; 22 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (17 posts) and TOBI (12 posts) generated successfully; 12:54–21:26 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3] (rotating from July 3: Marcus Cole [S1, S4])

### 2026-07-03 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 5 FB posts (5 long-form + 5 captions) = 13 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-03.xlsx (8 posts, 12:50–20:46 ET), tfr-postplanner-tobi-2026-07-03.xlsx (8 TOBI posts)
- **Coverage:** Eala history (def. Joint 3-6, 6-2, 6-0 — first Filipino in Grand Slam R3; next vs Swiatek Saturday; H2H 1-1; Court 3 packed with Filipino fans); Djokovic def. Rinderknech 6-3, 6-4, 6-2 (33 winners, 7 UEs, zero break pts conceded; into R4); Sinner def. Brooksby 7-6, 6-1 in 90 min (into R4); Swiatek def. Pliskova 6-1, 6-3 (63 pts to 36, 6 breaks from 8 games, 4 games total — into R3 vs Eala); Samsonova def. No. 15 Shnaider 6-4, 4-6, 6-2 (30-10 winners, 5/7 break pts; biggest women's Day 4 upset); Day 6 preview — Sabalenka vs Ostapenko (first grass meeting; Ostapenko 2 grass titles; won Stuttgart 2025 final 6-4, 6-1 vs Sab), Osaka vs Kasatkina, Gauff vs Liu, FAA vs Zheng
- **Notes:**
  - verify-facts.py: passed; 32 claims, 41 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 10 images; 23 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:50–20:46 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-07-02 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 8 X posts + 5 FB posts (5 long-form + 5 captions) = 13 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Ryan Calloway [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-02.xlsx (8 posts, 12:49–20:45 ET), tfr-postplanner-tobi-2026-07-02.xlsx (8 TOBI posts)
- **Coverage:** Djokovic def. Tsitsipas 6-3, 6-4, 6-2 in 98 min (match resumed from Day 2 darkness suspension; 33 winners, 7 UEs, 46/52 first-serve points; viral ball girl scissors prank mid-match; Djokovic H2H 13-2 vs Tsitsipas; into R3 without dropping set); Krejcikova def. No. 5 Andreeva 4-6, 7-5, 6-4 (defending Wimbledon champion beats French Open champion; needed 7 match points; biggest women's upset so far); Sinner def. Borges 7-6(4), 7-6(2), 6-4 (two tiebreaks, 47 winners, defending champion into R3; skipped all grass warm-ups); Women's Day 3 — Sabalenka def. Kessler 6-1, 7-6(9); Gauff def. Sierra 6-3, 3-6, 7-6(7) (came back from break down in final tiebreak); Osaka def. Gasanova 6-3, 6-2; Day 4 preview — Swiatek vs Pliskova R3 scheduled
- **Notes:**
  - verify-facts.py: passed; 15 claims, 36 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 23 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:49–20:45 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-07-01 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 8 X posts + 5 FB posts (5 long-form + 5 captions) = 13 total
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Marcus Cole [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-07-01.xlsx (8 posts, 12:52–20:48 ET), tfr-postplanner-tobi-2026-07-01.xlsx (8 TOBI posts)
- **Coverage:** Serena Williams exits Wimbledon (def. by Maya Joint 6-3, 6-7(6), 6-3; first singles since 2022 US Open; Joint 20yo No. 87 snapped 11-match losing streak; Serena won S2 TB; still doubles with Venus); Ben Shelton (No. 4) upset by Finnish qualifier Virtanen 6-4, 3-6, 6-7(8), 6-2, 7-6(9) — saved MP at 9-8 in supertiebreak; first Finnish man to beat top-5 at major in Open Era; "toughest loss of my career"; Svitolina (No. 8) exits — qualifier Snigur def. 7-5, 6-2 coming back from 0-4 in S1; first R1 exit since 2018; Vekić also out; Swiatek (No. 3) def. Townsend 6-1, 2-6, 6-3 + Rybakina (No. 2) def. Boisson 6-4, 1-6, 6-3 — both survived three-set scares; Djokovic vs Tsitsipas R2 suspended for darkness — resumes Day 3; Djokovic leads H2H 12-2; Day 3 preview: Andreeva vs Krejčíková CC, Sinner vs Borges R2, FAA vs Prizmic
- **Notes:**
  - verify-facts.py: passed; 16 claims, 41 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 23 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:52–20:48 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-30 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 5 FB posts (5 long-form + 5 captions) = 13 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S5], Elena Voss [S2, S4], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-30.xlsx (8 posts, 12:47–20:50 ET), tfr-postplanner-tobi-2026-06-30.xlsx (8 TOBI posts)
- **Coverage:** Sinner five-set scare (def. Kecmanovic 4-6, 6-3, 6-7(6), 6-2, 6-3 in 3h30m; defending champion who skipped all grass warm-ups; next vs Borges R2); Djokovic def. Wu Yibing 6-4, 5-7, 6-4, 6-4 (3h11m; 21-0 first rounds; viral marriage proposal in stands — "I want an invitation to the wedding"; next vs Tsitsipas); Draper withdraws from Wimbledon (arm injury recurrence; missed AO + RG 2026 same injury; lucky loser Lajovic replaces vs Fritz; third consecutive major interrupted); Women's Day 1 recap (Sabalenka def. Kostovic 6-2, 6-3 in 64 min — 23 consecutive R1 wins at majors; Gauff def. Korpatsch 6-2, 6-1 in 54 min — fastest Wimbledon win; Andreeva def. Linette 7-5, 6-4; UPSETS: Siniakova def. Zheng 6-4, 6-4; Zhang def. Andreescu 7-6(3), 7-6(6)); Men's Day 1 upsets (Ruud No. 11 lost to Hurkacz straight sets; Rublev No. 12 lost to Safiullin 5 sets; 12-10 deciding tiebreak; four seeds total fell Day 1)
- **Notes:**
  - verify-facts.py: passed; 18 claims, 40 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 23 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:47–20:50 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-29 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 8 X posts + 5 FB posts (5 long-form + 5 captions) = 13 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-29.xlsx (8 posts, 12:53–20:49 ET), tfr-postplanner-tobi-2026-06-29.xlsx (8 TOBI posts)
- **Coverage:** CORRECTION: Bergs wins Eastbourne def. Humbert 3-6, 6-1, 6-4 (June 28 pipeline did not confirm the final result; Bergs first ATP title; first Belgian ATP title on grass; 6-match losing streak before event; prior runner-up Auckland + 's-Hertogenbosch 2025; Bergs-Humbert Wimbledon R1 rematch Tuesday); Raducanu withdraws from Wimbledon (stress fracture lower right leg; announced Sunday evening; lucky loser Semenistaja Latvia No. 112 replaces vs Ruzic; reached Queen's final; 18 total withdrawals incl. Alcaraz); Wimbledon Day 1 opens (outside courts 11 AM BST; Bencic def. Stojsavljevic 6-2, 6-1; Fucsovics def. Van Assche 6-3, 4-0 ret.; Centre Court: Sinner/Kecmanovic, Sabalenka/Kostovic, Djokovic/Wu Yibing); Bergs-Humbert Wimbledon rematch (3 days, same surface, Wimbledon R1 stakes); Serena Williams Day 2 (44yo, first Grand Slam singles since 2022 US Open, vs Maya Joint 20yo Tuesday)
- **Notes:**
  - CORRECTION LOGGED: June 28 pipeline covered the Eastbourne rain-delayed final as "ongoing" but did not report the result. Result confirmed: Bergs def. Humbert 3-6, 6-1, 6-4.
  - verify-facts.py: passed; 23 claims, 68 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 23 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:53–20:49 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-28 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-28.xlsx (7 posts, 12:50–20:38 ET), tfr-postplanner-tobi-2026-06-28.xlsx (7 TOBI posts)
- **Coverage:** Keys wins Eastbourne third title (def. Maria 7-5, 6-3; joins Evert/Navratilova; first player to win first 3 Eastbourne finals; second set score MEDIUM — LTA says 6-4, majority says 6-3); CORRECTION: Davidovich Fokina wins Mallorca NOT Quinn — ADF def. Quinn 7-6(4), 6-3 in sixth career final; first career title; first Spanish Mallorca champion; rises No. 23; June 27 pipeline incorrectly reported Quinn won; Eastbourne men's final rain drama (Humbert vs Bergs halted 3 games Humbert 2-1; resumed Sunday Wimbledon-eve; both face each other AGAIN Wimbledon R1 Tuesday); Wimbledon Day 1 (CC 1:30 PM BST: Sinner/Kecmanovic, Sabalenka/Kostovic, Djokovic/Wu Yibing; C1: FAA + Andreeva; Serena 44 vs Joint 20 first Grand Slam singles since 2022 US Open); Wimbledon 5 storylines (Djokovic record chase; Serena comeback; Andreeva double chase; Raducanu fitness; Fritz vs Draper R1)
- **Notes:**
  - CORRECTION LOGGED: June 27 pipeline reported "Ethan Quinn wins Mallorca 6-1, 6-2" — actual result was ADF def. Quinn 7-6(4), 6-3. Semi-final scores in June 27 were correct (ADF def. Marozsan; Quinn def. Borges); only the final result was wrong.
  - Keys score: second set is MEDIUM confidence (LTA says 6-4, majority of sources say 6-3; used 6-3 with flag)
  - Eastbourne men's final result: NOT confirmed from named article; the match resumed Sunday June 28 but result was not confirmed in searches at content creation time
  - Djokovic 2026 match count: MEDIUM — one source says 13, another says 14
  - verify-facts.py: passed; 27 claims, 72 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 7 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 22 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (7 posts) and TOBI (7 posts) generated successfully; 12:50–20:38 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-27 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-27.xlsx (7 posts, 12:50–20:38 ET), tfr-postplanner-tobi-2026-06-27.xlsx (7 TOBI posts)
- **Coverage:** Ethan Quinn wins Mallorca ATP 250 (22yo Fresno CA, 2023 NCAA champ Georgia, first ATP title, def. ADF 6-1, 6-2; SF Quinn def. Borges 6-1, 6-2; ADF def. Marozsan 5-7, 6-2, 6-4; 3rd American Mallorca finalist/first winner; new career high ~No. 47); Muchova wins Bad Homburg WTA 500 (Osaka retired right foot injury 6-1, 1-0 after 49 min; Muchova 3rd career title, 2nd of 2026 Doha+BH; Osaka first career grass final; Wimbledon fitness Q); Wimbledon 13 withdrawals (men: Alcaraz wrist, Musetti thigh, Rune Achilles/knee, Korda, Machac foot, Vacherot No. 20, Opelka; women: Mboko No. 9 MCL Queen's, Baptiste, Kartal, Vondrousova, Kudermetova illness; Vidmanova 2025 NCAA champ replaces Mboko; video reviews debut; £64.2M prize record); Eastbourne finals Saturday (men: Humbert vs Bergs; women: Keys vs Maria); Wimbledon draw (Fritz 6 vs Draper R1; Ruud 11 vs Hurkacz R1; Sinner 1 vs Kecmanovic; Djokovic 7 vs Wu Yibing; Sinner/Djokovic same top half; Andreeva 5 vs Linette — RG/Wimbledon double chance last Henin 2006; Serena in Swiatek quarter)
- **Notes:**
  - CORRECTIONS LOGGED: (1) June 26 pipeline incorrectly reported Mallorca SFs as "Marozsan def. ADF 6-4, 6-3 and Borges def. Quinn 7-6(1), 6-4; final Marozsan vs Borges" — actual: ADF def. Marozsan 5-7, 6-2, 6-4 and Quinn def. Borges 6-1, 6-2; final Quinn vs ADF. (2) June 26 pipeline incorrectly stated Eastbourne SF "Samuel def. Bergs 6-3, 6-4" — actual: Bergs def. Samuel 4-6, 7-6(5), 6-2; correct final is Humbert vs Bergs (not Humbert vs Samuel).
  - verify-facts.py: passed; 29 claims, 72 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 7 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 22 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (7 posts) and TOBI (7 posts) generated successfully; 12:50–20:38 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-26 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (1 Tier 1, 4 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-26.xlsx (6 posts, 12:53–20:23 ET), tfr-postplanner-tobi-2026-06-26.xlsx (6 TOBI posts)
- **Coverage:** Wimbledon 2026 draw ceremony — Fritz (6) vs Draper R1 blockbuster; Ruud (11) vs Hurkacz R1; Sinner (1) vs Kecmanovic; Djokovic (7) vs Wu Yibing; Sinner/Djokovic in same top half (potential SF); Zverev (2) leads bottom half; Championships June 29); Eastbourne SFs — Humbert def. Draper in 3 sets, Samuel def. Bergs 6-3, 6-4; final Saturday: Humbert vs Samuel; Draper faces Fritz at Wimbledon R1); Bad Homburg WTA SFs — Osaka vs Wang + Ruse vs Muchova; Osaka seeking first career grass final (first grass SF in 7 years; def. Alexandrova 6-2, 6-2 QF); Wang via walkover (Svitolina hip); Ruse (No. 105) def. Navarro QF; Andreeva already out; Final Saturday); Wimbledon women's draw — Swiatek (3) vs Townsend; Serena vs Maya Joint in same quarter (potential R3 Swiatek/Serena); Sabalenka (1) vs Kostovic; Rybakina (2) vs Boisson; Andreeva (5) vs Linette — RG/Wimbledon double chance last achieved by Henin 2006; Gauff (7) vs Korpatsch); Mallorca SFs — Marozsan def. ADF 6-4, 6-3 (upset); Borges def. Quinn 7-6(1), 6-4; final Saturday: Marozsan vs Borges
- **Notes:**
  - verify-facts.py: passed; 24 claims, 56 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully; 12:53–20:23 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Eastbourne SF score (Humbert def. Draper) reported from single source — marked MEDIUM; three-set result confirmed by multiple sources
  - Bad Homburg SF results (Osaka vs Wang; Ruse vs Muchova) scheduled for June 26; actual scores not available at pipeline run time; story covers context and stakes

### 2026-06-25 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (1 Tier 1, 4 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-25.xlsx (6 posts, 12:48–20:18 ET), tfr-postplanner-tobi-2026-06-25.xlsx (6 TOBI posts)
- **Coverage:** Fritz last-minute withdrawal from Eastbourne as defending champion (Wimbledon preservation; Draper into SF; Toby Samuel through; Djokovic overtakes Fritz in ATP rankings); Dan Evans last-ever professional singles match (lost to Schoolkate 7-5, 6-0 Wimbledon qualifying R2; still doubles with Searle; Watson/Tarvet/Harris/Basing in final qualifying round); Bad Homburg WTA QFs (Navarro def. Swiatek 7-5, 2-6, 6-3; H2H 2-2; Swiatek first grass match of 2026 = loss; Alexandrova def. Andreeva 6-1 6-7 6-1 R2; Svitolina withdraws hip injury; Wang Xinyu to SF walkover); Wimbledon draw preview (draw Friday June 26 10 AM BST; seedings locked; Alcaraz out; Serena WC; Djokovic fitness unknown; Championships June 29); Mallorca/Eastbourne QFs (Dimitrov vs ADF; Draper def. Diallo 7-5 6-4; both finals Saturday June 27)
- **Notes:**
  - verify-facts.py: passed; 33 claims, 68 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully; 12:48–20:18 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-24 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (1 Tier 1, 4 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-24.xlsx (6 posts, 12:46–20:16 ET), tfr-postplanner-tobi-2026-06-24.xlsx (6 TOBI posts)
- **Coverage:** Djokovic mystery withdrawal from Hurlingham Giorgio Armani Tennis Classic (hours before scheduled vs Khachanov; replaced by Martin Damm; no explanation; 13 matches in 2026; last match RG R3 May 29; back treatment at All England Club; No. 7 seed; Wimbledon June 29); Sinner first grass of 2026 at Hurlingham vs Norrie (exhibition; defending champion; skipped all ATP warm-ups; draw Friday June 26); Wimbledon qualifying Day 3 (Watson def. Sherif 6-2, 6-2; Adeshina def. Uchijima 8th seed 6-1, 3-6, 7-5 biggest career win; Evans through; final day Thursday June 25); Bad Homburg WTA QFs (Osaka def. Mertens 6-3, 6-3 first QF of 2026; Andreeva def. Wang 6-3, 6-4; Swiatek def. Navarro 7-6(6), 6-3 + Kalinskaya 6-4, 6-1; potential Swiatek vs Andreeva QF; Final Saturday June 27); Mallorca + Eastbourne final days (Darderi def. Hanfmann 7-5, 6-3 first grass QF; Buse def. Tsitsipas; Walton def. Kyrgios; Dimitrov advancing; Fritz chasing 5th Eastbourne title; Draper at Eastbourne; both finals Saturday June 27)
- **Notes:**
  - verify-facts.py: passed; 46 claims, 108 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully; 12:46–20:16 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-23 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (1 Tier 1, 4 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-23.xlsx (6 posts), tfr-postplanner-tobi-2026-06-23.xlsx (6 TOBI posts)
- **Coverage:** Serena Williams accepts Wimbledon 2026 singles wild card (44yo, 7-time champion, first singles major since 2022 US Open R3; 8th and final women's WC; also doubles WC with Venus); Giorgio Armani Tennis Classic opens at Hurlingham (Sinner's first grass since 2025 Wimbledon; Sinner vs Norrie + Djokovic vs Khachanov scheduled Wednesday; field: Sinner/Djokovic/Shelton/Ruud/Lehecka/Cobolli/Darderi/Tien; June 23-27); Wimbledon wild cards (Wawrinka — 41, 3 slams, final career season; Dimitrov — No. 169, 2025 WC retired vs Sinner pectoral injury; British: Fearnley/Fery/Pinnington Jones/Samuel; women: Chwalinska + Serena); Wimbledon qualifying Day 2 (British charge: Evans/Searle/Harris/Tarvet/Basing/Jubb all through; Goffin out Day 1); Wimbledon preview (draw Friday June 26 10 AM BST; Sinner defending/Alcaraz out; Sabalenka No. 1 never won; Andreeva arrives with 0 Wimbledon pts)
- **Notes:**
  - verify-facts.py: passed; 29 claims, 94 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-22 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 8 X posts + 5 FB posts (5 long-form + 5 captions) = 13 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-22.xlsx (8 posts), tfr-postplanner-tobi-2026-06-22.xlsx (8 TOBI posts); 12:45–20:48 ET
- **Coverage:** Cerundolo wins Queen's Club (def. Paul 6-7(4), 6-4, 6-3; 3h03m longest final in tournament history; first Argentine champion; 5th career title; 1st ATP 500; 2nd grass title; ended Paul's 9-match QC streak); Noskova wins Berlin WTA 500 (def. Pegula 6-4, 4-6, 6-3; 2nd career title; first grass; Top 10 debut as world No. 10; new Czech No. 1); Bouzkova wins Nottingham WTA (def. Navarro 7-6(5), 4-6, 6-2; 2h57m longest WTA match of 2026; 4th career title; first grass; career-high No. 22); Wimbledon 2026 seedings locked (cutoff today June 22; Men: Sinner 1, Zverev 2, FAA 3, Shelton 4, de Minaur 5, Fritz 6, Djokovic 7, Medvedev 8; 6 Americans; Women: Sabalenka 1, Rybakina 2, Swiatek 3, Pegula 4, Andreeva 5; Alcaraz OUT wrist; draw June 26, Championships June 29); Wimbledon qualifying Day 1 at Roehampton (256 players, 32 spots, ESPN+ exclusive, through June 25)
- **Notes:**
  - Czech women sweep both WTA grass-court week 2 titles (Noskova Berlin + Bouzkova Nottingham) — highlighted across S2/S3
  - verify-facts.py: passed; 26 claims, 55 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 8 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 23 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (8 posts) and TOBI (8 posts) generated successfully; 12:45–20:48 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-21 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-21.xlsx (7 posts), tfr-postplanner-tobi-2026-06-21.xlsx (7 TOBI posts)
- **Coverage:** Tiafoe wins Halle ATP 500 (def. Fritz 6-4, 7-5; 4th career title; 2nd grass title; 1st ATP 500 title; first all-American Halle final in 33 editions; Fritz beat Zverev SF ending 10-match streak; Tiafoe beat Altmaier 6-1, 6-3 SF); Queen's Club final day (Paul [2024 champ, 9-match QC streak] vs Cerundolo [first ATP 500 final, H2H 5-2]; CORRECTION: June 20 pipeline wrongly said Humbert beat Paul — actual SF was Paul def. Humbert 6-3, 6-3); Berlin WTA final (Pegula defending, beat Sabalenka 6-4, 6-7(4), 6-0 in SF, 4th career win over No. 1; vs Noskova first grass final, 0 sets dropped; match rain-delayed) + Nottingham final (Bouzkova vs Navarro, first career meeting); Wimbledon qualifying starts Monday June 22 Roehampton (ESPN+ exclusive, £20 tickets, draw June 26, starts June 29, Sinner defending/Alcaraz out); American men dominate grass 2026 (Shelton won Stuttgart, Tiafoe wins Halle, Fritz two straight ATP finals, Paul in QC final — four Americans in three finals across grass weeks 1-2)
- **Notes:**
  - CORRECTION logged in story history: June 20 pipeline stated "Humbert def. Paul 7-5, 6-3" but actual SF result was Paul def. Humbert 6-3, 6-3 (confirmed via ATP Tour official)
  - verify-facts.py: passed; 29 claims, 61 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 7 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; 22 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (7 posts) and TOBI (7 posts) generated successfully; 12:48–20:36 ET
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-20 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-20.xlsx (7 posts), tfr-postplanner-tobi-2026-06-20.xlsx (7 TOBI posts)
- **Coverage:** Queen's Club SFs — Humbert def. Paul 7-5, 6-3 (ended 8-match streak); Cerundolo def. Nakashima 6-4, 6-7(5), 6-2; Final Sunday Cerundolo vs Humbert; Eala Berlin breakthrough — def. Rybakina (No. 2) + Svitolina back-to-back, 9-1 on grass 2026, WTA 125 Birmingham winner; Halle SF Saturday — Altmaier (WC, 81) stuns Medvedev (QF), Tiafoe saves 5 MPs vs FAA 3-6, 6-3, 7-6(14-12), Fritz def. Shelton QF, SFs today Zverev vs Fritz + Tiafoe vs Altmaier; Berlin WTA SFs (Sabalenka vs Pegula; Noskova vs Eala) + Nottingham SFs (Pliskova vs Bouzkova all-Czech; Navarro vs Golubic); Wimbledon countdown — 9 days, qualifying Monday June 22 Roehampton
- **Notes:**
  - verify-facts.py: passed; 21 claims, 60 HIGH; image not_started warnings cosmetic (expected for imagn source)
  - compile: 5 stories, 7 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; 22 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (7 posts) and TOBI (7 posts) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-19 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-19.xlsx (6 posts), tfr-postplanner-tobi-2026-06-19.xlsx (6 TOBI posts)
- **Coverage:** Fritz vs Shelton Halle QF rematch (5 days after Stuttgart final; Shelton 6-win streak, Fritz 5-1 grass); Queen's Club QF Day — de Minaur vs Nakashima, Paul vs Davidovich Fokina (both unbeaten in sets), Fery vs Cerundolo, Hijikata (who upset Lehecka 4-6, 7-5, 7-6(7)) in draw; Berlin WTA QF — Sabalenka vs Bartunkova, Badosa vs Noskova, Pegula vs Keys (final Sunday June 21); Wimbledon countdown — draw June 26, qualifying Monday June 22, Sinner cold (no ATP grass warm-ups), Alcaraz out (wrist), Williams sisters doubles wildcard, £64.2M prize; Nottingham QF — Fernandez upset by Sonmez 6-4, 7-6(1)
- **Notes:**
  - CORRECTION from June 18: Paul was NOT upset by van de Zandschulp (as reported). Multiple June 19 sources confirm Paul is alive in QF vs Davidovich Fokina. Real upset: Hijikata def. Lehecka (No. 2 seed) 4-6, 7-5, 7-6(7). This was a WebFetch distortion in June 18 pipeline.
  - verify-facts.py: passed; 43 claims, 86 HIGH; image not_started warnings cosmetic (imagn source, expected)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; posting window warnings cosmetic
  - dashboard: 21 items
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-18 — Full Pipeline Run
- **Steps completed:** All 15
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-18.xlsx (6 posts), tfr-postplanner-tobi-2026-06-18.xlsx (6 TOBI posts)
- **Coverage:** Halle R16 sweep; Badosa stuns Gauff 1-6, 6-3, 6-2 in Berlin; van de Zandschulp result noted as incorrect on June 19; Berlin QF set; Wimbledon countdown 11 days
- **Notes:** WordPress proxy error; Dashboard push failed; Correction: Paul vs van de Zandschulp story was inaccurate — Paul alive in QF per June 19 sources

### 2026-06-16 — Full Pipeline Run
- **Steps completed:** All 15
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
