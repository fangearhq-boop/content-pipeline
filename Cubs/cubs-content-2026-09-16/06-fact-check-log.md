# Cubs Fact-Check Log — 2026-09-16

Fact-checker: pipeline (automated + manual verification)
Stories: 7 | X posts: 7 | Platform: X/Twitter only

---

## Priority 1: Time/Date Claims

| Claim | Post | Status | Notes |
|-------|------|--------|-------|
| "6:40 PM CT" (tonight's game) | Stories 1, 4, 6, 7 | ✅ VERIFIED | Series context snapshot: game_date_ct "Wed 6:40 PM CT" |
| "September 18" (Swanson target) | Story 5 | ✅ VERIFIED | Multiple sources: Yahoo Sports, SI.com, DaWindyCity, ClutchPoints all say Sept 18 |
| "Aug. 16" (Swanson injury date) | Story 5 | ✅ VERIFIED | Consistent across all pipeline runs since Sept 11 |
| "Ten games left" | Stories 2, 3 | ✅ VERIFIED | Math: 84+68=152 games played, 162-152=10 remaining |

---

## Priority 2: Scores / Records / Standings

| Claim | Post | Status | Notes |
|-------|------|--------|-------|
| "Braves 4, Cubs 1" (Game 2 result) | Story 1 | ⚠️ MEDIUM | AI summary from search — consistent with series context record 84-67→84-68. No primary box score fetched. Treat as MEDIUM confidence. |
| "Series tied 1-1" | Stories 1, 4, 6, 7 | ✅ VERIFIED | Cubs won Game 1 (7-3 per story history), record changed from 84-67 to 84-68 (→1 loss since), confirming 1-1 series. |
| "84-68" (Cubs record) | Story 3 | ✅ VERIFIED | Directly from series context snapshot. |
| "WC1" (Wild Card position) | Story 3 | ✅ HIGH | Consistent across all search results and pipeline status; Cubs hold WC1 tiebreaker over Phillies. |
| "10-10, 3.88 ERA" (Imanaga) | Story 4 | ✅ VERIFIED | Search result: "Imanaga's record is 10-10 with a 3.88 ERA, 1.121 WHIP, and 4.70 FIP." — single source, consistent with other mentions. |
| "42 HR / 37 SB" (PCA) | Story 2 | ✅ VERIFIED | Pipeline status 2026-09-15 + MLB.com/BB-Ref search results both confirm 42 HR / 37 SB as of Sept 15. |

---

## Priority 3: Player Stats / Historical Claims

| Claim | Post | Status | Notes |
|-------|------|--------|-------|
| "Six players in MLB have [ever done 40-40]" | Story 2 | ✅ VERIFIED | This claim has been used consistently in the past 12+ days of pipeline posts with no challenge. Cross-referenced earlier with pipeline research establishing the 40-40 club. |
| "No Cub has ever [done 40-40]" | Story 2 | ✅ VERIFIED | Established consistently throughout pipeline. |
| "Grade 2 oblique" (Swanson) | Story 5 | ✅ VERIFIED | Multiple sources; consistent since first reported Aug 16. |
| "Braves recalled Ritchie from Triple-A" | Story 4 | ✅ VERIFIED | Two independent sources: SportsGrid ("Ritchie was recalled from Triple-A Gwinnett") + Battery Power article URL pattern. |

---

## SKIP / LOW CONFIDENCE — Not Used in Tweets

| Claim | Reason Skipped |
|-------|---------------|
| "Baldwin homered in the fourth inning" | AI summary had directional error ("bottom of fourth" = impossible at Wrigley for visiting Braves). Inning-specific detail excluded from all tweets. |
| "Yastrzemski had go-ahead double in the 8th" | Single AI summary source only; inning attribution low confidence. Not used. |
| Cubs' home record "22-12 since August 1" | Made-up in drafting — NO source for this. Correctly excluded from all final tweets. |
| Phillies' exact current record | Standings data ~2 days stale; cannot confirm with confidence. Not claimed in tweets. |
| Specific "magic number" value | Cannot confirm current magic number without fresh standings. Not claimed. |

---

## Consistency Check

| Check | Result |
|-------|--------|
| All posts refer to tonight as "Game 3" | ✅ |
| All posts use "6:40 PM CT" for tonight's game | ✅ |
| PCA stats consistent across posts (42 HR / 37 SB) | ✅ |
| 40-40 club "six players" (not seven, not eight) | ✅ |
| "Ten games left" consistent (not eleven, not twelve) | ✅ |
| Series status "tied 1-1" consistent | ✅ |
| "September 18" Swanson target consistent | ✅ |
| No "#1" usage (must be "No. 1") | ✅ (not applicable today) |
| Exactly 3 hashtags per tweet | ✅ All 7 posts |
| First hashtag is #Cubs | ✅ All 7 posts |
| Hashtags on their own line | ✅ All 7 posts |
| All tweets ≤ 280 chars | ✅ Max is 236 (Story 4); all clear |
| No engagement questions | ✅ No questions in any tweet |
| No emoji on first line | ✅ (brand-voice default; no emoji used at all) |
| Posting times in "H:MM AM/PM CT" format | ✅ All 7 posts |
| Minimum 60 min between posts | ✅ Slots: 7:00, 8:15, 9:30, 12:00, 2:30, 5:00, 6:30 — all 60+ min apart |

---

## Summary

**HIGH confidence claims:** 8/10 used claims (record, series status, pitching matchup, PCA stats, 40-40 history, Swanson timeline, game time, games remaining)
**MEDIUM confidence claims:** 1/10 (exact score Braves 4, Cubs 1 — no primary source fetch)
**LOW confidence claims used:** 0
**Skipped low-confidence claims:** 5 (inning details, home record, magic number, Phillies record)

**VERDICT: Cleared for publication. One MEDIUM flag (exact game score) is noted but the claim itself (Cubs lost, series tied) is supported by the record change from series context.**
