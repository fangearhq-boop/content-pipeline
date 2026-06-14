# Story Analysis — Cubs June 14, 2026

---

### Insights applied

**Today's `significant_findings` (generated 2026-06-14T08:30:00 UTC, 58 measured tweets):**

**Finding 1** — `posting_window=midday_12_18` beats `not_midday_12_18`
- Median impressions: 74.5 (midday) vs 41.5 (non-midday)
- n = 32 vs 26, p = 0.0361, Cliff's delta = 0.323 (small effect)
- **Action:** Shift maximum content into the 12:00 PM–5:00 PM CT range. Reduce morning slots. Game recap at 7:00 AM is mandatory (it's the overnight news anchor) but no additional morning posts are added. Stories 2-6 are all scheduled in or near midday window (12:00 PM, 1:15 PM, 2:30 PM, 3:45 PM, 5:00 PM).

**Finding 2** — `posting_window=morning_06_12` loses to `not_morning_06_12`
- Same underlying contrast as Finding 1 (mirror of the midday signal)
- Median impressions: 41.5 (morning) vs 74.5 (non-morning)
- **Action:** Hold morning to ONE post (the mandatory 7:00 AM game recap). Skip the 8:15 AM and 9:30 AM slots that were used in previous pipeline runs. The Ben Brown recap angle is folded into the 7:00 AM tweet or deferred to a midday slot.

**No other significant findings today** — no `has_emoji_first_line`, `len_bucket`, `has_score`, `has_stat`, or `content_type` contrasts cleared the significance gates (n≥8, p<0.05, |delta|≥0.20). Note: June 13's insights included `has_stat=True` as a finding — that was yesterday's snapshot; today's fresh snapshot does NOT include it. Brand-voice defaults apply for all dimensions not covered by today's findings.

**Brand-voice defaults maintained for:** emoji usage (1-3 per post, placed naturally), tweet length (punchy under 240 chars ideal; hard cap 280), hashtag format (exactly 3, #Cubs first, one line), no engagement questions.

---

### Series context

**Case: `is_series_start_today=false`, `off_day=false`**

- Cubs are mid-series vs San Francisco Giants at Oracle Park
- Series record: Cubs 2-0 (won 5-1 June 12, 6-1 June 13)
- Today is Game 3 (series finale): Cubs going for the SWEEP
- Giants record: 28-43 (worst or near-worst in NL)
- No mandatory series-preview tweet (not a series opener)
- The sweep angle is the hook — it replaces what would be a series-preview slot

Source: /tmp/cubs-series.json (rationale: "Same opponent as yesterday — this is mid-series, not a series opener")

---

## Story 1: Cubs 6, Giants 1 — PCA Leads Off With HR, Brown Wins

**Tier:** 1  
**Angle:** PCA homered on the very first pitch of the game — leadoff HR in the first at-bat — and the Cubs cruised to a 6-1 win. Ben Brown went 5 IP, 1 R, improved to 3-2. Ian Happ and Pedro Ramírez added solo shots.  
**Hook:** The "first pitch of the game" detail is viscerally satisfying for fans. PCA = the most exciting Cub on the field right now.  
**Format:** Stat-backed recap, winner-first score format, all three HR players named.  
**Insight note:** Morning post (7 AM) — underperforming window per Finding 2, but unavoidable as the Tier 1 game recap anchor. Keeping to one morning post total.

---

## Story 2: Game Preview — Rea vs Webb, 2:10 PM CT (National TV, ABC)

**Tier:** 1  
**Angle:** The Cubs go for the series sweep at Oracle Park on national TV. Webb is the one Giants starter they've been waiting for — the ace who didn't pitch in Games 1 or 2. Rea has been steady by necessity (5-4, 5.19 ERA) but Webb (3.88 ERA) is the real challenge.  
**Hook:** National TV + sweep on the line = maximum fan engagement. Must post before first pitch (2:10 PM CT).  
**Format:** Preview with pitching matchup, game time, stakes. Lead with the sweep context.  
**Posting window:** 12:00 PM CT — directly in the high-performing midday window.

---

## Story 3: Bold Take — Cubs Sweep the Giants (Series Lead 2-0)

**Tier:** 2  
**Angle:** The Cubs have taken two from a 28-43 Giants team and are one win from a series sweep at Oracle Park. This matters for the wild card chase — banking wins against losing teams is how you stay in the race when the division is out of reach.  
**Hook:** "Beat who's in front of you" theme. Fans love the competitive fire before game time.  
**Format:** Sharp, punchy take. Stat-backed (Cubs record, Giants record).  
**Posting window:** 1:15 PM CT — well inside the midday window, ~1 hour before first pitch.

---

## Story 4: Standings / Wild Card Analysis

**Tier:** 2  
**Angle:** Cubs at 37-34 — over .500, alive in the wild card race, but the NL Central is a lost cause with Brewers running away. The conversation needs to shift to "which teams are we chasing for a wild card spot."  
**Hook:** "Division is over, wild card begins" reframe is a real take, not a softball recap.  
**Format:** Division context + wild card framing. Keep specific to confirmed records (37-34 Cubs; hedge on Brewers current record).  
**Posting window:** 2:30 PM CT — midday, game already in progress.

---

## Story 5: Trade Deadline — 50 Days, 4 Starters Gone

**Tier:** 2  
**Angle:** August 3 is 50 days away. Steele (elbow), Horton (Tommy John), Taillon (hamstring), Boyd (IL). Rea is the de facto No. 2. Hoyer has confirmed they're shopping for rotation help.  
**Hook:** Countdown + crisis = urgency. The "50 days" anchor gives it a news peg.  
**Format:** Short declarative sentences. Bold take — name the problem plainly. Don't speculate on specific trade targets (only low-confidence rumor on Angels).  
**Posting window:** 3:45 PM CT — midday window, in-game.

---

## Story 6: Prospect Pulse — Knoxville's Ayers & Hartshorn

**Tier:** 3  
**Angle:** While the major league rotation burns, the farm system is producing bright spots. Owen Ayers and Josiah Hartshorn are on simultaneous hot streaks at Knoxville (AA). Jefferson Rojas back-to-back 3-hit games. Will Sanders returned to spin 5 scoreless for Iowa.  
**Hook:** "Cavalry is coming" angle resonates on a day when Cubs face Logan Webb with a leaky rotation.  
**Format:** Concise, name-check the players, give one concrete stat per player. Hedge on specific affiliates where uncertain.  
**Posting window:** 5:00 PM CT — edge of midday window; game will be finishing up.

---

## Publishing Schedule

| Slot | Time (CT) | Story | Window | Notes |
|------|-----------|-------|--------|-------|
| 1 | 7:00 AM | Game recap — Cubs 6, Giants 1 | Morning (loser) | Mandatory Tier 1; only morning post |
| 2 | 12:00 PM | Game preview — Rea vs Webb | Midday (winner) | Must post before 2:10 PM first pitch |
| 3 | 1:15 PM | Bold take — sweep on the line | Midday (winner) | Pre-game energy |
| 4 | 2:30 PM | Standings / wild card analysis | Midday (winner) | In-game |
| 5 | 3:45 PM | Trade deadline countdown | Midday (winner) | In-game |
| 6 | 5:00 PM | Prospect pipeline | Midday (winner) | Late-game / post-game |

**Total: 6 posts.** Skipping 8:15 AM and 9:30 AM slots per Finding 2 (morning underperforms). No filler added.
