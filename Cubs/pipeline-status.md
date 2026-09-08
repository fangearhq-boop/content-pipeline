# Cubs Pipeline Status — Updated 2026-09-08

## Latest Run
- **Date:** 2026-09-08 (Tuesday — GAME DAY; Cubs at Milwaukee Brewers, 6:40 PM CT, American Family Field — Game 2 of 3-game road series)
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-08)
- **Snapshot generated:** 2026-09-08T08:30:00Z (fresh, 30 min before trigger)
- **significant_findings count:** 5
- **Finding 1 (strongest):** `posting_window=midday_12_18` wins — median 111 vs 73.5, Cliff's delta=0.311 (small), p=0.0038
  - **Applied:** 5 of 6 posts placed in 12:00–5:00 PM CT window; only required 7 AM recap slot in morning window
- **Finding 2:** `posting_window=morning_06_12` loses — same test, inverse (loser = morning)
  - **Applied:** Eliminated 8:15 AM, 9:30 AM, 10:45 AM slots entirely
- **Finding 3:** `has_score=False` wins — median 108 vs 79, Cliff's delta=0.274 (small), p=0.0107
  - **Applied:** Recap tweet de-emphasizes score (narrative-first opening); score appears only as mid-tweet context. All other tweets score-free.
- **Finding 4:** `has_stat=True` wins — median 106 vs 79, Cliff's delta=0.264 (small), p=0.0142
  - **Applied:** All 6 tweets contain concrete numerical stats (ERA, HR/SB totals, rehab stats, standings records)
- **Finding 5:** `opening=statement` loses — median 79 vs 112 (not_statement wins), Cliff's delta=0.24 (small), p=0.0361
  - **Applied:** All 6 tweets use stat_lead or event_lead opening style. No flat declarative statement openings.

## Series Context (2026-09-08)
- **`is_series_start_today`:** FALSE (mid-series — Game 2 of 3-game road series at Milwaukee)
- **`off_day`:** false
- **Series:** Cubs (81-64) at Brewers (89-56), American Family Field, Game 2 tonight (6:40 PM CT)
- **Action:** No dedicated Series Preview slot reserved (not a series opener). Game recap + game preview cover the series narrative.

## Wild Card Status
- **Cubs position:** WC1
- **Record:** 81-64
- **Games remaining:** 17
- **Brewers lead NL Central:** 89-56

## Dashboard
- review-dashboard.html: ✅ Generated
- publish-unified-dashboard.py: ❌ Push to fangearhq-boop/content-dashboards blocked (not in session's authorized repo set — only content-pipeline authorized)

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
