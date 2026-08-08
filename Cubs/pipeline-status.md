# Cubs Pipeline Status — Updated 2026-08-08

## Latest Run
- **Date:** 2026-08-08 (Saturday)
- **Run time:** ~09:00 UTC
- **Stories:** 8
- **X posts:** 8
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-08)
- **Snapshot generated:** 2026-08-08T08:30:00Z (fresh)
- **Significant findings (2):**
  1. `opening=allcaps_lead` (winner: not_allcaps_lead) — medium effect (δ=0.332, p=0.0288)
     - n_winner=107 (not_allcaps_lead), n_loser=17 (allcaps_lead)
     - **Applied:** No tweet opens with an ALL CAPS word. Gausman recap opens "Kevin Gausman looked every bit..."; Holmes hype opens "Clay Holmes. Kauffman Stadium..."
  2. `has_score=False` beats `has_score=True` — small-to-medium effect (δ=0.316, p=0.0028)
     - n_winner=72 (no score), n_loser=52 (with score)
     - **Applied:** Zero tweets include any game score. Gausman recap uses his pitching line (7 IP, 2 ER) rather than "Cubs 6, Royals 4." Cardinals roast uses season record (54-57) which is a standings figure, not a game score.
- Both findings consistent with prior days and applied throughout all 8 tweets.

## Series Context (2026-08-08)
- `is_series_start_today`: FALSE (mid-series, Game 2 of 3)
- `off_day`: false
- Series: Cubs at Kansas City Royals (3 games, Aug 7-9), Kauffman Stadium
- Cubs (68-49) vs Royals (48-69)
- Yesterday: Cubs won (Gausman debut, 7 IP)
- Today: 6:10 PM CT — Clay Holmes makes his Cubs debut vs Seth Lugo
- No series-preview slot required today; led with Gausman recap at 7:00 AM

## Today's Content (2026-08-08)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Gausman debut recap (7 IP, 2 ER, 5th straight W) | 1 |
| 8:15 AM CT | PCA MVP Watch (tied at -110 with Ohtani; on pace for 30-30) | 2 |
| 9:30 AM CT | Bregman hot streak (.314 BA, 4 HR, 11 RBI in last 12 games) | 2 |
| 10:45 AM CT | Wild Card watch (Cubs 68-49, Cardinals 54-57 non-factor) | 2 |
| 12:00 PM CT | Clay Holmes debut preview (6:10 PM CT, Kauffman) | 1 |
| 1:15 PM CT | Cardinals roast (54-57, 15 GB, watching from the couch) | 3 |
| 2:30 PM CT | Steele mound work + Hollowell IL + Kelly call-up | 2 |
| 5:00 PM CT | Pre-game hype — Holmes debut first pitch (6:10 PM CT) | 1 |

## Pipeline Health (2026-08-08)
- JSON compiled: ✓ 07-content-data.json valid (schema 2.0, 8 stories, 8 X posts)
- Char count validation: ✓ All 8 posts under 280 chars (compile script confirmed)
- Review dashboard: ✓ Generated locally
- Dashboard push: ⚠ Skipped (content-dashboards repo not in session scope — same as prior days)
- Fact-check: ✓ All compound claims cross-referenced; 2 claims hedged or omitted (Bregman full slash line single-source; PCA .937 OPS single-source omitted from tweet)
- Insights applied: ✓ not_allcaps_lead + has_score=False both enforced across all 8 tweets

## Prior Runs (recent)
| Date | Stories | X Posts | Notes |
|------|---------|---------|-------|
| 2026-08-08 | 8 | 8 | Holmes debut day; Gausman recap; PCA/Bregman arcs; 2 insights applied |
| 2026-08-07 | 8 | 8 | KC road trip opener; Gausman + Holmes debuts; 2 insights applied |
| 2026-08-06 | 7 | 7 | Blue Jays single game; PCA 25/25 milestone; 1 insight applied |
| 2026-08-05 | 7 | 7 | Dodgers sweep game 3; Imanaga wins; 2 insights applied |
| 2026-08-04 | 6 | 6 | Assad vs Skubal night game; 1 insight applied |
| 2026-08-03 | 6 | 6 | Series opener vs Dodgers; Boyd 7-1 |
