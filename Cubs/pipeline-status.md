# Cubs Pipeline Status — Updated 2026-08-22

## Latest Run
- **Date:** 2026-08-22 (Saturday — GAME DAY, Game 2 of 3 vs Seattle Mariners at T-Mobile Park)
- **Run time:** ~09:20 UTC
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-22)
- **Snapshot generated:** 2026-08-22T08:30:00Z (fresh, 30 min before trigger)
- **significant_findings count:** 1
- **Finding:** `has_stat=True` beats `has_stat=False` — median impressions 104 vs 87, Cliff's delta=0.214 (small), p=0.046
- **Applied:** Every tweet drafted with at least one concrete stat embedded. No other brand-voice overrides (no emoji, char length, posting window, or content_type findings today).

## Series Context (2026-08-22)
- `is_series_start_today`: FALSE (mid-series)
- `off_day`: FALSE — Game 2 tonight 6:15 PM CT at T-Mobile Park, Seattle
- Opponent: Seattle Mariners (61-68)
- Cubs record: 74-55
- Series: Game 2 of 3 — Cubs lost Game 1 on Aug 21 (6-5 walk-off, 10 innings)
- Applied: No series-preview slot reserved. Lead slot = game 1 recap. Posting priority followed.

## Today's Content (2026-08-22)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Game 1 recap — Mariners 6-5 (10 inn) walk-off, Bregman 2 HRs | 1 |
| 9:30 AM CT | Kade Anderson MLB debut preview — No. 3 pick, 10-1, 1.06 ERA at AA | 2 |
| 12:00 PM CT | Daniel Palencia activated from IL (elbow inflammation) | 2 |
| 2:30 PM CT | Matt Shaw Triple-A Iowa rehab started Aug 19 | 2 |
| 5:00 PM CT | Wild card standings — WC1, 5-game cushion, Sept Brewers games | 2 |
| 6:15 PM CT | First pitch hype — Game 2, Peterson vs Anderson | 2 |

## Issues / Notes (2026-08-22)
- ESPN and MLB.com direct page fetches blocked by network proxy (CCR egress). Game 1 stats confirmed via search result AI summaries (MEDIUM confidence). No box score discrepancy found in cross-source comparison.
- Dashboard push to `fangearhq-boop/content-dashboards` blocked (repo not in session's authorized set). Content pipeline repo push succeeded.
- Story 4 (Shaw rehab) hit exactly 280 chars per compile script — within limit.
- Brewers NL Central clinch status excluded from tweets (ambiguous 2025 vs 2026 sources).

---

## Prior Run (2026-08-21)
- **Date:** 2026-08-21 (Friday — GAME DAY, Series Start vs Seattle Mariners)
- **Run time:** ~09:00 UTC
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-21)
- **Snapshot generated:** 2026-08-21T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 124
- **Significant findings:** 0 — no contrasts cleared all three gates (n≥8, p<0.05, |Cliff's delta|≥0.20)
- **significant_findings_note:** "No contrasts cleared all three gates (n>=8 per group, p<0.05, |Cliff's delta|>=0.2). Either too little data or no format/time differences are large enough yet."
- **Applied:** Fell through to brand-voice defaults. No performance-data-driven format adjustments. The `has_score` finding that ran Aug 15-20 did not clear gates today (124 tweets measured, pool up from 123). System may start producing new signals in 2-4 weeks as pool grows.

## Series Context (2026-08-21)
- `is_series_start_today`: TRUE
- `off_day`: FALSE — Game 1 tonight 9:10 PM CT at T-Mobile Park, Seattle
- Opponent: Seattle Mariners (60-68, out of playoff race)
- Cubs record: 74-54
- Series: 3 games — Aug 21, 22, 23
- Applied: 7:00 AM CT slot reserved for Series Preview (mandatory per is_series_start_today=true). Lead = matchup + length + location; pitcher + stakes = kicker.

## Today's Content (2026-08-21)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | Series Preview — Cubs at Mariners, 3 games, T-Mobile Park, 9:10 PM CT, Boyd vs Hancock | 1 |
| 9:30 AM CT | Matthew Boyd Game 1 starter — 8-2, 4.02 ERA, 1.24 WHIP through 85 IP | 2 |
| 12:00 PM CT | Rotation shuffle — Cabrera back on IL (blister), Peterson starts Sat, Assad recalled | 2 |
| 3:45 PM CT | Wild card / playoff stakes — Cubs WC1 (74-54), Phillies 4 back, Brewers gauntlet ahead | 2 |
| 8:00 PM CT | First pitch hype — 9:10 PM CT, Boyd on mound, Friday night in Seattle | 2 |

## Cubs Record as of 2026-08-21
- **Record:** 74-54 (No. 1 NL Wild Card)
- **NL Central gap:** ~5 GB behind Brewers
- **NL WC gap:** Phillies 4 GB back (70-58), Padres 6 GB back (68-60)

---

## Previous Run (2026-08-20)
- **Date:** 2026-08-20 (Thursday — Off Day, travel to Seattle)
- **Run time:** ~09:00 UTC
- **Stories:** 7 | **X posts:** 7 | **Status:** ✅ Complete
- **Insight applied:** has_score=False (small effect, p=0.0207, Cliff's delta=0.253) — 5th consecutive day this dimension cleared all gates; today (Aug 21) it did not clear.
- **Series context:** is_series_start_today=FALSE, off_day=TRUE. Content: Game 3 recap (shutout), Cardinals roast, Swanson oblique update, WC standings, Wiggins prospect, PCA MVP case, Steele/Brown bullpen.

---

## Previous Run (2026-08-18)
- **Date:** 2026-08-18 (Tuesday)
- **Run time:** ~09:00 UTC
- **Stories:** 8
- **X posts:** 8
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete

## Insights Summary (2026-08-18)
- **Snapshot generated:** 2026-08-18T08:30:00Z (fresh, 30 min before trigger)
- **measured_tweet_count:** 124
- **Significant findings (1):**
  1. `has_score=False` beats `has_score=True` — **small** effect (Cliff's delta=0.289, p=0.0069, n=76 vs 48, median impressions 109.5 vs 81.0)
     - **Applied:** All 8 tweets drafted without game scores. Last night's result (Cubs 7, White Sox 5, 10 inn.) referenced by describing the walk-off moment and milestone, NOT the score. Finding persists for third consecutive day.
- **Note vs yesterday:** Finding is same dimension (`has_score`) but effect size slightly decreased from medium (0.33) to small (0.289) and p-value weaker (0.0069 vs 0.0019). Still the only dimension clearing all three gates. Measurement pool size dropped by 1 (124 vs 125). Likely a measured-tweet reclassification. Finding remains actionable.

## Series Context (2026-08-18)
- `is_series_start_today`: FALSE — mid-series vs White Sox (Game 2 of 3)
- `off_day`: FALSE — Game 2 at 7:05 PM CT at Wrigley Field
- Cubs record: 73-53 | White Sox: 65-59
- Probable pitchers: Gausman (6-11, 4.53 ERA) for Cubs; White Sox TBD
- Applied: No series-preview slot required. 7:00 AM slot used for game recap (walk-off win, PCA milestone).

## Today's Content (2026-08-18)
| Slot | Story | Tier |
|------|-------|------|
| 7:00 AM CT | PCA walk-off HR (30th) + 30-30 game recap — first career walk-off; back-to-back 30-30 | 1 |
| 8:15 AM CT | PCA franchise history — first Cub with consecutive 30-30 seasons, only Sosa before | 2 |
| 9:30 AM CT | Wild Card: Cubs 73-53, WC1 by 5 over Phillies (68-58) and Padres (67-59) | 2 |
| 10:45 AM CT | Cardinals: 13.5 GB in division, playing Reds tonight, rival jab | 2 |
| 12:00 PM CT | Gausman starts Game 2 (6-11, 4.53 ERA), Cubs lead series 1-0, 7:05 PM CT | 1 |
| 2:30 PM CT | Swanson MRI: Grade 2 oblique, 4-6 weeks, hopeful Sept 15 return for October | 2 |
| 5:00 PM CT | Pre-game hype — Wrigley, 7:05 PM CT, Gausman starts, don't let Sox get comfortable | 1 |
| 6:30 PM CT | First pitch hype — GAME TWO, full lineup finishes the job | 1 |

## Cubs Record as of 2026-08-18 (after last night's win)
- **Record:** 73-53 (No. 1 NL Wild Card)
- **NL WC gap:** 5 games over Phillies (68-58) and Padres (67-59)
- **NL Central gap:** 4 GB behind Brewers (77-48)

---

## Previous Run (2026-08-17)
- **Date:** 2026-08-17 (Monday)
- **Run time:** ~09:00 UTC
- **Stories:** 7 | **X posts:** 7 | **Status:** ✅ Complete
- **Insight applied:** has_score=False (medium effect, p=0.0019, Cliff's delta=0.33)
- **Series context:** is_series_start_today=TRUE (Crosstown Classic Game 1, Imanaga vs Castillo, 7:05 PM CT)
- **Game result:** Cubs 7, White Sox 5 in 10 innings (PCA walk-off; Crosstown Classic Game 1 W)

---

## Previous Run (2026-08-16)
- **Date:** 2026-08-16 (Sunday)
- **Run time:** ~09:00 UTC
- **Stories:** 6 | **X posts:** 6 | **Status:** ✅ Complete
- **Insight applied:** has_score=False (small effect, p=0.0036)
- **Series context:** Mid-series vs Cardinals (Game 3). Báez historic 3-HR debut, Cabrera return, PCA chase, Cardinals reality check, rotation depth, pre-game hype.
- **Brewers:** 75-48 (NL Central leaders, ~3.5 GB ahead of Cubs)
- **Cardinals:** 62-61 (3 GB from WC3; sold deadline pieces)

## Key Storylines to Watch
- **Tonight's game:** Cubs at Mariners, Game 1 of 3, T-Mobile Park, 9:10 PM CT. Boyd vs Hancock.
- **Rotation:** Cabrera back on IL (blister); Peterson starts Sat; Imanaga starts Sun. Three different starters in 3 games.
- **PCA:** 30 HR, 31 SB, .281/.379/.550, 8.2 fWAR — historic back-to-back 30-30 seasons; NL MVP case heating up
- **Swanson:** Grade 2 oblique; 4-week target = mid-September; Hoerner at SS, Ramírez at 2B meanwhile
- **Matt Shaw:** On rehab assignment at Iowa (started Aug 19). Recovery from left hand sprain. Expected return TBD.
- **Cardinals:** ~13.5 GB in NL Central; no threat to wild card
- **Brewers:** Leading NL Central by ~5; 7 H2H remaining (Aug 31-Sep 3, Sep 7-9)

## Pipeline Health (2026-08-21)
- JSON compiled: ✓ 07-content-data.json valid (schema 2.0, 5 stories, 5 X posts)
- Char count validation: ✓ All 5 posts at or under 280 chars (177–280; Post 3 = exactly 280)
- Review dashboard: ✓ Generated locally (review-dashboard.html)
- Dashboard push: ⚠ Skipped (content-dashboards repo not in session scope — expected behavior)
- Fact-check: ✓ All claims reviewed; HIGH for times/records (from series-context.json), MEDIUM for Boyd ERA and Brewers division gap; 0 fails
- Insights applied: ✓ No significant findings; fell through to brand-voice defaults; documented in 02-story-analysis.md
- Story history: ✓ Appended 5 stories to Cubs/story-history.md

## Prior Runs (recent)
| Date | Stories | X Posts | Notes |
|------|---------|---------|-------|
| 2026-08-20 | 7 | 7 | Off day; White Sox recap (shutout); Cardinals roast; Swanson oblique; WC standings; Wiggins prospect; PCA MVP; Steele/Brown bullpen; 1 insight (has_score=False, small) |
| 2026-08-19 | 5 | 5 | Walk-off recap (Bregman); Wrigley walk-off culture (13 leading MLB); Gausman glove-hand cramp; NL standings/Cardinals jab; Game 3 preview sweep hunt |
| 2026-08-18 | 8 | 8 | PCA 30th HR walk-off recap; PCA franchise history; WC standings; Cardinals roast; Gausman Game 2 preview; Swanson MRI update; pre-game + first pitch hype; 1 insight applied |
| 2026-08-17 | 7 | 7 | Crosstown Classic series preview; Swanson IL; Suzuki activated; PCA 27HR/30SB; WC watch; Imanaga matchup preview; first pitch hype; 1 insight applied |
| 2026-08-16 | 6 | 6 | Báez historic 3-HR debut recap; Cabrera return/series decider; PCA 30-30; Cardinals check; rotation depth; pre-game hype; 1 insight applied |
| 2026-08-15 | 6 | 6 | Game 1 recap (Holmes shutout); Boyd preview; Cabrera return Sunday; PCA Bregman MVP; Cardinals roast; Cowles prospect; 1 insight applied |
| 2026-08-14 | 6 | 6 | Cardinals series start (Game 1 of 3); Nationals recap (Cavalli near no-hit); PCA 30-30; Bregman vs Liberatore; 4 insights applied |
| 2026-08-13 | 5 | 5 | Game 2 recap (71-50); Cardinals roast; PCA WAR 7.5; Gausman preview; sweep hype |
| 2026-08-12 | 6 | 6 | Game 1 recap (70-50 milestone); Suzuki 20 HR; June 10 run; WC watch; Peterson preview; hype |
| 2026-08-11 | 7 | 7 | Series start (Nationals); Imanaga streak; PCA MVP No. 1; Happ slump recovery; WC watch; matchup analysis; pre-game hype |
