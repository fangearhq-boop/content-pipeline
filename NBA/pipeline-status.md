# NBA Pipeline Status — Hoop Heroes

## Current Status
**Last Run:** 2026-09-03
**Steps Completed:** All pipeline steps (1-14); WordPress publish blocked by proxy policy

## Deploy Info
- **Repo:** fangearhq-boop/content-dashboards
- **Pages URL:** https://fangearhq-boop.github.io/content-dashboards/hh/
- **Build Type:** workflow
- **Note:** Dashboard publish push blocked (content-dashboards not in authorized repo set)

## Pipeline Run Log

### 2026-09-03 ✅ (Automated)
- Steps 1-9: Complete (research, daily brief, research notes, story analysis, X posts, FB posts, image concepts, 5 articles)
- Step 10: verify-facts.py run — 5 stories, 37 claims, no char limit violations
- Step 10b: compile-content-data.py — 5 stories, 7 tweets, 5 articles compiled
- Step 11: Image manifest created (not_started for all — imagn sourcing requires manual step)
- Step 12: Story history updated
- Step 13: generate-review-dashboard.py — 27 items in dashboard
- Step 14a: publish-unified-dashboard.py — push blocked (proxy policy for content-dashboards)
- Step 14b: generate-postplanner-export.py — 7 posts exported
- Step 14c: generate-postplanner-export.py --tobi — 7 TOBI posts exported
- Step 15: publish-to-wordpress.py — BLOCKED (fanrumor.com not allowed by egress proxy)
- Git commit + push: ✅ Complete (content-pipeline repo)

**Stories covered:**
1. T1 NEW: NBA Hammers Clippers — 5 Picks, $30M Fine, Ballmer Suspended
2. T1 FOLLOW UP: Kawhi Leonard Trade to Toronto Cleared
3. T2 FOLLOW UP: Wemby/France FIBA Window Sweep; Turkey Qualifies
4. T2 NEW: 2026-27 NBA Power Rankings — Contenders Edition
5. T2 FOLLOW UP: Blazers Backcourt Reset — Morant + Lillard After Sharpe Injury

**Issues:**
- WordPress publish blocked by proxy policy (fanrumor.com not reachable from remote environment)
- content-dashboards push blocked (not in authorized repo set)
- FB posts compiled as 0 — script may need Facebook post in code-fence format to count correctly

### 2026-09-02 ✅
- Steps 1-15 complete
- 5 stories covered
- WordPress draft publish succeeded

### 2026-09-01 ✅
- Steps 1-15 complete

