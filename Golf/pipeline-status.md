# Golf Fanrecap — Pipeline Status

## Latest Run: 2026-09-23

**Run completed:** 2026-09-23
**Stories:** 5
**Articles:** 5
**X posts:** 9
**Status:** COMPLETE

### Scripts Run
- [x] verify-facts.py — 14 claims, all HIGH confidence
- [x] compile-content-data.py — 5 stories, 9 tweets, 5 articles
- [x] generate-review-dashboard.py — 24 items
- [x] publish-unified-dashboard.py — blocked (content-dashboards repo not in authorized set)
- [x] generate-postplanner-export.py — 0 posts (known parsing issue)
- [x] generate-postplanner-export.py --tobi — 0 posts (known parsing issue)
- [x] publish-to-wordpress.py — blocked (fanrumor.com not in egress allowlist)

### Known Non-Blocking Issues
- Dashboard push blocked: content-dashboards repo not in this session's authorized repository set
- WordPress publish blocked: fanrumor.com egress denied by proxy
- PostPlanner export shows 0 posts: known social post format parsing issue
- FB posts show 0 in compile output: known parsing issue

### Stories Covered
1. Presidents Cup Day 1 Eve — Opening Ceremony Tomorrow at Medinah (T1 FOLLOW UP)
2. PGA Tour Slams the Door — LIV Players Have No Easy Path Back, 20 Days Left (T1 FOLLOW UP)
3. International Team's Last Stand — 28 Years Without a Win, Starting Tomorrow (T1 FOLLOW UP)
4. Rahm, DeChambeau, Smith Rejected the PGA Tour's Offer — Now What? (T2 NEW)
5. Walmart NW Arkansas Championship Preview — Korda and the Solheim Returnees (T2 FOLLOW UP)

---

## Previous Run: 2026-09-22

**Status:** COMPLETE
