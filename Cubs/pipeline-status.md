# Cubs Pipeline Status — Updated 2026-08-07

## Latest Run
- **Date:** 2026-08-07 (Friday)
- **Run time:** ~09:30 UTC
- **Stories:** 8
- **X posts:** 8
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-07)
- **Snapshot generated:** 2026-08-07T08:30:00Z (fresh)
- **Significant findings (2):**
  1. `opening=allcaps_lead` (winner: not_allcaps_lead) — medium effect (δ=0.393, p=0.0097)
     - n_winner=105 (not_allcaps_lead), n_loser=17 (allcaps_lead)
     - **Applied:** No tweet opens with an ALL CAPS word. Walk-off recap opens "Bregman with a two-out..." not "BREGMAN TIES IT..."; hype tweet opens "Gausman. Kauffman Stadium..." not "TONIGHT:..."
  2. `has_score=False` beats `has_score=True` — medium effect (δ=0.337, p=0.0015)
     - n_winner=69 (no score), n_loser=53 (with score)
     - **Applied:** Zero tweets include any game score. Walk-off recap leads with Bregman's shot and PCA's baserunning; "Cubs 3, Blue Jays 2" never appears.
- Both findings persist from prior days and strengthened. Both applied throughout all 8 tweets.

## Series Context (2026-08-07)
- `is_series_start_today`: TRUE — mandatory 7:00 AM series preview slot
- `off_day`: false
- 3-game road series: Cubs at Kansas City Royals, Kauffman Stadium
- Cubs (67-49) vs Royals (48-68)
- Kevin Gausman makes Cubs debut tonight (7:10 PM CT); Clay Holmes debuts Saturday
- Royals probable: TBD per snapshot
- 7:00 AM slot reserved for series preview per protocol

## Today's Content (2026-08-07)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Series Preview — Cubs at KC Royals (3-game road trip, Gausman debut) | 1 |
| 8:15 AM CT | Walk-Off Recap — Bregman 9th-inning HR + PCA steals game in 11th | 1 |
| 9:30 AM CT | Bregman Hot Streak (.370 avg, 1.082 OPS in last 11 games) | 2 |
| 10:45 AM CT | PCA MVP Watch (.333 last 15 games; 26 HR/28 SB/7.3 bWAR) | 2 |
| 12:00 PM CT | Gausman + Holmes Rotation Depth — Bold take | 1 |
| 1:15 PM CT | Wild Card Watch — Cubs 67-49, Cardinals below .500 | 2 |
| 2:30 PM CT | Cabrera Rehab (4 IP, 8 K, 0 BB, 97.4 mph; mid-Aug return on track) | 2 |
| 5:00 PM CT | Pre-Game Hype — Gausman debut at 7:10 PM CT | 1 |

## Pipeline Health (2026-08-07)
- JSON compiled: ✓ 07-content-data.json valid (schema 2.0, 8 stories, 8 X posts)
- Review dashboard: ✓ Generated locally
- Dashboard push: ⚠ Skipped (content-dashboards repo not in session scope)
- Fact-check: ✓ All compound claims cross-referenced; 1 claim hedged (PCA historical pace, single-source Yardbarker); PCA pace claim dropped from tweet copy
- Insights applied: ✓ not_allcaps_lead + has_score=False both enforced across all 8 tweets

## Prior Runs (recent)
| Date | Stories | X Posts | Notes |
|------|---------|---------|-------|
| 2026-08-07 | 8 | 8 | KC road trip opener; Gausman + Holmes debuts; 2 insights applied |
| 2026-08-06 | 7 | 7 | Blue Jays single game; PCA 25/25 milestone; 1 insight applied |
| 2026-08-05 | 7 | 7 | Dodgers sweep game 3; Imanaga wins; 2 insights applied |
| 2026-08-04 | 6 | 6 | Assad vs Skubal night game; 1 insight applied |
| 2026-08-03 | 6 | 6 | Series opener vs Dodgers; Boyd 7-1 |
