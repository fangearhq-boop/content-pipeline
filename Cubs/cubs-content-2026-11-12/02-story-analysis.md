# Story Analysis — 2026-11-12

**Day type:** OFF DAY (Offseason — BBWAA Awards Week, Day 2)
**Key anchor:** NL MVP announced tonight at 6 PM CT. PCA overwhelmingly favored.

---

## Series Context

**Case:** `off_day=true`, `is_series_start_today=false`. No Cubs game today.

Offseason, BBWAA Awards Week. No series preview slot needed. Lean into awards, roster moves, offseason news. Hot stove content is the daily slate.

---

## Insights Applied

### Findings from 2026-11-12T08:30 UTC snapshot (11 significant findings)

| # | Finding | Effect | Applied |
|---|---------|--------|---------|
| 1 | `posting_window=evening_18_24` WINNER | delta=0.956 (large) | Scheduled 3 of 5 posts in 6:30–8:15 PM CT window |
| 2 | `content_type=recap_longform` WINNER | delta=0.860 (large) | Off day — game recap not possible. All posts are substantive/analytical, not brief. |
| 3 | `hashtag_count=3` LOSER | delta=0.851 (large) | ⚠️ **CONFLICT** with pipeline hard rule (brand-voice.md: "Exactly 3 hashtags per tweet"). Keeping 3 per pipeline rule. Documented for second consecutive day. |
| 4 | `content_type=brief` LOSER | delta=0.847 (large) | All posts are substantive with stat context, not brief one-liners. |
| 5 | `hashtag_count=1` WINNER | delta=0.794 (large) | ⚠️ **CONFLICT** — cannot apply without overriding pipeline rule. |
| 6 | `opening=statement` WINNER | delta=0.712 (large) | All 5 posts open with declarative statements. |
| 7 | `opening=allcaps_lead` LOSER | delta=0.712 (large) | Zero ALL CAPS leads in any post. |
| 8 | `len_bucket=200-260` LOSER | delta=0.637 (large) | All posts kept under 200 chars. |
| 9 | `len_bucket=<140` WINNER | delta=0.447 (medium) | Targeted <140 where possible; none exceed 199 chars. |
| 10 | `posting_window=midday_12_18` LOSER | delta=0.286 (small) | Minimized midday slots; only Story 3 (Ben Brown injury — mandatory news) placed at 2:30 PM CT. |
| 11 | `posting_window=morning_06_12` LOSER | delta=0.280 (small) | Morning slots underperform, but off-day news requires 2 morning posts. Kept to minimum. |

**Net scheduling impact:** 3 of 5 posts in evening_18_24 (the massive winner window). Only 1 post in pure midday window. 2 morning posts (unavoidable for top-of-day coverage on a heavy-news day).

**Hashtag conflict note (3rd consecutive day):** `hashtag_count=3` LOSER (delta=0.851) and `hashtag_count=1` WINNER (delta=0.794) are the second and fifth strongest signals in the dataset. The pipeline hard rule overrides. This conflict should be surfaced to the account owner for a formal decision — the data strongly and consistently suggests reducing to 1 hashtag would improve reach.

---

## Story Selection

### STORY 1: PCA NL MVP Tonight — Hype Preview
- **Angle:** NL MVP announced TONIGHT at 6 PM CT. PCA is the -1500 favorite: 45 HR, 41 SB (40-40 club), Gold Glove, Platinum Glove. First Cubs NL MVP since Kris Bryant in 2016 would be history.
- **Tier:** 1
- **Slot:** 7:00 AM CT (morning — necessary top-of-day anchor for biggest story of the week)
- **Follow-up:** Story 5 (7:00 PM CT — reaction/celebration post after announcement)

### STORY 2: Misiorowski Wins NL Cy Young — Unanimous
- **Angle:** Result confirmed yesterday. Brewers now have World Series + unanimous NL Cy Young in same year. Cubs division context: blank rotation vs. a team with the best pitcher in the NL.
- **Tier:** 2
- **Slot:** 9:30 AM CT (morning — rivalry angle/follow-up to yesterday's conditional coverage)
- **Source:** Yahoo Sports, CBS Sports (Nov 11)

### STORY 3: Ben Brown Cervical Spine Surgery
- **Angle:** Surgery confirmed Nov 9 — C5 vertebra, stress fracture stabilized. Expected back first half of 2027. Cubs lose their most exciting internal rotation arm at the worst possible time — entering an offseason where they need 3 SPs.
- **Tier:** 1
- **Slot:** 2:30 PM CT (midday — loser window, but injury news warrants coverage regardless)
- **Source:** MLB.com, ESPN, CBS Sports (Nov 9-11)

### STORY 4: Suzuki Declines QO, Tests Free Agency
- **Angle:** Agent confirmed Nov 11 at GM Meetings. Suzuki turning down $23.15M QO to explore market. Cubs can still re-sign him, but other teams are now in play. Adds to the offseason complexity — pitching AND right field both open.
- **Tier:** 2
- **Slot:** 6:30 PM CT (entering evening_18_24 WINNER window)
- **Source:** NBC Sports, Bleacher Nation, Cubshq.com

### STORY 5: PCA WINS NL MVP — Celebration (CONDITIONAL)
- **Angle:** Assuming PCA wins (announced at 6 PM CT). First Cubs NL MVP since Kris Bryant in 2016. The 45 HR/41 SB/Gold Glove/Platinum Glove season gets its crown jewel. Reaction post.
- **Tier:** 1
- **Slot:** 7:00 PM CT (prime evening_18_24 WINNER window — peak reach)
- **⚠️ CONDITIONAL:** If Ohtani or Turang wins instead, this post must be updated before 7 PM CT. PCA odds: -1500 (essentially certain), but flag for verification.
- **Source:** Announcement on MLB Network 6 PM CT

### (STORY 6 SKIPPED — Kaima Taira)
- Considered a 6th post for 8:15 PM CT on Kaima Taira FA interest.
- Skipped because: Taira NPB posting hasn't been formally filed yet; content would be speculative rumor-level. Better to wait for concrete news. Per brand-voice: "No filler" and "Every tweet must be anchored to a specific news story."

---

## Slots Used: 5 of 12 available
- 7:00 AM CT — Story 1 (PCA MVP preview)
- 9:30 AM CT — Story 2 (Misiorowski Cy Young result)
- 2:30 PM CT — Story 3 (Ben Brown surgery)
- 6:30 PM CT — Story 4 (Suzuki declines QO)
- 7:00 PM CT — Story 5 (PCA wins NL MVP — conditional, reaction)

**Evening window (18-24 CT) coverage:** 2 posts (6:30 PM + 7:00 PM) — optimized for the top-performing reach window.
