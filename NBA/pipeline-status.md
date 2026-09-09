# NBA Pipeline Status — Hoop Heroes

## Current Status
**Last Run:** 2026-09-09
**Steps Completed:** All pipeline steps (1-14); WordPress publish blocked by proxy policy

## Deploy Info
- **Repo:** fangearhq-boop/content-dashboards
- **Pages URL:** https://fangearhq-boop.github.io/content-dashboards/hh/
- **Build Type:** workflow
- **Note:** Dashboard publish push blocked (content-dashboards not in authorized repo set)

## Pipeline Run Log

### 2026-09-09 ✅ (Automated)
- Steps 1-9: Complete (research, daily brief, research notes, story analysis, X posts, FB posts, image concepts, 5 articles)
- Step 10: verify-facts.py run — 5 stories, claims verified
- Step 10b: compile-content-data.py — 5 stories, 7 tweets, 5 articles compiled (3 char limit fixes applied)
- Step 11: Image manifest created
- Step 12: Story history updated
- Step 13: generate-review-dashboard.py — dashboard generated
- Step 14a: publish-unified-dashboard.py — push blocked (proxy policy for content-dashboards)
- Step 14b: generate-postplanner-export.py — 0 posts exported (known parsing issue)
- Step 14c: generate-postplanner-export.py --tobi — 0 posts (known parsing issue)
- Step 15: publish-to-wordpress.py — BLOCKED (fanrumor.com not allowed by egress proxy)
- Git commit + push: ✅ Committed and pushed to main

**Stories covered:**
1. T1 NEW: Kawhi Leonard Joins Miami — Raptors Minicamp Trade, "I Hope So" Quote
2. T1 FOLLOW UP: 76ers 34 National TV Games — Franchise Record, LeBron Matchups Drive Schedule
3. T2 NEW: James Harden Signs 3-Year, $97M Deal with Cavaliers — Official
4. T2 NEW: NBA East Power Rankings — Celtics, 76ers, Knicks, Pacers, Cavs Top 5
5. T2 NEW: NBA West Preview — Blazers, Thunder, Nuggets, Lakers Training Camp

**Issues:**
- WordPress publish blocked by proxy policy (fanrumor.com not reachable from remote environment)
- content-dashboards push blocked (not in authorized repo set)
- PostPlanner export parsed 0 posts (known script parsing issue; posts are in 03/04 files)

### 2026-09-08 ✅ (Automated)
- Steps 1-9: Complete (research, daily brief, research notes, story analysis, X posts, FB posts, image concepts, 5 articles)
- Step 10: verify-facts.py run — 5 stories, 36 claims verified
- Step 10b: compile-content-data.py — 5 stories, 7 tweets, 5 articles compiled (no errors)
- Step 11: Image manifest created (not_started for all — imagn sourcing requires manual step)
- Step 12: Story history updated
- Step 13: generate-review-dashboard.py — 22 items in dashboard
- Step 14a: publish-unified-dashboard.py — push blocked (proxy policy for content-dashboards)
- Step 14b: generate-postplanner-export.py — 0 posts exported (known parsing issue)
- Step 14c: generate-postplanner-export.py --tobi — 0 posts (known parsing issue)
- Step 15: publish-to-wordpress.py — BLOCKED (fanrumor.com not allowed by egress proxy)
- Git commit + push: ✅ Committed and pushed to main

**Stories covered:**
1. T1 NEW: LeBron vs. Knicks on Ring Night — Opening Night Matchup Headlines 2026-27 Schedule
2. T1 FOLLOW UP: Kawhi Leonard Trade Still Pending — NBA Investigation Delays Toronto Move
3. T2 NEW: Blazers Bold Offseason — Lillard Returns from Achilles, Morant Trade Sets West Contender
4. T2 NEW: Preseason Goes Global — Cavs to Spain, Blazers vs. BC London Lions Historic First
5. T2 NEW: 76ers Depth Chart Set — Brown, LeBron, Maxey, Embiid Ready for Oct. 20

**Issues:**
- WordPress publish blocked by proxy policy (fanrumor.com not reachable from remote environment)
- content-dashboards push blocked (not in authorized repo set)
- PostPlanner export parsed 0 posts (known script parsing issue; posts are in 03/04 files)

### 2026-09-07 ✅ (Automated)
- Steps 1-9: Complete (research, daily brief, research notes, story analysis, X posts, FB posts, image concepts, 5 articles)
- Step 10: verify-facts.py run — 5 stories, 23 claims verified
- Step 10b: compile-content-data.py — 5 stories, 7 tweets, 5 articles compiled
- Step 11: Image manifest created (not_started for all — imagn sourcing requires manual step)
- Step 12: Story history updated
- Step 13: generate-review-dashboard.py — 22 items in dashboard
- Step 14a: publish-unified-dashboard.py — push blocked (proxy policy for content-dashboards)
- Step 14b: generate-postplanner-export.py — 7 posts exported
- Step 14c: generate-postplanner-export.py --tobi — 7 TOBI posts exported
- Step 15: publish-to-wordpress.py — BLOCKED (fanrumor.com not allowed by egress proxy)
- Git commit + push: ✅ Committed
