# Chicago Cubs Fan HQ — Story Analysis
## Date: 2026-08-23 (Sunday CT)

---

### Insights applied

**Source:** Cubs/_data/insights.json — generated_at: 2026-08-23T08:30:00.137934+00:00
**Measured tweet population:** 127 tweets

**Significant findings (1 finding):**

| Dimension | Winner | Loser | Median Imp (W) | Median Imp (L) | n_winner | n_loser | p | Cliff's δ |
|-----------|--------|-------|---------------|---------------|----------|---------|---|-----------|
| has_stat | True | False | 107.5 | 87 | 44 | 83 | 0.0335 | 0.23 (small) |

**Application to today's drafts:**
- `has_stat=True` is the winner → **include at least one concrete numeric stat in every tweet**. Applied to all 6 tweets:
  - Tweet 1: score (5-4), inning details, Peterson 6 IP / 8 Ks
  - Tweet 2: Shaw's .246/.322/.415 / 56 games, Iowa 8-3 win
  - Tweet 3: Cardinals 66-64, Cubs 74-56, 2.5 games
  - Tweet 4: series scores (6-5 extras / 5-4), Mariners 62-68 below .500
  - Tweet 5: Brown targeting September, Steele late-September / Aug. 21 dates are factual anchors
  - Tweet 6: Cubs 74-56, game time 3:10 PM CT
- No `has_emoji_first_line` finding → brand-voice defaults apply (1-3 emoji per post placed naturally; no requirement to avoid leading emoji but also no performance signal to compel them)
- No `posting_window` loser finding → default schedule unchanged
- No `len_bucket` finding → standard tweet length guidance unchanged
- No `has_score` finding → including scores is brand-voice standard; confirmed appropriate

**No other significant findings.** Other dimensions not in `significant_findings` were not used to drive decisions (e.g., no `has_emoji_first_line` finding observed, no `content_type` finding today).

---

### Series context

**Source:** Cubs/_data/series-context.json — generated_at: 2026-08-23T08:30:00.634968+00:00

- `is_series_start_today`: **false** → No series preview tweet required at 7:00 AM slot
- `off_day`: **false** → Game today; normal game-day posting cadence
- Series: Cubs vs Seattle Mariners (mid-series, 3-game series; today is the finale, Game 3)
- Rationale: "Same opponent (Seattle Mariners) as yesterday — this is mid-series, not a series opener."
- Today's game: 3:10 PM CT, T-Mobile Park, Cubs 74-56 vs Mariners 62-68
- Cubs probables: TBD (Clay Holmes confirmed as starter via lineup search)
- Mariners probable: TBD

**Series context applied:** 7:00 AM slot is used for the Game 2 recap (not a series preview). Today's content centers on the finale and what a third consecutive walk-off loss would mean for the road trip.

---

### STORY 1: Game 2 Recap — Mariners 5, Cubs 4 (Arozarena Walkoff HR)

**Story type:** NEW STORY (follow-up to Game 2 preview on Aug 22)
**Tier:** 1 (game result — always leads the day)

**Best angles:**
1. Arozarena's extraordinary two-direction performance — opened and closed the game with HRs
2. Peterson was excellent — the Cubs SHOULD have won
3. Back-to-back walk-off losses — this is the emotional hook for fans
4. Game finale context: one more chance today

**Angle chosen:** Lead with the Arozarena historical oddity (leadoff + walkoff HR same game), pivot to the gut-punch narrative of a second straight walk-off L despite strong pitching, and tee up today's finale.

**Voice:** Informative with edge — the facts tell the emotional story. Score first, Arozarena's feat second, Peterson's strong line third (context: Cubs DID earn the lead), then today's preview.

---

### STORY 2: Matt Shaw Rehab — 2 Hits Saturday, September Return on Track

**Story type:** FOLLOW-UP (covered Aug 22 — first dedicated Shaw post)
**Tier:** 2

**Best angles:**
1. Shaw is progressing — two hits in Iowa is tangible evidence
2. The timing: September callup during a wild card chase is the narrative payoff
3. Lineup depth is a real question for the Cubs' stretch run

**Angle chosen:** Lead with the concrete update (2 hits, Iowa win), anchor with his pre-injury MLB slash for context, and close with the stretch-run implication.

**Voice:** Informative — roster news reads best as clear-eyed information delivery. Light hope note at close ("this lineup" framing).

---

### STORY 3: Cardinals Rival Watch — 66-64, Five Series Wins, 2.5 Back of WC

**Story type:** FOLLOW-UP (standings angle updated; cardinal rival-watch is covered regularly)
**Tier:** 2

**Best angles:**
1. The Cardinals are quietly dangerous — five series wins since the deadline
2. The Cubs' wild card cushion is smaller than fans might think
3. Rivals are earning their position while the Cubs are dropping walk-offs on the West Coast

**Angle chosen:** Bold take. The Cardinals' streak is the hook, the WC gap is the stat, and the Cubs' slide this weekend adds implicit urgency without being doom.

**Voice:** Bold/analytical — state the rival fact, connect to Cubs' race position.

---

### STORY 4: Series Finale Preview — Holmes Starts, 3:10 PM CT

**Story type:** NEW STORY (series finale preview)
**Tier:** 2

**Best angles:**
1. Sweep-avoidance context — two walk-off losses set the stakes
2. Holmes as the last line — how he pitches sets the tone for the trip home
3. The opponent comparison: a 62-68 team, playing at home with momentum — beatable but not easy

**Angle chosen:** Lead with time/venue, then the sweep stakes with brief series recap, then Holmes as the answer. Ends with a note on Holmes's recent form (referenced as "solid" without unverified ERA number).

**Voice:** Informative anchor → builds into game-day urgency.

---

### STORY 5: Rotation Reinforcements — Steele + Brown Face Live Hitters Aug. 21

**Story type:** NEW STORY (first dedicated post on both together — individual updates last ran Aug 20 via injury context)
**Tier:** 2

**Best angles:**
1. Both pitchers in live-hitter sessions on the same day — that's a real milestone
2. The timing: returning right before the playoff stretch is ideal
3. Bold take: this roster keeps getting better, which should scare the rest of the NL

**Angle chosen:** Bold/hopeful — frame as the "good news hiding behind the West Coast trip." Facts first (live BPs, timelines), then the bullish take.

**Voice:** Bold with factual grounding. Close with "the rest of the NL" framing for maximum fan energy.

---

### STORY 6: First Pitch Hype — Series Finale, 3:10 PM CT

**Story type:** NEW STORY (game-time energy post for series finale)
**Tier:** 2

**Best angles:**
1. Pre-game energy for fans tuning in before 3:10 CT
2. Cubs (74-56, WC leaders) vs sub-.500 team — they should win this
3. Holmes as the hero of the day narrative

**Angle chosen:** Short, punchy energy post. Time + venue → walk-off loss stakes → confident "this team doesn't come home 0-3" finish.

**Voice:** Passionate, brief — this is a hype post, not an analysis.
