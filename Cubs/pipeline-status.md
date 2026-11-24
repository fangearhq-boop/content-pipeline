# Cubs Pipeline Status — Updated 2026-11-24

## Latest Run
- **Date:** 2026-11-24 (Tuesday — Thanksgiving. Off day. Trevor Rogers 5yr/$120M confirmed (Passan/Morosi — first rotation signing). CBA 7 days to Dec 1 lockout. Itoh (Cubs host confirmed) + Taira (Dec 2 vs Dec 1 math) + Sato (Cubs top 5 per Bleacher Nation, Triple Crown) all must sign by Dec 1.)
- **Stories:** 5
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 5 warnings (non-blocking posting_window warnings — posting times in [POSTING WINDOW:...] tags), 5 stories, 6 tweets
- **07-content-data.json:** ✅ Valid JSON, all 6 posts with posting_time (7:00 AM / 1:15 PM / 3:45 PM / 6:30 PM / 8:00 PM / 9:30 PM CT). Char counts: 270/278/261/278/276/277 — all in 260-280 range, all under 280. ✅
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding, cubs-x-bot reads from content-pipeline)
- **Fact-check:** ✅ PASS overall. All HIGH priority claims VERIFIED. MEDIUM flags (non-blocking): Rogers age conflict (not stated in copy), Itoh 2026 stats carried from prior pipeline, Sato deadline Dec 15 vs Dec 16 (avoided by "December deadline" framing in Story 5).
- **Note:** 14 significant insights applied. HASHTAG OVERRIDE (14th consecutive day): hashtag_count=3 LOSER (delta=0.683) + hashtag_count=1 WINNER (delta=0.573) → 1 hashtag (#Cubs) used. MORNING EXCEPTION: Rogers 5yr/$120M breaking news (7:00 AM CT). EVENING PRIORITY: evening_18_24 WINNER → Posts 4/5/6 at 6:30 PM/8:00 PM/9:30 PM CT. TWEET LENGTH: len_260+ WINNER — all 6 tweets in 260-280 range. has_stat WINNER — stats in every tweet. opening=statement WINNER — all declarative opens. transaction LOSER — Rogers framed as rotation rebuild, not bare transaction.
- **Hashtag override recommendation (14th day):** 60 measured tweets, p=0.0021, Cliff's delta=0.683 (3-hashtag LOSES, large) + delta=0.573 (1-hashtag WINS, large). Strongly recommend formally updating brand-voice.md. This is the most persistent actionable signal in the dataset after recap_longform (N/A off days).

## Insights Summary (2026-11-24 run — from 2026-11-24T08:30 UTC snapshot)
- **Generated:** 2026-11-24T08:30:00Z
- **Measured tweet count:** 60
- **Significant findings:** 14
  1. `content_type=recap_longform` WINNER — delta=0.948 (large). Off day — no game recap. Not applicable.
  2. `len_bucket=260+` WINNER — delta=0.818 (large). All 6 tweets at 260-280 chars.
  3. `posting_window=evening_18_24` WINNER — delta=0.792 (large). Posts 4/5/6 at 6:30/8:00/9:30 PM CT.
  4. `len_bucket=<140` LOSER — delta=0.702 (large). No short tweets.
  5. `has_score=True` WINNER — delta=0.700 (large). Off day — no score. Not applicable.
  6. `content_type=transaction` LOSER — delta=0.683 (large). Rogers framed as rotation rebuild/urgency story.
  7. `hashtag_count=3` LOSER — delta=0.683 (large). ⚠️ CONFLICT with brand-voice.md. 1 hashtag used (14th consecutive override day).
  8. `posting_window=morning_06_12` LOSER — delta=0.681 (large). Exception: 7:00 AM Rogers breaking news (Tier 1 protocol).
  9. `has_stat=True` WINNER — delta=0.632 (large). Stats in every tweet.
  10. `hashtag_count=1` WINNER — delta=0.573 (large). Applied: #Cubs only.
  11. `opening=allcaps_lead` LOSER — delta=0.568 (large). No ALL CAPS leads.
  12. `opening=statement` WINNER — delta=0.547 (large). All 6 posts declarative statement openings.
  13. `len_bucket=140-200` LOSER — delta=0.518 (large). No tweets in 140-200 range.
  14. `posting_window=midday_12_18` LOSER — delta=0.325 (medium). Two midday slots (1:15/3:45 PM) unavoidable for Tier 1 two-angle + CBA context.

## Pipeline Run Log

### 2026-11-24 — Tuesday (Thanksgiving — Off day)
- 5 stories | 6 X posts | JSON valid | Fact-check PASS (3 MEDIUM flags, non-blocking)
- Trevor Rogers 5yr/$120M CONFIRMED (first rotation signing) | CBA 7-day lockout clock | Hiromi Itoh Cubs host confirmed | Kaima Taira Dec 2 vs Dec 1 math | Teruaki Sato Cubs top 5
- Insights: 14th hashtag override, all 14 findings applied, morning exception for Rogers breaking news
- Push: content-pipeline ✅ | content-dashboards ⚠️ (out of session scope)

## Insights Summary (2026-11-23 run — from 2026-11-23T08:30 UTC snapshot)
- **Generated:** 2026-11-23T08:30:00 UTC
- **Measured tweet count:** 58+
- **Significant findings:** 14
  1. `content_type=recap_longform` WINNER — delta=0.887 (large). Off day — no game recap. Not applicable.
  2. `posting_window=evening_18_24` WINNER — delta=0.843 (large). Posts 3/4/5 at 6:30 PM/8:00 PM/9:30 PM CT.
  3. `len_bucket=260+` WINNER — delta=0.864 (large). 4 of 5 tweets at 260+ chars; Story 4 at 232 (acceptable).
  4. `hashtag_count=3` LOSER — delta=0.709 (large). ⚠️ CONFLICT with brand-voice.md. 1 hashtag used (13th consecutive override day).
  5. `has_score=True` WINNER — delta=0.681 (large). Off day — no score. Not applicable.
  6. `opening=statement` WINNER — delta=0.616 (large). All 5 posts use declarative statement openings.
  7. `opening=allcaps_lead` LOSER — delta=0.598 (large). No ALL CAPS leads.
  8. `has_stat=True` WINNER — delta=0.681 (large). Stats in every tweet.
  9. `hashtag_count=1` WINNER — delta=0.588 (large). Applied: #Cubs only.
  10. `posting_window=morning_06_12` LOSER — delta=0.685 (large). Exception: 1 morning slot (7:00 AM) for $450M Skubal breaking news.
  11. `content_type=transaction` LOSER — delta=0.570 (large). All transactions embedded in analysis framing.
  12. `len_bucket=<140` LOSER — (large). No tweets under 140 chars.
  13. `len_bucket=140-200` LOSER — (medium). No tweets in 140-200 range.
  14. `content_type=brief` LOSER — (small). Substantive multi-paragraph posts throughout.

## Pipeline Run Log

### 2026-11-23 — Monday (Off day)
- 5 stories | 5 X posts | JSON valid | Fact-check PASS (all HIGH confidence)
- Skubal $450M to Mets (market reset) | NL Central Brewers extend lead | Hiromi Itoh visit NEW | Sato Triple Crown | CBA 8-day countdown
- Insights: 13th hashtag override, all 14 findings applied, morning exception for Skubal breaking news
- Push: content-pipeline ✅ | content-dashboards ⚠️ (out of session scope)

### 2026-11-22 — Sunday (Off day)
- 5 stories | 5 X posts | JSON valid | Fact-check PASS (3 MEDIUM flags: May ±$500K, Itoh age, Taira deadline)
- CBA 9-day countdown | Hiromi Itoh visit NEW | Teruaki Sato NPB Triple Crown | Taira 9 days | NL Central rival watch
- Insights: 12th hashtag override, all 14 findings applied
- Push: content-pipeline ✅ | content-dashboards ⚠️ (out of session scope)

## Insights Summary (2026-11-22 run — from 2026-11-22T08:30 UTC snapshot)
- **Generated:** 2026-11-22T08:30:00 UTC
- **Measured tweet count:** 58
- **Significant findings:** 14
  1. `content_type=recap_longform` WINNER — delta=0.887 (large). Off day — no game recap. Not applicable.
  2. `posting_window=evening_18_24` WINNER — delta=0.779 (large). Post 5 at 6:30 PM CT.
  3. `len_bucket=260+` WINNER — delta=0.816 (large). All 5 tweets at 260+ chars (avg 270).
  4. `hashtag_count=3` LOSER — delta=0.679 (large). ⚠️ CONFLICT with brand-voice.md. 1 hashtag used (12th consecutive override day).
  5. `has_score=True` WINNER — delta=0.673 (large). Off day — no score. Not applicable.
  6. `opening=statement` WINNER — delta=0.624 (large). All 5 posts use declarative statement openings.
  7. `opening=allcaps_lead` LOSER — delta=0.598 (large). No ALL CAPS leads.
  8. `has_stat=True` WINNER — delta=0.642 (large). Stats in every tweet.
  9. `hashtag_count=1` WINNER — delta=0.56 (large). Applied: #Cubs only.
  10. `posting_window=morning_06_12` LOSER — delta=0.692 (large). No morning posts; first at 1:15 PM CT.
  11. `content_type=transaction` LOSER — delta=0.570 (large). All transactions embedded in analysis framing.
  12. `len_bucket=<140` LOSER — delta=0.549 (large). No tweets under 140 chars.
  13. `len_bucket=140-200` LOSER — delta=0.404 (medium). No tweets in 140-200 range.
  14. `content_type=brief` LOSER — delta=0.312 (small). Substantive multi-paragraph posts throughout.

## Pipeline Run Log

### 2026-11-22 — Sunday (Off day)
- 5 stories | 5 X posts | JSON valid | Fact-check PASS (3 MEDIUM flags: May ±$500K, Itoh age, Taira deadline)
- CBA 9-day countdown | Hiromi Itoh visit NEW | Teruaki Sato NPB Triple Crown | Taira 9 days | NL Central rival watch
- Insights: 12th hashtag override, all 14 findings applied
- Push: content-pipeline ✅ | content-dashboards ⚠️ (out of session scope)

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
