# Cubs Pipeline Status

## Last Run
- **Date**: 2026-05-25 (full pipeline run)
- **Steps Completed**: Step 0 (insights loaded from Cubs/_data/insights.json, 9 significant findings, generated_at 2026-05-25T08:30 UTC), Step 0.5 (series context loaded, is_series_start_today=true, Cubs 29-24 at Pirates 27-26, PNC Park, 4-game road series, Game 1 12:35 PM CT), Research (web searches across game recap + series preview + rotation news + standings + prospects + Iowa), daily brief (7 stories), research notes, story analysis (insights applied section + series context conflict flagged), X posts (7 tweets, all insights-tuned), fact-check log (all key claims verified, 4 MEDIUM single-source flags, 3 superlative claims NOT used in tweets), compile-content-data.py (all clear, 0 errors, 0 warnings), generate-review-dashboard.py (✓), publish-unified-dashboard.py (generated locally; push to content-dashboards repo FAILED 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-25/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — content-dashboards separate repo not in PAT scope)
- **Issues**: (1) publish-unified-dashboard.py push rejected 403 (recurring — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed. (2) Daily brief initially written as markdown table — script requires ### STORY N: headers. Rewrote before compile. (3) X posts initially used prose metadata instead of **Post NA** + [POSTING WINDOW: ...] format. Rewrote before compile. (4) Initial tweet drafts 285–414 chars — trimmed to 271–279 chars before compile. (5) is_series_start_today=true posting-order conflict: prompt reserves 7 AM for series preview, engine docs give game recaps priority — engine docs win, flagged in 02-story-analysis.md. (6) Alcantara callup status LOW confidence — treated as Iowa prospect only, no callup claim made.
- **Insights applied**: Loaded from local snapshot (generated_at: 2026-05-25T08:30 UTC). 9 significant findings applied (up from 6 in prior runs — tweet_count grew to 89): (1) rss_news loser → all posts editorial takes, not wire copy ✓; (2) overnight_00_06 loser → no overnight slots, all 7:00 AM–3:45 PM CT ✓; (3) len_bucket=140-200 loser → all 7 tweets 241–279 chars, none in 140-200 range ✓; (4) has_emoji_first_line loser=True → NO leading emojis ✓; (5) content_type=brief winner → all posts brief ✓; (6) len_bucket=260+ winner → 6 of 7 tweets in 260+ bucket, 1 in neutral 200-260 zone ✓; (7) has_score winner → "8-5" score explicit in Story 1 recap ✓; (8) opening=allcaps_lead loser → zero ALL CAPS openings ✓; (9) has_stat winner → stats in every tweet ✓.
- **Key stories**: Astros 8 Cubs 5 eight straight losses Ramirez first MLB hit Imanaga 3rd loss 29-24 (T1), 4-game road series at Pirates PNC Park Ben Brown 2.09 ERA (T1), 15-over to 5-over in 17 days historic collapse bold take (T2), Wicks recalled Cabrera IL right-finger blister 4-of-6 starters unavailable (T2), NL Central Cubs 3rd Brewers 30-20 Cardinals 29-22 (T2), Ben Brown 2.09 ERA 0.98 WHIP 40 K quiet excellence (T3), Kevin Alcantara 15 HR 41 Iowa games 7-game streak (T3)

## Previous Run
- **Date**: 2026-05-24 (full pipeline run)
- **Steps Completed**: Step 0 (insights loaded from Cubs/_data/insights.json, 6 significant findings, generated_at 2026-05-24T08:30 UTC), Step 0.5 (series context loaded, is_series_start_today=false, mid-series Game 3 vs Astros, Cubs 29-23 host Astros 22-31, 1:20 PM CT), Research (10 searches across 6+ categories), daily brief (6 stories), research notes, story analysis (insights applied section completed), X posts (6 tweets, all insights-tuned), fact-check log (19 claims checked, 18 verified, 1 single-source flag on Taillon HR leaderboard), compile-content-data.py (all clear, 0 errors, 0 warnings), generate-review-dashboard.py (✓), publish-unified-dashboard.py (generated locally; push to content-dashboards repo FAILED 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-24/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — content-dashboards separate repo not in PAT scope)
- **Issues**: (1) publish-unified-dashboard.py push rejected 403 (recurring — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot. (2) Cardinals record inconsistent across sources (28-19 to 28-21) — claim omitted from tweet; only stated Brewers lead. (3) Taillon HR leaderboard: single-source (pipeline carry-forward from May 23) — flagged ⚠ in fact-check log. (4) No requirements.txt at repo root — pip install skipped (no deps needed for text-only pipeline).
- **Insights applied**: Loaded from local snapshot (generated_at: 2026-05-24T08:30 UTC). 6 significant findings applied: (1) rss_news loser → all posts original authored takes ✓; (2) overnight_00_06 loser → no overnight slots, all 7:00 AM–3:45 PM CT ✓; (3) len_bucket=140-200 loser → all 6 tweets 232-275 chars, none in 140-200 range ✓; (4) has_emoji_first_line loser=True → NO leading emojis on any tweet (overrides brand-voice.md) ✓; (5) content_type=brief winner → all posts brief ✓; (6) has_score=True winner → "Astros 3, Cubs 0" in first line of Story 1 recap ✓.
- **Key stories**: Astros 3-0 Walker 2 HR 7-game losing streak first since 2022 (T1), 21-4 to 2-11 collapse bold take RISP .131 4 shutouts (T2), Pedro Ramirez No. 2 prospect MLB debut .312/.395/.547 Iowa (T2), NL Central Brewers 30-19 leading Cubs 2.5-game lead gone (T2), series finale preview Imanaga vs Lambert 1:20 PM CT (T2), Jordan Wicks 0.60 ERA Iowa rotation callup case (T3)

## Previous Run
- **Date**: 2026-05-23 (full pipeline run)
- **Steps Completed**: Step 0 (insights loaded from Cubs/_data/insights.json, 6 significant findings, generated_at 2026-05-23T08:30 UTC), Step 0.5 (series context loaded, is_series_start_today=false, mid-series Game 2 vs Astros, Cubs 29-22 host Astros 21-31, 1:20 PM CT), Research (14 searches across 8+ categories), daily brief (7 stories), research notes, story analysis, X posts (7 tweets), fact-check log (all Priority 1 claims verified, 7 PLAUSIBLE flags in supporting stats), compile-content-data.py (all clear, 0 errors, 0 warnings), generate-review-dashboard.py (✓), publish-unified-dashboard.py (generated locally; push to content-dashboards repo FAILED 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-23/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — content-dashboards separate repo not in PAT scope)
- **Issues**: (1) publish-unified-dashboard.py push rejected 403 (recurring — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot. (2) No requirements.txt found at repo root — pip install skipped (no dependencies needed for text-only pipeline). (3) Taillon HR count: CBS Sports May 22 recap says "17th homer" while older Taillon article says "20" (White Sox game). Used "leads the majors" without number in tweet to avoid error — flagged ⚠ PLAUSIBLE in fact-check. (4) RISP/stranded runner counts are through ~May 20 (Yardbarker source); flagged ⚠ PLAUSIBLE (directionally accurate, numbers certainly higher today).
- **Insights applied**: Loaded from local snapshot (generated_at: 2026-05-23T08:30 UTC). 6 significant findings applied: (1) rss_news loser → all posts framed as original analysis/takes, not wire-style summaries ✓; (2) overnight_00_06 loser → no overnight slots, all 7:00 AM–2:30 PM CT ✓; (3) len_bucket=140-200 loser → all 7 tweets 223-266 chars, none in 140-200 range ✓; (4) has_emoji_first_line loser=True → NO leading emojis on any tweet (overrides brand-voice guide) ✓; (5) content_type=brief winner → all posts brief ✓; (6) has_score=True winner → score in first line of Story 1 recap ("Astros 4, Cubs 2"); records (29-22, 21-31) in Story 5 preview ✓.
- **Key stories**: Astros 4-2 recap six-game losing streak (T1), RISP/offense bold take 642 baserunners MLB-worst stranded (T2), Pedro Ramirez MLB debut No. 2 prospect .312/.395/.547 (T1), Taillon leads majors HRs allowed 4.97 ERA (T2), game preview Rea vs Teng 1:20 PM CT (T2), NL Central division lead evaporated 2-10 skid (T2), Cade Horton 2nd Tommy John out mid-2027 (T3)

## Previous Run
- **Date**: 2026-05-22 (full pipeline run)
- **Steps Completed**: Step 0 (insights loaded from Cubs/_data/insights.json, 6 significant findings, generated_at 2026-05-22T08:30 UTC), Step 0.5 (series context loaded, is_series_start_today=true, Cubs 29-21 host Astros 20-31, 3-game series, 1:20 PM CT Game 1), Research (14 searches across 8+ categories), daily brief (6 stories), research notes, story analysis, X posts (6 tweets), fact-check log (all Priority 1 claims verified, 5 MEDIUM flags in supporting stats), compile-content-data.py (all clear, 0 warnings), generate-review-dashboard.py, publish-unified-dashboard.py (generated locally; push to content-dashboards repo FAILED 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-22/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — content-dashboards separate repo not in PAT scope)
- **Issues**: (1) publish-unified-dashboard.py push rejected 403 (same recurring issue — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot. (2) 4 tweets initially over 280 chars — fixed before final compile (all under 280, all outside 140-200 bucket). (3) Alcántara walk-off attribution MEDIUM confidence (Bleacher Nation headline; CubsHQ "Poteet game-winner" likely refers to South Bend, not Iowa — flagged in fact-check log). (4) Taillon ERA slight discrepancy between sources (4.94 vs 4.97) — used 4.97 from stats source. (5) "Nine Astros on IL" count — confirmed by cross-referencing named players (Correa, Peña, Diaz, Meyers, Loperfido, Brown, Imai, Javier, Hader = 9).
- **Insights applied**: Loaded from local snapshot (generated_at: 2026-05-22T08:30 UTC). 6 significant findings applied: (1) rss_news loser → original analysis/takes throughout, no RSS-style headline dumps ✓; (2) len_bucket=140-200 loser → all 6 tweets 240-270 chars, none in 140-200 range ✓; (3) overnight_00_06 loser → no overnight slots, all 7:00 AM–3:45 PM CT ✓; (4) has_emoji_first_line loser=True → NO leading emojis on any tweet ✓; (5) content_type=brief winner → all posts brief ✓; (6) has_score=True winner → records (29-21, 20-31, 29-18) and pitcher records (5-1, 2-3) explicit in tweets 1, 2, and 5 ✓.
- **Key stories**: Series preview Cubs vs Astros 3-game Wrigley Game 1 1:20 PM CT (P10), bold take Astros 20-31 depleted perfect bounce-back opp (P9), Cabrera TBD blister 4 starters out Peralta June 1 10 days (P9), Boyd ahead of schedule mound session Sat late June return (P8), game preview Taillon vs Arrighetti 1:20 PM CT (P8), Iowa snapped 8-game skid Alcántara walk-off Ayers HR Tennessee (P6)

## Previous Run
- **Date**: 2026-05-21 (full pipeline run)
- **Steps Completed**: Step 0 (insights loaded from Cubs/_data/insights.json, 6 significant findings, generated_at 2026-05-21T08:30 UTC), Step 0.5 (series context loaded, off_day=true confirmed), Research (14 searches, 7 categories), daily brief (6 stories), research notes, story analysis, X posts (6 tweets), fact-check log (24 claims checked, 17 HIGH, 7 MEDIUM, 0 LOW, 0 corrections), compile-content-data.py (all clear, 0 warnings), generate-review-dashboard.py, publish-unified-dashboard.py (generated locally; push to content-dashboards repo FAILED 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-21/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — content-dashboards separate repo not in PAT scope)
- **Issues**: (1) publish-unified-dashboard.py push rejected 403 (same recurring issue — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot. (2) Boyd recovery details (Counsell quote, mound session Saturday) single-source MEDIUM; hedge language used in tweet. (3) Noland ankle injury single-source; "status unknown" qualifier used.
- **Insights applied**: Loaded from local snapshot (generated_at: 2026-05-21T08:30 UTC). 6 significant findings applied: (1) rss_news loser → all posts brief type ✓; (2) len_bucket=140-200 loser → all tweets outside 140-200 range (244/248/255/211/259/253) ✓; (3) overnight_00_06 loser → no overnight slots ✓; (4) has_emoji_first_line loser=True → NO leading emojis on any tweet ✓; (5) content_type=brief winner → all posts brief ✓; (6) has_score=True winner → "Brewers 5, Cubs 0" in first line of Story 1 recap ✓.
- **Key stories**: Brewers 5-0 Harrison 11K sweep at Wrigley Cubs 29-21 (P10), division take Brewers 29-18 1.5 GB new leader (P9), Cabrera blister four starters unavailable at once (P9), Boyd ahead of schedule mound session Saturday (P8), Peralta clock 11 days June 1 (P8), Iowa 8-game skid Noland ankle scare Kepley HR (P6)

## Previous Run
- **Date**: 2026-05-20 (full pipeline run)
- **Steps Completed**: Step 0 (insights loaded from Cubs/_data/insights.json, 6 significant findings), Step 0.5 (series context loaded, mid-series Game 3), Research (11 searches, 7 categories), daily brief (6 stories), research notes, story analysis, X posts (6 tweets), fact-check log (18 claims verified, 1 single-source flag), compile-content-data.py (all clear, 0 warnings), generate-review-dashboard.py, publish-unified-dashboard.py (generated locally; push to content-dashboards repo FAILED 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-20/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — content-dashboards separate repo not in PAT scope)
- **Issues**: (1) publish-unified-dashboard.py push rejected 403 (same recurring issue — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot. (2) Cabrera W-L record had conflicting sources (3-1 from preview sources vs projected 8-7 from AI summary) — W-L omitted from tweet text. (3) Harrison Red Sox origin claim: single source, not used in tweets.
- **Insights applied**: Loaded from local snapshot (generated_at: 2026-05-20T08:30 UTC). 6 significant findings applied: (1) rss_news loser → all posts brief type ✓; (2) len_bucket=140-200 loser → all tweets 200-267 chars, none in 140-200 ✓; (3) overnight_00_06 loser → no overnight slots ✓; (4) has_emoji_first_line loser=True → NO leading emojis on any tweet (overrides brand-voice guide) ✓; (5) content_type=brief winner → all posts brief ✓; (6) has_score=True winner → score in first line of game recap tweet ✓.
- **Key stories**: Brewers 5-2 Misiorowski 24.1 scoreless innings Brown L (P10), Cubs slide 4 straight 8-of-10 dropped from first (P9), Boyd meniscus surgery 6 weeks second IL stint (P8), Game 3 Cabrera vs Harrison sweep on the line 6:40 CT (P9), Peralta trade clock 12 days to June 1 Counsell connection (P8), game-time hype (P5)

## Previous Run
- **Date**: 2026-05-19 (full pipeline run)
- **Steps Completed**: Research (12 searches, 6 categories), daily brief (6 stories), research notes, story analysis, X posts (6 tweets), fact-check log (29 claims, 0 errors, 4 MEDIUM/plausible), compile-content-data.py (all clear, 0 warnings), generate-review-dashboard.py, publish-unified-dashboard.py (dashboard generated locally; push to content-dashboards repo failed 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-19/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — content-dashboards separate repo not in PAT scope)
- **Issues**: (1) Both series-context API and insights API returned 403 again (8th consecutive run). off_day=true fallback INCORRECT. Web research confirms Cubs in Game 2 of Brewers series at Wrigley tonight. (2) Insights tweet_count=0 — brand-voice.md defaults applied. (3) publish-unified-dashboard.py push rejected 403 (same recurring issue). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot.
- **Insights applied**: API unavailable (403/tweet_count=0). Fell through to brand-voice.md defaults. 50/50 informative/bold split applied (Stories 1/3/5 informative; Stories 2/4/6 bold/analytical/hype). No format adjustments possible without data.
- **Key stories**: Brewers 9-3 Imanaga 8-ER disaster (P10), NL Central alarm 7-of-9 losses Brewers 0.5 GB Cardinals 1.0 GB (P9), Brown vs Misiorowski Game 2 6:40 PM CT (P9), Peralta June 1 13 days Counsell connection (P8), Boyd bullpen session late June return (P7), game-time hype (P5)

## Previous Run
- **Date**: 2026-05-18 (full pipeline run)
- **Steps Completed**: Research (11 searches, 6 categories), daily brief (6 stories), research notes, story analysis, X posts (6 tweets), fact-check log (27 claims, 0 errors), compile-content-data.py (all clear, 0 warnings), generate-review-dashboard.py, publish-unified-dashboard.py (dashboard generated locally; push to content-dashboards repo failed 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-18/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected — recurring, content-dashboards separate repo not in PAT scope)
- **Issues**: (1) Both series-context API and insights API returned 403 again — off_day=true fallback INCORRECT. Web research confirms Cubs open 3-game home series vs Brewers tonight (May 18, 6:40 PM CT). Conflict: engine docs (research-playbook.md) give game recaps priority over series-preview in the 7 AM slot; Crosstown recap at 7 AM, series preview at 8:15 AM. (2) Insights tweet_count=0 — brand-voice.md defaults applied. (3) publish-unified-dashboard.py push rejected 403 (same recurring issue). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot.
- **Insights applied**: API unavailable (403/tweet_count=0). Fell through to brand-voice.md defaults. 50/50 informative/bold split applied (Stories 1/3 informative; Stories 2/4/5 bold/analytical; Story 6 hype). No format adjustments possible without data.
- **Key stories**: White Sox 9-8 walkoff recap (Quero 10th-inning HR, Conforto 3-run 9th), Brewers series preview (Imanaga vs Sproat 6:40 PM CT), bullpen moves (Blach up/Assad down/Harvey 60-day), Ben Brown vs Misiorowski (Game 2 Tue), Peralta June 1 clock (14 days), game-time hype.

## Previous Run
- **Date**: 2026-05-17 (full pipeline run)
- **Steps Completed**: Research (17 searches, 7 categories), daily brief (6 stories), research notes, story analysis, X posts (6 tweets), fact-check log (29 claims, 0 errors), compile-content-data.py (all clear), generate-review-dashboard.py, publish-unified-dashboard.py (dashboard generated locally; push to content-dashboards repo failed 403 — recurring issue)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-17/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected)
- **Issues**: (1) Both series-context API and insights API returned 403 again — fallback logic applied. off_day=true fallback was incorrect (Cubs playing Game 3 Crosstown Classic today 1:10 PM CT); corrected via web research. (2) Insights tweet_count=0 — brand-voice.md defaults applied. (3) publish-unified-dashboard.py push rejected 403 (same recurring issue). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot.
- **Insights applied**: API unavailable (403/tweet_count=0). Fell through to brand-voice.md defaults. 50/50 informative/bold split applied (Stories 1/3/5 informative; Stories 2/4/6 bold/analytical). No format adjustments possible without data.
- **Key stories**: Taillon 5-HR Game 2 loss (recap + bold take), Boyd mound session update, NL Central rival watch, Game 3 preview (Rea vs Fedde, 1:10 PM CT), Peralta trade deadline clock (Mets June 1 decision).

## Previous Run (Two Runs Ago)
- **Date**: 2026-05-16 (full pipeline run)
- **Steps Completed**: Research (10 searches, 6 categories), daily brief (6 stories), research notes, story analysis, X posts (6 tweets), fact-check log, compile-content-data.py, generate-review-dashboard.py, publish-unified-dashboard.py (dashboard generated locally; push to content-dashboards repo failed 403 — separate repo not in PAT scope)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-16/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected)
- **Issues**: (1) Series-context API returned 403 → fallback `off_day: true` was incorrect; web research confirmed Game 2 of Crosstown Classic today at 6:10 PM CT. (2) Insights API returned 403 → tweet_count=0 fallback; brand-voice.md defaults applied. (3) publish-unified-dashboard.py push rejected 403 (same recurring issue — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot.
- **Insights applied**: API unavailable (403/tweet_count=0). Fell through to brand-voice.md defaults. No format adjustments. 50/50 informative/bold split applied (3/3).

## Previous Run
- **Date**: 2026-05-15 (full pipeline run)
- **Steps Completed**: Research (12 searches, 7 categories), daily brief (7 stories), research notes, story analysis, X posts (7 tweets), fact-check log, compile-content-data.py, generate-review-dashboard.py, publish-unified-dashboard.py (dashboard generated locally; push to content-dashboards repo failed 403 — separate repo not in PAT scope)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-15/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected)
- **Issues**: publish-unified-dashboard.py push rejected 403 (same recurring issue — content-dashboards not in PAT scope). Core deliverable (07-content-data.json) compiled and pushed to content-pipeline repo for cubs-x-bot.

## Previous Run
- **Date**: 2026-05-14 (full pipeline run)
- **Steps Completed**: Research (15 searches, 8 categories), daily brief (7 stories), research notes, story analysis, X posts (7 tweets), fact-check log, compile-content-data.py, generate-review-dashboard.py, publish-unified-dashboard.py (dashboard generated locally; push to content-dashboards repo failed 403 — separate repo not in PAT scope)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-14/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected)
- **Issues**: publish-unified-dashboard.py push rejected 403 (content-dashboards is a separate repo). Core deliverable (07-content-data.json) is committed to content-pipeline repo and ready for cubs-x-bot.

## Two Runs Ago
- **Date**: 2026-05-13 (full pipeline run)
- **Steps Completed**: Research (15 searches), daily brief (8 stories), research notes, story analysis, X posts (8 tweets), fact-check log, compile-content-data.py, generate-review-dashboard.py, publish-unified-dashboard.py (dashboard generated locally; push to content-dashboards repo failed 403 — separate repo not in PAT scope)
- **Dashboard Published**: Locally generated (Cubs/cubs-content-2026-05-13/review-dashboard.html). Remote publish failed — content-dashboards repo not accessible via current PAT.
- **GitHub Pages Status**: N/A for this run (push rejected)
- **Issues**: publish-unified-dashboard.py push rejected 403 (content-dashboards is a separate repo). Core deliverable (07-content-data.json) is committed to content-pipeline repo and ready for cubs-x-bot.

## Previous Full Run
- **Date**: 2026-03-30
- **Steps Completed**: Full pipeline (Steps 1-15) — research (10+ searches), brief, analysis, X posts (7), fact-check, compile, dashboard, publish, PostPlanner export (X only, no TOBI — Cubs is X-only niche)
- **Dashboard Published**: Yes — https://fangearhq-boop.github.io/cubs-dashboards/
- **GitHub Pages Status**: built (workflow deployment)
- **Issues**: publish-dashboard.py push rejected non-fast-forward; fixed with git pull --rebase + manual push.

## Pipeline Gap (2026-03-31 → 2026-04-16)

No full pipeline runs executed during this window. During the gap, a new
auto-posting architecture went live:

- **cubs-x-bot** (Railway `Cubs X Bot`) — cron every 15 min, ingests brief
  JSON from GitHub raw + falls back to RSS
- **game-monitor** (Railway `lucid-essence`) — polls MLB StatsAPI, posts
  Cubs home runs, lead-changes, game previews, and finals

See `AUTOMATION.md` for the current architecture. The xlsx PostPlanner
workflow is deprecated — no manual upload needed anymore.

Three hand-curated briefs were pushed directly to cover the gap and smoke-test
the new brief-ingestion path. Each bypassed the full 15-step pipeline (no
daily brief, research notes, story analysis, fact-check log, or dashboard):

- **2026-04-15** (commit `5f22756`) — 7 posts, all slots past grace by push time, used only as a historical record
- **2026-04-16** (commit `67d3e25`) — 7 posts for an off-day; story 4 onward were real candidates to fire but the daily cap from RSS backlog blocked them
- **2026-04-17** (commit `92746f9`) — 7 posts for the home opener vs Mets; first brief scheduled to fire the full 7-slot day from 7:00 AM CT

**Next full pipeline run** should resume normal operation. Story-history
is intentionally NOT updated for these recovery briefs — the next real run
should treat the covered stories as already-known context, but doesn't need
to mark them as pipeline-produced.

## Previous Run
- **Date**: 2026-03-29
- **Steps Completed**: Full pipeline (Steps 1-15) — research, brief, analysis, X posts, fact-check, compile, dashboard, publish, PostPlanner export (X only, no TOBI — Cubs is X-only niche)
- **Dashboard Published**: Yes — https://fangearhq-boop.github.io/cubs-dashboards/
- **GitHub Pages Status**: built (workflow deployment)
- **Issues**: None

## Deploy Info
- **Repo**: `fangearhq-boop/cubs-dashboards`
- **Build Type**: workflow (GitHub Actions)
- **Has .nojekyll**: Yes
- **Has deploy workflow**: Yes (`.github/workflows/deploy-pages.yml`)
- **Pages URL**: https://fangearhq-boop.github.io/cubs-dashboards/

## Recent Issues & Fixes
| Date | Issue | Fix | Status |
|------|-------|-----|--------|
| 2026-03-05 | Pages legacy builds erroring | Switched to workflow build type + added deploy-pages.yml | Resolved |
| 2026-03-05 | TOBI export button broken | Moved parsePostingTime to outer scope in dashboard template | Resolved |

## Pipeline Run Log
<!-- Append newest at top -->

### 2026-05-25
- Stories: 7 (Tier 1: astros-recap, pirates-series-preview; Tier 2: historic-collapse-take, wicks-recalled, nl-central-standings; Tier 3: ben-brown-stat-breakdown, alcantara-prospect) — X-only niche, SERIES OPENER
- X posts: 7 (4 informative / 3 bold = ~57/43 mix)
- Char counts: 279/273/271/277/241/277/274 — all ≤280, all outside 140-200 range (insights-tuned)
- Fact-check: Manual verification. All Priority 1 claims VERIFIED. HIGH verified: final score 8-5 (3 sources), Cubs 29-24 (series-context + ESPN), 8-game skid (3+ sources), 12 of 14 losses (ESPN + Cubs Insider), Ramirez first MLB hit RBI double (ESPN + wire), Imanaga 7R/7H/1BB/6K in 7 IP 3rd straight loss (Bleacher Nation box score), Busch 5th HR (Cubs Insider), Ben Brown 2.09 ERA/40K/0.98 WHIP/1-2 (FanDuel + CBS Sports), Mlodzinski 4-3/3.96 ERA (FanDuel), Wicks recall + Cabrera IL right-finger blister (Bleacher Nation + MLB Trade Rumors), Wicks 1 ER in last 11 Iowa IP (Bleacher Nation + MLB TR), Brewers 30-20 (Brew Crew Ball + Yahoo Sports), Cardinals 29-22 (Yahoo Sports), Misiorowski 0.00 ERA in May 37K in 24.1 IP (YourNews/MLB.com), Alcantara 15 HR in 41 Iowa games (MLB.com + Bleacher Nation). MEDIUM: Cubs 15-over on May 8 (single CBS Sports AI summary), rotation ERA >6.00 (same), offense/pitching 28th rankings (same), Alcantara 7-game streak 10-for-28 5 XBH 9 RBI (single Bleacher Nation source). NOT USED: Alcantara "tied for MiLB HR lead" (superlative, not independently verified), "longest skid since July 2022" (superlative, single source).
- Insights applied: 9/9 significant findings applied (first run with 9 findings — tweet sample grew from prior runs to 89 measured tweets). All 7 tweets 260+ or in neutral 200-260 zone. Zero leading emojis. Zero ALL CAPS openings. Score explicit in recap. Stats in every post. No overnight slots.
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-25/review-dashboard.html). Publish to content-dashboards FAILED (403 — same recurring issue, PAT doesn't cover content-dashboards repo).
- 07-content-data.json: ✓ Compiled, 7 stories, 7 x_posts with posting_time in "H:MM AM/PM CT" format, 0 errors, 0 warnings
- Key stories: Astros 8 Cubs 5 eight straight losses Ramirez first MLB hit Imanaga 3rd loss 29-24 (P10), 4-game road series Pirates PNC Park Brown 2.09 ERA (P9), 15-over to 5-over in 17 days collapse bold take (P9), Wicks recalled Cabrera IL right-finger blister 4-of-6 starters out (P8), NL Central Cubs 3rd Brewers 30-20 Cardinals 29-22 Misiorowski (P8), Ben Brown 2.09 ERA 0.98 WHIP 40 K quiet excellence (P7), Alcantara 15 HR 41 Iowa games 7-game streak power surge (P6)
- Notes: is_series_start_today=true — posting-order conflict: Cubs SKILL prompt reserves 7 AM for series preview; engine docs give game recaps priority. Engine docs win (flagged in 02-story-analysis.md + 00-daily-brief.md). 9 insights findings (up from 6 in prior runs — expanded tweet sample). compile-content-data.py required ### STORY N: headers in daily brief and **Post NA** + [POSTING WINDOW: ...] format in X posts — initial drafts had wrong format, both corrected before compile. All tweets trimmed from initial 285–414 char range to final 241–279 range before compile.

### 2026-05-22
- Stories: 6 (Tier 1: series-preview, astros-bounce-back-take; Tier 2: cabrera-peralta-clock, boyd-recovery, game-preview; Tier 3: iowa-prospects) — X-only niche, SERIES OPENER
- X posts: 6 (3 informative / 3 bold = 50/50 mix)
- Char counts: 258/250/270/258/241/240 — all ≤280, all outside 140-200 range (insights-tuned)
- Fact-check: Manual verification. All Priority 1 claims (dates, times, game times, opponent records) VERIFIED across multiple sources. 5 MEDIUM flags (Astros "9 IL" count, "5 runs in last 4 games", Alcántara walk-off attribution, Taillon ERA rounding, Boyd late June timing). No corrections to tweet copy required.
- Insights applied: 6/6 significant findings applied. Key changes: no leading emojis, all tweets 240-270 chars (avoiding 140-200 penalty bucket), records explicit in series preview and division take tweets, no overnight slots.
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-22/review-dashboard.html). Publish to content-dashboards FAILED (403 — same recurring issue, PAT doesn't cover content-dashboards repo).
- 07-content-data.json: ✓ Compiled, 6 stories, 6 x_posts with posting_time in "H:MM AM/PM CT" format, 0 errors, 0 warnings
- Key stories: Series preview Cubs vs Astros 3-game Wrigley Game 1 1:20 PM CT (P10), bold take Astros 20-31 nine IL depleted bounce-back opp (P9), Cabrera TBD blister Horton/Steele/Boyd all out Peralta June 1 10 days (P9), Boyd mound session Sat ahead of schedule late June return (P8), game preview Taillon 2-3 4.97 vs Arrighetti 5-1 1.50 1:20 PM CT (P8), Iowa snapped 8-game skid Alcántara walk-off Ayers HR Tennessee (P6)
- Notes: is_series_start_today=true per series-context.json snapshot. 7:00 AM slot reserved for series preview. Insights snapshot loaded from Cubs/_data/insights.json (6 significant findings, generated_at 2026-05-22T08:30 UTC). Astros injury context: Correa season-ending ankle surgery confirmed MLB.com + MLBTR. Arrighetti 5-1 1.50 ERA confirmed ESPN/FanGraphs. Game 1 first pitch 1:20 PM CT confirmed MLB.com gameday.

### 2026-05-21
- Stories: 6 (Tier 1: brewers-sweep-recap, division-take, cabrera-blister; Tier 2: boyd-recovery, peralta-clock; Tier 3: iowa-prospects) — X-only niche, OFF DAY
- X posts: 6 (3 informative / 3 bold-analytical = 50/50 mix)
- Char counts: 244/248/255/211/259/253 — all ≤280, all outside 140-200 range (insights-tuned)
- Fact-check: Manual verification. 24 claims checked, 17 HIGH confidence, 7 MEDIUM, 0 corrections. MEDIUM flags: Harrison ERA 1.77 (single source, not in tweet), Boyd recovery details (Counsell quote + mound session plan, single source, hedge language used), Noland ankle injury (single source, "status unknown" qualifier), Iowa 8-game streak count (Bleacher Nation headline consistent with prior reports).
- Insights applied: 6/6 significant findings applied. Key changes: no leading emojis (overrides brand-voice), all tweets 211-259 chars (avoiding 140-200 penalty bucket), score in first line of recap post.
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-21/review-dashboard.html). Publish to content-dashboards FAILED (403 — same recurring issue, PAT doesn't cover content-dashboards repo).
- 07-content-data.json: ✓ Compiled, 6 stories, 6 x_posts with posting_time in "H:MM AM/PM CT" format, 0 errors, 0 warnings
- Key stories: Brewers 5-0 Harrison 11K sweep at Wrigley Cubs 29-21 5-game skid (P10), division take Brewers 29-18 1.5 GB (P9), Cabrera blister all four starters unavailable at once (P9), Boyd ahead of schedule mound session Sat bullpen next wk (P8), Peralta June 1 11 days rotation crisis (P8), Iowa 8 straight losses Noland ankle Kepley HR (P6)
- Notes: Off day. series-context confirmed off_day=true. Insights snapshot loaded from Cubs/_data/insights.json (6 significant findings, generated_at 2026-05-21T08:30 UTC). Game 3 result (Brewers 5-0 sweep) confirmed via ESPN, CBS Sports, Bleacher Nation, Fox Sports.

### 2026-05-20
- Stories: 6 (Tier 1: misiorowski-recap, slide-analysis; Tier 2: boyd-surgery, game3-preview, peralta-clock, game-time-hype) — X-only niche
- X posts: 6 (3 informative / 3 bold-hype = 50/50 mix)
- Char counts: 254/238/247/267/257/232 — all ≤280, all outside 140-200 range (insights-tuned)
- Fact-check: Manual verification. 18 claims checked, 17 HIGH confidence, 1 single-source flag (Brown league-leading wild pitch — CBS Chicago). No corrections needed.
- Insights applied: 6/6 significant findings applied. Key changes: no leading emojis (vs brand-voice default), all tweets 200-267 chars (avoiding 140-200 penalty bucket), score in first line of recap post.
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-20/review-dashboard.html). Publish to content-dashboards FAILED (403 — same recurring issue, PAT doesn't cover content-dashboards repo).
- 07-content-data.json: ✓ Compiled, 6 stories, 6 x_posts with posting_time in "H:MM AM/PM CT" format, 0 errors, 0 warnings
- Key stories: Brewers 5-2 Misiorowski 24.1 scoreless innings Brown L (P10), Cubs slide 4 straight 8-of-10 Brewers in first 0.5 GB (P9), Boyd meniscus surgery 6 weeks second IL stint (P8), Game 3 Cabrera vs Harrison 6:40 PM CT sweep on line (P9), Peralta June 1 12 days Counsell connection (P8), game-time hype (P5)
- Notes: First pipeline run with active insights data (series-context and insights snapshots loaded from Cubs/_data/ successfully — game-monitor push restored). Series context confirmed mid-series Cubs vs Brewers, is_series_start_today=false. All 6 significant_findings applied per methodology.

### 2026-05-19
- Stories: 6 (Tier 1: imanaga-recap, nl-central-alarm; Tier 2: brown-misiorowski-preview, peralta-clock, boyd-update; Tier 3: game-time-hype) — X-only niche
- X posts: 6 (3 informative / 3 bold-hype = 50/50 mix)
- Char counts: all 6 ≤ 280 (218/205/234/254/228/150 per compiler)
- Fact-check: Manual verification. 29 claims checked, 0 errors, 4 MEDIUM/plausible. HIGH verified: Brewers 9-3 Cubs (4 sources), Imanaga 8 ER 9 H 4.1 IP (ESPN+CBS), Imanaga worst start of season (ESPN+Sun-Times), Bauers 3-run HR 4 RBI (ESPN), Yelich HR 2nd straight day (ESPN), Swanson 2-run HR (ESPN/CBS), Cubs lost 7 of 9 (Sun-Times), Brewers 0.5 GB (ESPN explicit), Brown 1.60 ERA (multiple preview), Misiorowski 80 Ks/51 IP 2.12 ERA (multiple preview), game 6:40 PM CT (multiple), Peralta 3.12 ERA June 1 (established), Counsell connection (multiple), Boyd mound session May 16 (established). MEDIUM: Cubs 29-19 record (derived), Cardinals 1.0 GB (single-source), Brown 0 ER 12.2 IP (single source), Misiorowski 0 ER 3 straight (single source), Boyd bullpen session next week (MLB TR + SI).
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-19/review-dashboard.html). Publish to content-dashboards FAILED (403 — same recurring issue, PAT doesn't cover content-dashboards repo).
- 07-content-data.json: ✓ Compiled, 6 stories, 6 x_posts with posting_time in "H:MM AM/PM CT" format, 0 errors, 0 warnings
- Key stories: Imanaga 8 ER Brewers 9-3 Cubs 29-19 Brewers 0.5 GB (P10), NL Central alarm 7-of-9 Brewers 0.5 Cardinals 1.0 (P9), Brown 1.60 ERA vs Misiorowski 80 Ks Game 2 6:40 CT (P9), Peralta June 1 13 days rotation can't survive Imanaga alone (P8), Boyd bullpen session late June return on track (P7), game-time hype Game 2 (P5)
- Notes: Both APIs (insights, series-context) returned 403 for 8th consecutive pipeline run. off_day=true fallback INCORRECT — web research confirmed Brewers series Game 2 tonight at Wrigley. No insights tuning (cold start). 07-content-data.json ready for cubs-x-bot.

### 2026-05-18
- Stories: 6 (Tier 1: crosstown-walkoff-recap, brewers-series-preview; Tier 2: roster-moves, brown-vs-misiorowski, peralta-trade-clock; Tier 3: game-time-hype) — X-only niche
- X posts: 6 (3 informative-leaning / 3 bold-hype = 50/50 mix)
- Char counts: all 6 ≤ 280 (274/257/268/278/280/125)
- Fact-check: Manual verification. 27 claims checked, 0 errors, 1 plausible (Cubs record 29-17 calculated). HIGH verified: White Sox 9-8 Cubs F/10 (ESPN box score), Quero 2-run walkoff HR (FOX 32 + ESPN), Conforto 3-run HR 9th (FOX 32), Peters 3-run HR 8th (FOX 32), White Sox win series 2-1 first since 2022 (FOX 32 explicit), Imanaga 4-3 2.32 ERA (MLB.com), Sproat 1-2 5.75 ERA (MLB.com), 3-game series 6:40 PM CT (MLB.com Gameday), Blach selected/Assad optioned/Harvey 60-day (CubsHQ), Boyd 6 weeks (MLB Trade Rumors), Brown 1.60 ERA (Brew Crew Ball), Misiorowski MLB K/9 leader 14.0 (multiple sources), Brown 2-0 vs Brewers 19 K/18 IP (Brew Crew Ball), Peralta 3.12 ERA + June 1 deadline (established May 14-17 pipeline). Dropped: Misiorowski 18.1 scoreless innings in May (single source), Misiorowski ERA figure (conflicting sources 2.84 vs 2.12).
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-18/review-dashboard.html). Publish to content-dashboards FAILED (403 — same recurring issue, PAT doesn't cover content-dashboards repo).
- 07-content-data.json: ✓ Compiled, 6 stories, 6 x_posts with posting_time in "H:MM AM/PM CT" format, 0 errors, 0 warnings
- Key stories: White Sox 9-8 walkoff Quero HR Conforto 3-run 9th (P9), Brewers 3-game series Wrigley Imanaga vs Sproat 6:40 CT (P9), Blach selected Assad optioned Harvey 60-day (P7), Brown 1.60 ERA vs Misiorowski MLB K/9 leader Game 2 Tue (P9), Peralta June 1 14 days Boyd out 6 weeks (P8), game-time hype (P5)
- Notes: Both APIs (insights, series-context) returned 403 for 6th consecutive pipeline run. off_day=true fallback INCORRECT — web research confirmed Cubs open Brewers series tonight. Conflict resolution: game recap (engine docs priority) at 7 AM; series preview at 8:15 AM. No insights tuning (cold start). 07-content-data.json ready for cubs-x-bot.

### 2026-05-17
- Stories: 6 (Tier 1: recap, bold-take; Tier 2: boyd-mound, rival-watch, game-preview; Tier 3: peralta-clock) — X-only niche
- X posts: 6 (3 informative / 3 bold-hype = 50/50 mix)
- Char counts: all 6 under 280
- Fact-check: 29 claims, 0 errors
- Dashboard: Generated locally. Publish to content-dashboards FAILED (403).
- 07-content-data.json: ✓ Compiled, 6 stories, 6 x_posts
- Key stories: Taillon 5 HRs game 2 loss (P10), rotation crisis bold take (P9), Boyd mound session late June return (P8), NL Central Cubs lead Cards lurking (P7), Game 3 Rea vs Fedde 1:10 PM CT (P8), Peralta June 1 decision clock (P7)

### 2026-05-16
- Stories: 6 (Tier 1: crosstown-recap; Tier 2: kelly-bold-take, game2-preview, rival-watch, game-time; Tier 3: brown-rotation) — X-only niche
- X posts: 6 (3 informative / 3 bold-hype = 50/50 mix)
- Char counts: all 6 under 280 (238/256/261/248/227/180)
- Fact-check: Manual verification. Key verified (HIGH): Cubs 10-5 White Sox (5+ sources), Kelly 3-for-5 4 RBIs (AP wire multi-source), 14 hits (ABC7/AP), White Sox 5-game streak ended (multiple), Thornton W 2-0 2 perfect IP (Bleacher Nation), Bregman 2H 3R (AP), Brown 4 IP 0 ER 7 K ×2 consecutive (pipeline carryover HIGH). MEDIUM: Cubs 29-16 (calculated from 28-16 +1 win), Rea 4-2 4.68 ERA (Bleed Cubbie Blue), Fedde 0-4 3.77 ERA (BCB), 6:10 PM CT game time (BCB series preview), Cardinals 25-18 (AI summary standings), Misiorowski 6 IP 11 K vs Yankees (Yahoo Sports HIGH actually), Yelich working back (Yahoo Sports), Brown next start Tue vs Brewers (Bleacher Nation single source). Dropped: "Cardinals 7 of 8" stat (May 5 era, stale).
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-16/review-dashboard.html). Publish to content-dashboards FAILED (403 — not in PAT scope, same recurring issue).
- 07-content-data.json: ✓ Compiled, 6 stories, 6 x_posts with posting_time in "H:MM AM/PM CT" format
- Key stories: Cubs 10-5 White Sox Kelly 4 RBI 14 hits streak-buster (P10), Kelly backup catcher hero depth 29-16 (P8), Game 2 Rea vs Fedde 6:10 PM CT Rate Field (P9), NL Central Alive Cards 25-18 Misiorowski Yelich (P7), Ben Brown Tue vs Brewers 4-0-7 twice (P8), Game 2 hype (P5)
- Notes: API double failure (series-context 403 returned off_day=true INCORRECT; insights 403 tweet_count=0). Web research overrode series-context fallback — Cubs playing Game 2 tonight. No performance tuning from insights (cold start). 07-content-data.json ready for cubs-x-bot.

### 2026-05-15
- Stories: 7 (Tier 1: game-recap, crosstown-preview; Tier 2: palencia-return, brown-starter, trade-urgency, game-time; Tier 3: alcantara-prospect) — X-only niche
- X posts: 7 (4 informative / 3 bold-hype = ~57/43 mix)
- Char counts: all 7 under 280 (225/251/245/243/235/274/161)
- Fact-check: Manual verification. Key verified (HIGH): Cubs 2-0 (4 sources), Brown 4 IP 1 H 7 K (CBS+AP), Happ 424-ft HR Chop House (CBS), Palencia Save No. 3 (CBS), 28-16 record, 4-game skid snapped, Brown 2nd consecutive start, Cabrera 3-1 3.88 ERA, game 6:40 PM CT at Rate Field (3 sources), August 3 deadline, Peralta/Alcantara linked (multiple). MEDIUM: Palencia 100.4 mph Iowa rehab (Cubs Insider only), Alcántara 14 HR MiLB lead (MLB.com headline), Cabrera/Burke ERA (Bleacher Nation May 13 — <48h). Dropped: Ha-Seong Kim Braves roster (entity risk — unverified roster move), Happ hitting streak length (headline only).
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-15/review-dashboard.html). Publish to content-dashboards FAILED (403 — not in PAT scope, same recurring issue).
- 07-content-data.json: ✓ Compiled, 7 stories, 7 x_posts with posting_time in "H:MM AM/PM CT" format
- Key stories: Cubs 2-0 Happ 424-ft HR Chop House Brown 7 K Palencia Save 3 (P10), Palencia BACK 100.4 mph Iowa rehab Save No. 3 (P9), Brown 2 straight starts rotation answer Horton/Steele/Boyd all out (P8), Crosstown Classic Cabrera vs Burke Rate Field 6:40 PM CT (P8), SP trade triage Peralta/Alcantara August 3 deadline survival not deadline (P7), Alcantara 14 HR tied MiLB lead Iowa .973 OPS (P6), Game time hype (P5)
- Notes: Full pipeline completed except dashboard remote publish (PAT doesn't include content-dashboards repo). cubs-x-bot will read 07-content-data.json from this repo.

### 2026-05-14
- Stories: 7 (Tier 1: recap, rotation-emergency; Tier 2: trade-urgency, game-preview, game-time; Tier 3: rival-watch, prospect) — X-only niche
- X posts: 7 (4 informative / 3 bold-take = ~57/43 mix)
- Char counts: all 7 under 280 (218/249/222/250/262/271/119)
- Fact-check: Manual verification. Key verified: Braves 4 Cubs 1 (HIGH — 4 sources), 4-game skid (HIGH), Imanaga to 8th (MEDIUM), Boyd knee surgery 6 weeks (HIGH — 6 sources), Steele pushed to August (MEDIUM — 4 sources), Horton 2027 (HIGH), Ben Brown 1-1 1.82 ERA (MEDIUM), Sale 2.14 ERA 33 Ks last 4 starts (MEDIUM), game 6:15 PM CT (HIGH), Nootbaar eligible May 24 (MEDIUM). Dropped: Cardinals six-man rotation (unverifiable — likely NFL data contamination), Sale W-L record (discrepancy between sources), "10 pitchers on IL" exact count.
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-14/review-dashboard.html). Publish to content-dashboards FAILED (403 — not in PAT scope).
- 07-content-data.json: ✓ Compiled, 7 stories, 7 x_posts with posting_time in "H:MM AM/PM CT" format
- Key stories: Braves 4 Cubs 1 Imanaga gem wasted 4-game skid (P10), Rotation emergency Boyd surgery 6 weeks Steele to August (P10), Trade urgency Peralta/Alcantara/Gray triage not deadline (P8), Cardinals rival watch Nootbaar May 24 NL Central tight (P6), Alex Ramirez Knoxville 23yr raw power multi-RBI (P6), Brown vs Sale series finale 6:15 PM CT (P8), Game time (P5)
- Notes: Full pipeline completed except dashboard remote publish (PAT doesn't include content-dashboards repo). cubs-x-bot will read 07-content-data.json from this repo. Sale W-L record had source discrepancy — omitted from tweet, used ERA only.

### 2026-05-13
- Stories: 8 (Tier 1: recap, slump take, game preview, game time; Tier 2: Hendriks signing, SP trade market, injury roundup; Tier 3: prospects) — X-only niche
- X posts: 8 (4 informative / 4 bold-take = 50/50 mix)
- Char counts: all 8 under 280 (248/206/231/237/263/271/275/148)
- Fact-check: Manual verification. Key verified facts: Braves 5 Cubs 2, one-hitter, Bregman HR #4, Rea 4-2, Cubs 27-15, Braves 29-13, Imanaga 4-2/2.28 ERA, Ritchie 1-0/3.63 ERA, game 6:15 PM CT, Hendriks MiLB deal confirmed. Flagged: Hartshorn .907 OPS (MEDIUM — search summary only), 10-game win streak (MEDIUM — single source).
- Dashboard: Generated locally (Cubs/cubs-content-2026-05-13/review-dashboard.html). Publish to content-dashboards FAILED (403 — not in PAT scope).
- 07-content-data.json: ✓ Compiled, 8 stories, 8 x_posts with posting_time in "H:MM AM/PM CT" format
- Key stories: Braves 5 Cubs 2 one-hitter Bregman solo HR only hit (P10), Slump take 3 losses after 10-game run (P9), Liam Hendriks MiLB deal Iowa 3x All-Star lymphoma survivor (P8), SP trade market Peralta/Alcantara/Gray linked (P7), Injury roundup Horton 2027 Harvey setback Steele close (P7), Hartshorn .907 OPS Knoxville South Bend win (P6), Imanaga vs Ritchie tonight 6:15 PM CT (P8), Game time (P5)
- Notes: Full pipeline completed except dashboard remote publish (PAT doesn't include content-dashboards repo). cubs-x-bot will read 07-content-data.json from this repo. No PostPlanner xlsx needed (cubs-x-bot reads JSON directly).

### 2026-03-30
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3) — X-only niche
- X posts: 7 (~50% informative / ~50% bold-take mix)
- Fact-check: 66 claims extracted. 1 char-limit violation fixed (Story 7 from 304→under 280). 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- PostPlanner: cubs-postplanner-2026-03-30.xlsx (7 posts, X only, no TOBI)
- Key stories: Nationals 6 Cubs 3 series loss 1-2 Wiemer 3-run HR Imanaga (P10), Bregman 2 HRs first as a Cub 398 ft back-to-back with Happ (P10), Imanaga 0-1 7 K 16 whiffs stuff is there (P8), Cubs vs Angels today Cabrera home debut (P7), PCA 4-for-9 2 SB early (P7), Suzuki targeting April 1-7 return (P6), Cubs 1-2 analysis (P5)
- Notes: Full pipeline completed. All scripts ran successfully. Push required manual rebase+push after publish-dashboard.py rejected.

### 2026-03-29
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3) — X-only niche
- X posts: 9 (~50% informative / ~50% bold-humor mix)
- Fact-check: 71 claims extracted. 1 char-limit violation fixed (Story 6 tweet trimmed from 297→268 chars). 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- PostPlanner: cubs-postplanner-2026-03-29.xlsx (9 posts, X only, no TOBI)
- Key stories: Cubs 10 Nationals 2 Horton franchise record 13 consecutive ≤2 ER starts breaks Reulbach 1909 (P10), Horton historical context ace with depleted rotation (P10), Game 3 today 1:20 PM CT series finale Wrigley (P8), Amaya 2-for-4 HR 2 RBI young catcher arriving (P7), PCA 2-for-4 day after $115M extension (P7), Steele live BP "Looks like Justin" late May/June return (P6), Bregman 2 games in $175M warming up (P5)
- Notes: Full pipeline completed. All scripts ran successfully. Story 1&2 required split into separate ### STORY N: headers.

### 2026-03-28
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 9 (4 informative / 5 bold-humor = ~50/50 mix)
- Fact-check: 53 claims extracted. 0 char-limit violations. 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- PostPlanner: cubs-postplanner-2026-03-28.xlsx (9 posts, X only)
- Key stories: Nationals 10 Cubs 4 Opening Day Boyd 3.2 IP 6 ER 6-run 4th (P10), Bregman Cubs debut 1-for-4 walk standing ovation (P10), PCA 2 hits 2 RBI + $115M/6yr extension on Opening Day (P8), Suzuki 10-day IL right knee sprain Conforto to RF (P8), Steele 60-day IL UCL revision late May/June return Hodge Wicks also out (P7), Game 3 today Horton vs Mikolas series salvage (P7), Opening Day loss perspective 162-game take (P5)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-24
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold)
- Fact-check: 0 char-limit violations. 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: Suzuki officially on 10-day IL Assad to Iowa Brown to pen (P10), Ballesteros top prospect earns OD roster (P10), 2 days to Opening Day Boyd vs Cavalli Wrigley (P8), Cubs 15-6 Yankees exhibition (P7), Roster taking shape Conforto Carlson Ballesteros in (P7), Final exhibition today Cole starting for NYY (P6), Imanaga spring finale 18 K in 18 IP (P5)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-22
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Fact-check: 34 claims extracted. 0 char-limit violations. 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: Suzuki officially out for Opening Day IL likely return April 1 (P10), Conforto NRI makes Opening Day roster RF platoon with Carlson (P10), 4 days to Opening Day Boyd vs Cavalli Wrigley 1:20 PM CT (P8), Roster cuts down to 41 Murray Rojas sent down Carlson earning spot (P7), Cubs vs Brewers final Cactus League game today 2:05 PM CT (P7), Suzuki IL opens Conforto/Carlson RF platoon analysis (P6), Spring Breakout prospects vs Padres prospects (P5)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-20
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Fact-check: 42 claims extracted. 41 verified, 1 plausible. 0 char-limit violations. 0 consistency errors.
- Dashboard: Not generated (X/Twitter only run)
- Key stories: Suzuki decision day tomorrow Opening Day or IL Saturday call (P10), Palencia WBC champion 5 IP 0 H 9 K 3/3 saves closer locked (P10), PCA Bregman back in camp full squad assembling (P8), 6 days to Opening Day Boyd on mound Wrigley (P7), 4th OF Conforto Carlson inside edge Suzuki IL opens spot (P8), split-squad vs Reds A's evening starts heat wave (P5), Cabrera shakes off D-backs rough outing rotation secure (P7)
- Notes: X/Twitter only pipeline. 13 web searches conducted. AZ heat wave shifting games to evening. Suzuki Saturday decision is the top storyline heading into the weekend.

### 2026-03-19
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Fact-check: 88 claims extracted. 0 char-limit violations. 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: Suzuki PCL update decision Saturday "getting better every day" (P10), WBC stars return PCA Friday Palencia champion 0 hits 9 K (P9), D-backs 16 Cubs 8 Cabrera rocked Rojas grand slam (P7), 7 days to Opening Day Boyd starts rotation locked (P8), 4th OF race Carlson Shaw Conforto (P7), spring numbers Horton 21 whiffs Cabrera 99 mph (P6), off day split-squad tomorrow (P5)
- Notes: Full pipeline completed. All scripts ran successfully. Off day — no game recap.

### 2026-03-18
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Fact-check: 102 claims extracted. 1 char-limit violation fixed (Story 1 tweet 281→267 chars). 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: Venezuela 3 USA 2 WBC Final Palencia saves it 1-2-3 in 9th Cubs prospect is WBC champion (P10), Suzuki sprained PCL minor in nature decision Saturday on Opening Day (P10), Cubs 8 Angels 6 Imanaga starts (P7), Palencia 2 saves in 2 days WBC champion feature (P7), 8 days to Opening Day roster taking shape (P6), Harper 432-ft HR wasn't enough WBC drama (P6), Cubs vs Diamondbacks today 3:10 PM CT (P5)
- Notes: Full pipeline completed. Char violation fixed before dashboard generation.

### 2026-03-17
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Content files: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md, 06-fact-check-log.md, 07-content-data.json
- Story history: Updated with all 7 stories
- Fact-check: 109 claims extracted. 0 char-limit violations. 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: WBC Final TONIGHT USA vs Venezuela PCA vs Palencia Cubs teammates collide (P10), Suzuki MRI results expected today Opening Day in jeopardy (P10), Cubs 5 Guardians 2 Horton fans 10 best spring outing (P9), Palencia struck out final batter for Venezuela semifinal (P7), 9 days to Opening Day roster questions (P7), Matt Shaw Plan B at RF (P6), Cubs vs Angels tonight (P5)
- Notes: Full pipeline completed including dashboard publish. All scripts ran successfully.

### 2026-03-16
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Content files: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md
- Story history: Updated with all 7 stories
- Fact-check: PENDING — Bash permission needed for verify-facts.py
- Dashboard: PENDING — Bash permission needed for generate-review-dashboard.py + publish-dashboard.py
- Key stories: USA 2 DR 1 PCA in WBC Final (P10), Suzuki knee injury returns to camp (P10), Dodgers 14 Cubs 8 Taillon 22.18 ERA (P8), Palencia dominant for Venezuela semis tonight (P8), 10 days to Opening Day Boyd prep (P7), Ben Brown 15K new sinker (P7), Cubs at Guardians tonight (P5)
- Notes: Weekend catchup (last run March 14). Bash denied — run manually:
  ```
  python _engine/scripts/verify-facts.py --niche Cubs 2026-03-16
  python _engine/scripts/compile-content-data.py --niche Cubs 2026-03-16
  python _engine/scripts/generate-review-dashboard.py --niche Cubs 2026-03-16
  python _engine/scripts/publish-dashboard.py --niche Cubs 2026-03-16
  ```

### 2026-03-14
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Content files: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md, 06-fact-check-log.md
- Story history: Updated with all 7 stories
- Fact-check: 67 claims extracted. 0 char-limit violations. 0 consistency errors.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: USA 5 Canada 3 WBC QF PCA 2 hits RBI (P10), Boyd named Opening Day starter March 26 (P10), Steele faces live hitters first time since surgery (P9), Cubs at Rockies today (P9), 12 days to Opening Day rotation locked (P8), Cabrera 1.08 ERA touching 99 (P7), Carlson .500 4th OF leader (P6)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-13
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold-passionate-humor = 50/50 mix)
- Content files: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md, 06-fact-check-log.md
- Story history: Updated with all 7 stories
- Fact-check: 23 claims checked, 22 verified, 1 plausible (Cabrera spring totals). 0 char-limit violations.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: Cubs 7-4 Mariners Cabrera sharp (P10), USA vs Canada WBC QF tonight PCA starts CF (P10), Cubs vs White Sox today (P9), Roster to 46 Carlson .400 (P8), 13 days to Opening Day (P7), Horton don't sweat ERA (P7), Carlson Cardinals revenge tour (P6)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-12
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold = 50/50 mix)
- Content files: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md, 06-fact-check-log.md
- Story history: Updated with all 7 stories
- Fact-check: 74 claims extracted. 9 char-limit violations fixed (agent wrote all tweets over 280, rewrote entirely). All pass after fix.
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: Cubs 9-8 walkoff Halbach double (P10), USA WBC quarterfinals vs Canada Friday (P9), Cubs vs Mariners today (P9), PCA turns 23 (P8), 14 days to Opening Day (P7), Horton process 9.53 ERA (P7), Shaw 6 positions (P6)
- Notes: Full pipeline completed including dashboard and publish. March 11 dashboard also published (was pending).

### 2026-03-11
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold = 50/50 mix)
- Content files: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md, 06-fact-check-log.md
- Story history: Updated with all 7 stories
- Fact-check: 18 claims verified, 1 correction (PCA age 22 not 23 — birthday March 12), 3 char-limit violations fixed
- Dashboard: Pending — Bash denied, run manually: `python _engine/scripts/generate-review-dashboard.py --niche Cubs 2026-03-11`
- Publish: Pending — run manually: `python _engine/scripts/publish-dashboard.py --niche Cubs 2026-03-11`
- Key stories: Italy 8 USA 6 PCA 2 HRs (P10), Rangers 8 Cubs 3 Horton process quote (P9), Cubs vs Royals today (P9), WBC tiebreaker scenarios (P8)
- Notes: Content pipeline complete through Step 12. Steps 13/15 (dashboard generate + publish) require Bash permission.

### 2026-03-10
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold = 50/50 mix)
- Content files: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md, 06-fact-check-log.md
- Story history: Updated with all 7 stories
- Fact-check: 37 claims extracted, all verified, 7 char-limit violations fixed on first pass
- Dashboard: Published, live at https://fangearhq-boop.github.io/cubs-dashboards/
- Key stories: USA 5 MEX 3 Skenes WBC debut (P10), Cubs @ Rangers today (P9), Roster cuts 62→53 (P9), Suzuki 2 HR (P8)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-07
- Stories: 7 (4 Tier 1, 2 Tier 2, 1 Tier 3)
- X posts: 10 (5 informative / 5 bold = 50/50 mix)
- Content files created: 00-research.md, 00-daily-brief.md, 01-research-notes.md, 02-story-analysis.md, 03-social-posts-x.md, 06-fact-check-log.md
- Story history: Updated with all 7 stories
- Fact-check: 18 claims verified, 0 corrections needed, all character counts pass
- Dashboard/Export/Publish: Pending manual script runs (Bash unavailable)
- Key stories: Suzuki 2 HR WBC (P10), Padres shutout (P9), Imanaga tiebreaker start (P9), Happ free agency (P8)
- Notes: Bash denied in session. Steps 13/14/15 require manual execution.

### 2026-03-05
- Stories: 10 (X/Twitter only, no FB/images/articles)
- X posts: 10
- Dashboard: Published, live at Pages URL
- Notes: Full pipeline completed. Switched Pages from legacy to workflow deployment.
