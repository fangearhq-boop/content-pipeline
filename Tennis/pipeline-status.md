# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-05-13 |
| Writing | Complete (all steps) | 2026-05-13 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 26 claims, image warnings cosmetic) | 2026-05-13 |
| Compile | Complete (07-content-data.json — 5 stories, 8 X posts, 0 FB (format), 5 articles) | 2026-05-13 |
| Dashboard | Complete (review-dashboard.html, 23 items) | 2026-05-13 |
| PostPlanner Export | Complete (standard 8 posts + TOBI 8 posts) | 2026-05-13 |
| WordPress Publish | Attempted — proxy blocks fanrumor.com (same as all previous runs) | 2026-05-13 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-05-13 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-05-13 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-13.xlsx (8 posts), tfr-postplanner-tobi-2026-05-13.xlsx (8 TOBI posts)
- **Coverage:** Sinner vs Rublev ATP Rome QF (31 consecutive M1000 wins = tied Djokovic all-time record; win = sole record + Career Golden Masters quest; Rome only M1000 Sinner hasn't won); Swiatek def. Pegula 6-1, 6-2 (dropped 3 games; Pegula had won last 2 meetings; new coach Roig; RG 12 days away); Gauff def. Andreeva 4-6, 6-2, 6-4 (5 match points, 2h17m; up 5-1 broken, still won; SF vs Cirstea); Cirstea first career Rome SF at 36 (final season; def. Ostapenko 6-1, 7-6(7); ran through Sabalenka/Noskova/Ostapenko); Jodar (19) vs Darderi QF (youngest Rome QFer since Djokovic 2007; Darderi def. Zverev saving 4 MPs 1-6, 7-6(10), 6-0)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 26 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 8 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (23 items)
  - PostPlanner exports: both standard (8) and TOBI (8) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-05-11 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Ryan Calloway x2, Elena Voss x2, Marcus Cole x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-11.xlsx (7 posts), tfr-postplanner-tobi-2026-05-11.xlsx (7 TOBI posts)
- **Coverage:** Sinner vs Popyrin ATP Rome R3 (29 consecutive M1000 wins = Federer 3rd all-time; Career Golden Masters — Rome is only M1000 Sinner hasn't won; Popyrin beat Berrettini + Mensik en route; scheduled 3 PM CEST); Swiatek vs Osaka WTA Rome R16 (rematch of 2024 RG classic; Roig (new coach, Nadal's coach 2005-22) tore Achilles courtside; Sabalenka/Paolini both out = winner is title contender; H2H Swiatek 2-1); WTA R16 day (Gauff vs Jovic all-American, Andreeva vs Mertens, Cirstea vs Noskova); ATP R3 results (Cobolli 7-6(1) 6-3, Nakashima 6-4 6-0, Tiafoe 6-7(5) 6-3 6-2, Rublev 6-4 6-4, Navone def. FAA 7-6(4) 7-6(5)); Cirstea Cinderella continues (36yo, final season, def. Sabalenka Sat, faces Noskova R16)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 22 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 7 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (22 items)
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-05-10 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 6 X posts + 10 FB posts (5 long-form + 5 captions) = 16 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-10.xlsx (6 posts), tfr-postplanner-tobi-2026-05-10.xlsx (6 TOBI posts)
- **Coverage:** Cirstea stuns Sabalenka 2-6, 6-3, 7-5 (world No. 1 exits with lower back/hip injury; first career win over No. 1 for 36yo Cirstea in final season; French Open now in serious doubt; 2nd consecutive early exit after Madrid QF); Paolini's title defense ends (Mertens saves 3 MPs, wins 4-6, 7-6(5), 6-3, 2h44m; home crowd silenced at Foro Italico); Sinner def. Ofner 6-3, 6-4 (29 consecutive M1000 wins ties Federer 3rd all-time; zero BPs conceded; next vs Popyrin); Gauff def. Sierra 5-7 6-0 6-4 + Andreeva def. Golubic 6-1 4-6 6-0 (draw wide open after Sabalenka/Paolini exits); Roland Garros 14 days away (Alcaraz out, Djokovic doubtful, Sabalenka injured — men's draw Sinner's to lose; women's wide open)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 38 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 6 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (21 items)
  - PostPlanner exports: both standard (6) and TOBI (6) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
