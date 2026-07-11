# 02-story-analysis.md — Angles, Hooks, Headlines
# Date: 2026-07-11 (Saturday) | CT

---

### Insights applied

**Findings read (2 significant findings from Cubs/_data/insights.json, generated_at: 2026-07-11T08:30:00Z, n=78 measured tweets):**

**Finding 1 — `posting_window=midday_12_18` is a WINNER**
- Winner: midday_12_18 (median impressions: 61), Loser: not_midday_12_18 (median impressions: 25)
- n_winner=51, n_loser=27, p=0.0394, Cliff's delta=0.28 (small effect)
- **Action:** Bias all non-required slots to the 12:00 PM–6:00 PM CT window. Stories 2-6 all fall within this window. ✓

**Finding 2 — `posting_window=morning_06_12` is a LOSER**
- Loser: morning_06_12 (median impressions: 25), Winner: not_morning_06_12 (median impressions: 61)
- Same data as Finding 1, inverse framing. p=0.0394, Cliff's delta=0.28
- **Action:** Only 7:00 AM slot (Story 1 — game recap) uses the morning window. Game recap is an explicitly-required exception per pipeline instructions. All other slots are outside morning. ✓

**No findings** on emoji_first_line, content_type, len_bucket, or has_score. Brand-voice defaults apply for those dimensions.

**Effect on today's drafts:**
- Slot distribution: 7:00 AM (1 tweet, required exception) + 12:00–5:00 PM (5 tweets, all midday window) = maximizes the midday_12_18 signal
- No emoji adjustments needed (no findings)
- Tweet length: no len_bucket findings → targeting 200-270 chars per brand voice (verified below)

---

### Series context

**From Cubs/_data/series-context.json (generated_at: 2026-07-11T08:30:00Z):**
- `is_series_start_today`: **false** (series started yesterday, July 10 — Game 1)
- `off_day`: **false** — Cubs play today at 6:10 PM CT
- **Series:** Cubs at Cincinnati Reds, Great American Ball Park
  - Series length: 2 games (July 11 @ 6:10 PM CT + July 12 @ 12:40 PM CT)
  - Cubs record: 52-42; Reds record: 43-50
  - Both probable pitchers listed as TBD in snapshot — updated via research: Assad (Cubs) vs Lodolo (Reds)
  - Rationale: Mid-series, not a series opener — no mandatory 7 AM series preview slot
- **Today's game:** Game 2 of 2 at Great American Ball Park, 6:10 PM CT

**Application:** No series-preview format required. Game recap from last night leads the day, with Game 2 preview slotted at 12:00 PM. Last two games before All-Star break — every WC point matters.

---

## Story Selection

### STORY 1 — Reds 4, Cubs 0 Game Recap [TIER 1]
**Angle:** Hunter Greene allowed 8 ER in his July 4 season debut. Six days later he threw a 7-inning shutout against the Cubs — 12 K, 3 hits. Three Reds pitchers combined for 16 Cubs strikeouts (season high). Cubs' 9th shutout loss of the year. Imanaga took the loss. Honest, frustrated recap that also previews tonight.
**Hook:** The contrast — Greene's debut disaster vs. this dominant performance — is the most compelling frame.
**Posting window:** 7:00 AM CT (required game recap exception — morning penalty accepted)
**Type:** Informative recap

### STORY 2 — Game 2 Preview: Assad vs Lodolo [TIER 1]
**Angle:** Javier Assad (6-1, 4.04 ERA) takes the ball tonight — the rotation anchor who's quietly been outstanding while four other starters are on the IL. He faces Nick Lodolo (4.68 ERA) in a game Cubs need before the All-Star break. Bounce-back frame.
**Hook:** Assad has carried this rotation. Tonight is his turn to answer.
**Posting window:** 12:00 PM CT (midday window ✓)
**Type:** Preview/informative

### STORY 3 — Bold Take: Cubs Offense Needs a Wake-Up Call [TIER 2]
**Angle:** The 16-K game is a statement about Cubs offensive fragility entering the second half. The fact that Greene imploded on July 4 then made the Cubs look helpless on July 10 is a meaningful data point, not a fluke. 9 shutout losses in a playoff contender's first half is a problem.
**Hook:** "He was an 8-ER disaster 6 days ago. Then he made us look like a high school team." — stark contrast, honest fire.
**Posting window:** 1:15 PM CT (midday window ✓)
**Type:** Bold/passionate take

### STORY 4 — Wild Card Standings: Cubs 52-42, Tied [TIER 2]
**Angle:** Quick standings check after the loss — Cubs fell into a three-way tie with Phillies and Marlins. WC1 is now a tie. Every game this weekend matters before the break.
**Hook:** "TIED" is the operative word. Statline leads, urgency closes.
**Posting window:** 2:30 PM CT (midday window ✓)
**Type:** Informative/standings

### STORY 5 — Iowa Cubs 21-7 + Jayden Murray Acquisition [TIER 3]
**Angle:** The farm system delivered a fun Friday: Iowa crushed St. Paul 21-7. Also fresh news: Cubs grabbed RHP Jayden Murray from the Astros (1.17 ERA, 6 saves at Triple-A). Minor league system is producing; bullpen reinforcements are coming.
**Hook:** Two pieces of good news on a down morning after the shutout.
**Posting window:** 3:45 PM CT (midday window ✓)
**Type:** Informative/mixed

### STORY 6 — Pre-Game Hype: Last Weekend Before All-Star Break [TIER 2]
**Angle:** Three days until PCA heads to Philadelphia. Cubs have two games left before the break — and they're tied in the Wild Card. No time for coasting. Assad on the mound tonight at 6:10 PM CT.
**Hook:** All-Star weekend = context for urgency, not distraction.
**Posting window:** 5:00 PM CT (midday window ✓; 5 PM lands within midday_12_18 window)
**Type:** Bold/hype

---

## Story History Cross-Reference

| Story | Decision | Prior Coverage |
|-------|----------|---------------|
| Game 1 recap (Reds 4-0) | NEW STORY (new game result) | Yesterday's pipeline covered Game 1 preview; today covers result |
| Assad vs Lodolo preview | NEW STORY | No prior coverage of Assad's start vs Reds this series |
| 16-K offense bold take | NEW STORY (tied to today's recap) | Offense angle is fresh from last night's specific shutout data |
| Wild card standings | FOLLOW UP | Last covered July 10 (52-41 WC1 framing); updated to 52-42 tied |
| Iowa Cubs 21-7 + Murray | NEW STORY | Iowa last covered July 9 in previous pipeline; Murray is fresh news |
| Pre-game hype | NEW STORY | Tonight's game; All-Star break angle is new |

**Not covered today (decisions):**
- Taillon return timeline: was covered yesterday (3:45 PM slot); repeating today adds no new info since there's no new development
- PCA All-Star feature: covered July 10 (1:15 PM slot); no new angle today beyond the "3 days away" reference in Story 6
- David Peterson: acquired June 25, well past its news shelf life; no new info warrants repeat
- Joe Ryan trade target: covered yesterday (5:00 PM slot); no new reporting since then
