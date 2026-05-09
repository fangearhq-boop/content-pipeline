# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-05-09 |
| Writing | Complete (all steps) | 2026-05-09 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 22 claims, image warnings cosmetic) | 2026-05-09 |
| Compile | Complete (07-content-data.json — 5 stories, 7 X posts, 0 FB (format), 5 articles) | 2026-05-09 |
| Dashboard | Complete (review-dashboard.html, 22 items) | 2026-05-09 |
| PostPlanner Export | Complete (standard 7 posts + TOBI 7 posts) | 2026-05-09 |
| WordPress Publish | Attempted — proxy blocks fanrumor.com (same as all previous runs) | 2026-05-09 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-05-09 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-05-09 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Marcus Cole x2, Ryan Calloway x2, Elena Voss x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-09.xlsx (7 posts), tfr-postplanner-tobi-2026-05-09.xlsx (7 TOBI posts)
- **Coverage:** Djokovic upset by Prizmic 2-6, 6-2, 6-4 (first opening-round Rome loss in 18 appearances; Djokovic physically hampered from 57-day shoulder layoff; Prizmic 20yo Croatian qualifier; Roland Garros now in doubt); Sinner Rome debut tonight vs Ofner (30-2 in 2026, 5 consecutive M1000 titles, Career Golden Masters quest, last Italian winner Panatta 1976); WTA Rome R3 day (Sabalenka/Gauff/Paolini/Andreeva all in action, projected Sabalenka-Gauff QF); ATP Rome R2 day (Medvedev vs Machac, Zverev fresh off 7-5, 6-3 win vs Altmaier); Roland Garros 15 days away (Alcaraz out, Djokovic doubtful, Sinner overwhelming favourite for Career Grand Slam)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 22 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 7 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (22 items)
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-05-08 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-08.xlsx (7 posts), tfr-postplanner-tobi-2026-05-08.xlsx (7 TOBI posts)
- **Coverage:** Sabalenka def. Krejcikova 6-2, 6-3 (R2 result, 84 min, 26 winners, 28-1 season, R3 vs Cirstea, still chasing first Rome title in 8 appearances); Paolini def. Jeanjean 6-7(4), 6-2, 6-4 (defending champ survives nearly 3 hours, 57 UE + 54 winners, R3 vs Mertens); Swiatek def. McNally 6-2, 6-3 (clay return after Madrid virus, four-time RG champion back in form, 17 days to RG main draw); Djokovic vs Prizmic + Sinner vs Ofner R2 evening preview (Djokovic first clay since IW March 12, 6-time Rome champ; Sinner 28-match M1000 streak; Zverev vs Altmaier afternoon); Sinner Career Golden Masters feature (8 of 9 M1000 titles, Rome the last piece, 2nd after Djokovic to complete if wins, SF = pass Djokovic 2011 31-win streak record, no Italian winner since Panatta 1976)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 20 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 7 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (22 items)
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-05-07 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 10 FB posts (5 long-form + 5 captions) = 16 total
- **Articles:** 5 (bylines: Ryan Calloway x2, Elena Voss x2, Marcus Cole x1)
- **PostPlanner exports:** tfr-postplanner-2026-05-07.xlsx (16 posts), tfr-postplanner-tobi-2026-05-07.xlsx (11 TOBI posts)
- **Coverage:** Andreeva def. Ruzic 6-1, 6-0 (WTA Rome R2 — bounced back from Madrid final; tour-leading 13 clay wins; first-time RG seeding); WTA Rome Day 3 (Sabalenka vs Krejcikova headliner — Sabalenka eyes first Rome title vs 2-time Grand Slam champ; Gauff vs Valentova; Paolini defends vs Jeanjean); Djokovic vs qualifier Prizmic R2 preview (Prizmic beat Fucsovics; Djokovic first clay match since IW March 12; Sinner also enters R2); ATP Rome Day 2 (Berrettini vs Popyrin; Sonego vs Buse; Tsitsipas vs Machac; Day 1 upset Hanfmann def. Hurkacz); WTA Roland Garros form guide (Rome last WTA 1000 before RG May 25; Gauff defending; Sabalenka No. 1; Andreeva 13 clay wins; Swiatek needs form; Rybakina targets AO-RG double)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 21 claims; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 6 X posts, 10 FB posts, 5 articles, 5 images
  - review-dashboard.html generated (21 items)
  - PostPlanner exports: both standard (16) and TOBI (11) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
