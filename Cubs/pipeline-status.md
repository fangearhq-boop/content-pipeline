# Cubs Pipeline Status — Updated 2026-09-10

## Latest Run
- **Date:** 2026-09-10 (Thursday — OFF DAY; Cubs swept 3-0 by Brewers on Sept 7-9)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-10)
- **Snapshot generated:** 2026-09-10T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 116
- **significant_findings count:** 3
- **Finding 1 (strongest):** `has_score=False` wins — median 110 vs 75.5, Cliff's delta=0.282 (small), p=0.0094
  - **Applied:** No final scores embedded in any tweet body. Sweep reaction uses narrative framing (three HRs, bullpen rally) not "Brewers 8, Cubs 6."
- **Finding 2:** `posting_window=midday_12_18` wins — median 107 vs 76.5, Cliff's delta=0.229 (small), p=0.0338
  - **Applied:** 4 of 5 posts in 12:00–5:00 PM window. Only 7:00 AM post (off-day lead story, purpose-required).
- **Finding 3:** `posting_window=morning_06_12` loses — mirror of Finding 2
  - **Applied:** Only one morning post (7:00 AM — off-day sweep reaction; mandatory Tier 1). No 8:15 AM or 9:30 AM slots used.
- **Note:** Down from 5 findings yesterday (2026-09-09) to 3 today. Likely due to overlap in the midday/morning findings being the same contrast.

## Series Context (2026-09-10)
- **`is_series_start_today`:** FALSE
- **`off_day`:** TRUE
- **Action:** Series-preview 7:00 AM slot NOT reserved. Lead with sweep recap; lean into prospects, standings, upcoming home stand.
- **Next series:** Pittsburgh Pirates at Wrigley Field, September 11-13, 1:20 PM CT

## Wild Card Status
- **Cubs position:** WC2 (0.5 GB behind Phillies WC1)
- **Record:** 81-66
- **Games remaining:** 15
- **Brewers NL Central lead:** 10.0 GB (91-56 vs 81-66)

## Dashboard
- review-dashboard.html: ✅ Generated
- publish-unified-dashboard.py: ❌ Push to fangearhq-boop/content-dashboards blocked (not in session's authorized repo set — only content-pipeline authorized)

## Previous Run — 2026-09-09
- **Stories:** 6 | **X posts:** 6 | **Status:** ✅ Complete
- **Insights:** 5 significant findings (has_score=False WINNER; opening=not_statement WINNER; midday WINNER; morning LOSER; has_stat WINNER)
- **Series context:** is_series_start_today=FALSE (Game 3 of 3-game road series at Milwaukee)

## Previous Run — 2026-09-08
- **Stories:** 6 | **X posts:** 6 | **Status:** ✅ Complete
- **Insights:** 5 significant findings (midday WINNER; morning LOSER; has_score=False WINNER; has_stat WINNER; opening=statement LOSER)
- **Series context:** is_series_start_today=FALSE (Game 2 of 3-game road series at Milwaukee)

## Previous Run — 2026-09-07
- **Stories:** 6 | **X posts:** 6 | **Status:** ✅ Complete
- **Insights:** 4 significant findings (midday WINNER; morning LOSER; has_stat WINNER; has_score=False WINNER)
- **Series context:** is_series_start_today=TRUE (3-game road series vs Milwaukee, Game 1 of 3)

## Previous Run — 2026-09-06
- **Stories:** 5 | **X posts:** 5 | **Status:** ✅ Complete
- **Insights:** 4 significant findings (has_score=False WINNER; midday WINNER; morning LOSER; has_stat WINNER)
- **Series context:** is_series_start_today=FALSE (Game 2 of 3 vs Miami)

## Previous Run — 2026-09-04
- **Stories:** 7 | **X posts:** 7 | **Status:** ✅ Complete
- **Insights:** 2 significant findings (opening=statement LOSER; has_stat=True WINNER)
- **Series context:** is_series_start_today=TRUE (3-game road series vs Miami, Game 1 of 3)
