# Cubs Pipeline Status — Updated 2026-08-14

## Latest Run
- **Date:** 2026-08-14 (Friday)
- **Run time:** ~09:00 UTC
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-14)
- **Snapshot generated:** 2026-08-14T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 126
- **Significant findings (4):**
  1. `has_score=False` beats `has_score=True` — **medium** effect (Cliff's delta=0.376, p=0.0004, n=79 vs 47, median impressions 123 vs 78)
     - **Applied:** All 6 tweets drafted without final game scores. Game recap leads with Cavalli's near no-hitter (a performance stat, not a score). Pre-game tweets use team W-L records (71-51 vs 61-60), which are standings records not game scores. H2H tweet uses win differential (10 more wins), not score.
  2. `posting_window=midday_12_18` wins — **small** effect (Cliff's delta=0.217, p=0.0426, median 123 vs 92)
     - **Applied:** Two of 6 slots placed in 12:00-18:00 CT window: 12:00 PM (pre-game hype) and 1:15 PM (H2H bold take). Both carry high-engagement rivalry content.
  3. `posting_window=morning_06_12` loses — **small** effect (Cliff's delta=0.217, p=0.0426, median 92 vs 123)
     - **Applied:** Morning slots (7 AM, 8:15 AM, 9:30 AM, 10:45 AM) used only for mandatory/time-sensitive content. Non-time-sensitive bold takes pushed to midday where possible.
  4. `has_stat=True` wins — **small** effect (Cliff's delta=0.21, p=0.0465, median 123 vs 93)
     - **Applied:** Every tweet includes at least one stat (ERAs, records, slash lines, RBIs, HR counts).

## Series Context (2026-08-14)
- `is_series_start_today`: TRUE (Game 1 of 3 vs Cardinals at Wrigley)
- `off_day`: FALSE — Cardinals at Cubs, 1:20 PM CT
- Series: Cubs (71-51) vs Cardinals (61-60), 3-game home series Aug 14-16, Wrigley Field
- Game 1: Clay Holmes vs Matthew Liberatore (5-9, 5.15 ERA), 1:20 PM CT, Apple TV+
- Applied: 7:00 AM slot reserved for mandatory series preview per STEP 0.5 rule. Yesterday's game recap moves to 8:15 AM.

## Today's Content (2026-08-14)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Cardinals series preview: Game 1 of 3, Holmes vs Liberatore, 1:20 PM CT | 1 |
| 8:15 AM CT | Nationals recap: Cavalli near no-hitter; Gausman 4.2 IP, 6 R; Cubs take series 2-1 | 1 |
| 9:30 AM CT | PCA: 30 SB, 27 HR, leads MLB in WAR, three HR from 30-30 | 2 |
| 10:45 AM CT | Bregman .394/.460/.788 since July 27, faces Liberatore (5.15 ERA) at Wrigley | 2 |
| 12:00 PM CT | Pre-game hype: Cubs 71-51 vs Cardinals 61-60, rivalry live at Wrigley | 2 |
| 1:15 PM CT | Bold take: Cardinals lead H2H 4-2 but Cubs have 10 more wins (only October matters) | 2 |

## Cubs Record as of 2026-08-14 (entering game)
- **Record:** 71-51 (No. 1 NL Wild Card)
- **NL WC cushion:** ~6-7 games over Padres (~65-57) and D-backs (~64-58)
- **Brewers:** 74-47 (NL Central leaders, ~3 GB ahead of Cubs)
- **Cardinals:** 61-60 (out of Wild Card picture; ~10 games behind Cubs in win column)
- **37-16+ since June 10**

## Key Storylines to Watch
- **Today's game:** Holmes vs Liberatore at Wrigley, 1:20 PM CT, Apple TV+
- **PCA:** 30 SB, 27 HR — three HR from 30-30; leads MLB in WAR; MVP odds -120 DraftKings
- **Bregman August tear:** .394/.460/.788 since July 27; Aug 12 career-best 3-HR/7-RBI game
- **Cardinals weekend series:** 3 games at Wrigley Aug 14-16 — H2H implications (currently Cardinals lead 4-2)
- **Holmes second Cubs start:** Coming off rusty debut (4 IP, 4 ER vs Royals); looking to settle in
- **Gausman:** Rough second Cubs start (4.2 IP, 6 ER) — monitor going forward
- **Palencia:** Rehab appearances at minors; expected return mid-August (not yet activated)
- **PCA 30th HR:** 3 away — milestone watch for next several games

## Pipeline Health (2026-08-14)
- JSON compiled: ✓ 07-content-data.json valid (schema 2.0, 6 stories, 6 X posts)
- Char count validation: ✓ All 6 posts under 280 chars (range: 222–257; compile script all clear)
- Review dashboard: ✓ Generated locally (review-dashboard.html)
- Dashboard push: ⚠ Skipped (content-dashboards repo not in session scope — expected)
- Fact-check: ✓ 25 claims reviewed; 12 HIGH confidence, 10 MEDIUM; 0 claims rejected
- Insights applied: ✓ All 4 significant findings applied (has_score=False; midday wins; morning loses; has_stat=True)
- Story history: ✓ Appended 6 stories to Cubs/story-history.md

## Prior Runs (recent)
| Date | Stories | X Posts | Notes |
|------|---------|---------|-------|
| 2026-08-14 | 6 | 6 | Cardinals series start (Game 1 of 3); Nationals recap (Cavalli near no-hit); PCA 30-30; Bregman vs Liberatore; 4 insights applied |
| 2026-08-13 | 5 | 5 | Game 2 recap (71-50); Cardinals roast; PCA WAR 7.5; Gausman preview; sweep hype |
| 2026-08-12 | 6 | 6 | Game 1 recap (70-50 milestone); Suzuki 20 HR; June 10 run; WC watch; Peterson preview; hype |
| 2026-08-11 | 7 | 7 | Series start (Nationals); Imanaga streak; PCA MVP #1; Happ slump recovery; WC watch; matchup analysis; pre-game hype |
| 2026-08-10 | 8 | 8 | Off day; Boyd recap; PCA WAR milestone; rotation depth; Nationals preview; Cabrera watch; Cardinals roast; Happ; prospects |
| 2026-08-09 | 5 | 5 | Holmes recap; PCA solo MVP frontrunner; Wild Card; Bregman; Boyd preview |
| 2026-08-08 | 8 | 8 | Holmes debut day; Gausman recap; PCA/Bregman arcs; 2 insights applied |
| 2026-08-07 | 8 | 8 | KC road trip opener; Gausman + Holmes debuts; 2 insights applied |
