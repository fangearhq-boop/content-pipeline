# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-04-23 |
| Writing | Complete (all steps) | 2026-04-23 |
| Fact-check | Complete (verify-facts.py passed) | 2026-04-23 |
| Compile | Complete (07-content-data.json — 5 stories, 8 X posts, 5 FB posts, 5 articles) | 2026-04-23 |
| Dashboard | Complete (review-dashboard.html, 28 items) | 2026-04-23 |
| PostPlanner Export | Complete (standard + TOBI) | 2026-04-23 |
| WordPress Publish | Attempted — proxy blocks fanrumor.com (same as all previous runs) | 2026-04-23 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | 2026-04-23 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-04-23 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 5 FB posts (5 long-form + 5 captions) = 13 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-04-23.xlsx (8 posts), tfr-postplanner-tobi-2026-04-23.xlsx (8 TOBI posts)
- **Coverage:** Sinner hunts unprecedented 5th consecutive Masters 1000 title at Madrid (4-in-a-row: Paris/IW/Miami/MC); Sabalenka and Swiatek clay season debuts same day at Madrid (Sabalenka vs. Stearns, Swiatek vs. Snigur); Alcaraz wrist injury — French Open defense in serious doubt, test results pending; Eala def. Pavlyuchenkova 6-3, 6-3 at Madrid (No. 41 live, RG seeding possible); Madrid Day 1 ATP recap — Berrettini fell to Prizmic 6-3, 6-4; Shelton vs. Prizmic R2 set up
- **Notes:**
  - 3 X posts had char limit violations (Story 2 Post B, Story 3 Posts A+B) — fixed before re-run of verify-facts
  - Facebook posts initially had wrong format (em dashes vs double dashes) — fixed, recompiled, FB posts: 5
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Image warnings are cosmetic (not_started is expected at this stage)

### 2026-04-22 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 9 X posts + 5 FB posts (5 long-form + 5 captions) = 14 total
- **Articles:** 5 (bylines: Elena Voss x2, Marcus Cole x2, Ryan Calloway x1)
- **PostPlanner exports:** tfr-postplanner-2026-04-22.xlsx (9 posts), tfr-postplanner-tobi-2026-04-22.xlsx (9 TOBI posts)
- **Coverage:** Arthur Fils wins Barcelona 6-2, 7-6(2) over Rublev — 4th career title, 1st since 7-month injury return; Ben Shelton wins Munich 6-2, 7-5 over Cobolli — first American since Agassi 2002 to win ATP 500+ on clay (24-year drought); Rybakina wins Stuttgart 7-5, 6-1 over Muchova — 13th career WTA title, first repeat title of career (12 cities in 12 titles); Alcaraz arm cast / French Open doubt — Feliciano Lopez fears 2-month layoff; Madrid Open 2026 opens — Sinner No. 1 hunting 5th straight Masters 1000 title
- **Notes:**
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo
