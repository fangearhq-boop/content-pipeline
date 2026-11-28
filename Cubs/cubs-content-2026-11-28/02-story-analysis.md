# Cubs Story Analysis — 2026-11-28

## Overview

Today is Saturday, November 28 — an off day, three days before the December 1 CBA expiration. Two major developments broke Friday night: Hiromi Itoh's agreement was confirmed by the AP, ESPN, and MLB.com, and Trevor Rogers' physical was confirmed by Bob Nightengale. This is a genuinely big news day despite being an off day: the Cubs completed their Japanese-arm pursuit and their first rotation agreement went official. Five stories planned.

---

### Insights Applied

**Data window:** 21 days, 55 measured tweets. Generated 2026-11-28T08:30:00Z.

**Findings consumed (13 significant findings — all applied):**

1. **content_type=recap_longform WINNER** (delta=0.908, large; median 10,721 vs 1,912 impressions)
   → Added Story 5: Nightly recap longform at 9:30 PM CT. The pipeline has not been using this format recently (Nov 24-27 had no nightly recap). The data strongly supports restoring it. **This reintroduces the highest-performing format.**

2. **len_bucket=260+ WINNER** (delta=0.755, large; median 6,782 vs 807)
   → All five individual tweets drafted at 260-280 chars. The nightly recap longform is intentionally longer (the 260+ bucket captures all long posts; top performers in the data are 1,000-1,900 chars, suggesting X Premium long-form is in use).
   → **CONFLICT NOTE:** The prompt instructions say "Every tweet ≤ 280 chars including newlines and hashtags" and _engine/CLAUDE.md says "Absolute limit: 280 characters." However, the data's top-5 performers are all 1,200-1,900 chars (recap_longform type). These cannot be under 280 chars — they must be X Premium long posts. Following the data for Story 5 (recap_longform), keeping Stories 1-4 at ≤280 chars.

3. **posting_window=evening_18_24 WINNER** (delta=0.737, large; median 8,712 vs 1,510)
   → 3 of 5 posts in evening window (6:30 PM, 8:00 PM, 9:30 PM). The other 2 are at 1:15 PM and 3:45 PM (Tier 1 Itoh/Rogers exceptions).

4. **has_score=True WINNER** (delta=0.693, large)
   → Not applicable today (off day, no game scores). Skipped.

5. **posting_window=morning_06_12 LOSER** (delta=0.667, large)
   → Strictly observed: 0 morning posts today.

6. **opening=allcaps_lead LOSER** (delta=0.580, large)
   → No tweet opens with ALL CAPS. All story tweets begin with a statement.

7. **hashtag_count=1 WINNER** (delta=0.580, large)
   → 1 hashtag (#Cubs) only. 18th consecutive day of overriding the brand-voice/prompt "exactly 3 hashtags" rule based on data. The data is unambiguous and stable.
   → **CONFLICT NOTE:** Prompt says "Exactly 3 hashtags per tweet on ONE line, space-separated, first one #Cubs." `significant_findings` override rule applied. Continuing established override.

8. **has_stat=True WINNER** (delta=0.540, large)
   → Stats included in all five posts: Itoh's ERA/IP/walks, Rogers' ERA/IP/K, King's ERA, Horton/Brown return timelines.

9. **has_allcaps=True WINNER** (delta=0.532, large)
   → ALLCAPS used mid-tweet in all posts (REBUILT, OFFICIAL, LOCKED, etc.), never as the opening word.

10. **content_type=brief LOSER** (delta=0.480, large)
    → No standalone briefs. Each post has substantive context and analysis.

11. **len_bucket=140-200 LOSER** (delta=0.479, large)
    → All tweets targeted at 260+ chars. Confirmed at drafting.

12. **opening=statement WINNER** (delta=0.429, medium)
    → All tweets start with declarative statements about the Cubs or the news event.

13. **posting_window=midday_12_18 LOSER** (delta=0.410, medium)
    → Minimized. Only 2 midday slots used (1:15 PM and 3:45 PM), both for Tier 1 breaking news (Itoh agreement, Rogers confirmation). Both are unavoidable given news prominence.

---

### Series Context

**Series context snapshot:** off_day=true, is_series_start_today=false, series=null, today_cubs_game=null.
**Rationale:** No upcoming Cubs game on today's CT calendar date.

**Applied:** No series-preview tweet. No game-related content. Leaning into offseason hot stove news (Itoh, Rogers, rotation outlook, CBA). This is correct per instructions — off day, so prospect news, roster moves, division watch.

---

## Story-by-Story Analysis

### STORY 1: Hiromi Itoh — Cubs Agreed Terms
**Selected:** YES — Tier 1
**Why:** This is the top story of the day. Multiple major outlets (AP, ESPN, MLB.com, NBC Sports) reported the agreement Friday night. This is a NEW signing not covered in yesterday's pipeline. The Cubs just locked in Japan's 2025 Sawamura Award winner before the Dec 1 lockout.
**Angle:** Informative/breaking. Statement opening (not allcaps). Stats front-loaded (3.18 ERA, 172.2 IP, 34 walks). One hashtag.
**Previous coverage:** Itoh was covered Nov 25 (CBA window), Nov 26 (decision imminent), Nov 27 (last quality arm) — all as PENDING. Today: AGREED. New news, different angle.
**Hook:** "The Cubs agreed to terms with Hiromi Itoh — Japan's best pitcher in 2025."
**Slot:** 1:15 PM CT (midday LOSER — Tier 1 exception)

### STORY 2: Trevor Rogers — Now Official
**Selected:** YES — Tier 1
**Why:** Rogers passing his physical and the deal becoming official is newsworthy confirmation. Fans care when "pending physical" becomes real. This is a different angle from Nov 24's initial agreement coverage.
**Angle:** Confirmation. Statement opening. Lead with the confirmed fact (physical passed, deal official). Include his best stretch stats (2.90 ERA, final 20 starts) to validate the investment.
**Previous coverage:** Nov 24 as breaking agreement. Nov 25 as "physical still pending." Today: OFFICIAL. New status.
**Hook:** "Trevor Rogers passed his physical Friday. The 5-year, $120 million deal is now OFFICIAL."
**Slot:** 3:45 PM CT (midday LOSER — Tier 1 exception, strong confirmation news)

### STORY 3: 2027 Rotation — Where It Stands Now
**Selected:** YES — Tier 2
**Why:** With both Rogers official and Itoh agreed in the last 24 hours, this is the first time the full rotation picture can be drawn. Fans want to see the visual breakdown. This is fresh analysis enabled by today's news.
**Angle:** Breakdown list format (LOCKED IN / RETURNING). Statement opening. ALLCAPS section headers. Stats for depth.
**Previous coverage:** Partial rotation pieces on Nov 24-27. This is the first post-Itoh full picture.
**Hook:** "Where the Cubs 2027 rotation stands — right now, post-Itoh:"
**Slot:** 6:30 PM CT (evening WINNER)

### STORY 4: CBA Phoenix / 3 Days
**Selected:** YES — Tier 2
**Why:** Dec 1 is 3 days away. Last-ditch Phoenix meeting is happening THIS WEEKEND. The CBA countdown has been a daily story since Nov 15, but today's angle is specific: face-to-face weekend talks, 3 days left, Cubs have their pieces in place.
**Angle:** Urgency. Statement opening ("Three days until baseball shuts down."). Data-backed (MLB cap numbers, union position). Cubs angle as kicker.
**Previous coverage:** CBA countdown covered daily. Today's specific hook: Phoenix face-to-face talks + "Cubs beat the clock."
**Slot:** 8:00 PM CT (evening WINNER)

### STORY 5: Nightly Recap Longform — 9:30 PM CT
**Selected:** YES — Tier 1 recap
**Why:** `content_type=recap_longform` has by far the highest median impressions (10,721) in the dataset. The "In case you missed Cubs news today:" format is the best-performing content type. With four major stories today (Itoh, Rogers, rotation, CBA), this is the right day to run the full digest.
**Angle:** Evening summary digest. All four stories, plus Michael King status. Standard "In case you missed" header with bullet points.
**Length:** ~1,200 chars (X Premium long post). See conflict note in Insights Applied section.
**Slot:** 9:30 PM CT (evening WINNER)

---

## Stories Skipped

- **Michael King dedicated tweet:** Covered yesterday (Nov 27, 3:45 PM). No new development. Mentioned in Stories 3 and 5 as context. No dedicated tweet today.
- **Prospect news:** No fresh November 2026 Iowa/Tennessee developments found. Skipped.
- **NL Central rivals:** No specific Nov 28 transaction news. Brewers/Cardinals referenced contextually.
- **Teruaki Sato physical update:** MLB.com transaction shows Nov 25 date — appears official. Already covered Nov 24-26. No new angle for today.
