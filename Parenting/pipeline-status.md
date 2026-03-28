# COS Parenting — Pipeline Status

## Latest Run: March 28, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (7 searches) | COMPLETE | D49 fiscal crisis/accounting error, Evenflo car seat recall, D11/D49 graduation dates, Blodgett trails, AAP anaphylaxis plan |
| Story History Check | COMPLETE | 5 NEW STORY |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM confidence tagging |
| Story Analysis | COMPLETE | 02-story-analysis.md — 5 stories, tier + window assignments |
| X Posts | COMPLETE | 03-social-posts-x.md — 6 posts, all under 280 chars (4 char fixes applied) |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions = 10 posts |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts |
| Articles | COMPLETE | 5 articles in articles/ folder (500-1000 words each) |
| Fact-Check | COMPLETE | verify-facts.py passed — 5 stories present in all files |
| Compile | COMPLETE | 07-content-data.json (5 stories, 6 X, 5 FB, 5 articles) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images, all not_started |
| Dashboard | COMPLETE | review-dashboard.html (26 items) |
| PostPlanner Export | COMPLETE | Standard (16 posts) + TOBI (11 posts) |
| Publishing | Attempted — push failed (PAT lacks write access to content-dashboards repo) | Dashboard committed locally in tmp clone |

## Story Count by Pillar

| Pillar | Count | Target |
|--------|-------|--------|
| Local News | 2 | 1-2 |
| Local Events | 1 | 1-2 |
| National Parenting | 2 | 1-2 |
| Evergreen | 0 | 0-1 |
| Humor | 0 | 0-1 |
| **Total** | **5** | **5-8** |

## Previous Runs

| Date | Stories | Posts | Status |
|------|---------|-------|--------|
| 2026-03-28 | 5 | 6 X + 10 FB | Current — Full pipeline (all 15 steps) |
| 2026-03-27 | 5 | 6 X + 10 FB | Complete (all 15 steps) |
| 2026-03-20 | 7 | 9 X posts | Complete (X only, no FB/articles) |
| 2026-02-24 | 7 | X + FB | Complete |
| 2026-02-23 | 7 | X + FB | Complete |
| 2026-02-22 | 7 | X + FB | Complete |

## Pipeline Run Log

### 2026-03-28 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 10 FB posts (5 long-form + 5 captions) = 16 total
- **Articles:** 5
- **PostPlanner exports:** cosp-postplanner-2026-03-28.xlsx (16 posts), cosp-postplanner-tobi-2026-03-28.xlsx (11 TOBI posts)
- **Coverage:** D49 fiscal crisis ($2M accounting error before teacher cuts), Evenflo LiteMax 30 car seat recall (Spanish manual error), D11+D49 graduation dates May 2026, Blodgett Open Space 14-mile trail expansion summer 2026, AAP updated pediatric anaphylaxis action plan
- **Research:** 7+ web searches covering D49 fiscal crisis, Evenflo NHTSA recall, D11/D49 graduation schedules, Blodgett Open Space TOPS2026, AAP anaphylaxis Annals study
- **Notes:**
  - verify-facts.py initially flagged 4 char count violations in X posts (290, 315, 307, 318 chars); all fixed before final pass
  - Image manifest uses `  "N":` indented quoted key format (required by verify-facts.py parser)
  - Push to content-dashboards failed: PAT lacks write permission to fangearhq-boop/content-dashboards repo (same as all previous runs)
  - Gemini image generation not run (base_only mode prompts written in 05-image-concepts.md; generation requires GEMINI_API_KEY)
  - Dual-format FB posts used: `#### Long-Form Post -- time MT` heading + `**Long-Form Post (time MT)**` bold marker
- **Files created:**
  - `parenting-content-2026-03-28/00-daily-brief.md`
  - `parenting-content-2026-03-28/01-research-notes.md`
  - `parenting-content-2026-03-28/02-story-analysis.md`
  - `parenting-content-2026-03-28/03-social-posts-x.md`
  - `parenting-content-2026-03-28/04-social-posts-facebook.md`
  - `parenting-content-2026-03-28/05-image-concepts.md`
  - `parenting-content-2026-03-28/06-fact-check-log.md`
  - `parenting-content-2026-03-28/07-content-data.json`
  - `parenting-content-2026-03-28/07-image-manifest.md`
  - `parenting-content-2026-03-28/review-dashboard.html`
  - `parenting-content-2026-03-28/articles/article-01-d49-fiscal-crisis-accounting-error-teacher-cuts.html`
  - `parenting-content-2026-03-28/articles/article-02-evenflo-litemax-30-car-seat-recall.html`
  - `parenting-content-2026-03-28/articles/article-03-d11-d49-graduation-dates-may-2026.html`
  - `parenting-content-2026-03-28/articles/article-04-blodgett-open-space-trail-expansion-2026.html`
  - `parenting-content-2026-03-28/articles/article-05-aap-anaphylaxis-action-plan-2026.html`
  - `postplanner-imports/cosp-postplanner-2026-03-28.xlsx`
  - `postplanner-imports/cosp-postplanner-tobi-2026-03-28.xlsx`

### 2026-03-27 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (1 Tier 1, 3 Tier 2, 1 Tier 3)
- **Posts:** 6 X posts + 10 FB posts (5 long-form + 5 captions) = 16 total
- **Articles:** 5
- **PostPlanner exports:** cosp-postplanner-2026-03-27.xlsx (16 posts), cosp-postplanner-tobi-2026-03-27.xlsx (11 TOBI posts)
- **Coverage:** CPSC recalls (Vevor baby swings + Zigjoy sleep sacks), D11 spring break ends + weekend activities, Rock Island Trail bridge + Pikes Peak Greenway expansion, AAP 2026 screen time update, Spring COS family events (Garden of Gods Art Festival, Spring Fling)
- **Research:** 7 web searches covering D11/D20 school news, COS family events, CPSC recalls, AAP screen time guidelines, COS parks/trails, spring weather
- **Notes:**
  - Dual-format FB posts used
  - Image manifest uses `  "N":` indented quoted key format
  - Push to content-dashboards failed: PAT lacks write permission

### 2026-03-20 — Partial Run (X Only)
- **Steps completed:** Research, Story History, Daily Brief, Verified Facts, Story Analysis, X Posts
- **Stories:** 7 stories (2 Tier 1, 3 Tier 2, 2 Tier 3)
- **Posts:** 9 X posts
- **Notes:** First full COS Parenting run. FB posts, image concepts, articles, dashboard steps deferred (not requested).
