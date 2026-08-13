# Cubs Pipeline Status — Updated 2026-08-13

## Latest Run
- **Date:** 2026-08-13 (Thursday)
- **Run time:** ~09:00 UTC
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-13)
- **Snapshot generated:** 2026-08-13T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 127 (same as yesterday; game-monitor likely hasn't updated overnight yet)
- **Significant findings (1):**
  1. `has_score=False` beats `has_score=True` — **medium** effect (Cliff's delta=0.409, p=0.0001, n=80 vs 47, median impressions 124 vs 78)
     - **Applied:** All 5 tweets drafted without final game scores. Game 2 recap leads with "Bregman and Swanson went to work" not "Cubs won 12-6." Cardinals tweet uses "59-59" and "71-50" (team W-L records, not game scores). No game scores in any tweet.
     - Note: Effect size increased from 0.348 (Aug 12) to 0.409 (Aug 13) as sample distribution shifts. Signal is strong and consistent.
- `significant_findings_note`: null — single finding cleared all three gates. No other contrasts significant.

## Series Context (2026-08-13)
- `is_series_start_today`: FALSE (mid-series, Game 3 of 3)
- `off_day`: FALSE — Cubs at Washington Nationals, 3:05 PM CT
- Series: Series finale (3-game road trip at Nationals Park, Aug 11-13). Cubs lead series 2-0.
- Game 3: Kevin Gausman vs Cade Cavalli, 3:05 PM CT
- Applied: No mandatory series-preview slot. 7:00 AM = Game 2 recap (highest priority). Sweep angle embedded in game preview and hype tweets.

## Today's Content (2026-08-13)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Game 2 recap: Cubs offense dominant; Bregman/Swanson/Peterson/Webb; Cubs 71-50 | 1 |
| 8:15 AM CT | Cardinals at .500 (59-59) while Cubs are 71-50; sharp rivalry roast | 2 |
| 9:30 AM CT | PCA: WAR 7.5 MLB-best; DraftKings -120; All-Star break +700 → now -120 | 2 |
| 12:00 PM CT | Game 3 preview: Gausman vs Cavalli, 3:05 PM CT; sweep on the line | 1 |
| 1:15 PM CT | Pre-game hype: two wins in series, sweep momentum | 2 |

## Cubs Record as of 2026-08-13 (entering game)
- **Record:** 71-50 (No. 1 NL Wild Card)
- **NL WC cushion:** ~7 games over D-backs and Padres (both ~64-57)
- **Brewers:** 74-47 (NL Central leaders, 3 GB ahead of Cubs)
- **Cardinals:** 59-59 (out of contention, ~15 GB back in division)
- **37-16 since June 10**

## Key Storylines to Watch
- **Tonight's game:** Gausman vs Cavalli at Nationals Park, 3:05 PM CT (series finale — sweep possible)
- **Tomorrow:** Cubs vs Cardinals? Check schedule — Aug 14 homestand could be rivalry series
- **PCA MVP:** WAR 7.5 (MLB No. 1), DraftKings -120 — 30 HR milestone watch (at 26)
- **Bregman August hot streak:** Continued dominance in D.C. — track through month
- **Gausman's role:** First start as a Cub (acquired at deadline); monitor performance
- **Cade Horton:** Out 15-16 months (UCL revision); no return timeline this season
- **Daniel Palencia:** Expected back mid-August from 15-day IL (right elbow)

## Pipeline Health (2026-08-13)
- JSON compiled: ✓ 07-content-data.json valid (schema 2.0, 5 stories, 5 X posts)
- Char count validation: ✓ All 5 posts under 280 chars (range: 235–271; compile script all clear)
- Review dashboard: ✓ Generated locally (review-dashboard.html)
- Dashboard push: ⚠ Skipped (content-dashboards repo not in session scope — expected)
- Fact-check: ✓ 16 claims reviewed; Bregman specific-HR-count claim (LOW) excluded; compound WAR claim two-source verified (SI + Covers)
- Insights applied: ✓ has_score=False enforced across all 5 tweets (Cliff's delta=0.409, strongest signal yet)
- Story history: ✓ Appended 5 stories to Cubs/story-history.md

## Prior Runs (recent)
| Date | Stories | X Posts | Notes |
|------|---------|---------|-------|
| 2026-08-13 | 5 | 5 | Game 2 recap (71-50); Cardinals roast; PCA WAR 7.5; Gausman preview; sweep hype |
| 2026-08-12 | 6 | 6 | Game 1 recap (70-50 milestone); Suzuki 20 HR; June 10 run; WC watch; Peterson preview; hype |
| 2026-08-11 | 7 | 7 | Series start (Nationals); Imanaga streak; PCA MVP #1; Happ slump recovery; WC watch; matchup analysis; pre-game hype |
| 2026-08-10 | 8 | 8 | Off day; Boyd recap; PCA WAR milestone; rotation depth; Nationals preview; Cabrera watch; Cardinals roast; Happ; prospects |
| 2026-08-09 | 5 | 5 | Holmes recap; PCA solo MVP frontrunner; Wild Card; Bregman; Boyd preview |
| 2026-08-08 | 8 | 8 | Holmes debut day; Gausman recap; PCA/Bregman arcs; 2 insights applied |
| 2026-08-07 | 8 | 8 | KC road trip opener; Gausman + Holmes debuts; 2 insights applied |
| 2026-08-06 | 7 | 7 | Blue Jays single game; PCA 25/25 milestone; 1 insight applied |
