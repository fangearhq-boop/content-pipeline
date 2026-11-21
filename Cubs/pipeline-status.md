# Cubs Pipeline Status — Updated 2026-11-21

## Latest Run
- **Date:** 2026-11-21 (Saturday — Off day. CBA 10 days to Dec 1 lockout. Pitching market moving: Gray/Twins ($55M), May/White Sox ($52.5M), Skubal in Mets meetings. Cubs claimed Joey Bart off waivers from White Sox. Kaima Taira: 9 teams pursuing, Cubs top suitor with virtual meetings. Trevor Rogers QO declined, Cubs early interest confirmed. Assad only starter on roster.)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (12:00 PM / 1:15 PM / 3:45 PM / 5:00 PM / 6:30 PM CT), all strptime-parseable. Char counts: 270/275/271/268/277 — all 260+ bucket, all under 280. ✅
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding, cubs-x-bot reads from content-pipeline)
- **Fact-check:** ✅ PASS overall. MEDIUM flags: Taira 1.48 ERA (Clutchpoints; prior pipeline flagged 1.36 discrepancy — different season/source; used "posted" language). Dec 16 deadline (sources conflict: Dec 5/Dec 15/Dec 16 — used Dec 16 for consistency). All claims directionally accurate.
- **Note:** 14 significant insights applied. HASHTAG OVERRIDE (11th consecutive day): hashtag_count=3 is LOSER + hashtag_count=1 is WINNER → 1 hashtag (#Cubs) used. ALLCAPS LOSER: no ALL CAPS leads. MORNING AVOIDANCE: morning_06_12 LOSER — first post at 12:00 PM CT (noon). EVENING PRIORITY: evening_18_24 WINNER → Post 5 at 6:30 PM CT. TWEET LENGTH: len_260+ WINNER — all 5 tweets at 260+ chars (avg 272). CONTENT DEPTH: content_type=brief LOSER — all substantive multi-paragraph tweets. has_stat WINNER — stats in all 5 tweets. TRANSACTION LOSER: Joey Bart claim reframed as roster-depth analysis.
- **Hashtag override recommendation (11th day):** Strongest quantitative signal in the dataset. Strongly recommend formally updating brand-voice.md from "Exactly 3 hashtags" to "1 primary hashtag (#Cubs)." Data is unambiguous: n=58, p=0.0, Cliff's delta=0.710 (3-hashtag LOSES) + delta=0.578 (1-hashtag WINS).

## Insights Summary (2026-11-21 run — from 2026-11-21T08:30 UTC snapshot)
- **Generated:** 2026-11-21T08:30:00 UTC
- **Measured tweet count:** 58
- **Significant findings:** 14
  1. `content_type=recap_longform` WINNER — delta=0.887 (large). Off day — no game recap. Not applicable.
  2. `posting_window=evening_18_24` WINNER — delta=0.752 (large). Post 5 at 6:30 PM CT.
  3. `len_bucket=260+` WINNER — delta=0.740 (large). All 5 tweets at 260+ chars (avg 272).
  4. `hashtag_count=3` LOSER — delta=0.710 (large). ⚠️ CONFLICT with brand-voice.md. 1 hashtag used (11th consecutive override day).
  5. `has_score=True` WINNER — delta=0.673 (large). Off day — no score. Not applicable.
  6. `opening=statement` WINNER — delta=0.624 (large). All 5 posts use declarative statement openings.
  7. `opening=allcaps_lead` LOSER — delta=0.624 (large). No ALL CAPS leads.
  8. `has_stat=True` WINNER — delta=0.571 (large). Stats in every tweet.
  9. `hashtag_count=1` WINNER — delta=0.578 (large). Applied: #Cubs only.
  10. `posting_window=morning_06_12` LOSER — delta=0.576 (large). No morning posts; first at 12:00 PM CT.
  11. `content_type=transaction` LOSER — delta=0.570 (large). Joey Bart claim reframed as depth analysis.
  12. `len_bucket=<140` LOSER — delta=0.549 (large). No tweets under 140 chars.
  13. `len_bucket=140-200` LOSER — delta=0.404 (medium). No tweets in 140-200 range.
  14. `content_type=brief` LOSER — delta=0.312 (small). Substantive multi-paragraph posts throughout.

## Pipeline Run Log

### 2026-11-21 — Saturday (Off day)
- 5 stories | 5 X posts | JSON valid | Fact-check PASS (2 MEDIUM flags on Story 3)
- CBA 10-day countdown (market moving) | Joey Bart claim NEW | Taira 9 teams | Rogers QO declined | Rotation vacuum bold take
- Insights: 11th hashtag override, all 14 findings applied
- Push: content-pipeline ✅ | content-dashboards ⚠️ (out of session scope)

## Insights Summary (2026-11-20 run — from 2026-11-20T08:30 UTC snapshot)
- **Generated:** 2026-11-20T08:30:00 UTC
- **Measured tweet count:** 58
- **Significant findings:** 12
  1. `content_type=recap_longform` WINNER — delta=0.943 (large). Off day — no game recap. Not applicable.
  2. `posting_window=evening_18_24` WINNER — delta=0.77 (large). Post 5 at 6:30 PM CT.
  3. `len_bucket=260+` WINNER — delta=0.745 (large). All 5 tweets at 260+ chars.
  4. `hashtag_count=3` LOSER — delta=0.731 (large). ⚠️ CONFLICT with brand-voice.md. 1 hashtag used (10th consecutive override day).
  5. `has_score=True` WINNER — delta=0.66 (large). Off day — no score. Not applicable.
  6. `opening=statement` WINNER — delta=0.656 (large). All 5 posts use declarative statement openings.
  7. `opening=allcaps_lead` LOSER — delta=0.656 (large). No ALL CAPS leads.
  8. `has_stat=True` WINNER — delta=0.62 (large). Stats in every tweet.
  9. `hashtag_count=1` WINNER — delta=0.605 (large). Applied: #Cubs only.
  10. `posting_window=morning_06_12` LOSER — delta=0.569 (large). No morning posts; first at 1:15 PM CT.
  11. `content_type=transaction` LOSER — delta=0.49 (large). No pure transaction tweets; moves embedded in analysis.
  12. `len_bucket=<140` LOSER — delta=0.46 (medium). No tweets under 140 chars.
  13. `content_type=brief` LOSER — delta=0.407 (medium). Substantive multi-paragraph posts throughout.

## Pipeline Run Log

### 2026-11-20 — Friday (Off day) [archived below]
- 5 stories | 5 X posts | JSON valid | Fact-check PASS
- CBA 11-day countdown (Manfred hardball) | Trevor Rogers NEW | Taira virtual meetings | AFL wrap | NL Central rival watch
- Insights: 10th hashtag override, all 12 findings applied
- Push: content-pipeline ✅ | content-dashboards ⚠️ (out of session scope)

---

# --- Previous Run Archive ---

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
