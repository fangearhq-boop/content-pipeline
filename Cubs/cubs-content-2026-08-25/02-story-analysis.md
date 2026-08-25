# Chicago Cubs Fan HQ — Story Analysis
## Date: 2026-08-25

---

### Insights Applied

**Findings from /tmp/cubs-insights.json (generated 2026-08-25T08:30:00Z):**

Two findings cleared all three significance gates (n≥8, Mann-Whitney U p<0.05, |Cliff's delta|≥0.20):

**Finding 1: `has_stat=True` beats `has_stat=False`**
- Median impressions: 103.5 (with stat) vs 85.0 (without stat)
- Effect size: Cliff's delta = 0.217 (small), p = 0.045
- Action: Every tweet drafted with ≥1 concrete, specific stat. This finding has cleared gates three consecutive runs (Aug 22, 23, 24 all showed has_stat=True as winner) — signal is stable.

**Finding 2: `has_score=False` beats `has_score=True`**
- Median impressions: 102.5 (no score) vs 80.0 (with score)
- Effect size: Cliff's delta = 0.210 (small), p = 0.049
- Action: No tweet leads with a final game score. This directly overrides the brand-voice.md rule "Score format: Winner first." Instead, game recap tweet leads with Gausman's pitching stat line (7 IP / 6 K / 0 ER), not "Cubs 7, Diamondbacks 0." Final scores are omitted from all tweets.
- Note: Season records (e.g., "76-56") are stats, not game scores — they are kept per has_stat=True finding.

**Applied changes from standard brand-voice defaults:**
- Recaps restructured around performance stats, not final scores
- No tweet opens with "Cubs won X-Y" format

---

### Series Context

`is_series_start_today=FALSE`. Mid-series vs Arizona Diamondbacks (Game 2 of 3).
- Cubs 76-56 (WC1) vs D-backs 69-63
- Cubs won Game 1 (Gausman shutout per research)
- Tonight: Game 2 at 8:40 PM CT, Holmes vs Pfaadt
- Tomorrow: Series finale, Wed 2:40 PM CT

No dedicated series-preview slot per STEP 0.5 rules (reserved only for is_series_start_today=TRUE). Today's 12:00 PM CT slot carries the Game 2 preview angle. Series stakes referenced in WC Watch and First Pitch Hype tweets.

---

### STORY 1: Game 1 Recap — Gausman's Masterclass

**Freshness tags:** Gausman-shutout, Chase-Field, Game1-win

**Summary:** Kevin Gausman delivered one of his sharpest starts as a Cub, throwing 7 scoreless innings on 3 hits and 6 strikeouts in a dominant shutout of the Diamondbacks. The Cubs, playing in Arizona with playoff seeding implications, got exactly what a trade-deadline rotation upgrade is supposed to produce.

**Relevance:** Cubs fans have been waiting for this version of Gausman since he arrived. He'd been solid but uneven since the trade — this outing was the full package. Leading a WC1-vs-WC-bubble matchup with a gem sets the tone for a pivotal series.

**Angles:**
1. The performance angle: 7 IP, 6 K, 0 ER is ace-level work. Gausman didn't just win — he dominated.
2. The deadline-investment angle: This is what Jed Hoyer paid for. The trade looks great right now.
3. The series-control angle: Cubs lead 1-0, forcing D-backs into must-win territory.
4. The bullpen-rest angle: 7 innings saved the pen. With two more games including a day game tomorrow, this matters.
5. The postseason-form angle: If Gausman pitches like this in October, Cubs are dangerous.

**Engagement hooks:**
- Bold: "This is what a playoff rotation ace looks like. Gausman gets it."
- Fan energy: Dominant road shutout in a WC battle is peak Cubs fan satisfaction.

**Tone:** Informative with bold undertone. Gausman gets the respect he earned.

---

### STORY 2: Cardinals Rival Watch

**Freshness tags:** Cardinals-fading, 66-66, WC-out-of-reach

**Summary:** The Cardinals are 66-66 in late August, five games out of the final NL Wild Card spot. Their run since the trade deadline has been flat and uninspiring. They're playing Baltimore tonight while the Cubs are extending their own playoff lead in Arizona.

**Relevance:** Cubs fans love a Cardinals-are-bad take in any month. When the Cards are legitimately sinking in August, that's validated schadenfreude. This is the rivalry content that performs.

**Angles:**
1. The record angle: .500 in August is brutal when you're chasing a WC spot.
2. The math angle: 5 games out with 37 games remaining — they'd need to go something like 25-12 to have a chance.
3. The summer-of-mediocrity angle: The Cardinals peaked in spring, faded through August.
4. The comparison angle: Cubs 76-56 while Cards are 66-66 — a 10-win gap.
5. The timing angle: Mid-August is the last moment to mount a run. They're out of runway.

**Tone:** Sharp, witty. Classic Cubs-fan-roasting-Cardinals energy.

---

### STORY 3: Pete Crow-Armstrong MVP Watch

**Freshness tags:** PCA-MVP, 30-30, season-arc

**Summary:** Pete Crow-Armstrong sits at .279, 33 HR, 31 SB, and approximately 8.2 fWAR — leading all of baseball in the latter. He's currently the favorite on most NL MVP betting markets, overtaking Shohei Ohtani in recent weeks. This is his second consecutive 30-30 season.

**Relevance:** PCA is the centerpiece of the Cubs' playoff push AND a historic individual performance. Cubs fans have a genuine MVP candidate in the outfield for the first time in years. This isn't premature hype — it's documented via fWAR leadership.

**Angles:**
1. The fWAR angle: Leading all of baseball is the most objective MVP metric.
2. The 30-30 angle: Two straight 30-30 seasons is Hall of Fame territory in the making.
3. The two-way angle: Power + speed + elite center-field defense = no comparable player.
4. The Ohtani comparison: PCA is ahead of Ohtani in MVP betting — that's not a small claim.
5. The timing angle: Peak PCA coincides with peak Cubs playoff push. This team is built around him.

**Tone:** Stat-backed confidence. This is what the "Informed" brand voice pillar was made for.

---

### STORY 4: Wild Card Watch

**Freshness tags:** WC1-Cubs, D-backs-sliding, playoff-race

**Summary:** With the Game 1 win, Cubs are 76-56 and holding WC1 with distance to spare. The Diamondbacks, now 69-63, lost their best chance to close ground. Arizona is chasing WC3 with Padres ahead of them.

**Relevance:** Playoff context is always relevant in late August. With every Cubs win, the margin for error shrinks for their competition — that's a story worth telling in standings form.

**Angles:**
1. The Cubs' cushion angle: 76-56 and WC1 with Phillies, Padres behind them.
2. The D-backs' math angle: They needed this series to make a run — now they need to win the next two.
3. The calendar angle: With 30 games left, each loss matters more.
4. The WC3 angle: D-backs vs Padres fight for the last spot is a subplot to watch.
5. The confidence angle: Cubs have won 5 of their last 7 in a stretch of tough road play.

**Tone:** Informative with an edge of confidence. Cubs are in the driver's seat.

---

### STORY 5: Game 2 Preview — Holmes vs. Pfaadt

**Freshness tags:** Holmes-starts, Pfaadt-matchup, Game2-preview

**Summary:** Tonight's Game 2 is Clay Holmes vs. Brandon Pfaadt at 8:40 PM CT. Holmes (2.49 ERA) has been steady since joining Chicago at the trade deadline. Pfaadt (3.39 ERA) is Arizona's most consistent arm. This has the look of a low-run pitcher's duel.

**Relevance:** After Gausman's shutout in Game 1, the Cubs need their No. 2 deadline acquisition to match the energy. Holmes has been doing exactly that since his return from injury.

**Angles:**
1. The deadline-investment angle: Holmes and Gausman are the 1-2 punch the Cubs needed.
2. The ERA comparison angle: 2.49 vs 3.39 — Cubs have a meaningful edge on paper.
3. The injury-return narrative: Holmes missed two months with a fractured fibula, came back throwing 2.49 ERA baseball.
4. The series-control angle: A Cubs win tonight forces Arizona to avoid being swept in a must-win situation.
5. The pitchers' duel angle: After yesterday's 7-0 game, an expectation of low offense sets an interesting tone.

**Tone:** Informative with a confident take. Cubs have the pitching edge tonight.

---

### STORY 6: Iowa Prospects Update

**Freshness tags:** Garrett-gem, Iowa-win, Shaw-rehab

**Summary:** Iowa beat Toledo 4-2 on Sunday behind Braxton Garrett's outstanding outing (5 IP, 7 K, 0 ER). Matt Shaw continues his rehab assignment with the I-Cubs. The system is healthy and active as September approaches.

**Relevance:** Cubs fans tracking the prospect pipeline want to know the minor league system is producing. With Shaw, Brown, and others progressing, September depth looks real.

**Angles:**
1. The Garrett angle: 7 strikeouts in 5 scoreless innings is a breakout-caliber outing for the starter.
2. The Shaw-return angle: Still rehabbing but progressing toward September activation.
3. The depth angle: Iowa going 4-2 with Garrett dealing shows the system has more than just the top guys.
4. The September roster angle: Cubs can add 28-man September roster flexibility — healthy arms matter.
5. The development angle: Garrett flashing this stuff in late August bodes well for future rotation depth.

**Tone:** Informative/feature. Understated confidence in the system.

---

### STORY 7: First Pitch Hype

**Freshness tags:** Holmes-starts, Chase-Field, Game2-hype

**Summary:** Clay Holmes takes the mound at Chase Field at 8:40 PM CT. The Cubs lead this series 1-0 after Gausman's gem. Arizona is desperate to avoid falling down two games in their Wild Card window.

**Angles:**
1. The matchup setup angle: Holmes on the mound, Cubs up 1-0, Arizona desperate.
2. The urgency angle: Every win for the Cubs here tightens the noose on D-backs playoff math.
3. The road-warrior angle: Cubs are winning away from Wrigley when it matters most.
4. The momentum angle: Back-to-back great starts from deadline acquisitions would be a statement.
5. The fan energy angle: Road games in playoff battles are where October legacies are built.

**Tone:** Bold, hype, electric. Evening slot energy.
