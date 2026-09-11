# Cubs Pipeline Status — Updated 2026-09-11

## Latest Run
- **Date:** 2026-09-11 (Friday — is_series_start_today=TRUE; Cubs host Pirates 3-game series at Wrigley)
- **Stories:** 7
- **X posts:** 7
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-11)
- **Snapshot generated:** 2026-09-11T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 114
- **significant_findings count:** 1 (down from 3 yesterday)
- **Finding 1:** `has_score=False` wins — median 110 vs 72, Cliff's delta=0.271 (small), p=0.0135
  - **Applied:** No tweets lead with scores. All 7 posts use player name, stat framing, or stakes setup as the opener. Preview tweets are naturally score-free.
- **Note:** Only 1 finding passed the significance gates today. Midday/morning window findings from prior days are no longer clearing (likely lost significance as window shifted). Raw buckets show stat_lead and allcaps_lead openings with higher impressions but those did NOT clear the significance gate — not acted on.

## Series Context (2026-09-11)
- **`is_series_start_today`:** TRUE
- **`off_day`:** FALSE
- **Opponent:** Pittsburgh Pirates (74-73)
- **Venue:** Wrigley Field
- **Games:** Sept 11-13, all 1:20 PM CT
- **Action:** 7:00 AM slot reserved for series preview (mandatory rule). Followed the rule.

## Wild Card Status
- **Cubs position:** WC2 (1.5 GB behind Phillies WC1)
- **Record:** 81-66
- **Games remaining:** ~17
- **Magic number to clinch any WC:** 12
- **Brewers NL Central lead:** 10.0 GB (91-56 vs 81-66)

## Dashboard
- review-dashboard.html: ✅ Generated
- 07-content-data.json: ✅ Compiled (7 stories, 7 X posts, all under 280 chars)
- publish-unified-dashboard.py: ❌ Push to fangearhq-boop/content-dashboards blocked (not in session's authorized repo set — only content-pipeline authorized). Expected — same as yesterday.

## Previous Run — 2026-09-10
- **Stories:** 5 | **X posts:** 5 | **Status:** ✅ Complete
- **Insights:** 3 significant findings (has_score=False WINNER; posting_window=midday WINNER; morning LOSER)
- **Series context:** is_series_start_today=FALSE (off day)

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
