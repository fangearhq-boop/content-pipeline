# Cubs Pipeline Status — Updated 2026-11-01

## Latest Run
- **Date:** 2026-11-01 (Sunday — Off day. Brewers WS champs confirmed (beat Rays 4-1, Game 5 Oct 28). King FA opens Nov 2. PCA BBWAA finalists Nov 2. Suzuki QO expected this week. Cubs rotation: 5 arms gone, Horton out mid-2027.)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (7:00 AM / 9:30 AM / 12:00 PM / 2:30 PM / 3:45 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 2 significant insights applied: allcaps_lead WINNER (delta=0.27, small, p=0.035) + not_statement LOSER (delta=0.264, small, p=0.044). All 5 tweets open with ALL CAPS fragment. Off day — Brewers WS confirmed (Game 5 Oct 28) + King FA tomorrow + PCA BBWAA finalists Monday + Cubs rotation all-gone + Suzuki QO imminent. Skipped Sato (Cubs connection speculative) and AFL (Cole Mathis traded to Mets in June, no confirmed Cubs AFL stats).

## Previous Run
- **Date:** 2026-10-31 (Saturday — Off day. Halloween. Free agency opens Monday Nov 2. Gold Gloves TOMORROW Nov 1 ESPN. King free agent, Padres exclusive window closes Monday. Happ QO deadline Monday. Kanzler/Mariners still no hire. AFL: Reid leads AFL with 14 Ks.)
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 6 stories, 6 tweets
- **07-content-data.json:** ✅ Valid JSON, all 6 posts with posting_time (7:00 AM / 8:15 AM / 9:30 AM / 10:45 AM / 12:00 PM / 2:30 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 2 significant insights applied: allcaps_lead WINNER (delta=0.265, small, p=0.035) + not_statement LOSER (delta=0.259, small, p=0.043). All 6 tweets open with ALL CAPS fragment. Off day — Gold Gloves eve (PCA back-to-back + historic sweep) + 5-SP rotation crisis scope + Happ QO Monday deadline + King/FA opens Monday + Kanzler/Mariners waiting + AFL Reid AFL-leading 14 Ks.

## Insights Summary (2026-11-01 run — from 2026-11-01T08:30 UTC snapshot)
- **Generated:** 2026-11-01T08:30:00 UTC
- **Measured tweet count:** 84
- **Significant findings:** 2
  1. `opening=allcaps_lead` WINNER — dimension=opening=allcaps_lead, delta=0.27 (small), p=0.035; winner median 97.5 (n=48) vs loser median 60.5 (n=36). ALL CAPS leads outperform.
  2. `opening=statement` LOSER — `not_statement` WINNER, delta=0.264 (small), p=0.044; winner median 97.5 (n=52) vs loser median 60.5 (n=32). Plain statement openers underperform.
- **Action:** All 5 tweets open with ALL CAPS fragment on line 1, satisfying both signals simultaneously.
- **Note:** Third consecutive run with allcaps_lead significant. not_statement also significant again (like Oct 31, not Oct 30). Measured tweet count dropped from 87 (Oct 30) → 84 (Nov 1) — likely a few tweets aged out of the 30-day measurement window. Both effect sizes stable in the 0.26-0.27 range.

## Insights Summary (2026-10-31 run — from 2026-10-31T08:30 UTC snapshot)
- **Generated:** 2026-10-31T08:30:00 UTC
- **Significant findings:** 2
  1. `opening=allcaps_lead` WINNER — delta=0.265 (small), p=0.035; winner median 99 (n=47) vs loser median 60 (n=39). ALL CAPS leads outperform.
  2. `opening=statement` LOSER — `not_statement` WINNER, delta=0.259 (small), p=0.043; winner median 99 (n=51) vs loser median 60 (n=35). Plain statement openers underperform.
- **Action:** All 6 tweets open with ALL CAPS fragment on line 1, satisfying both signals simultaneously.

## Insights Summary (2026-10-30 run — from 2026-10-30T08:30 UTC snapshot)
- **Generated:** 2026-10-30T08:30:00 UTC
- **Measured tweet count:** 87
- **Significant findings:** 1
  1. `opening=allcaps_lead` winner=True, delta=0.245 (small), p=0.05 — ALL CAPS leads outperform
- **Note:** Prior run had 2 findings (allcaps_lead + not_statement); today only allcaps_lead cleared the gates. `opening=statement` not significant this snapshot (dropped out). Continued to avoid plain declarative openers per brand voice defaults.
- **Action:** All 6 tweets open with ALL CAPS fragment on line 1.

## Pipeline Run Log

| Date | Stories | Tweets | Status | Notes |
|------|---------|--------|--------|-------|
| 2026-11-01 | 5 | 5 | ✅ | Off day. Brewers WS, King FA, PCA BBWAA, rotation, Suzuki QO. |
| 2026-10-31 | 6 | 6 | ✅ | Off day. Gold Gloves, rotation, Happ QO, King FA, Kanzler, AFL Reid. |
| 2026-10-30 | 6 | 6 | ✅ | Off day. BREAKING: King opts out + Holmes/Boyd options declined. |
| 2026-10-29 | 5 | 5 | ✅ | Off day. Ian Happ, PCA Players Choice, Brewers WS G5, King countdown. |
| 2026-10-28 | 5 | 5 | ✅ | Off day. WS G5 preview, King, Suzuki, PCA, Sato. |
| 2026-10-27 | 5 | 5 | ✅ | Off day. WS updates, King, rotation, Suzuki, Sato. |
