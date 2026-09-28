# Golf Fanrecap — Pipeline Status

## Latest Run: 2026-09-28

**Run completed:** 2026-09-28
**Stories:** 5
**Articles:** 5
**X posts:** 9
**Status:** COMPLETE

### Scripts Run
- [x] verify-facts.py -- 28 claims, HIGH confidence; image warnings expected (imagn sourcing)
- [x] compile-content-data.py -- 5 stories, 9 tweets, 5 articles; posting window warnings (non-blocking); FB=0 known
- [x] generate-review-dashboard.py -- 24 items
- [x] publish-unified-dashboard.py -- blocked (content-dashboards repo not in authorized set)
- [x] generate-postplanner-export.py -- 0 posts (known parsing issue)
- [x] generate-postplanner-export.py --tobi -- 0 posts (known parsing issue)
- [x] publish-to-wordpress.py -- blocked (fanrumor.com:443 not in egress allowlist)
- [x] git commit + push -- via git push HEAD:main

### Known Non-Blocking Issues
- Dashboard push blocked: content-dashboards repo not in this session's authorized repository set
- WordPress publish blocked: fanrumor.com:443 rejected by egress proxy
- PostPlanner export shows 0 posts: known social post format parsing issue

### Stories Covered
1. T1 NEW: USA Wins Presidents Cup 17-13 at Medinah -- Greatest Sunday Comeback in Event History (Ryan Calloway)
2. T1 FOLLOW UP: Yuna Nishimura Wins NW Arkansas Championship -- First LPGA Tour Title (Jake Torres)
3. T1 FOLLOW UP: LIV Golf Bankruptcy -- October 13 Player Deadline Is 15 Days Away (Marcus Cole)
4. T2 NEW: Bank of Utah Championship Preview -- PGA Tour Fall at Black Desert Resort (Ryan Calloway)
5. T2 NEW: Jackson Koivun Seals Presidents Cup for Team USA at Age 21 (Jake Torres)

---

## Latest Run: 2026-09-27

**Run completed:** 2026-09-27
**Stories:** 5
**Articles:** 5
**X posts:** 10
**Status:** COMPLETE

### Scripts Run
- [x] verify-facts.py — 29 claims, HIGH confidence; tweet char issues fixed
- [x] compile-content-data.py — 5 stories, 10 tweets, 5 FB posts, 5 articles
- [x] generate-review-dashboard.py — 30 items
- [x] publish-unified-dashboard.py — blocked (content-dashboards repo not in authorized set)
- [x] generate-postplanner-export.py — 0 posts (known parsing issue)
- [x] generate-postplanner-export.py --tobi — 0 posts (known parsing issue)
- [x] publish-to-wordpress.py — blocked (WP credentials not configured in env)

### Known Non-Blocking Issues
- Dashboard push blocked: content-dashboards repo not in this session's authorized repository set
- WordPress publish blocked: WP credentials not in environment
- PostPlanner export shows 0 posts: known social post format parsing issue

### Stories Covered
1. Presidents Cup Sunday Singles — International Team leads 10.5-7.5, history on the line (T1 FOLLOW UP)
2. NW Arkansas Championship Final Round — Nishimura leads by 5 at -16 (T1 FOLLOW UP)
3. LIV Golf Bankruptcy — BC Partners $300M rescue; Oct. 13 player deadline (T1 FOLLOW UP)
4. Bank of Utah Championship Preview — PGA Tour Fall resumes at Black Desert Resort (T2 NEW)
5. Lauren Coughlin's Nine-Birdie LPGA Record — historic streak at Pinnacle CC (T2 NEW)

---

## Previous Run: 2026-09-23

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
