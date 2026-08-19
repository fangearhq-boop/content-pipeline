# Chicago Cubs Fan HQ — Story Analysis
**Date:** August 19, 2026

---

### Insights applied

**Finding (sole significant finding from insights.json, generated 2026-08-19T08:30:00 UTC):**

```
dimension: has_score
kind: binary
winner: False
loser: True
median_impressions_winner: 110
median_impressions_loser: 81.0
n_winner: 77 / n_loser: 48
p_value: 0.0052
effect_size_cliffs_delta: 0.298 (small)
```

**Interpretation:** Tweets that do NOT include a game score outperform those that do, by a meaningful margin (p<0.01, small-to-medium effect). This is counterintuitive but statistically robust at 125 measured tweets.

**How it changed today's drafts:**
1. **Story 1 (Game 2 Recap):** Tweet does NOT lead with "Cubs won 4-3." Instead leads with "Alex Bregman. One out. Ninth inning. Walkoff single." Score is omitted from the tweet body entirely.
2. **Story 5 (Game 3 Preview):** No score embedded in the preview; frame is sweep-hunt narrative, not W-L framing.
3. **Stories 2, 3, 4, 6:** Not game-recap content; insight has no direct bearing on drafting. No changes needed beyond the already-active standard.

**Overall:** Insight is applied consistently to any tweet anchored to a game result. No violation of the data in any tweet drafted today.

---

### Series context

**Source:** Cubs/_data/series-context.json (generated 2026-08-19T08:30:00 UTC)

**Key fields:**
- `off_day`: false — game today ✓
- `is_series_start_today`: false — mid-series ✓
- `series.opponent`: Chicago White Sox
- `series.is_cubs_home`: true (Wrigley Field)
- `series.series_length`: 1 (one game remaining today — Game 3)
- `today_cubs_game.game_date_ct`: "Wed 1:20 PM CT"
- `today_cubs_game.status`: "Preview" (Scheduled)
- `series.rationale`: "Same opponent (Chicago White Sox) as yesterday — this is mid-series, not a series opener."

**Case applied:** `is_series_start_today=false` — no reserved 7:00 AM series preview slot. The 7:00 AM slot is used for the Game 2 recap instead (per research-playbook.md posting priority: game recaps go in first available slot).

The series context confirms Cubs are 2-0 heading into today's Game 3 finale. Today's story framing: **sweep hunt at Wrigley, 1:20 PM CT afternoon game.**

---

## Story-by-Story Analysis

### Story 1: Game 2 Recap — Bregman Walk-off, Cubs 4-3

**Angle:** Bregman walkoff single in 9th after rain delay drama and Gausman's early exit. 13th Wrigley walk-off win of 2026 season, leading all of MLB. Cubs 2-0 in Crosstown Classic.

**Hook:** The drama escalated (Gausman exits early, rain delay 90 min) and Bregman delivered anyway. Lead with the moment, not the score (has_score=False insight).

**Tier:** 1 — game recap, first morning slot mandatory.

**Insight application:** Score intentionally omitted. Lead: "Alex Bregman. One out. Ninth inning. Walkoff single."

---

### Story 2: Wrigley Walk-off Culture Bold Take

**Angle:** 13 walk-off wins at Wrigley in 2026, leading all of MLB. This team wins ugly, wins in extras, wins on rain-delayed nights. Bold take on Cubs clutch culture.

**Hook:** The number alone (13 walk-offs, MLB-leading) is the hook. Keep it stat-led, bold-voiced.

**Tier:** 1 — top-tier engagement content for morning.

**Insight application:** No score embedded. Pure milestone framing.

**Caution:** "Ties the 2015 franchise record" — single source; omitted from tweet. Verified claim: "13 Wrigley walk-offs, leading MLB."

---

### Story 3: Gausman Injury Update

**Angle:** Left hand cramp in the glove hand (non-throwing hand). Expected to make next start. Still adjusting to Cubs after deadline acquisition. Rotation health remains intact for October.

**Hook:** Reassurance for concerned fans. The injury sounds worse than it is; clarify quickly.

**Tier:** 2 — injury update, roster news.

**Insight application:** N/A (not a game result tweet).

---

### Story 4: NL Standings + Cardinals Jab

**Angle:** Cubs WC1, 4 GB of division-leading Brewers with 7 head-to-head games remaining. Cardinals sit 13.5 back — great rival burn. Cubs own the Wild Card; September will be the real test.

**Hook:** Cardinals GB + Cubs playoff context in one tweet. Rival jab + standings update hybrid.

**Tier:** 2 — rival watch + standings context.

**Fact-check note:** Cardinals are 64-62 = barely above .500. Do NOT call them "below .500" (tweet avoids this).

---

### Story 5: Game 3 Preview — Sweep Hunt

**Angle:** Cubs 2-0, going for the Crosstown sweep at 1:20 PM CT. Newcomb (LHP) vs Holmes (RHP). Back-to-back walk-offs heading into a daylight game. This is closure time.

**Hook:** "Sweep time." — two words, the strongest possible opener.

**Tier:** 1 — game preview, must post before 1:20 PM CT first pitch.

**Insight application:** No score from prior games embedded. Frame: narrative (sweep mission), not statistical.

---

### Story 6: First Pitch Hype

**Angle:** 1:15 PM CT, five minutes before first pitch. Short, punchy. PCA + Bregman as name anchors. Fly the W in daylight.

**Hook:** "First pitch in five minutes." — crisp urgency.

**Tier:** 1 — game day content.
