# Cubs Pipeline Status — Updated 2026-08-29

## Latest Run
- **Date:** 2026-08-29 (Saturday — GAME DAY; Cubs vs Reds Game 2 of 2, 1:20 PM CT, Wrigley Field)
- **Run time:** ~09:00 UTC
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-29)
- **Snapshot generated:** 2026-08-29T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 124
- **significant_findings count:** 2
- **Finding 1 (strongest):** `has_stat=True` beats `has_stat=False` — median impressions 109 vs 82, Cliff's delta=0.308 (small), p=0.0038
- **Finding 2:** `has_score=False` beats `has_score=True` — median impressions 101 vs 79, Cliff's delta=0.256 (small), p=0.0155
- **Applied:** (1) Every tweet contains ≥1 concrete numeric stat (ERAs, innings, HRs, SBs, WAR, W-L records). (2) No raw game scores in any tweet — lead with performance stats instead.
- **Notes:** Both findings stable vs Aug 28 readings; effect sizes consistent. `has_stat` overtook `has_score` as the stronger signal this cycle.

## Series Context (2026-08-29)
- `is_series_start_today`: FALSE (mid-series, Game 2 of 2 with Reds)
- `off_day`: FALSE — Cubs vs Reds Game 2, 1:20 PM CT, Wrigley Field
- `series`: Reds (64-71) at Cubs (76-59), 2 games (Aug 29-30)
- `rationale`: "Same opponent (Cincinnati Reds) as yesterday — mid-series, not a series opener."
- Applied: No series-preview slot reserved. 12:00 PM game preview slot used for Game 2 matchup coverage. No post-game slots (day game ends ~4-4:30 PM CT; pipeline pre-schedules and cannot predict result).

## Today's Content (2026-08-29)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Thornton collapse recap — 5 ER in 0.2 IP, Game 1 loss | 1 |
| 8:15 AM CT | Bullpen red flag — October concern, Wiggins callup case | 2 |
| 9:30 AM CT | PCA MVP Watch — .279/32 HR/31 SB, 7.9 bWAR (leads MLB) | 2 |
| 10:45 AM CT | Wild Card Watch — Cubs 76-59 WC1, Cardinals 67-68 fading | 2 |
| 12:00 PM CT | Game 2 preview — Gausman (7 IP/0 ER last start) vs Abbott (4.15 ERA) | 1 |
| 2:30 PM CT | Matt Shaw activation — back from 10-day IL, stretch run depth | 2 |

## Previous Run (2026-08-28)
- Stories: 6 | X posts: 6 | Status: ✅ Complete
- Insights: has_score=False + has_stat=True (both found again)
- Key content: Series preview (Reds at Wrigley), Peterson/Lowder matchup, Wild Card standings, PCA MVP, Swanson IL update, Wiggins prospect

## Previous Run (2026-08-27)
- Stories: 6 | X posts: 6 | Status: ✅ Complete
- Key content: D-backs series recap (1-2 loss), Swanson oblique injury, PCA MVP, Wild Card standings, Reds series preview

## Recurring Follow-Ups Queued
- Gausman Game 2 result → recap Monday 7:00 AM
- Wiggins September callup watch (expansion opens Sept 1)
- Alcántara return watch (expansion Sept 1)
- PCA 33rd HR milestone
- Cardinals WC elimination watch
- Cubs WC clinch magic number tracking
- Bullpen ERA tracking through September

## Pipeline Notes
- Unified dashboard push to content-dashboards repo: blocked (not in session scope — expected). Dashboard HTML compiled locally at Cubs/cubs-content-2026-08-29/review-dashboard.html.
- `Cubs/_data/` not modified (managed by game-monitor).
