# Cubs Pipeline Status — Updated 2026-11-19

## Latest Run
- **Date:** 2026-11-19 (Thursday — Off day. CBA 12 days to Dec 1 lockout. Cubs reportedly out on Michael King (Sharma/Athletic). Kaima Taira Dec 16 deadline complicates lockout. Two Cubs AFL All-Stars. Five starters + Horton = blank rotation.)
- **Stories:** 5
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 6 tweets
- **07-content-data.json:** ✅ Valid JSON, all 6 posts with posting_time (12:00 PM / 1:15 PM / 3:45 PM / 5:00 PM / 6:30 PM / 8:00 PM CT), all strptime-parseable. Char counts: 265/279/270/273/264/274 — all 260+ bucket, all under 280. ✅
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding, cubs-x-bot reads from content-pipeline)
- **Fact-check:** ✅ All 11 claims passed. One MEDIUM-confidence claim (Taira window lockout pause) uses conditional language ("could pause") — appropriate.
- **Note:** 12 significant insights applied. HASHTAG OVERRIDE (9th consecutive day): hashtag_count=3 is LOSER (p=0.0, large) + hashtag_count=1 is WINNER (p=0.0, large) → 1 hashtag (#Cubs) used, overrides brand-voice 3-hashtag rule. ALLCAPS LOSER: no ALL CAPS leads. MORNING AVOIDANCE: morning_06_12 LOSER — first post at 12:00 PM CT. EVENING PRIORITY: evening_18_24 WINNER → Stories 5 + 1B in 6:30 PM and 8:00 PM CT. TWEET LENGTH: len_bucket=260+ WINNER — all 6 tweets at 260+ chars. CONTENT DEPTH: content_type=brief LOSER — all substantive multi-paragraph tweets. has_stat WINNER — stats in all 6 tweets.
- **Hashtag override recommendation:** 9 consecutive days of data showing hashtag_count=3 underperforming (Cliffs delta 0.786, p=0.0, n=58). Strongly recommend formally updating brand-voice.md hashtag rule from "Exactly 3" to "1 primary hashtag (#Cubs)." This is the most persistent and strongest quantitative signal in the pipeline.

## Insights Summary (2026-11-19 run — from 2026-11-19T08:30 UTC snapshot)
- **Generated:** 2026-11-19T08:30:00 UTC
- **Measured tweet count:** 58 (n_winner + n_loser from hashtag finding)
- **Significant findings:** 12
  1. `content_type=recap_longform` WINNER — delta=0.917 (large). Off day — no game recap. Applied as instruction to write substantive, context-rich posts.
  2. `posting_window=evening_18_24` WINNER — delta=0.822 (large). Two evening slots: 6:30 PM (Story 5) and 8:00 PM (Story 1B).
  3. `hashtag_count=3` LOSER — delta=0.786 (large). ⚠️ CONFLICT with brand-voice.md hard rule. 1 hashtag used (9th consecutive override day).
  4. `opening=statement` WINNER — delta=0.722 (large). All 6 posts use declarative statement openings.
  5. `opening=allcaps_lead` LOSER — delta=0.722 (large). No ALL CAPS leads.
  6. `has_stat=True` WINNER — delta=0.671 (large). Stats in every tweet: 12 days/99 days/3 starters, 12-10/3.21 ERA/185 IP/$75-90M/12 days, Dec 16/45-day/99+ days, 5 starters, 5 starters/mid-2027/12 days.
  7. `posting_window=morning_06_12` LOSER — delta=0.661 (large). No morning posts; first at 12:00 PM CT.
  8. `hashtag_count=1` WINNER — delta=0.659 (large). Applied: #Cubs only on every tweet.
  9. `len_bucket=260+` WINNER — delta=0.639 (large). All 6 tweets at 260+ chars (avg 271).
  10. `len_bucket=200-260` LOSER — delta=0.635 (large). All tweets avoid 200-260 range.
  11. `has_score=True` WINNER — delta=0.533 (large). Off day — no score available. Not applied.
  12. `content_type=brief` LOSER — delta=0.484 (large). All posts substantive, multi-paragraph.
- **Action:** All 12 insights applied where applicable. 1-hashtag override active (9th day). All tweets 260-280 chars. No morning slots. Two evening prime slots.

## Previous Run (2026-11-18)
- **Date:** 2026-11-18 (Wednesday — Off day. Cubs protected Wiggins + McCullough (40-man deadline Nov 17). CBA 13 days to Dec 1. Kaima Taira top target. Suzuki QO declined. Rival watch.)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (1:15 PM / 2:30 PM / 3:45 PM / 5:00 PM / 6:30 PM CT), all strptime-parseable. All 5 tweets in 260+ char bucket (276/265/274/273/278). All under 280. ✅
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped
- **Note:** 12 significant insights applied. HASHTAG OVERRIDE (8th consecutive day): 1 hashtag (#Cubs). No morning posts. Evening prime at 6:30 PM.
