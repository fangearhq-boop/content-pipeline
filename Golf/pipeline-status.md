# Golf Fanrecap — Pipeline Status

## Last Run: 2026-09-05

**Status:** COMPLETE (with known proxy limitations)
**Niche:** Golf Fanrecap
**Stories:** 5
**Articles:** 5

---

## Step Completion

| Step | Status | Notes |
|------|--------|-------|
| Research / WebSearch | ✅ Complete | 5 stories — Solheim Cup (2 days out), LIV Golf bankruptcy, Presidents Cup rosters, Biltmore Championship, Nordqvist pairings |
| Daily Brief | ✅ Complete | 00-daily-brief.md |
| Research Notes | ✅ Complete | 01-research-notes.md |
| Story Analysis | ✅ Complete | 02-story-analysis.md |
| X Posts | ✅ Complete | 03-social-posts-x.md — 7 posts, all ≤280 chars |
| Facebook Posts | ✅ Complete | 04-social-posts-facebook.md — 5 stories |
| Image Concepts | ✅ Complete | 05-image-concepts.md |
| Articles | ✅ Complete | 5 HTML articles in articles/ |
| Fact Check | ✅ Complete | 06-fact-check-log.md — 21 claims verified |
| Compile Content Data | ✅ Complete | 07-content-data.json (7 tweets, 5 articles) |
| Image Manifest | ✅ Complete | 07-image-manifest.md (10 images, status: not_started) |
| Review Dashboard | ✅ Complete | review-dashboard.html — 17 items |
| Publish Dashboard | ⚠ Partial | Dashboard generated locally; push to content-dashboards blocked (not in authorized repo set) |
| PostPlanner Export | ✅ Complete | gfr-postplanner-2026-09-05.xlsx (7 posts) |
| PostPlanner TOBI | ✅ Complete | gfr-postplanner-tobi-2026-09-05.xlsx (7 posts) |
| WordPress Publish | ❌ Blocked | fanrumor.com:443 rejected by egress proxy (403); articles ready for manual publish |
| Story History | ✅ Complete | story-history.md updated |

---

## Known Issues

1. **WordPress publish blocked** — egress proxy rejects fanrumor.com:443 with 403. Run `publish-to-wordpress.py` manually from a machine with direct internet access.
2. **Content-dashboards push blocked** — fangearhq-boop/content-dashboards not in authorized repository set. Push manually or add repo to session sources.
3. **Facebook posts = 0 in compile** — compile-content-data.py does not detect FB long-form posts. Posts are authored in 04-social-posts-facebook.md and ready for manual scheduling.

---

## Articles

| File | Author | Story |
|------|--------|-------|
| article-01-solheim-cup-preview-usa-europe-netherlands.html | Ryan Calloway | Solheim Cup 2 days out |
| article-02-liv-golf-bankruptcy-chapter-11-pif.html | Jake Torres | LIV Golf bankruptcy |
| article-03-presidents-cup-rosters-snedeker-koivun.html | Marcus Cole | Presidents Cup rosters |
| article-04-biltmore-championship-asheville-pga-tour-debut.html | Ryan Calloway | Biltmore Championship debut |
| article-05-nordqvist-solheim-cup-captain-pairings-puzzle.html | Jake Torres | Nordqvist pairings strategy |

---

## Previous Run: 2026-09-04

- LIV Golf bankruptcy expected by Sept 7 — Players offered pennies
- Solheim Cup rosters complete (4 days out)
- Korda vs Hull Solheim matchup analysis
- Presidents Cup full teams set, 3 weeks to Medinah
- Biltmore Championship preview (new fall swing event)
