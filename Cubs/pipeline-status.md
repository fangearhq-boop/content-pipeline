# Cubs Pipeline Status — Updated 2026-09-05

## Latest Run
- **Date:** 2026-09-05 (Saturday — GAME DAY; Cubs at Miami Marlins, 3:10 PM CT, loanDepot park — Game 2 of 3)
- **Run time:** ~09:00 UTC
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-05)
- **Snapshot generated:** 2026-09-05T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 123
- **significant_findings count:** 4
- **Finding 1 (strongest):** `has_score=False` beats `has_score=True` — median 105.5 vs 79, Cliff's delta=0.291 (small), p=0.005, n=64/59.
  - **Applied:** All 5 tweets lead with player stats, standings, or narratives — not final scores. The game recap opens with Imanaga's pitching line.
- **Finding 2:** `posting_window=midday_12_18` wins — median 104 vs 79, Cliff's delta=0.225 (small), p=0.033.
  - **Applied:** 4 of 5 posts (Stories 2-5) scheduled in the 12:00–3:45 PM CT window.
- **Finding 3:** `posting_window=morning_06_12` loses — same test, inverse.
  - **Applied:** Only 1 morning slot used (7:00 AM game recap, time-sensitive purpose). Morning slots 8:15, 9:30, 10:45 all skipped.
- **Finding 4:** `has_stat=True` beats `has_stat=False` — median 104 vs 80, Cliff's delta=0.211 (small), p=0.049.
  - **Applied:** Every tweet contains ≥1 concrete numeric stat.

## Series Context (2026-09-05)
- **`is_series_start_today`:** false (Game 2 of 3 vs Miami Marlins at loanDepot park)
- **Series:** Cubs (80-62) at Marlins (71-71); 2 games remaining (Sept 5 + 6)
- **Action:** No series-preview slot reserved. Standard content slate.

## Wild Card Status
- **Cubs position:** WC1 (moved up from WC2 after Friday's 6-1 win at Miami)
- **Record:** 80-62
- **Games remaining:** 20

## Previous Run — 2026-09-04
- **Stories:** 7 | **X posts:** 7 | **Status:** ✅ Complete
- **Insights:** 2 significant findings (opening=statement LOSER; has_stat=True WINNER)
- **Series context:** is_series_start_today=TRUE (3-game road series vs Miami, Game 1 of 3)
