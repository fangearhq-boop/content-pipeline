# Cubs Pipeline Status — Updated 2026-09-15

## Latest Run
- **Date:** 2026-09-15 (Tuesday — Game 2 of 3 vs Atlanta Braves at Wrigley, 6:40 PM CT)
- **Stories:** 7
- **X posts:** 7
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ All clear, 0 errors, 0 warnings
- **07-content-data.json:** ✅ Valid JSON, all 7 posts with posting_time

## Insights Summary (2026-09-15)
- **Snapshot generated:** 2026-09-15T08:30:00.083815Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 115
- **significant_findings count:** 3
- **Finding 1 (strongest):** `has_stat=True` WINNER — median 106 vs 68.5, Cliff's delta 0.284, p=0.0088
  - **Applied:** Every tweet contains at least one concrete stat (score, HR, SB, ERA, record, games count). Zero stat-free tweets.
- **Finding 2:** `opening=statement` LOSER — not_statement wins, median 106 vs 69, Cliff's delta 0.27, p=0.0152
  - **Applied:** All 7 tweet openers are stat-first (score, numbers, record). No tweet starts with a declarative sentence.
- **Finding 3:** `opening=stat_lead` WINNER — median 106 vs 69.5, Cliff's delta 0.262, p=0.0259
  - **Applied:** All 7 tweets open with a stat-lead format. Examples: "Cubs 7, Braves 3." / "42 HR. 37 SB." / "84-67. WC1." / "Gausman: 9-12, 4.60 ERA. Pérez: 8-9, 3.08 ERA."

## Series Context (2026-09-15)
- **`is_series_start_today`:** FALSE (mid-series — Game 2 of 3 vs Braves)
- **`off_day`:** FALSE
- **Opponent:** Atlanta Braves (88-63)
- **Venue:** Wrigley Field (home)
- **Today's game:** 6:40 PM CT
- **Pitchers:** Kevin Gausman (9-12, 4.60 ERA) vs Martin Pérez (8-9, 3.08 ERA)
- **Action:** No series-preview slot (mid-series). Game preview in 12:00 PM slot.

## Current Wild Card Status
- **Cubs position:** WC1
- **Record:** 84-67 (11 games remaining)
- **Phillies:** ~0.5-1 game behind Cubs for WC1
- **Cardinals:** Eliminated from playoff contention
- **Brewers:** NL Central champions (93-57), clinched postseason
- **Braves:** 88-63, NL East, pushing for No. 2 seed and possible first-round bye

## PCA 40-40 Watch
- **Current (after Sept 14 game):** 42 HR / 37 SB
- **Target:** 3 more SBs for 40-40 (first Cub ever, 7th MLB player ever)
- **Games remaining:** 11
- **Other milestone:** HR No. 42 ties Billy Williams (1970) for franchise LH HR record
- **Note:** PCA on HOT streak — key story for next 1-2 weeks

## Swanson Return
- **Status:** Doing Trajekt/machine work at Wrigley; NOT yet on Iowa rehab
- **Target activation:** ~September 18 in Cincinnati
- **Injury:** Grade 2 left oblique strain (out since Aug. 16, ~30 games)
- **Note:** Multiple sources confirm Sept 18 target. Still needs short Iowa rehab before activation.

## Braves Series Notes (Sept 14-16)
- **Gausman (Cubs):** 9-12, 4.60 ERA — inconsistent in Cubs starts; 6-ER meltdown vs Brewers Sept 9
- **Pérez (Braves):** 8-9, 3.08 ERA — has been excellent lately (≤1 ER in 3 of last 4 starts)
- **Braves:** Trying to clinch postseason berth in this series (with D-backs help)
- **Stake:** Cubs series win extends WC1 lead; Braves possible October NLDS opponent

## Compilation Notes
- **Dashboard publish:** cubs-x-bot target (07-content-data.json) confirmed clean. Content-dashboards push skipped (out-of-scope repo, expected behavior).

## Previous Run (2026-09-13)
- **Stories:** 5 / **X posts:** 5
- **Series:** Cubs vs Pirates Game 3 (series finale)
- **Insights:** 3 findings (`opening=statement` LOSER, `has_score=False` WINNER, `has_stat=True` WINNER) applied
- **Result:** Pirates 4, Cubs 3 (loss; series still 2-1 Cubs)
- **Cubs record at time of run:** 83-66

## Previous Run (2026-09-12)
- **Stories:** 6 / **X posts:** 6
- **Series:** Cubs vs Pirates Game 2 (mid-series)
- **Insights:** 2 findings (`has_score=False`, `opening=not_statement`) applied
- **Cubs record:** 82-66 at time of run
- **Result:** Cubs 4-3 Pirates (confirmed post-run); won with 8th-inning rally

## Previous Run (2026-09-11)
- **Stories:** 7 / **X posts:** 7
- **Series:** Cubs vs Pirates Game 1 (series start mandatory slot used)
- **Insights:** 1 finding (`has_score=False`) applied
- **Cubs record:** 81-66 at time of run
