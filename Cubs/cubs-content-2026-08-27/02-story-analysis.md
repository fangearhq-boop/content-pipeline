# Story Analysis — August 27, 2026

---

### Insights applied

**Source:** Cubs/_data/insights.json (generated_at: 2026-08-27T08:30:00Z, measured_tweet_count: 126)

Two significant findings cleared all three gates (n≥8, Mann-Whitney U p<0.05, |Cliff's delta|≥0.20):

**Finding 1: has_stat=True beats has_stat=False**
- Effect size: small (Cliff's delta = 0.26)
- Median impressions: 103.5 (with stat) vs. 84.0 (no stat)
- Decision: Include at least one specific numerical stat in every tweet today. Game recap, prospect update, standings tweet — all get hard numbers.

**Finding 2: has_score=False beats has_score=True**
- Effect size: small (Cliff's delta = 0.223)
- Median impressions: 100.5 (no score) vs. 80.0 (with score)
- Decision: Do NOT lead any tweet with the game score. The Aug 26 recap leads with pitching/performance angle, not "Cubs lost 2-0." The score is either omitted entirely or buried at the end of the body copy.

These two findings are in mild tension for a game recap: we want stats but not the specific final score. Resolution: use the pitching stat (Rodriguez's 9 Ks) and Boyd's ERA/start quality as the stat hook, skipping the "2-0" score in the lead.

**Slot timing check:** No posting_window findings in significant_findings, so default schedule stands.

---

### Series context

**Source:** Cubs/_data/series-context.json (generated_at: 2026-08-27T08:30:00Z)

- `off_day: true` — No Cubs game today (Aug 27)
- `is_series_start_today: false` — No series preview slot required for 7:00 AM
- `series: null` — No active series snapshot
- `today_cubs_game: null`
- `rationale: "No upcoming Cubs game on today's CT calendar date."`

**Applied:** Today's 7:00 AM slot goes to the overnight game recap (D-backs 2, Cubs 0 on Aug 26) per research-playbook.md slow-day guidance. Off-day content leans into prospect news, roster moves, division watch, and series preview. No game-day hype slots used. Slots beyond 5:00 PM (pre-game, in-game, post-game) are omitted.

---

### STORY 1: Series Finale Recap — D-backs 2, Cubs 0

**Angle:** Eduardo Rodriguez overpowered the Cubs offense — 9 strikeouts in 7 innings — while Boyd pitched well enough but couldn't get Cubs any runs. Cubs go 1-2 in Arizona. Leads with the pitching performance (stat: 9 Ks), NOT the final score (per has_score=False finding).

**Hook options:**
- "Eduardo Rodriguez threw a NINE-strikeout gem and the Cubs offense had no answer" → stat-forward, no score in lead
- "Boyd's ERA held at X but E-Rod's 9 Ks shut the door in the rubber game" → pitching duel framing

**Insight adjustment:** Lead with "9 strikeouts" stat, avoid "2-0" in the first line. Kicker can acknowledge split.

**Tone:** Measured — a game-two loss on the road, series split. Not devastating. Informative.

---

### STORY 2: Swanson Injury Update

**Angle:** Dansby Swanson's oblique strain (4-6 weeks, Grade 2) is the most pressing roster story of the stretch run. Hoerner to SS (natural position), Ramirez stepping up at 2B. This isn't a doom post — it's a real baseball consequence with a silver lining (Hoerner is a plus SS defender).

**Hook options:**
- "Hoerner to shortstop is the move — he's the best defensive option. The question is who covers 2B down the stretch."
- "Swanson's oblique ends his regular season. Cubs are counting on Ramirez + Hoerner's defense to hold up."

**Tone:** Bold, honest — fan frustration channel without being doom-and-gloom. Silver lining: postseason return is possible.

---

### STORY 3: PCA MVP Watch

**Angle:** 7.9 bWAR leading all of baseball through Aug 26, 33 HRs, 155 OPS+. This isn't just a Cubs talking point — it's an elite season by any historical standard. 29/37 MLB experts agree. That's a stat + opinion sandwich.

**Hook options:**
- "7.9 bWAR. He's leading EVERY PLAYER IN BASEBALL. Not just the NL."
- "29 of 37 MLB experts voted Pete Crow-Armstrong as NL MVP. The other 8 haven't watched enough Cubs games this summer."

**Tone:** Bold, proud. Classic Cubs brand voice stat-backed take.

---

### STORY 4: Wild Card Watch

**Angle:** Cubs sitting comfortable at 76-57, WC1. Phillies and Padres are the main competition. Cardinals are fading (66-66). Division leader Brewers still the class of the NL Central but Cubs are well-positioned for October.

**Hook options:**
- "Cardinals 66-66. It's almost September. The math isn't kind to St. Louis."
- "Cubs WC1, 19 games over .500. They need roughly 14 more wins in 29 remaining games for a comfortable October."

**Tone:** Rival jab (Cardinals) + confident standings take. Analytics-backed.

---

### STORY 5: Reds Series Preview

**Angle:** Cubs return home to Wrigley for a 3-game set vs. 62-70 Cincinnati. Reds are 14 games under .500, 24 games behind the Cubs. Favorable matchup on paper. Sunday Night Baseball game (Aug 30) adds national spotlight. Cubs' .554 slugging vs. Reds' .470 is the matchup edge.

**Hook options:**
- "Cubs are back home at Wrigley. The Reds (62-70) are coming to town. Let's win the damn series."
- "Friday. Wrigley. Cubs hosting a 62-70 Reds squad. The offense wakes up now."

**Tone:** Confident, fan-energy preview. Home series hype.

---

### STORY 6: Jaxon Wiggins Prospect Spotlight

**Angle:** Wiggins hasn't allowed a hit in 4 straight relief appearances for Iowa. That's a legitimate statistical standout — not a "he looks promising" take, but a hard performance data point. Pair with Kipp's 7-K outing for a broader Iowa prospects update.

**Hook options:**
- "Jaxon Wiggins: 4 appearances. 0 hits allowed. Still going."
- "The Cubs' top pitching prospect hasn't been touched in four straight relief outings at Iowa."

**Tone:** Informative, stat-forward (per has_stat finding). Low-key excitement — this is a prospect note, not a headline.
