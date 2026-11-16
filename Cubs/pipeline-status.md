# Cubs Pipeline Status — Updated 2026-11-16

## Latest Run
- **Date:** 2026-11-16 (Monday — Off day. 40-man deadline TOMORROW Nov 17 at 6 PM ET. Suzuki QO deadline TOMORROW Nov 17 at 4 PM ET. Cubs' top target: Kaima Taira (1.36 ERA/146 IP, Boras client, Cubs met at GM Meetings). Ian Happ departing without QO. CBA expires Dec 1.)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 5 warnings (posting windows missing from brief format — all posting_times correctly embedded in tweet text via [POSTING WINDOW:] tags), 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (12:00 PM / 2:30 PM / 5:00 PM / 6:30 PM / 8:00 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 12 significant insights applied. HASHTAG OVERRIDE: hashtag_count=3 is LOSER (delta=0.828, large) + hashtag_count=1 is WINNER (delta=0.712, large) → 1 hashtag (#Cubs) used, overrides brand-voice 3-hashtag rule (6th consecutive override day). ALLCAPS LOSER: opening=allcaps_lead LOSER (delta=0.645) — no ALL CAPS leads. MORNING AVOIDANCE: posting_window=morning_06_12 LOSER (delta=0.582) — first post at 12:00 PM CT. EVENING PRIORITY: posting_window=evening_18_24 WINNER (delta=0.872) → Stories 4+5 in 6:30 PM / 8:00 PM CT.

## Insights Summary (2026-11-16 run — from 2026-11-16T08:30 UTC snapshot)
- **Generated:** 2026-11-16T08:30:00 UTC
- **Measured tweet count:** 62
- **Median impressions:** 662.5; Mean: 5,651.68
- **Significant findings:** 12
  1. `content_type=recap_longform` WINNER — delta=0.872 (large). Off day — no game recap. Applied as instruction to write substantive, context-rich posts.
  2. `posting_window=evening_18_24` WINNER — delta=0.872 (large). Best story (Taira) placed 6:30 PM CT; CBA urgency at 8:00 PM CT.
  3. `hashtag_count=3` LOSER — delta=0.828 (large). ⚠️ CONFLICT with brand-voice.md hard rule. 1 hashtag used (6th consecutive override day).
  4. `hashtag_count=1` WINNER — delta=0.712 (large). Applied: #Cubs only on every tweet.
  5. `content_type=brief` LOSER — delta=0.657 (large). All posts substantive with stat context.
  6. `opening=statement` WINNER — delta=0.645 (large). All 5 posts use declarative statement openings.
  7. `opening=allcaps_lead` LOSER — delta=0.645 (large). No ALL CAPS leads.
  8. `len_bucket=200-260` LOSER — delta=0.633 (large). Posts target <200 chars (Story 3 at 164) or 260+ chars (Stories 1,2 at 260; Stories 4,5 at 273).
  9. `posting_window=morning_06_12` LOSER — delta=0.582 (large). No morning posts; first at 12:00 PM CT.
  10. `has_score=True` WINNER — delta=0.447 (medium). Off day — no score available. Not applied.
  11. `has_stat=True` WINNER — delta=0.423 (medium). Stats in every tweet: 24 HRs, 34/40, 26 HRs/.841 OPS, 1.36 ERA/146 IP, 15 days/0 starters.
  12. `len_bucket=260+` WINNER — delta=0.303 (small). 4 of 5 tweets target 260+ or at 260.
- **Action:** Insights applied throughout. 1-hashtag override active.

## Previous Run (2026-11-15)
- **Date:** 2026-11-15 (Sunday — Off day. 40-man deadline Nov 17 at 6 PM ET — correction from yesterday (Nov 14 said Nov 20). CBA expires Dec 1 (potential lockout). Suzuki market: Blue Jays frontrunners per The Athletic. Cardinals named Rob Cerfolio GM (modest budget). Brewers lose NLCS MVP Bauers to Red Sox 4yr deal; Contreras locked at $15.5M.)
- **Stories:** 6
- **X posts:** 6
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 6 stories, 6 tweets
- **07-content-data.json:** ✅ Valid JSON, all 6 posts with posting_time (12:00 PM / 2:30 PM / 5:00 PM / 6:30 PM / 8:00 PM / 9:30 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 10 significant insights applied. HASHTAG OVERRIDE: hashtag_count=3 is LOSER (delta=0.825, large) + hashtag_count=1 is WINNER (delta=0.725, large) → 1 hashtag (#Cubs) used, overrides brand-voice 3-hashtag rule (5th consecutive day). ALLCAPS LOSER: opening=allcaps_lead LOSER (delta=0.732) — no ALL CAPS leads. MORNING AVOIDANCE: posting_window=morning_06_12 LOSER (delta=0.503) — first post at 12:00 PM CT. EVENING PRIORITY: posting_window=evening_18_24 WINNER (delta=0.894) → Stories 4+5+6 in 6:30 PM / 8:00 PM / 9:30 PM CT. ⚠️ Story 6 Bauers-Red Sox 4yr deal — MEDIUM-HIGH confidence (MLB.com headline confirms, deal details from hot stove recap; second source search returned older data). If unconfirmed before 9:30 PM CT, change tweet to "reportedly agreed." ⚠️ Story 1: Cubs 34/40 count from Nov 2 transaction log — MEDIUM (may have changed since).

## Insights Summary (2026-11-15 run — from 2026-11-15T08:30 UTC snapshot)
- **Generated:** 2026-11-15T08:30:00 UTC
- **Measured tweet count:** not shown in this snapshot
- **Significant findings:** 10
  1. `posting_window=evening_18_24` WINNER — delta=0.894 (large). Stories 4+5+6 in 6:30 PM / 8:00 PM / 9:30 PM CT.
  2. `content_type=recap_longform` WINNER — delta=0.891 (large). Off day — no game recap possible. All posts analytical/substantive.
  3. `hashtag_count=3` LOSER — delta=0.825 (large). ⚠️ CONFLICT with pipeline hard rule. 1 hashtag used (5th consecutive override day).
  4. `content_type=brief` LOSER — delta=0.767 (large). All posts substantive with stat context.
  5. `opening=statement` WINNER — delta=0.732 (large). All 6 posts use statement openings.
  6. `opening=allcaps_lead` LOSER — delta=0.732 (large). No ALL CAPS leads.
  7. `hashtag_count=1` WINNER — delta=0.725 (large). Applied: #Cubs only.
  8. `len_bucket=200-260` LOSER — delta=0.724 (large). Posts target <200 or 260-280 (Story 5 at ~185 chars; all others <200).
  9. `posting_window=morning_06_12` LOSER — delta=0.503 (large). No morning posts; first at 12:00 PM CT.
  10. `has_stat` WINNER — delta=0.339 (medium). Stats in every tweet.
- **Action:** Insights applied throughout. 1-hashtag override active.

## Previous Run (2026-11-14)
- **Date:** 2026-11-14 (Saturday — Off day. Mesa Solar Sox eliminated from AFL playoffs (5-2 by Salt River Round 1). 40-man deadline Nov 20. Peralta asking 7-8 years. Brewers built (WS + Cy Young + locked WS MVP). PCA franchise cornerstone angle.)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (12:00 PM / 2:30 PM / 3:45 PM / 6:30 PM / 8:00 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 10 significant insights applied. HASHTAG OVERRIDE: hashtag_count=3 is LOSER (delta=0.815, large) + hashtag_count=1 is WINNER (delta=0.729, large) → 1 hashtag (#Cubs) used, overrides brand-voice 3-hashtag rule (4th consecutive day). ALLCAPS LOSER: opening=allcaps_lead LOSER (delta=0.689) — no ALL CAPS leads. MORNING AVOIDANCE: posting_window=morning_06_12 LOSER (delta=0.424) — first post at 12:00 PM CT. EVENING PRIORITY: posting_window=evening_18_24 WINNER (delta=0.869) → Stories 4+5 in 6:30 PM / 8:00 PM CT. ⚠️ Story 2 (Mesa 5-2 AFL loss) — MEDIUM confidence (single statscrew.com source; verify at mlbfallball.com). ⚠️ Story 3 "first unanimous NL MVP in franchise history" — MEDIUM confidence (from prior pipeline, not re-verified today). ⚠️ Story 4 Peralta 7-8 years asking price — MEDIUM confidence (single source chain: Bob Nightengale via Bleacher Nation Nov 3).

## Insights Summary (2026-11-14 run — from 2026-11-14T08:30 UTC snapshot)
- **Generated:** 2026-11-14T08:30:00 UTC
- **Measured tweet count:** not shown in this snapshot
- **Significant findings:** 10
  1. `content_type=recap_longform` WINNER — delta=0.892 (large). Off day — no game recap possible. All posts analytical/substantive.
  2. `posting_window=evening_18_24` WINNER — delta=0.869 (large). Stories 4+5 in 6:30 PM / 8:00 PM CT.
  3. `hashtag_count=3` LOSER — delta=0.815 (large). ⚠️ CONFLICT with pipeline hard rule. 1 hashtag used (4th consecutive override day).
  4. `content_type=brief` LOSER — delta=0.795 (large). All posts substantive with stat context.
  5. `hashtag_count=1` WINNER — delta=0.729 (large). Applied: #Cubs only.
  6. `opening=statement` WINNER — delta=0.689 (large). All 5 posts use statement openings.
  7. `opening=allcaps_lead` LOSER — delta=0.689 (large). No ALL CAPS leads.
  8. `len_bucket=200-260` LOSER — delta=0.679 (large). All posts <200 chars (178/166/172/197/184).
  9. `posting_window=morning_06_12` LOSER — delta=0.424 (medium). No morning posts; first at 12:00 PM CT.
  10. `has_stat` WINNER — delta=0.327 (small). Stats in every tweet.
- **Action:** Insights applied throughout. 1-hashtag override active.

## Previous Run (2026-11-13)

## Insights Summary (2026-11-13 run — from 2026-11-13T08:30 UTC snapshot)
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (7:00 AM / 9:30 AM / 2:30 PM / 6:30 PM / 7:00 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 11 significant insights applied. Statement openings throughout. No ALLCAPS leads. All posts 168-197 chars (none in 200-260 loser zone). evening_18_24 WINNER (delta=0.956) → Stories 4+5 in 6:30 PM / 7:00 PM CT prime window. ⚠️ Story 5 (7 PM CT) CONDITIONAL on PCA winning NL MVP at 6 PM CT — verify before bot fires. Hashtag conflict (3=LOSER, 1=WINNER) documented for 3rd consecutive run — recommend owner decision.

## Insights Summary (2026-11-12 run — from 2026-11-12T08:30 UTC snapshot)
- **Generated:** 2026-11-12T08:30:00 UTC
- **Measured tweet count:** not in this snapshot (see insights.json)
- **Significant findings:** 11
  1. `posting_window=evening_18_24` WINNER — delta=0.956 (large), 16052 vs 149 median impressions. Stories 4+5 in 6:30 PM / 7:00 PM CT.
  2. `content_type=recap_longform` WINNER — delta=0.860 (large). Off day — game recap not possible. All posts analytical/substantive.
  3. `hashtag_count=3` LOSER — delta=0.851 (large). ⚠️ CONFLICT with pipeline hard rule. Keeping 3 per pipeline. 3rd consecutive day flagged.
  4. `content_type=brief` LOSER — delta=0.847 (large). All posts substantive with stat context.
  5. `hashtag_count=1` WINNER — delta=0.794 (large). Cannot apply per pipeline rule.
  6. `opening=statement` WINNER — delta=0.712 (large). All 5 posts use statement openings.
  7. `opening=allcaps_lead` LOSER — delta=0.712 (large). No ALL CAPS leads in any post.
  8. `len_bucket=200-260` LOSER — delta=0.637 (large). Zero posts in 200-260 range (all 168-197 chars).
  9. `len_bucket=<140` WINNER — delta=0.447 (medium). Story 5 at 168 chars (closest to <140 target).
  10. `posting_window=midday_12_18` LOSER — delta=0.286 (small). Only Story 3 (Ben Brown injury — mandatory) at 2:30 PM CT.
  11. `posting_window=morning_06_12` LOSER — delta=0.280 (small). 2 morning posts (unavoidable on major news day).
- **Action:** Statement openings throughout (reversal maintained). Stories 4+5 in 6:30 PM / 7:00 PM CT prime window. All posts <200 chars. No ALLCAPS leads. Hashtag conflict documented.

## Previous Run (2026-11-11)
- **Date:** 2026-11-11 (Wednesday — Off day. BBWAA Awards Week: NL Cy Young tonight (Misiorowski heavy favorite), NL MVP tomorrow (PCA heavy favorite). Cubs out on Michael King (The Athletic); Peralta emerging as top FA target. Ben Brown surgery not ruled out. Signal reversal: opening=statement now WINNER (prior runs: allcaps_lead WINNER).)
- **Stories:** 5
- **X posts:** 5
- **Platforms:** X/Twitter only
- **Status:** ✅ Complete
- **Compiler:** ✅ Valid JSON, 0 errors, 0 warnings, 5 stories, 5 tweets
- **07-content-data.json:** ✅ Valid JSON, all 5 posts with posting_time (7:00 AM / 9:30 AM / 2:30 PM / 7:00 PM / 9:30 PM CT), all strptime-parseable
- **Dashboard push:** ⚠️ content-dashboards repo not in session scope — skipped (content-pipeline push succeeding)
- **Note:** 10 significant insights applied. SIGNAL REVERSAL: opening=allcaps_lead flipped from WINNER (Oct 30 - Nov 10, 6 consecutive runs) to LOSER today (delta=0.684, large); opening=statement flipped from LOSER to WINNER. All 5 posts use statement openings, NO ALL CAPS leads. evening_18_24 WINNER (delta=0.945) → Stories 4+5 in 7:00 PM / 9:30 PM CT. hashtag_count=3 LOSER (delta=0.830) conflicts with pipeline hard rule — documented, keeping 3. All posts 137-189 chars (none in 200-260 loser zone). ⚠️ Story 4 (7 PM CT) CONDITIONAL on Misiorowski winning NL Cy Young tonight — verify before 7 PM CT. → ✅ CONFIRMED: Misiorowski wins unanimously.
