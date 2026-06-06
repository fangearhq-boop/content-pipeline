# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-06-06 |
| Writing | Complete (all steps) | 2026-06-06 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 33 claims; image warnings cosmetic/expected for imagn) | 2026-06-06 |
| Compile | Complete (07-content-data.json — 5 stories, 9 X posts, 0 FB posts, 5 articles, 5 images) | 2026-06-06 |
| Dashboard | Complete (review-dashboard.html, 24 items) | 2026-06-06 |
| PostPlanner Export | Complete (standard 9 posts + TOBI 9 posts) | 2026-06-06 |
| WordPress Publish | Attempted — proxy blocks WordPress API (same as all previous runs) | 2026-06-06 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-06-06 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

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
