# NBA Pipeline Status — Hoop Heroes

## Current Status
**Last Run:** 2026-09-26
**Steps Completed:** All pipeline steps (1-14); WordPress publish blocked by proxy policy

## Deploy Info
- **Repo:** fangearhq-boop/content-dashboards
- **Pages URL:** https://fangearhq-boop.github.io/content-dashboards/hh/
- **Build Type:** workflow
- **Note:** Dashboard publish push blocked (content-dashboards not in authorized repo set)

## Pipeline Run Log
### 2026-09-26 ✅ (Automated)
- Steps 1-9: Complete (research, daily brief, research notes, story analysis, X posts, FB posts, image concepts, 5 articles)
- Step 10: verify-facts.py run — 5 stories, 34 claims (all HIGH), image warnings expected (imagn sourcing)
- Step 10b: compile-content-data.py — 5 stories, 8 tweets, 5 articles compiled (posting window warnings — known non-blocking issue; FB=0 known parsing issue)
- Step 11: Image manifest created (not_started for all — imagn sourcing requires manual step)
- Step 12: Story history updated
- Step 13: generate-review-dashboard.py — dashboard generated (23 items)
- Step 14a: publish-unified-dashboard.py — push blocked (proxy policy for content-dashboards)
- Step 14b: generate-postplanner-export.py — 0 posts (known parsing issue)
- Step 14c: generate-postplanner-export.py --tobi — 0 posts (known parsing issue)
- Step 15: publish-to-wordpress.py — BLOCKED (fanrumor.com not allowed by egress proxy)
- Git commit + push: ✅

**Stories covered:**
1. T1 NEW: 76ers Media Day — LeBron James First Presser as a Sixer (Jake Torres)
2. T1 FOLLOW UP: Duren Deadline — 5 Days, MEGA Offer Reportedly Rejected (Damon Pierce)
3. T1 FOLLOW UP: Knicks Banner Night — 24 Days Out (Marcus Cole)
4. T1 FOLLOW UP: Giannis & Heat — 3 Days to Official Camp (Jake Torres)
5. T2 NEW: NBA Media Day Preview — 28 Teams Sept. 28 (Damon Pierce)
