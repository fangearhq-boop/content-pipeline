# Cubs Pipeline Status — Updated 2026-08-15

## Latest Run
- **Date:** 2026-08-15 (Saturday)
- **Run time:** ~09:20 UTC
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-15)
- **Snapshot generated:** 2026-08-15T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 125
- **Significant findings (1):**
  1. `has_score=False` beats `has_score=True` — **small** effect (Cliff's delta=0.324, p=0.0022, n=75 vs 50, median impressions 112 vs 81.5)
     - **Applied:** All 6 tweets drafted without final game scores. Recap leads with Holmes/Suzuki performance narrative, not "Cubs 3, Cardinals 0." Cardinals standings tweet uses W-L records (61-61), not a game score.
- **Note vs yesterday:** Yesterday's snapshot had 4 significant findings (has_score, posting_window wins/loses, has_stat). Today's snapshot has 1 finding only. Likely reflects dataset fluctuation at n=125 tweets. Posting slots retained from brand-voice defaults; `has_stat` guidance removed from decisions since it did not clear today's gates.

## Series Context (2026-08-15)
- `is_series_start_today`: FALSE (mid-series, Game 2 of 3 vs Cardinals at Wrigley)
- `off_day`: FALSE — Cardinals at Cubs, 1:20 PM CT
- Series: Cubs (72-51) vs Cardinals (61-61), Game 2 of 3 at Wrigley (Cubs lead 1-0 after Friday shutout)
- Game 2: Boyd (8-1) vs McGreevy (4-9, 5.68 xERA), 1:20 PM CT
- Game 3 (Aug 16): Cabrera (returning from IL) vs TBD, 2:15 PM CT
- Applied: No dedicated series-preview slot (mid-series). Boyd matchup angle covers the preview.

## Today's Content (2026-08-15)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Game 1 recap: Holmes shutout, Suzuki 3-run HR, Cubs take series lead | 1 |
| 8:15 AM CT | Game 2 preview: Boyd 2.35 ERA L7 vs McGreevy 5.68 xERA, 1:20 PM CT | 1 |
| 9:30 AM CT | Cabrera off IL to start Sunday: 5 hitless IP rehab, replaces Imanaga slot | 2 |
| 10:45 AM CT | PCA: 30 SB, 27 HR, 3 from 30-30; Bregman "I think Pete should win MVP" | 2 |
| 12:00 PM CT | Cardinals roast: 61-61, 7 GB out of Wild Card, Cubs lead season series 6-5 | 2 |
| 3:45 PM CT | Prospect: Cowles 2 HR / 4 RBI for Iowa; Palencia rehabbing; pipeline depth | 3 |

## Cubs Record as of 2026-08-15 (entering game)
- **Record:** 72-51 (No. 1 NL Wild Card)
- **NL WC cushion:** ~7 games over Padres (65-57) and Phillies (65-58)
- **Brewers:** 75-47 (NL Central leaders, ~3 GB ahead of Cubs)
- **Cardinals:** 61-61 (7+ GB out of Wild Card; Cubs lead season series 6-5)

## Key Storylines to Watch
- **Today's game:** Boyd vs McGreevy at Wrigley, 1:20 PM CT
- **Sunday's game:** Cabrera vs TBD at Wrigley, 2:15 PM CT (Cabrera returning from IL)
- **PCA:** 30 SB done, 27 HR — 3 HRs from 30-30 milestone
- **Cardinals series:** Cubs lead 1-0 after Friday shutout; can take series Saturday and sweep Sunday
- **Holmes:** Excellent in Game 1 shutout (career debut at Wrigley went much better than KC start)
- **Gausman:** Still monitoring after Aug 13 rough outing (4.2 IP, 6 ER) — not in this weekend's rotation

## Pipeline Health (2026-08-15)
- JSON compiled: ✓ 07-content-data.json valid (schema 2.0, 6 stories, 6 X posts)
- Char count validation: ✓ All 6 posts under 280 chars (range: 231–271; compile script all clear)
- Review dashboard: ✓ Generated locally (review-dashboard.html)
- Dashboard push: ⚠ Skipped (content-dashboards repo not in session scope — expected)
- Fact-check: ✓ 29 claims reviewed; 17 HIGH confidence, 9 MEDIUM, 3 LOW/not used; 0 claims rejected; 1 compound claim (PCA 30-30 "back-to-back") hedged appropriately
- Insights applied: ✓ 1 significant finding applied (has_score=False); 3 findings from yesterday dropped (did not clear gates in today's snapshot)
- Story history: ✓ Appended 6 stories to Cubs/story-history.md

## Prior Runs (recent)
| Date | Stories | X Posts | Notes |
|------|---------|---------|-------|
| 2026-08-15 | 6 | 6 | Game 1 recap (Holmes shutout); Boyd preview; Cabrera return Sunday; PCA Bregman MVP; Cardinals roast; Cowles prospect; 1 insight applied |
| 2026-08-14 | 6 | 6 | Cardinals series start (Game 1 of 3); Nationals recap (Cavalli near no-hit); PCA 30-30; Bregman vs Liberatore; 4 insights applied |
| 2026-08-13 | 5 | 5 | Game 2 recap (71-50); Cardinals roast; PCA WAR 7.5; Gausman preview; sweep hype |
| 2026-08-12 | 6 | 6 | Game 1 recap (70-50 milestone); Suzuki 20 HR; June 10 run; WC watch; Peterson preview; hype |
| 2026-08-11 | 7 | 7 | Series start (Nationals); Imanaga streak; PCA MVP #1; Happ slump recovery; WC watch; matchup analysis; pre-game hype |
| 2026-08-10 | 8 | 8 | Off day; Boyd recap; PCA WAR milestone; rotation depth; Nationals preview; Cabrera watch; Cardinals roast; Happ; prospects |
| 2026-08-09 | 5 | 5 | Holmes recap; PCA solo MVP frontrunner; Wild Card; Bregman; Boyd preview |
| 2026-08-08 | 8 | 8 | Holmes debut day; Gausman recap; PCA/Bregman arcs; 2 insights applied |
