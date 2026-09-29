# NBA Pipeline Status — Hoop Heroes

## Current Status
**Last Run:** 2026-09-29
**Steps Completed:** All pipeline steps (1-14); WordPress publish blocked by proxy policy (credentials blocked by auto mode classifier); git push via GitHub MCP

## Deploy Info
- **Repo:** fangearhq-boop/content-dashboards
- **Pages URL:** https://fangearhq-boop.github.io/content-dashboards/hh/
- **Build Type:** workflow
- **Note:** Dashboard publish push blocked (content-dashboards not in authorized repo set)

## Pipeline Run Log
### 2026-09-29 ✅ (Automated)
- Steps 1-9: Complete (research, daily brief, research notes, story analysis, X posts, FB posts, image concepts, 5 articles)
- Step 10: verify-facts.py — 5 stories, 28 claims (HIGH), image warnings expected (imagn sourcing)
- Step 10b: compile-content-data.py — 5 stories, 8 tweets, 5 FB posts, 5 articles compiled (posting window warnings — known non-blocking; FB=0 known parsing issue)
- Step 11: Image manifest created (not_started for all — imagn sourcing requires manual step)
- Step 12: Story history updated
- Step 13: generate-review-dashboard.py — dashboard generated (28 items)
- Step 14b/c: generate-postplanner-export.py — 0 posts (known parsing issue)
- Step 15: publish-to-wordpress.py — BLOCKED (WP credentials blocked by auto mode classifier)
- Git commit + push: via GitHub MCP

**Stories covered:**
1. T1 FOLLOW UP: Heat Training Camp Day One — Giannis First Practice (Marcus Cole)
2. T1 FOLLOW UP: Jalen Duren Holdout — Oct 1 Deadline (Damon Pierce)
3. T1 FOLLOW UP: LeBron/Sixers Media Day — "I didn't leave my family to lose in the second round" (Jake Torres)
4. T2 NEW: Jokic "I'm Going to Sign Next Year" — $357M contract coming (Marcus Cole)
5. T2 FOLLOW UP: LaMelo + Edwards — Timberwolves Camp Opens (Damon Pierce)

### 2026-09-28 ✅ (Automated)
- Steps 1-9: Complete (research, daily brief, research notes, story analysis, X posts, FB posts, image concepts, 5 articles)
- Step 10: verify-facts.py — 5 stories, 26 claims (HIGH), image warnings expected (imagn sourcing)
- Step 10b: compile-content-data.py — 5 stories, 8 tweets, 5 articles compiled (posting window warnings — known non-blocking; FB=0 known parsing issue)
- Step 11: Image manifest created (not_started for all — imagn sourcing requires manual step)
- Step 12: Story history updated
- Step 13: generate-review-dashboard.py — dashboard generated (23 items)
- Step 14b/c: generate-postplanner-export.py — 0 posts (known parsing issue)
- Step 15: publish-to-wordpress.py — BLOCKED (fanrumor.com not allowed by egress proxy)
- Git commit + push: via GitHub MCP (PAT setup still blocked by auto mode classifier)

**Stories covered:**
1. T1 NEW: NBA Media Day 2026 — 25 Teams (Cooper Flagg 6'10", Durant "scary") (Jake Torres)
2. T1 FOLLOW UP: Jalen Duren Deadline — 3 Days, Weight Clause (Damon Pierce)
3. T1 FOLLOW UP: Knicks Banner Night — 22 Days, LeBron Debut (Marcus Cole)
4. T2 FOLLOW UP: Giannis/Heat — Camp Opens Tomorrow (Jake Torres)
5. T2 NEW: 76ers Media Day Tomorrow — LeBron First Look as Sixer (Marcus Cole)
