# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-05-18 |
| Writing | Complete (all steps) | 2026-05-18 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 25 claims, image warnings cosmetic) | 2026-05-18 |
| Compile | Complete (07-content-data.json — 5 stories, 7 X posts, 5 FB posts, 5 articles, 10 images) | 2026-05-18 |
| Dashboard | Complete (review-dashboard.html, 27 items) | 2026-05-18 |
| PostPlanner Export | Complete (standard 7 posts + TOBI 7 posts) | 2026-05-18 |
| WordPress Publish | Attempted — proxy blocks fanrumor.com (same as all previous runs) | 2026-05-18 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-05-18 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-05-18 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-18.xlsx (7 posts), tfr-postplanner-tobi-2026-05-18.xlsx (7 TOBI posts)
- **Coverage:** Sinner def. Ruud 6-4, 6-4 Rome Final (Career Golden Masters complete, 2nd man ever after Djokovic; 6 consecutive M1000 titles; 34-match streak; swept MC+Madrid+Rome — only Nadal 2010 before him; first Italian Rome champion since Panatta 1976; H2H 6-0); Roland Garros qualifying opens today (Dimitrov vs Faria, Goffin vs Tseng farewell, women: Andreescu/Pliskova/Stephens/Badosa; Monfils farewell Thursday at Chatrier; draw May 21, main draw May 25); ATP rankings after Rome (Darderi career-high No. 16, Ruud top 20 return, Medvedev +2); WTA rankings after Rome (Svitolina No. 7, Cirstea first-ever top-20 debut at 36, Paolini drops out top 10, Zheng -21 places); Sinner to RG (Career Golden Masters done, only Slam missing is RG, Alcaraz out, Djokovic uncertain)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 25 claims; image warnings cosmetic (not_started expected)
  - compile: 5 stories, 7 X posts, 5 FB posts, 5 articles, 10 images (initial X posts format caused char violations → fixed to code block format, reran compile — clean)
  - dashboard: 27 items
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-05-17 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 5 FB long-form + 5 FB captions = 17 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-17.xlsx (7 posts), tfr-postplanner-tobi-2026-05-17.xlsx (7 TOBI posts)
- **Coverage:** Svitolina def. Gauff 6-4, 6-7(3), 6-2 WTA Rome final (3rd Rome title, 20th WTA crown, first Ukrainian in Open Era to 20 wins, clay finals 8-0, beat Nos. 2/3/4 in four days, dedicated to Ukrainians from "bomb shelters"); ATP Rome Final today Sinner vs Ruud (Career Golden Masters, Rome only missing M1000, 33-match M1000 streak, Sinner first Italian to reach back-to-back finals, H2H 5-0, match not before 5 PM CEST / 11 AM ET); Svitolina as RG contender (No. 7 seed, form player, 8-0 clay finals, only top-10 woman to win outdoor clay in 2026); RG qualifying starts Monday May 18 (draw May 21, main draw May 25, Alcaraz out, Wawrinka/Monfils wild cards); Ruud's Rome drought (5 finals, 0 titles, 3 GS runner-up spots, quote "try not to think about the big wave")
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 31 claims; image warning cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 7 X posts, 5 FB posts, 5 articles, 10 images
  - review-dashboard.html generated (27 items)
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
