# Cubs Pipeline Status — Updated 2026-08-28

## Latest Run
- **Date:** 2026-08-28 (Friday — GAME DAY; Cubs vs Reds Game 1 of 3, 1:20 PM CT, Wrigley Field)
- **Run time:** ~09:00 UTC
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-28)
- **Snapshot generated:** 2026-08-28T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 127
- **significant_findings count:** 2
- **Finding 1:** `has_score=False` beats `has_score=True` — median impressions 99 vs 79, Cliff's delta=0.264 (small), p=0.0123
- **Finding 2:** `has_stat=True` beats `has_stat=False` — median impressions 104 vs 83, Cliff's delta=0.261 (small), p=0.0137
- **Applied:** (1) No game scores in any tweet body. (2) Every tweet includes ≥1 concrete numeric stat. Both findings stable and consistent with Aug 27 readings.

## Series Context (2026-08-28)
- `is_series_start_today`: TRUE
- `off_day`: FALSE — Cubs vs Reds Game 1, 1:20 PM CT, Wrigley Field
- `series`: Reds (63-71) at Cubs (76-58), 3 games (Aug 28-30)
- `rationale`: "Off day yesterday. Today: Cubs host Cincinnati Reds → game 1 of 3."
- Applied: 7:00 AM slot RESERVED for Series Preview per pipeline rules. Game hype at 12:00 PM CT (80 min before first pitch). Post-game slots skipped (pipeline runs pre-game).

## Today's Content (2026-08-27)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Series finale recap — E-Rod 9 Ks, Cubs drop G3 0-2 | 1 |
| 8:15 AM CT | Swanson injury — Grade 2 oblique, regular season likely done | 2 |
| 9:30 AM CT | PCA MVP Watch — 7.9 bWAR leads baseball | 2 |
| 10:45 AM CT | Wild Card Watch — Cubs 76-57 WC1, Cardinals 66-66 fading | 2 |
| 12:00 PM CT | Reds series preview — Wrigley, Aug 28-30 | 2 |
| 3:45 PM CT | Jaxon Wiggins — 4 straight scoreless outings, 0 hits allowed | 3 |

## Today's Content (2026-08-28)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Series Preview — Cubs vs Reds, 3 games at Wrigley, Peterson vs Lowder | 1 |
| 8:15 AM CT | Justin Steele — live BP this week, October bullpen weapon incoming | 2 |
| 9:30 AM CT | PCA MVP Watch — 7.7 fWAR leads all baseball, 2nd straight 30-30 pace | 2 |
| 10:45 AM CT | Wild Card — Cubs 76-58 WC1, Cardinals 67-68 nine games back | 2 |
| 12:00 PM CT | Game Day Hype — first pitch 80 min out, Peterson on hill | 1 |
| 3:45 PM CT | Jaxon Wiggins — September callup imminent, 4 hitless relief outings | 3 |

## Previous Run (2026-08-27)
- **Stories:** 6 | **X posts:** 6
- **Insights:** 2 significant findings (has_stat=True winner; has_score=False winner)
- **Series context:** Off day, Reds series preview

## Previous Run (2026-08-26)
- **Stories:** 6 | **X posts:** 6
- **Insights:** 2 significant findings (has_stat=True winner; has_score=False winner)
- **Series context:** Game 3 rubber match at Arizona, 2:40 PM CT

## Cumulative Notes
- Insights signals stable for 4 consecutive days: has_stat=True and has_score=False confirmed winners (measured_tweet_count now at 127).
- Dansby Swanson (oblique, Grade 2, IL since Aug 17): 4-6 week timeline = likely misses regular season. Postseason return possible if Cubs clinch early. Hoerner at SS, Ramirez at 2B.
- Justin Steele: threw live BP this week (Aug 2026 in Mesa), MiLB rehab imminent — bullpen-only role for October.
- Ben Brown: bridge camp game Aug 25 — progressing.
- Jaxon Wiggins: 4 straight scoreless relief outings, 0 hits allowed — September callup now "when not if."
- October rotation: Boyd/Gausman/Holmes/Imanaga (Taillon DFA'd prior to Aug 26).
- Dashboard publish to content-dashboards repo skipped this session (repo not in authorized set — expected behavior).
