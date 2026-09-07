# Golf Fanrecap — Pipeline Status

## Last Run: 2026-09-07

**Status:** COMPLETE (with known proxy limitations)
**Niche:** Golf Fanrecap
**Stories:** 5
**Articles:** 5

---

## 2026-09-07 Run Log

| Step | Status | Notes |
|------|--------|-------|
| Research / WebSearch | ✅ Complete | 5 stories — LIV Golf bankruptcy imminent, Jon Rahm $100M+ owed, Solheim Cup practice week, Presidents Cup 2026 preview, PGA Tour Fall Swing preview |
| Daily Brief | ✅ Complete | 00-daily-brief.md |
| Research Notes | ✅ Complete | 01-research-notes.md |
| Story Analysis | ✅ Complete | 02-story-analysis.md |
| X Posts | ✅ Complete | 03-social-posts-x.md — 7 posts, all ≤280 chars |
| Facebook Posts | ✅ Complete | 04-social-posts-facebook.md — 5 stories |
| Image Concepts | ✅ Complete | 05-image-concepts.md |
| Articles | ✅ Complete | 5 HTML articles |
| Fact Check | ✅ Complete | 06-fact-check-log.md — 29 claims |
| Compile Content Data | ✅ Complete | 07-content-data.json (7 tweets, 5 articles) |
| Image Manifest | ✅ Complete | 07-image-manifest.md (10 images, status: not_started) |
| Review Dashboard | ✅ Complete | review-dashboard.html — 22 items |
| Publish Dashboard | ⚠ Partial | Dashboard generated locally; push to content-dashboards blocked (not in authorized repo set) |
| PostPlanner Export | ✅ Complete | gfr-postplanner-2026-09-07.xlsx (7 posts) |
| PostPlanner TOBI | ✅ Complete | gfr-postplanner-tobi-2026-09-07.xlsx (7 posts) |
| WordPress Publish | ⚠ Blocked | fanrumor.com:443 blocked by egress proxy (organization policy) |
| Git Commit + Push | ✅ Complete | Pushed to origin/main |

---

## 2026-09-06 Run Log

| Step | Status | Notes |
|------|--------|-------|
| Research / WebSearch | ✅ Complete | 5 stories — Paul Casey Omega European Masters win, LIV Golf bankruptcy filing this week, Solheim Cup eve/practice begins, Jackson Koivun Presidents Cup, Jon Rahm LIV contract |
| Daily Brief | ✅ Complete | 00-daily-brief.md |
| Research Notes | ✅ Complete | 01-research-notes.md |
| Story Analysis | ✅ Complete | 02-story-analysis.md |
| X Posts | ✅ Complete | 03-social-posts-x.md — 7 posts, all ≤280 chars |
| Facebook Posts | ✅ Complete | 04-social-posts-facebook.md — 5 stories |
| Image Concepts | ✅ Complete | 05-image-concepts.md |
| Articles | ✅ Complete | 5 HTML articles |
| Fact Check | ✅ Complete | 06-fact-check-log.md — 20 claims |
| Compile Content Data | ✅ Complete | 07-content-data.json (7 tweets, 5 articles) |
| Image Manifest | ✅ Complete | 07-image-manifest.md (10 images, status: not_started) |
| Review Dashboard | ✅ Complete | review-dashboard.html — 17 items |
| Publish Dashboard | ⚠ Partial | Dashboard generated locally; push to content-dashboards blocked (not in authorized repo set) |
| PostPlanner Export | ✅ Complete | gfr-postplanner-2026-09-06.xlsx (6 posts) |
| PostPlanner TOBI | ✅ Complete | gfr-postplanner-tobi-2026-09-06.xlsx (6 posts) |
| WordPress Publish | ❌ Blocked | fanrumor.com:443 rejected by egress proxy (403); articles ready for manual publish |
| Story History | ✅ Complete | story-history.md updated |

**Stories covered:**
1. T1 FOLLOW UP: Paul Casey Wins Omega European Masters — Pledges Prize to Crans-Montana Fire Victims
2. T1 FOLLOW UP: LIV Golf Bankruptcy Filing Expected This Week — PIF Ends Funding
3. T2 FOLLOW UP: Solheim Cup Eve — Practice Begins Tomorrow at Bernardus Golf
4. T2 FOLLOW UP: Jackson Koivun — The 21-Year-Old Heading to Medinah
5. T2 FOLLOW UP: Jon Rahm's $100M Question — What LIV Bankruptcy Means for Golf's Biggest Contract

---

## Known Issues

1. **WordPress publish blocked** — egress proxy rejects fanrumor.com:443 with 403. Run `publish-to-wordpress.py` manually from a machine with direct internet access.
2. **Content-dashboards push blocked** — fangearhq-boop/content-dashboards not in authorized repository set. Push manually or add repo to session sources.
3. **Facebook posts = 0 in compile** — compile-content-data.py does not detect FB long-form posts. Posts are authored in 04-social-posts-facebook.md and ready for manual scheduling.

---

## Articles

| File | Author | Story |
|------|--------|-------|
| article-01-paul-casey-omega-european-masters-charity.html | Ryan Calloway | Paul Casey win + charity pledge |
| article-02-liv-golf-bankruptcy-filing-september-2026.html | Jake Torres | LIV Golf bankruptcy filing |
| article-03-solheim-cup-2026-eve-bernardus-golf.html | Marcus Cole | Solheim Cup eve |
| article-04-jackson-koivun-presidents-cup-2026-medinah.html | Ryan Calloway | Jackson Koivun Presidents Cup |
| article-05-jon-rahm-liv-bankruptcy-contract.html | Jake Torres | Jon Rahm / LIV contract |

---

## Previous Run: 2026-09-05

- Solheim Cup 2026 — Two Days Out at Bernardus Golf
- LIV Golf Bankruptcy Chapter 11 Filing Expected Week of Sept 7
- Presidents Cup Rosters — Snedeker Leads USA, Ogilvy Captains International
- Biltmore Championship Asheville — New PGA Tour Event Sept 17-20
- Anna Nordqvist's Pairings Puzzle — Inside Europe's Solheim Strategy
