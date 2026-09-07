# Cubs Pipeline Status — Updated 2026-09-07

## Latest Run
- **Date:** 2026-09-07 (Monday — GAME DAY; Cubs at Milwaukee Brewers, 1:10 PM CT, American Family Field — Series opener, Game 1 of 3)
- **Run time:** ~09:18 UTC- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-07)
- **Snapshot generated:** 2026-09-07T08:30:00Z (fresh, 30 min before trigger)
- **significant_findings count:** 4
- **Finding 1 (strongest):** `posting_window=midday_12_18` wins — median 110.5 vs 79, Cliff's delta=0.281 (small), p=0.0085
  - **Applied:** 5 of 6 posts placed in 12-5 PM CT window; only required 7 AM series-preview slot in morning window
- **Finding 2:** `posting_window=morning_06_12` loses — same test, inverse (loser = morning)
  - **Applied:** Eliminated 8:15 AM, 9:30 AM, 10:45 AM slots entirely
- **Finding 3:** `has_stat=True` wins — median 106 vs 79, Cliff's delta=0.255 (small), p=0.0175
  - **Applied:** All 6 tweets contain concrete numerical stats (ERA, HR/SB totals, records, standings gaps)
- **Finding 4:** `has_score=False` wins — median 109 vs 79, Cliff's delta=0.244 (small), p=0.0218
  - **Applied:** No game scores in any tweet. PCA milestone tweet leads with HR count + footage, not the 10-3 final score.

## Series Context (2026-09-07)
- **`is_series_start_today`:** TRUE
- **`off_day`:** false
- **Series:** Cubs (81-63) at Brewers (88-56), American Family Field, 3-game road series (Sept 7-9)
- **Action:** RESERVED 7:00 AM CT slot for Series Preview per pipeline rule

## Wild Card Status
- **Cubs position:** WC2 (Phillies WC1, Cubs WC2, Padres WC3)
- **Record:** 81-63
- **Games remaining:** 18
- **Brewers lead NL Central:** 88-56 (7.0 GB ahead of Cubs in division)
- **Cushion:** 5.0 games ahead of WC3 (Padres)

## Dashboard
- review-dashboard.html: ✅ Generated
- publish-unified-dashboard.py: ❌ Push to fangearhq-boop/content-dashboards blocked (not in session's authorized repo set — only content-pipeline authorized)

## Previous Run — 2026-09-06
- **Stories:** 5 | **X posts:** 5 | **Status:** ✅ Complete
- **Insights:** 4 significant findings (has_score=False WINNER; midday WINNER; morning LOSER; has_stat WINNER)
- **Series context:** is_series_start_today=FALSE (Game 2 of 3 vs Miami)
## Previous Run — 2026-09-04
- **Stories:** 7 | **X posts:** 7 | **Status:** ✅ Complete
- **Insights:** 2 significant findings (opening=statement LOSER; has_stat=True WINNER)
- **Series context:** is_series_start_today=TRUE (3-game road series vs Miami, Game 1 of 3)
