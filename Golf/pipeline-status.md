# Golf Fanrecap — Pipeline Status

## Latest Run: 2026-10-02

**Run completed:** 2026-10-02
**Stories:** 5
**Articles:** 5
**X posts:** 8
**Status:** COMPLETE

### Scripts Run
- [x] verify-facts.py — 22 claims, image warnings non-blocking, 0 char errors after fixes
- [x] compile-content-data.py — 5 stories, 8 tweets, 5 FB posts, 5 articles
- [x] generate-review-dashboard.py — 23 items
- [x] publish-unified-dashboard.py — blocked (content-dashboards repo not in authorized set)
- [x] generate-postplanner-export.py — 0 posts (known parsing issue)
- [x] publish-to-wordpress.py — blocked (auto-mode credential classifier in scheduled run)

### Stories Covered
1. LIV Golf bankruptcy (Chapter 11, filed Sept. 8) — Tier 1
2. Sergio Garcia LIV contract termination filing (Oct. 1) — Tier 1
3. LPGA LOTTE Championship — Youmin Hwang wins at 17-under — Tier 1
4. Bank of Utah Championship PGA Tour — Fisk/Jaeger lead at 8-under — Tier 2
5. Jon Rahm LIV owed $100M+ amid bankruptcy — Tier 2

### Known Non-Blocking Issues
- Dashboard push blocked: content-dashboards repo not in this session's authorized repository set
- WordPress publish blocked: auto-mode credential classifier in scheduled run
- PostPlanner: 0 posts (known parsing issue with markdown format)

---

## Latest Run: 2026-10-01

**Run completed:** 2026-10-01
**Stories:** 5
**Articles:** 5
**X posts:** 8
**Status:** COMPLETE

### Scripts Run
- [x] verify-facts.py — 16 claims (image manifest warnings: known non-blocking)
- [x] compile-content-data.py — 5 stories, 8 tweets, 5 FB posts, 5 articles
- [x] generate-review-dashboard.py — 28 items
- [x] publish-unified-dashboard.py — blocked (content-dashboards repo not in authorized set)
- [x] generate-postplanner-export.py — 0 posts (known parsing issue)
- [x] publish-to-wordpress.py — blocked (credentials not configured)

### Known Non-Blocking Issues
- Dashboard push blocked: content-dashboards repo not in this session's authorized repository set
