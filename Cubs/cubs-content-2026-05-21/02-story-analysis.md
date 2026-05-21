# Story Analysis — 2026-05-21

---

### Insights applied

**Source:** `Cubs/_data/insights.json` — generated_at: 2026-05-21T08:30:00 UTC
**Measured tweet count:** 66 tweets (significance gates applied)
**Significant findings:** 6 (sorted by descending effect size)

| # | Finding | Effect | Applied |
|---|---------|--------|---------|
| 1 | `content_type=rss_news` loser (large, Cliff's δ=0.48, p=0.0008) | RSS-sourced content underperforms | N/A — all posts are brief type, not rss_news ✓ |
| 2 | `posting_window=overnight_00_06` loser (medium, δ=0.453, p=0.0188) | Overnight posts underperform | No overnight slots used. Earliest slot 7:00 AM CT ✓ |
| 3 | `len_bucket=140-200` loser (medium, δ=0.451, p=0.0039) | Tweets in the 140-200 char range underperform | All 6 tweets drafted to fall either <140 OR in the 200-260 char range. Verified after drafting ✓ |
| 4 | `has_emoji_first_line` winner=False (medium, δ=0.444, p=0.0029) | Leading emojis hurt performance | NO tweet leads with an emoji. This overrides the brand-voice guide which allows leading emojis ✓ |
| 5 | `content_type=brief` winner (medium, δ=0.434, p=0.0025) | Brief format outperforms | All posts are brief type ✓ |
| 6 | `has_score=True` winner (medium, δ=0.373, p=0.023) | Including the final score boosts performance | Score ("Brewers 5, Cubs 0") is in the first line of the game recap tweet (Story 1). Not applicable to non-result tweets ✓ |

**Net changes from insights vs brand-voice defaults:**
- Leading emojis removed from all tweets (insight overrides brand-voice which allowed them)
- All tweets drafted to be either <140 or 200–260 total chars (avoids 140-200 range)
- Score explicitly in first line of Story 1 recap

---

### Series context

**Source:** `Cubs/_data/series-context.json` — generated_at: 2026-05-21T08:30:00 UTC

- `off_day=true`: No Cubs game on today's CT date (May 21, 2026)
- `is_series_start_today=false`: No new series begins today
- `series=null`, `today_cubs_game=null`
- Rationale from snapshot: "No upcoming Cubs game on today's CT calendar date."

**Applied:** Off-day slate — no game preview, no in-game content, no recap slot beyond the morning Game 3 write-up. Lean into: prospect news, roster injury updates, division analysis, trade storyline. No series-preview slot reserved (series start is May 22, outside today's pipeline date). Slots 5:00 PM, 6:30 PM, 8:00 PM, 9:30 PM skipped (no game).

---

### STORY 1: Brewers 5-0 Sweep — Five-Game Slide

**Angle:** Game 3 recap. Harrison was dominant (11 K, 7 IP). Cabrera's early exit with blister compounds the crisis. Three errors. The sweep itself — Brewers outscored Cubs 19-5 in 3 games — is the headline stat.

**Hook:** Score first (insights: has_score winner). Then Harrison's line. Then Cabrera's blister exit. Then the losing streak context in one sentence.

**Kicker:** Cubs 1.5 games back — sets up the division take in Story 2.

**Tone:** Informative. Controlled disappointment. No hysteria.

**Hashtags:** #Cubs #GoCubs #FlyTheW (game result context)

---

### STORY 2: Cubs 29-21, Brewers 29-18 — Division Has a New Leader

**Angle:** Bold take. The series outscoring (19-5) is damning context. Cubs and Brewers have the same win total (29) but Brewers have 3 fewer losses. Division lead has flipped and this isn't noise — Brewers are 14-4 in last 18 games.

**Hook:** Run differential as the opening data point. Then the record contrast.

**Kicker:** "Chicago needs to start playing like they belong in first place." — strong take backed by the numbers.

**Tone:** Bold, competitive. Not panic, but urgency.

**Hashtags:** #Cubs #NorthSiders #MLB (division/standings context)

---

### STORY 3: Cabrera Blister — Four Starters in Question Simultaneously

**Angle:** Informative rotation crisis update. The Cabrera blister isn't catastrophic on its own, but combined with Horton/Steele/Boyd, the Cubs are now down to essentially a skeleton crew. Makes the Peralta case even stronger.

**Hook:** Cabrera's exit and finger injury. Then the cumulative damage (Horton/Steele/Boyd/Cabrera).

**Kicker:** Implicit — the next story (Peralta) answers the question this story poses.

**Tone:** Informative. Clinical. Let the facts make the case.

**Hashtags:** #Cubs #MLB #CubsBaseball (roster/injury news context)

---

### STORY 4: Boyd Ahead of Schedule

**Angle:** Bold/upbeat. Contrast to the doom. Boyd isn't just recovering — he's reportedly ahead of schedule with a mound session Saturday. In the context of a rotation crisis, this is genuinely meaningful news.

**Hook:** "Ahead of schedule" first. Then the specific Counsell-cited pace.

**Kicker:** "This rotation needed good news and finally got some." — simple, honest, earned.

**Tone:** Upbeat but grounded. Not over-celebrating — a mound session is not a comeback. But it's real progress.

**Hashtags:** #Cubs #GoCubs #CubsBaseball

---

### STORY 5: Peralta Trade Clock — 11 Days

**Angle:** Analytical/bold. June 1 Mets decision point is the peg. Cabrera's fresh blister makes the urgency tangible today even though this is an established arc. Counsell connection and ERA are the strongest factual anchors.

**Hook:** Three data points in one compact line (ERA, contract status, Counsell familiarity). Then the clock and why it matters today.

**Kicker:** "The case for this trade has never been stronger." — this is bold but backed by the morning's rotation news.

**Tone:** Analytical/bold hybrid. Not alarmist but clear-eyed about the urgency.

**Hashtags:** #Cubs #MLB #CubsBaseball

---

### STORY 6: Iowa 8-Game Losing Streak — Noland, Kepley

**Angle:** Informative off-day prospect update. Iowa's losing streak is the lead. Noland ankle injury is a genuine concern (pitcher carted off field). Kepley's HR is the bright spot. Compact, factual.

**Hook:** Iowa's eighth straight loss + the score + Noland injury.

**Kicker:** Kepley's HR as the one positive note.

**Tone:** Informative, matter-of-fact.

**Hashtags:** #Cubs #MLB #CubsBaseball
