# Story Analysis — July 10, 2026

## Insights Applied

**Source:** Cubs/_data/insights.json (generated 2026-07-10T08:30:00, n=75 tweets)

**Significant findings (2):**
1. `posting_window=midday_12_18` WINS — median engagement 63 vs 26, p=0.027, Cliff's delta=0.307 (small effect)
2. `posting_window=morning_06_12` LOSES — mirror finding, same stats

**No significant findings on:** has_emoji_first_line, has_stat, len_bucket, has_score, has_allcaps, content_type

**Application decisions:**
- Morning slot (7 AM) retained ONLY for Story 1 (game recap). Rationale: recap posts are required early morning; this is the explicit "required purpose" exception to the morning_06_12 loser finding.
- Stories 2-7 all scheduled in midday/afternoon window (12:00 PM–6:30 PM) to exploit midday_12_18 advantage.
- No emoji pressure applied (no significant finding on emoji).
- No stat-stuffing or all-caps optimization (no significant findings).

---

## Series Context

**Source:** Cubs/_data/series-context.json (generated 2026-07-10T08:30:00)

- is_series_start_today: **true** → mandatory series preview tweet required
- Series preview assigned to 12:00 PM (first available midday slot) per is_series_start_today rule
- Cubs are away (is_cubs_home: false) at Great American Ball Park
- Game 1 first pitch: 6:10 PM CT — pre-game hype tweet placed at 6:30 PM (game is in progress ~20 min, but hype posts near first pitch are acceptable for scheduled content)

---

## Story-by-Story Analysis

### STORY 1: Game 3 Recap — Orioles 3, Cubs 2
**Tier:** 1 | **Time:** 7:00 AM CT | **Type:** Recap

**Angle:** The bullpen failed again — but the Cubs still won the series. Frame the loss in context: frustrating but not damaging. Rolison was the villain; Suzuki was the hero who set it up.

**Hook strategy:** Lead with score (brand rule: score first on recaps). Move to the failure moment. End with the forward-looking positive (took series 2-of-3, Cincinnati next).

**Tone:** Matter-of-fact with a twinge of frustration. Don't catastrophize — the Cubs won the series.

**Series context applied:** Game 3 loss on July 9; today is series start (Cincinnati). Recap must acknowledge loss but pivot forward to tonight.

**Insights applied:** 7 AM exception (required recap purpose). No morning preference otherwise.

---

### STORY 2: Series Preview — Cubs at Reds
**Tier:** 1 | **Time:** 12:00 PM CT | **Type:** Preview

**Angle:** Mandatory series start coverage. Cubs (52-41, WC leaders) vs weak opponent (Reds 42-50). Frame as a series the Cubs must protect.

**Hook strategy:** Per rules, lead with matchup itself — opponent, length, location. Do not lead with a player or narrative.

**Tone:** Confident. Cubs are favored; frame the expectation.

**Insights applied:** Moved from potential early slot to 12:00 PM to land in midday_12_18 window.

---

### STORY 3: PCA — First 20/20, All-Star
**Tier:** 1 | **Time:** 1:15 PM CT | **Type:** Feature

**Angle:** PCA has achieved the first 20/20 of 2026 and is heading to Philadelphia as the Cubs' lone All-Star. The WAR comparison to Ohtani is the bold claim. The "best player in baseball right now" is the kicker opinion.

**Hook strategy:** Lead with the milestone number (21 HR) then the 20/20 historic moment. Build to All-Star and WAR.

**Tone:** Bold, celebratory. This is one of the team's signature stories of the season.

**Insights applied:** 1:15 PM — solidly in midday_12_18 window.

---

### STORY 4: Wild Card Standings
**Tier:** 2 | **Time:** 2:30 PM CT | **Type:** Standings

**Angle:** A quick standings snapshot. Cubs lead, Phillies and Marlins close, Cardinals faded. Frame as Cubs owning the race they were once chasing.

**Hook strategy:** List format for standings — scannable and clear. End with the "Next stop: Cincinnati" pivot to keep it timely.

**Tone:** Confident, forward-looking. Not boastful — just factual with a kicker.

**Insights applied:** 2:30 PM in midday_12_18 window.

**Fact caution:** Phillies and Marlins records are MEDIUM confidence (single source). Cardinals position is directional language only — "have faded" avoids specific claims.

---

### STORY 5: Reinforcements — Taillon, Shaw, Maton
**Tier:** 2 | **Time:** 3:45 PM CT | **Type:** Roster

**Angle:** Three pieces coming back. Frame as a wave of reinforcement arriving just before the second half. Creates anticipation and optimism without over-promising.

**Hook strategy:** "Reinforcements are coming." Then three bullets. End with kicker.

**Tone:** Optimistic, building anticipation.

**Insights applied:** 3:45 PM in the midday_12_18 window (window is 12–6 PM).

---

### STORY 6: Trade Deadline — Joe Ryan
**Tier:** 2 | **Time:** 5:00 PM CT | **Type:** Deadline

**Angle:** 24 days out. Ryan is still the top fit. The healthy rotation is a partial answer, not the whole answer. Pressure on Hoyer.

**Hook strategy:** Open with days remaining — creates urgency. Then the target. End with the accountability kicker on Hoyer.

**Tone:** Analytical, pointed. Slight edge — it's a "Jed, make the call" take.

**Insights applied:** 5:00 PM still in midday_12_18 window (before 6 PM).

---

### STORY 7: Pre-Game Hype
**Tier:** 3 | **Time:** 6:30 PM CT | **Type:** Hype

**Angle:** Game is underway / about to start. Simple call-to-action energy. Records + context in two lines, then a one-word kicker.

**Hook strategy:** "First pitch in Cincinnati." Immediate, visual, timely.

**Tone:** Punchy, direct, minimal. The 6:30 slot is a game-time slot — brevity is right.

**Insights applied:** 6:30 PM is technically in evening_18_24 window; no finding was significant for that window. Placed here because game time dictates placement — content purpose overrides preference.
