# Cubs Pipeline Status — Updated 2026-11-10

## Latest Run
- **Date:** 2026-11-10 (Tuesday — Off day. BBWAA awards week: Cy Young Nov 11, NL MVP Nov 12. PCA 48 hrs from history. Cubs 40-man moves (Orze/Webb/Kelly). Rotation blank, Assad only internal option. Suzuki QO deadline Nov 17. Brewers WS champs + Misiorowski NL Cy Young frontrunner.)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (7:00 AM / 9:30 AM / 2:30 PM / 7:00 PM / 9:30 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 10 significant insights applied from expanded snapshot. Major signal: evening_18_24 WINNER (delta=0.956, massive) → Stories 4+5 in 7:00 PM / 9:30 PM. hashtag_count=3 LOSER (delta=0.829) conflicts with pipeline hard rule — documented, keeping 3 hashtags per pipeline. All posts <200 chars (not in 200-260 loser zone). Statement openings throughout. Transaction content labeled. Off day — BBWAA awards week + 40-man moves + rotation/Suzuki + PCA MVP hype + Misiorowski/Brewers rivalry.

## Insights Summary (2026-11-10 run — from 2026-11-10T08:30 UTC snapshot)
- **Generated:** 2026-11-10T08:30:00 UTC
- **Measured tweet count:** (see insights.json)
- **Significant findings:** 10
  1. `posting_window=evening_18_24` WINNER — evening (6PM-midnight) MASSIVE outperform, delta=0.956 (large), p=0.0; median 15,176 vs 111. Stories 4+5 in prime evening slots.
  2. `content_type=not_brief` WINNER — delta=0.902 (large), p=0.0; median 772 vs 66. All posts are analytical/substantive.
  3. `content_type=recap_longform` WINNER — delta=0.864 (large), p=0.0. Off-day, not applicable.
  4. `hashtag_count=3` LOSER — delta=0.829 (large), p=0.0. ⚠️ CONFLICT with pipeline hard rule. Keeping 3 hashtags per pipeline.
  5. `hashtag_count=1` WINNER — delta=0.799 (large), p=0.0. Cannot apply per pipeline rule.
  6. `len_bucket=<140` WINNER — delta=0.575 (large), p=0.0019. All posts targeted <200 chars.
  7. `opening=statement` WINNER — delta=0.563 (large), p=0.0001. All posts open with declarative statement.
  8. `opening=allcaps_lead` LOSER — delta=0.522 (large), p=0.0002. No ALLCAPS lead in any post.
  9. `content_type=transaction` WINNER — delta=0.516 (large), p=0.0186. Story 2 and 3 labeled transaction/analysis.
  10. `len_bucket=200-260` LOSER — delta=0.509 (large), p=0.0014. Zero posts in 200-260 range.
- **Action:** Stories 4+5 in 7:00 PM / 9:30 PM CT (evening prime). All 5 posts analytical (not_brief). All <200 chars. Statement openings. No ALLCAPS leads. Hashtag conflict documented.

## Previous Run (2026-11-04)
- **Date:** 2026-11-04 (Wednesday — Off day. Kanzler hired as Mariners manager Nov 3. PCA NL MVP finalist (45 HR, 41 SB, Gold Glove). Cubs declined Happ QO (Suzuki only). King market open. Rotation blank. AFL Reid 14 Ks.)
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 6 stories, 6 tweets
- **07-content-data.json:** ✅ Valid JSON, all 6 posts with posting_time (7:00 AM / 8:15 AM / 9:30 AM / 10:45 AM / 12:00 PM / 2:30 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 2 significant insights applied: not_brief WINNER (large, delta=0.829, p=0.0) + not_200-260 chars WINNER (small, delta=0.261, p=0.0488). Posts 1–2 target 260–280 chars; posts 3–6 target <200 chars. All "not_brief" content types (analysis, roster news, stat breakdown, prospect feature). Off day — Kanzler/Mariners (breaking) + PCA MVP finalist + Happ QO declined + King open market + rotation blank slate + AFL Reid.

## Insights Summary (2026-11-04 run — from 2026-11-04T08:30 UTC snapshot)
- **Generated:** 2026-11-04T08:30:00 UTC
- **Measured tweet count:** 82
- **Significant findings:** 2
  1. `content_type=brief` LOSER — `not_brief` WINNER, delta=0.829 (large), p=0.0; winner median 629 (n=12) vs loser median 83 (n=70). Non-brief content types massively outperform.
  2. `len_bucket=200-260` LOSER — `not_200-260` WINNER, delta=0.261 (small), p=0.0488; winner median 110 (n=51) vs loser median 62 (n=31). Avoid 200–260 char tweets.
- **Action:** All 6 tweets labeled as substantive types (analysis, roster news, stat breakdown, prospect feature). Tweets 1–2 in 260–280 range (264 chars each). Tweets 3–6 under 200 chars (153–190 chars). No tweets in the 200–260 loser zone.
- **Note:** Major signal shift from prior runs. allcaps_lead and not_statement are no longer in significant_findings for today — they are NOT applied (even though prior runs showed them as significant). not_brief effect is enormous (delta=0.829, 629 vs 83 median impressions) — strongest signal seen in this pipeline. Measured tweet count stable at 82.

## Previous Run
- **Date:** 2026-11-02 (Monday — Off day. Free agency open. Gold Gloves Nov 1: PCA back-to-back CF GG, Bregman 3B GG (only 2nd Cub after Ron Santo). Happ QO deadline TODAY 5 PM ET — no Cubs announcement yet. King Padres window closes today → Cubs in play. Kanzler/Mariners decision expected this week. AFL: Reid AFL-leading 14 Ks, 1.50 ERA.)
- **Stories:** 7
- **X posts:** 7
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 7 stories, 7 tweets
- **07-content-data.json:** ✅ Valid JSON, all 7 posts with posting_time (7:00 AM / 8:15 AM / 9:30 AM / 10:45 AM / 12:00 PM / 2:30 PM / 3:45 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 2 significant insights applied: allcaps_lead WINNER (delta=0.304, small, p=0.020) + not_statement WINNER (delta=0.294, small, p=0.028). All 7 tweets open with ALL CAPS fragment. Off day — Gold Gloves (PCA + Bregman) + Bregman/Santo historical take + Happ QO deadline + King free to sign + 5 SPs in FA + Kanzler/Mariners + AFL Reid 14Ks.

## Previous Run
- **Date:** 2026-11-01 (Sunday — Off day. Brewers WS champs confirmed (beat Rays 4-1, Game 5 Oct 28). King FA opens Nov 2. PCA BBWAA finalists Nov 2. Suzuki QO expected this week. Cubs rotation: 5 arms gone, Horton out mid-2027.)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (7:00 AM / 9:30 AM / 12:00 PM / 2:30 PM / 3:45 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 2 significant insights applied: allcaps_lead WINNER (delta=0.27, small, p=0.035) + not_statement LOSER (delta=0.264, small, p=0.044). All 5 tweets open with ALL CAPS fragment. Off day — Brewers WS confirmed (Game 5 Oct 28) + King FA tomorrow + PCA BBWAA finalists Monday + Cubs rotation all-gone + Suzuki QO imminent. Skipped Sato (Cubs connection speculative) and AFL (Cole Mathis traded to Mets in June, no confirmed Cubs AFL stats).

## Insights Summary (2026-11-02 run — from 2026-11-02T08:30 UTC snapshot)
- **Generated:** 2026-11-02T08:30:00 UTC
- **Measured tweet count:** 82
- **Significant findings:** 2
  1. `opening=allcaps_lead` WINNER — delta=0.304 (small), p=0.020; winner median 107 (n=48) vs loser median 60.5 (n=34). ALL CAPS leads outperform.
  2. `opening=statement` LOSER — `not_statement` WINNER, delta=0.294 (small), p=0.028; winner median 104 (n=52) vs loser median 60.5 (n=30). Plain statement openers underperform.
- **Action:** All 7 tweets open with ALL CAPS fragment on line 1, satisfying both signals simultaneously.
- **Note:** Fourth consecutive run with allcaps_lead significant. Effect size increased to 0.304 (from 0.27 yesterday) — strongest signal yet. not_statement also significant again. Measured tweet count dropped 84 → 82 (likely 2 tweets aged out of 30-day window). Both signals stable and strengthening.

## Previous Insights Summary (2026-11-01 run — from 2026-11-01T08:30 UTC snapshot)
- **Generated:** 2026-11-01T08:30:00 UTC
- **Measured tweet count:** 84
- **Significant findings:** 2
  1. `opening=allcaps_lead` WINNER — dimension=opening=allcaps_lead, delta=0.27 (small), p=0.035; winner median 97.5 (n=48) vs loser median 60.5 (n=36). ALL CAPS leads outperform.
  2. `opening=statement` LOSER — `not_statement` WINNER, delta=0.264 (small), p=0.044; winner median 97.5 (n=52) vs loser median 60.5 (n=32). Plain statement openers underperform.
- **Action:** All 5 tweets open with ALL CAPS fragment on line 1, satisfying both signals simultaneously.
- **Note:** Third consecutive run with allcaps_lead significant. not_statement also significant again (like Oct 31, not Oct 30). Measured tweet count dropped from 87 (Oct 30) → 84 (Nov 1) — likely a few tweets aged out of the 30-day measurement window. Both effect sizes stable in the 0.26-0.27 range.

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
| 2026-11-02 | 7 | 7 | ✅ | Off day. Gold Gloves, Bregman/Santo, Happ QO deadline, King open, rotation 5FA, Kanzler, AFL Reid. |
| 2026-11-01 | 5 | 5 | ✅ | Off day. Brewers WS, King FA, PCA BBWAA, rotation, Suzuki QO. |
| 2026-10-31 | 6 | 6 | ✅ | Off day. Gold Gloves, rotation, Happ QO, King FA, Kanzler, AFL Reid. |
| 2026-10-30 | 6 | 6 | ✅ | Off day. BREAKING: King opts out + Holmes/Boyd options declined. |
| 2026-10-29 | 5 | 5 | ✅ | Off day. Ian Happ, PCA Players Choice, Brewers WS G5, King countdown. |
| 2026-10-28 | 5 | 5 | ✅ | Off day. WS G5 preview, King, Suzuki, PCA, Sato. |
| 2026-10-27 | 5 | 5 | ✅ | Off day. WS updates, King, rotation, Suzuki, Sato. |
