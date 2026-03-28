# Golf Fanrecap — Pipeline Status

Dashboard subfolder: `gfr`
Dashboard URL: https://fangearhq-boop.github.io/content-dashboards/gfr/

## Current Pipeline

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-03-28 |
| Writing | Complete (all 7 files + 5 articles) | 2026-03-28 |
| Fact-check | Complete (verify-facts.py run) | 2026-03-28 |
| Scripts | Complete (all 6 scripts run) | 2026-03-28 |
| PostPlanner | Complete (standard + TOBI exports) | 2026-03-28 |
| Dashboard | Generated locally (push blocked — see notes) | 2026-03-28 |
| Published | Pending upload | — |

## Queue

(No items in queue.)

## Notes

### Pipeline Run: 2026-03-28
- **Research:** Web searches across PGA Tour (Houston Open), LPGA (Ford Championship, Founders Cup), LIV Golf (Singapore/South Africa)
- **Stories:** 7 stories tiered (2x T1, 4x T2, 1x T3)
- **Coverage:** PGA Tour (2), LPGA (2), LIV Golf (1), Masters Preview (2)
- **X Posts:** 9 posts across 6 time slots (8 AM - 8:30 PM ET), all verified under 280 chars
- **Facebook Posts:** 14 posts (7 long-form + 7 image captions)
- **Articles:** 5 HTML5 articles written with semantic structure and "What's Next" sections
- **Scripts run:**
  - `verify-facts.py`: 36 claims, 80% HIGH confidence; advisory warnings (missing article for Story 6 — expected, 5 articles per instructions)
  - `compile-content-data.py`: 7 stories, 9 tweets, 5 articles compiled to JSON
  - `generate-review-dashboard.py`: Dashboard HTML generated (28 items)
  - `publish-unified-dashboard.py`: Push to content-dashboards failed (PAT scope limited to content-pipeline)
  - `generate-postplanner-export.py`: `gfr-postplanner-2026-03-28.xlsx` (23 posts)
  - `generate-postplanner-export.py --tobi`: `gfr-postplanner-tobi-2026-03-28.xlsx` (16 TOBI posts)
- **Files created:**
  - `golf-content-2026-03-28/00-daily-brief.md`
  - `golf-content-2026-03-28/01-research-notes.md`
  - `golf-content-2026-03-28/02-story-analysis.md`
  - `golf-content-2026-03-28/03-social-posts-x.md`
  - `golf-content-2026-03-28/04-social-posts-facebook.md`
  - `golf-content-2026-03-28/05-image-concepts.md`
  - `golf-content-2026-03-28/06-fact-check-log.md`
  - `golf-content-2026-03-28/07-content-data.json`
  - `golf-content-2026-03-28/07-image-manifest.md`
  - `golf-content-2026-03-28/review-dashboard.html`
  - `golf-content-2026-03-28/articles/article-01-woodland-leads-houston-open-brain-surgery-comeback.html`
  - `golf-content-2026-03-28/articles/article-02-lydia-ko-shoots-60-ford-championship.html`
  - `golf-content-2026-03-28/articles/article-03-dechambeau-liv-back-to-back-march-dominance.html`
  - `golf-content-2026-03-28/articles/article-04-masters-2026-preview-scheffler-mclroy-grand-slam.html`
  - `golf-content-2026-03-28/articles/article-05-scheffler-wd-houston-open-grand-slam-chasers.html`
  - `Golf/postplanner-imports/gfr-postplanner-2026-03-28.xlsx`
  - `Golf/postplanner-imports/gfr-postplanner-tobi-2026-03-28.xlsx`
- **Key events covered:** Texas Children's Houston Open (PGA Tour, Moving Day), Ford Championship (LPGA, Phoenix), DeChambeau LIV March sweep, Masters 2026 preview

### Pipeline Run: 2026-03-20 (First Run)
- **Research:** 10+ web searches across PGA Tour, LIV Golf, LPGA, OWGR, merger news, injuries
- **Stories:** 7 stories tiered (1x T1, 5x T2, 1x T3)
- **Coverage:** PGA Tour (2), LIV Golf (1), LPGA (1), Business (1), Injuries (1), Rankings (1)
- **X Posts:** 10 posts across 6 time slots (8 AM - 8:30 PM ET), all verified under 280 chars
- **Files created:**
  - `golf-content-2026-03-20/00-daily-brief.md`
  - `golf-content-2026-03-20/01-verified-facts.md`
  - `golf-content-2026-03-20/02-story-analysis.md`
  - `golf-content-2026-03-20/03-social-posts-x.md`
- **Also updated:** `story-history.md`, `pipeline-status.md`
- **Remaining steps:** FB posts, image concepts, articles, fact-check script, dashboard generation, publishing
- **Key events this week:** Valspar Championship (PGA Tour, R2 today), LIV Golf South Africa (R2 today), Fortinet Founders Cup (LPGA, R2 today)
