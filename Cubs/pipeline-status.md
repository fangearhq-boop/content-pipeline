# Cubs Pipeline Status — Updated 2026-09-06

## Latest Run
- **Date:** 2026-09-06 (Sunday — GAME DAY; Cubs at Miami Marlins, 12:40 PM CT, loanDepot park — Series finale, Game 3 of 3)
- **Run time:** ~09:00 UTC
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-06)
- **Snapshot generated:** 2026-09-06T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 121
- **significant_findings count:** 6
- **Finding 1 (strongest):** `posting_window=midday_12_18` wins — median 110 vs 78.5, Cliff's delta=0.311 (small), p=0.0033
  - **Applied:** Stories 4, 5, 6 placed in 1:15 PM, 2:30 PM, 3:45 PM CT (midday window)
- **Finding 2:** `posting_window=morning_06_12` loses — same test, inverse
  - **Applied:** Only 3 morning slots used (all editorially necessary: overnight recap, PCA follow-up, pre-noon game preview)
- **Finding 3:** `opening=stat_lead` wins — median 109.5 vs 84, Cliff's delta=0.277 (small), p=0.0427
  - **Applied:** ALL 6 tweets open with "Player: stat." or "Record — context." format
- **Finding 4:** `has_stat=True` wins — median 106 vs 79, Cliff's delta=0.275 (small), p=0.0102
  - **Applied:** Every tweet contains ≥2 concrete numerical stats
- **Finding 5:** `has_score=False` wins — median 105.5 vs 79, Cliff's delta=0.243 (small), p=0.0212
  - **Applied:** Game recap (Story 1) does NOT include the final score (6-5). Opens with player stats. Team record (81-62) included as season record, not game score.
- **Finding 6:** `opening=statement` loses — median 82 vs 109.5, Cliff's delta=0.234 (small), p=0.0427
  - **Applied:** No tweet opens with generic declarative statement. All open with player names or records.

## Series Context (2026-09-06)
- **`is_series_start_today`:** false (Game 3 of 3 vs Miami Marlins — series finale)
- **`off_day`:** false
- **Series:** Cubs (81-62) at Marlins (71-72); series finale today at 12:40 PM CT
- **Cubs lead series 2-0** (Sept 4: 6-1 W; Sept 5: 6-5 W)
- **Action:** No series-preview slot. Game recap at 7:00 AM + game preview at 11:00 AM (before 12:40 PM first pitch).

## Wild Card Status
- **Cubs position:** WC2 (Phillies WC1, Cubs WC2, Padres WC3)
- **Record:** 81-62
- **Games remaining:** ~18-19
- **Brewers lead NL Central:** 88-54 (7.5 GB ahead of Cubs in division)

## Previous Run — 2026-09-05
- **Stories:** 5 | **X posts:** 5 | **Status:** ✅ Complete
- **Insights:** 4 significant findings (has_score=False WINNER; midday WINNER; morning LOSER; has_stat WINNER)
- **Series context:** is_series_start_today=FALSE (Game 2 of 3 vs Miami)

## Previous Run — 2026-09-04
- **Stories:** 7 | **X posts:** 7 | **Status:** ✅ Complete
- **Insights:** 2 significant findings (opening=statement LOSER; has_stat=True WINNER)
- **Series context:** is_series_start_today=TRUE (3-game road series vs Miami, Game 1 of 3)
