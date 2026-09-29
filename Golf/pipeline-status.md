# Golf Fanrecap — Pipeline Status

## Latest Run: 2026-09-29

**Run completed:** 2026-09-29
**Stories:** 5
**Articles:** 5
**X posts:** 7
**Status:** COMPLETE

### Scripts Run
- [x] verify-facts.py -- 19 claims, HIGH confidence; image warnings expected (imagn sourcing)
- [x] compile-content-data.py -- 5 stories, 7 tweets, 5 articles; posting window warnings (non-blocking); FB=0 known
- [x] generate-review-dashboard.py -- 22 items
- [x] publish-unified-dashboard.py -- blocked (content-dashboards repo not in authorized set)
- [x] generate-postplanner-export.py -- 0 posts (known parsing issue)
- [x] generate-postplanner-export.py --tobi -- 0 posts (known parsing issue)
- [x] publish-to-wordpress.py -- blocked (WP credentials not configured)
- [x] git commit + push -- via GitHub MCP (mcp__github__push_files)

### Known Non-Blocking Issues
- Dashboard push blocked: content-dashboards repo not in this session's authorized repository set
- WordPress publish blocked: credentials not configured in session
- PostPlanner export shows 0 posts: known social post format parsing issue

### Stories Covered
1. T1 FOLLOW UP: Presidents Cup Aftermath: USA Won, But Left More Questions Than Answers (Ryan Calloway)
2. T1 FOLLOW UP: Bank of Utah Championship Preview — Black Desert's $6M FedExCup Fall Stop Opens Thursday (Jake Torres)
3. T1 FOLLOW UP: LIV Golf's October 13 Deadline Is 14 Days Away — Players Own 52.5% If They Sign (Marcus Cole)
4. T2 FOLLOW UP: Scheffler Won the FedEx Cup. Now He Plays October Golf — and He's Still World No. 1. (Ryan Calloway)
5. T2 NEW: 2027 Ryder Cup Preview — Furyk Leads USA to Adare Manor, Donald Returns for Europe (Jake Torres)

---

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
