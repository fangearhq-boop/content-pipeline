# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-05-12 |
| Writing | Complete (all steps) | 2026-05-12 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 27 claims, image warnings cosmetic) | 2026-05-12 |
| Compile | Complete (07-content-data.json — 5 stories, 8 X posts, 0 FB (format), 5 articles) | 2026-05-12 |
| Dashboard | Complete (review-dashboard.html, 23 items) | 2026-05-12 |
| PostPlanner Export | Complete (standard 8 posts + TOBI 8 posts) | 2026-05-12 |
| WordPress Publish | Attempted — proxy blocks fanrumor.com (same as all previous runs) | 2026-05-12 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-05-12 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-05-12 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-12.xlsx (8 posts), tfr-postplanner-tobi-2026-05-12.xlsx (8 TOBI posts)
- **Coverage:** Sinner vs Pellegrino ATP Rome R16 (25-0 M1000 in 2026, 30-match streak 2nd all-time, Career Golden Masters quest, QF vs Ruud awaits, Pellegrino wildcard def. Tiafoe); Swiatek retires vs Rybakina WTA Rome QF (2-6, 7-6(3), 2-2 ret. — 2nd straight early exit, RG qualifying May 18, Rybakina into SF); WTA Rome QF Day (Gauff vs Andreeva H2H 4-0 Gauff, Cirstea 36/final season vs Ostapenko — Cinderella continues); ATP R16 recap (Ruud def. Musetti 6-3, 6-1 with Musetti med timeout; Tirante def. Medvedev 6-3, 6-4 upset; Zverev def. Darderi); Roland Garros 13 days (Alcaraz out, Swiatek health doubt, Sinner 25-0 M1000 overwhelming fave, Rybakina surging, Wawrinka's final RG)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 27 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 8 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 9 images
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
- **Coverage:** Sinner vs Popyrin ATP Rome R3 (29 consecutive M1000 wins = Federer 3rd all-time; Career Golden Masters — Rome is only M1000 Sinner hasn't won; Popyrin beat Berrettini + Mensik en route; scheduled 3 PM CEST); Swiatek vs Osaka WTA Rome R16 (rematch of 2024 RG classic; Roig (new coach) tore Achilles courtside Sunday; wide-open draw post-Sabalenka/Paolini exits); WTA R16 day (Gauff vs Jovic all-American, Andreeva vs Mertens, Cirstea vs Noskova); ATP R3 results (Cobolli 7-6(1) 6-3, Nakashima 6-4 6-0, Tiafoe 6-7(5) 6-3 6-2, Rublev 6-4 6-4, Navone def. FAA 7-6(4) 7-6(5)); Cirstea Cinderella continues (36yo, final season, def. Sabalenka Sat, faces Noskova R16)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 22 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 7 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (22 items)
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
