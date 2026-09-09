# Cubs Pipeline Status — Updated 2026-09-09

## Latest Run
- **Date:** 2026-09-09 (Wednesday — GAME DAY; Cubs at Milwaukee Brewers, 6:40 PM CT, American Family Field — Game 3 of 3-game road series)
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-09)
- **Snapshot generated:** 2026-09-09T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 116
- **significant_findings count:** 5
- **Finding 1 (strongest):** `has_score=False` wins — median 107 vs 79, Cliff's delta=0.268 (small), p=0.0129
  - **Applied:** No scores as opening hooks. Recap tweet opens with the dramatic play (Chourio HR), not "Brewers 4, Cubs 3."
- **Finding 2:** `opening=not_statement` wins — median 115 vs 79, Cliff's delta=0.227 (small), p=0.0466
  - **Applied:** All 6 tweets use stat_lead or allcaps_lead opening. Zero plain statement openers.
- **Finding 3:** `posting_window=midday_12_18` wins — median 107 vs 79, Cliff's delta=0.224 (small), p=0.0378
  - **Applied:** 4 of 6 posts in 12:00–6:30 PM window; only required 7 AM recap post is morning.
- **Finding 4:** `posting_window=morning_06_12` loses — same delta/p as Finding 3 (inverse)
  - **Applied:** Eliminated all optional morning slots. Only 7:00 AM game recap (mandatory Tier 1).
- **Finding 5:** `has_stat=True` wins — median 106 vs 79, Cliff's delta=0.223 (small), p=0.0391
  - **Applied:** All 6 tweets include at least one concrete stat.

## Series Context (2026-09-09)
- **`is_series_start_today`:** FALSE (mid-series — Game 3 of 3-game road series at Milwaukee)
- **`off_day`:** false
- **Series:** Cubs (81-65) at Brewers (90-56), American Family Field, Game 3 tonight (6:40 PM CT)
- **Action:** No dedicated Series Preview slot. Game 2 recap + Game 3 preview cover the series narrative.
- **Series result:** Cubs 0-2; must win tonight to avoid sweep.

## Wild Card Status
- **Cubs position:** WC1 (approx. — slight degradation after two series losses)
- **Record:** 81-65
- **Games remaining:** 16
- **Brewers NL Central lead:** 90-56

## Dashboard
- review-dashboard.html: ✅ Generated
- publish-unified-dashboard.py: ❌ Push to fangearhq-boop/content-dashboards blocked (not in session's authorized repo set — only content-pipeline authorized)

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
