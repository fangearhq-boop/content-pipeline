# Cubs Pipeline Status — Updated 2026-08-16

## Latest Run
- **Date:** 2026-08-16 (Sunday)
- **Run time:** ~09:00 UTC
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-16)
- **Snapshot generated:** 2026-08-16T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 124
- **Significant findings (1):**
  1. `has_score=False` beats `has_score=True` — **small** effect (Cliff's delta=0.31, p=0.0036, n=75 vs 49, median impressions 110 vs 82)
     - **Applied:** All 6 tweets drafted without final game scores. Game 2 recap leads with Báez's historic debut (3 HRs in first 3 ABs), not the 8-4 score. Game 3 preview leads with Cabrera's narrative arc, not team records. Cardinals jab tweet uses W-L records (62-61), not a game score.
- **Note vs yesterday:** Same single `has_score` finding. Dataset slightly smaller (124 vs 125) — likely measurement timing. Finding remains statistically robust (p=0.0036). No other dimensions cleared the significance gates.

## Series Context (2026-08-16)
- `is_series_start_today`: FALSE (mid-series, Game 3 of 3 vs Cardinals at Wrigley)
- `off_day`: FALSE — Cardinals at Cubs, 2:15 PM CT on ABC
- Series: Cubs (72-52) vs Cardinals (62-61), Game 3 (deciding) at Wrigley — tied 1-1
  - Game 1 (Aug 14): Cubs won (Holmes shutout, Suzuki 3-run HR)
  - Game 2 (Aug 15): Cardinals won 8-4 (Báez historic 3-HR debut)
  - Game 3 (Aug 16): Cabrera (returning from IL) vs Dobbins (stats conflicting — omitted from tweets)
- Applied: No dedicated series-preview slot. Báez recap + Cabrera return are the twin leads. Pre-game hype at 1:15 PM.

## Today's Content (2026-08-16)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Game 2 recap: Báez first-ever 3-HR debut in MLB history at Wrigley | 1 |
| 8:15 AM CT | Cabrera return / Game 3 preview: 9 scoreless rehab innings, series decider 2:15 PM ABC | 1 |
| 9:30 AM CT | PCA: 27 HR, 30 SB, MLB-best fWAR — 3 HRs from back-to-back 30-30 | 2 |
| 10:45 AM CT | Cardinals reality check: 62-61, sold deadline pieces, 3 GB from even Wild Card | 2 |
| 12:00 PM CT | Rotation depth: Horton/Miller TJ, Harvey 60-day IL — Cabrera's return is a September lifeline | 3 |
| 1:15 PM CT | Pre-game hype: series tied 1-1, Wrigley, ABC, 2:15 PM CT | 2 |

## Cubs Record as of 2026-08-16 (entering game)
- **Record:** 72-52 (No. 1 NL Wild Card)
- **NL WC gap:** ~6 games over Padres (66-57), ~7 over D-backs (65-58)
- **Brewers:** 75-48 (NL Central leaders, ~3.5 GB ahead of Cubs)
- **Cardinals:** 62-61 (3 GB from WC3; sold deadline pieces)

## Key Storylines to Watch
- **Today's game:** Cabrera vs Cardinals at Wrigley, 2:15 PM CT, ABC — series decider
- **PCA:** 27 HR, 30 SB — 3 HRs from back-to-back 30-30 milestone
- **Rotation depth:** Cabrera needs to hold up through September (Horton/Miller out for year)
- **Palencia:** Rehabbing; activation target mid-August — monitor
- **Harvey:** Threw bullpen Aug 15 in Arizona; return timeline still TBD
- **Cardinals:** Báez debuts; 62-61 club; 3 GB from Wild Card; sellers at deadline

## Pipeline Health (2026-08-16)
- JSON compiled: ✓ 07-content-data.json valid (schema 2.0, 6 stories, 6 X posts)
- Char count validation: ✓ All 6 posts under 280 chars (range: 218–279; compile script all clear)
- Review dashboard: ✓ Generated locally (review-dashboard.html)
- Dashboard push: ⚠ Skipped (content-dashboards repo not in session scope — expected behavior)
- Fact-check: ✓ 27 claims reviewed; lead claims confirmed by multiple primary sources; Dobbins stats omitted due to conflicting sources; distances cited as LOW confidence supporting detail
- Insights applied: ✓ 1 significant finding applied (has_score=False)
- Story history: ✓ Appended 6 stories to Cubs/story-history.md

## Prior Runs (recent)
| Date | Stories | X Posts | Notes |
|------|---------|---------|-------|
| 2026-08-16 | 6 | 6 | Báez historic 3-HR debut recap; Cabrera return/series decider; PCA 30-30; Cardinals check; rotation depth; pre-game hype; 1 insight applied |
| 2026-08-15 | 6 | 6 | Game 1 recap (Holmes shutout); Boyd preview; Cabrera return Sunday; PCA Bregman MVP; Cardinals roast; Cowles prospect; 1 insight applied |
| 2026-08-14 | 6 | 6 | Cardinals series start (Game 1 of 3); Nationals recap (Cavalli near no-hit); PCA 30-30; Bregman vs Liberatore; 4 insights applied |
| 2026-08-13 | 5 | 5 | Game 2 recap (71-50); Cardinals roast; PCA WAR 7.5; Gausman preview; sweep hype |
| 2026-08-12 | 6 | 6 | Game 1 recap (70-50 milestone); Suzuki 20 HR; June 10 run; WC watch; Peterson preview; hype |
| 2026-08-11 | 7 | 7 | Series start (Nationals); Imanaga streak; PCA MVP No. 1; Happ slump recovery; WC watch; matchup analysis; pre-game hype |
| 2026-08-10 | 8 | 8 | Off day; Boyd recap; PCA WAR milestone; rotation depth; Nationals preview; Cabrera watch; Cardinals roast; Happ; prospects |
| 2026-08-09 | 5 | 5 | Holmes recap; PCA solo MVP frontrunner; Wild Card; Bregman; Boyd preview |
| 2026-08-08 | 8 | 8 | Holmes debut day; Gausman recap; PCA/Bregman arcs; 2 insights applied |
