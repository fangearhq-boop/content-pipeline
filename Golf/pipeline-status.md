# Golf Fanrecap — Pipeline Status

## Last Run: 2026-09-04

**Status:** COMPLETE (with known proxy limitations)
**Niche:** Golf Fanrecap
**Stories:** 5
**Articles:** 5

---

## Step Completion

| Step | Status | Notes |
|------|--------|-------|
| Research / WebSearch | ✅ Complete | 5 stories researched across LIV bankruptcy, Solheim Cup, PGA Tour, Presidents Cup, NW Arkansas |
| Daily Brief | ✅ Complete | 00-daily-brief.md |
| Research Notes | ✅ Complete | 01-research-notes.md |
| Story Analysis | ✅ Complete | 02-story-analysis.md |
| X Posts | ✅ Complete | 03-social-posts-x.md — 7 posts, all ≤280 chars |
| Facebook Posts | ✅ Complete | 04-social-posts-facebook.md — 5 stories |
| Image Concepts | ✅ Complete | 05-image-concepts.md |
| Articles | ✅ Complete | 5 HTML articles in articles/ |
| Fact Check | ✅ Complete | 06-fact-check-log.md — 14 claims verified |
| Compile Content Data | ✅ Complete | 07-content-data.json (7 tweets, 5 articles) |
| Image Manifest | ✅ Complete | 07-image-manifest.md (10 images, status: not_started) |
| Review Dashboard | ✅ Complete | review-dashboard.html — 27 items |
| Publish Dashboard | ⚠ Partial | Dashboard generated locally; push to content-dashboards blocked (not in authorized repo set) |
| PostPlanner Export | ✅ Complete | gfr-postplanner-2026-09-04.xlsx (7 posts) |
| PostPlanner TOBI | ✅ Complete | gfr-postplanner-tobi-2026-09-04.xlsx (7 posts) |
| WordPress Publish | ❌ Blocked | fanrumor.com:443 rejected by egress proxy (403); articles ready for manual publish |
| Story History | ✅ Complete | story-history.md updated |

---

## Known Issues

1. **WordPress publish blocked** — egress proxy rejects fanrumor.com:443 with 403. Run `publish-to-wordpress.py` manually from a machine with direct internet access.
2. **Content-dashboards push blocked** — fangearhq-boop/content-dashboards not in authorized repository set.
3. **Facebook posts = 0 in compile** — known script parsing issue; posts are in 04-social-posts-facebook.md.

---

## Articles

| File | Author | Story |
|------|--------|-------|
| article-01-liv-golf-bankruptcy-rahm-100m-september-2026.html | Ryan Calloway | LIV bankruptcy/Rahm $100M |
| article-02-solheim-cup-2026-preview-netherlands-korda-hull.html | Jake Torres | Solheim Cup 3 days out |
| article-03-pga-tour-no-path-back-liv-golfers-rolapp.html | Marcus Cole | PGA Tour "no path back" |
| article-04-presidents-cup-2026-medinah-tiger-scheffler.html | Ryan Calloway | Presidents Cup preview |
| article-05-walmart-nw-arkansas-championship-20th-anniversary-lpga.html | Jake Torres | Walmart NW Arkansas 20th anniv |

---

## Previous Run: 2026-09-03

- LIV Golf bankruptcy expected by Sept 7 — Players offered pennies
- Solheim Cup rosters complete (4 days out)
- Korda vs Hull Solheim matchup analysis
- Presidents Cup full teams set, 3 weeks to Medinah
- Biltmore Championship preview (new fall swing event)
