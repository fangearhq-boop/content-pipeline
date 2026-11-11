# Cubs Story Analysis — 2026-11-11

---

## ### Insights applied

**Snapshot generated:** 2026-11-11T08:30:00+00:00
**Measured tweet count:** 66
**Significant findings:** 10 (all large effect except #10 medium)

| # | Dimension | Winner | Effect | Delta | Action taken |
|---|-----------|--------|--------|-------|--------------|
| 1 | posting_window | evening_18_24 | large | 0.945 | Stories 4+5 placed in 7:00 PM and 9:30 PM CT slots |
| 2 | content_type | not_brief | large | 0.899 | All 5 posts are substantive (analysis, transaction, injury, reaction, hype) |
| 3 | content_type | recap_longform | large | 0.852 | Off day — no game recap. Not applicable. |
| 4 | hashtag_count | NOT 3 (1 wins) | large | 0.830 | ⚠️ **CONFLICT** — pipeline rule requires exactly 3 hashtags. Keeping 3 per pipeline. See conflict note below. |
| 5 | hashtag_count=1 | 1 wins | large | 0.800 | Cannot apply per pipeline rule (requires 3). |
| 6 | opening=statement | statement wins | large | 0.684 | All 5 posts open with declarative statement. **SIGNAL REVERSAL — see note below.** |
| 7 | opening=allcaps_lead | NOT allcaps wins | large | 0.684 | No ALL CAPS leads in any post. **SIGNAL REVERSAL — see note below.** |
| 8 | len_bucket=200-260 | NOT 200-260 wins | large | 0.615 | All posts targeted <200 chars. Final range: 137–189 chars. Zero posts in 200-260. |
| 9 | len_bucket=<140 | <140 wins | large | 0.534 | Story 1 tweet targeted <140 (137 chars). Others 155–189 chars. |
| 10 | content_type=transaction | transaction wins | medium | 0.444 | Story 2 (King/Peralta) labeled as roster/transaction type. |

**⚠️ HASHTAG CONFLICT:** `hashtag_count=3` is a large LOSER (delta=0.830, median 102 vs 2197 for not-3). The pipeline hard rule requires exactly 3 hashtags per tweet. This conflict has persisted across all runs since Nov 10. Keeping 3 hashtags per pipeline rule. This is a documented discrepancy for the pipeline maintainer to resolve (possibly update the rule, or investigate whether the classifier counts differently than expected).

**⚠️ SIGNAL REVERSAL (Opening type):** This is the most important shift in today's data.
- Prior runs (Oct 30 through Nov 10, 6 consecutive runs): `opening=allcaps_lead` was WINNER (delta 0.245–0.304), `opening=statement` was LOSER (Oct 31, Nov 1, Nov 2, Nov 10).
- Today's snapshot (Nov 11): `opening=statement` is WINNER (delta=0.684, large) and `opening=allcaps_lead` is LOSER (delta=0.684, large).
- Effect size is significantly larger today (0.684 vs 0.265–0.304 in prior runs).
- Possible explanation: As more analytical/transaction content gets posted in the evening_18_24 window (itself a large WINNER), statement openings correlate with that high-performing content. ALL CAPS leads may be working against the statement pattern. The measured tweet count dropped from 82 (Oct 30-Nov 2) to 66 today — the 30-day window may now contain different composition.
- **Action:** Following today's data. ALL CAPS leads removed from all 5 posts. Statement openings throughout.

---

## ### Series context

**`off_day=true`** — No Cubs game today (Nov 11). No game tomorrow either.
**`is_series_start_today=false`** — No series-preview slot needed.
**`series=null`** — No upcoming series in snapshot.
**`today_cubs_game=null`** — No game info.
**Season context:** Hot Stove / Offseason per seasonal-calendar.md. BBWAA Awards Week in progress. Free agency open since Nov 2.

---

## Story Angles and Hooks

### STORY 1: NL Cy Young Is Tonight — Misiorowski the Heavy Favorite
- **Hook:** The award drops tonight. Cubs fans will watch a division rival (most likely) win the NL's top pitching honor.
- **Angle:** Morning context-setter for awards week. Not celebratory for Cubs — purely contextual / motivational.
- **Opening type:** Statement. "The NL Cy Young is tonight."
- **Tone:** Informative with a sharp rivalry kicker.
- **Posting window:** 7:00 AM CT (morning news slot)
- **Char target:** <140 (winner) — achieved at 137.

### STORY 2: Cubs Out on King, Peralta Emerging as Top Target
- **Hook:** One of the Cubs' top-linked rotation targets is off the board (per The Athletic). The next name is a familiar one.
- **Angle:** Transaction/roster update. King departure framed as a pivot. Peralta's Counsell connection and NL Central familiarity are the hook.
- **Opening type:** Statement. "Cubs and Michael King are reportedly not a fit."
- **Tone:** Informative with analytical kicker.
- **Posting window:** 9:30 AM CT (roster news slot)
- **Char target:** 140-200 range — 164 chars.
- **Content type classifier:** transaction (WINNER per insights)

### STORY 3: Ben Brown Surgery Not Ruled Out
- **Hook:** Another rotation depth piece is at risk. The Cubs' situation just got worse.
- **Angle:** Injury update connecting to the broader zero-confirmed-starters narrative.
- **Opening type:** Statement. "Ben Brown still hasn't been cleared to throw."
- **Tone:** Informative, slightly urgent.
- **Posting window:** 2:30 PM CT (injury/roster slot)
- **Char target:** 140-200 range — 183 chars.

### STORY 4: Misiorowski Wins NL Cy Young — Brewers Own the NL (CONDITIONAL)
- **Hook:** By 7 PM CT, the Cy Young is announced. If Misiorowski wins (overwhelming favorite), the Brewers complete a historic double: WS title + NL Cy Young in the same year.
- **Angle:** Rivalry fuel. Cubs have an empty rotation while the Brewers have everything. This contrast is the story.
- **Opening type:** Statement. "Misiorowski wins the NL Cy Young."
- **Tone:** Bold take, rivalry-driven. Sharp and factual.
- **Posting window:** 7:00 PM CT ⭐️ (prime evening slot per insights)
- **Char target:** 140-200 range — 189 chars.
- **⚠️ CONDITIONAL:** See fact-check log. Must verify before 7 PM CT posting.

### STORY 5: PCA Is 24 Hours from NL MVP History
- **Hook:** The first Cubs NL MVP since Kris Bryant in 2016 is one day away.
- **Angle:** Hype post. The numbers make the case: 45 HR, 41 SB, 10.6 fWAR (MLB-best). Award tomorrow 6 PM CT.
- **Opening type:** Statement. "Pete Crow-Armstrong is 24 hours from NL MVP history."
- **Tone:** Bold take, celebratory anticipation.
- **Posting window:** 9:30 PM CT ⭐️ (prime evening slot per insights)
- **Char target:** 140-200 range — 154 chars.
