# F1 Fanrecap — Pipeline Status

## Last Run: 2026-09-04

**Status:** COMPLETE (with known proxy limitations)
**Niche:** F1 Fanrecap
**Stories:** 5
**Articles:** 5

---

## Step Completion

| Step | Status | Notes |
|------|--------|-------|
| Research / WebSearch | ✅ Complete | 5 stories researched — Italian GP, Ferrari Schumacher tribute, calendar uncertainty, Antonelli penalty, Norris title charge |
| Daily Brief | ✅ Complete | 00-daily-brief.md |
| Research Notes | ✅ Complete | 01-research-notes.md |
| Story Analysis | ✅ Complete | 02-story-analysis.md |
| X Posts | ✅ Complete | 03-social-posts-x.md — 7 posts, all ≤280 chars |
| Facebook Posts | ✅ Complete | 04-social-posts-facebook.md — 5 stories |
| Image Concepts | ✅ Complete | 05-image-concepts.md |
| Articles | ✅ Complete | 5 HTML articles in articles/ |
| Fact Check | ✅ Complete | 06-fact-check-log.md — 19 claims verified |
| Compile Content Data | ✅ Complete | 07-content-data.json (7 tweets, 5 articles) |
| Image Manifest | ✅ Complete | 07-image-manifest.md (10 images, status: not_started) |
| Review Dashboard | ✅ Complete | review-dashboard.html — 27 items |
| Publish Dashboard | ⚠ Partial | Dashboard generated locally; push to content-dashboards blocked (not in authorized repo set) |
| PostPlanner Export | ✅ Complete | f1fr-postplanner-2026-09-04.xlsx (7 posts) |
| PostPlanner TOBI | ✅ Complete | f1fr-postplanner-tobi-2026-09-04.xlsx (7 posts) |
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
| article-01-italian-gp-antonelli-norris-monza-preview.html | Ryan Calloway | Italian GP preview |
| article-02-ferrari-schumacher-tribute-livery-monza.html | Marcus Cole | Ferrari Schumacher tribute |
| article-03-f1-season-finale-qatar-abudhabi-middle-east.html | Elena Voss | Season finale in doubt |
| article-04-antonelli-engine-penalty-monza-championship.html | Ryan Calloway | Antonelli engine penalty |
| article-05-norris-three-straight-monza-title-charge.html | Elena Voss | Norris title charge |

---

## Previous Run: 2026-09-03

- 5 articles published
- Ferrari ADUO-2 engine, Antonelli penalty (covered again with fresh angle), Norris streak, Monza power struggles, F1 calendar
