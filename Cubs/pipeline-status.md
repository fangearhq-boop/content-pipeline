# Cubs Pipeline Status — Updated 2026-09-13

## Latest Run
- **Date:** 2026-09-13 (Sunday — Game 3/finale of Cubs vs Pirates, Wrigley Field, 1:20 PM CT)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-09-13)
- **Snapshot generated:** 2026-09-13T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 115
- **significant_findings count:** 3
- **Finding 1 (strongest):** `opening=statement` LOSER — not_statement wins, Cliff's delta 0.252, p=0.025
  - **Applied:** All 5 tweet openers are stat leads or standings-data, not declarative statements. Examples: "Two solo shots off Skenes. Six strikeouts from Holmes." / "Cubs 83-66. Phillies 82-66." / "Matthew Boyd's ERA since returning from the IL: 2.08" / "Clay Holmes: 5⅔ innings, six strikeouts..."
- **Finding 2:** `has_score=False` WINNER — Cliff's delta 0.234, p=0.033
  - **Applied:** Game recap (Story 1) does NOT state "4-3" final score anywhere. Framed entirely through game events.
- **Finding 3:** `has_stat=True` WINNER — Cliff's delta 0.226, p=0.037
  - **Applied:** Every tweet contains at least one concrete stat (IP, ERA, K, record). Even the hype tweet has a game time.

## Series Context (2026-09-13)
- **`is_series_start_today`:** FALSE (mid-series / finale)
- **`off_day`:** FALSE
- **Opponent:** Pittsburgh Pirates (74-75)
- **Venue:** Wrigley Field
- **Game today:** Sept 13 (Game 3, series finale, 1:20 PM CT)
- **Action:** No series-preview slot. Morning recap + standings + preview + Holmes take + hype.

## Wild Card Status
- **Cubs position:** WC1 (lead Phillies by ~1 game)
- **Record:** 83-66
- **Games remaining:** ~15
- **Phillies:** ~82-66 (estimated; exact record not confirmed from primary source)
- **Cardinals:** Eliminated from playoff contention
- **Brewers:** NL Central champions (clinched)

## PCA 40-40 Watch
- **Current:** 41 HR / 36 SB
- **Target:** 40/40 — would be 7th player ever, first Cub ever
- **Games remaining:** ~15
- **4 SB needed**
- **Note:** No progress confirmed in Sept 12 game. Holding for next milestone.

## Swanson Return
- **Status:** Iowa rehab in progress this week
- **Target activation:** September 18 in Cincinnati
- **Injury:** Grade 2 left oblique (out since Aug 16)
- **Note:** Covered on 9/12; no new development on 9/13

## Wiggins Callup Note
- **Status:** NOT called up for September roster expansion
- **Cubs went with:** B.J. Murray (IF) and Tyler Ferguson (RHP)
- **Iowa form:** 8+ scoreless IP in bullpen since Aug 11, 10 K, 101 mph
- **Opportunity:** October playoff roster still in play; flag for future prospect-angle tweet

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
