# Story Analysis — Cubs 2026-08-13

---

### Insights applied

**Significant findings (generated_at: 2026-08-13T08:30:00 UTC, measured_tweet_count: 127):**

| Dimension | Winner | Loser | Median W | Median L | n_W | n_L | p | delta | Label |
|-----------|--------|-------|----------|----------|-----|-----|---|-------|-------|
| has_score | False | True | 124 | 78 | 80 | 47 | 0.0001 | 0.409 | medium |

**Finding 1: has_score=False > has_score=True (p=0.0001, Cliff's delta=0.409)**
- Effect: tweets that do NOT mention the final score get 59% higher median impressions than those that do
- This is counter-intuitive but statistically robust (p=0.0001, medium effect size, n=80 vs n=47)
- Application:
  - Story 1 (Game 2 Recap): Lead is "Bregman and Swanson went to work again" — NOT "Cubs won 12-6." Final score appears only in research files, not in the tweet itself.
  - Story 2 (Cardinals/WC): Cardinals' W-L record (59-59) is standings data, not a game score — this is acceptable per the `has_score` dimension which refers to game final scores.
  - Story 4 (Game Preview): No score reference in the preview (there is no score yet).
  - Story 5 (Hype): No score reference.
- Net effect: Changed all drafts to lead with narrative, players, or narrative context rather than final score.

**No other significant findings.** (significant_findings has 1 entry, sorted by descending effect size.)

**Methodology note:** raw_buckets were NOT consulted for drafting decisions. Only significant_findings were used.

---

### Series context

**is_series_start_today:** false
**off_day:** false
**Opponent:** Washington Nationals (59-63)
**Venue:** Nationals Park (Cubs away)
**Series:** Mid-series (Game 3 of 3); rationale from snapshot: "Same opponent (Washington Nationals) as yesterday — this is mid-series, not a series opener."
**Today's game:** Thu Aug 13, 3:05 PM CT

**Implication:** No dedicated series-preview tweet required (not a series opener). The game preview (Story 4) notes this is the series finale with a sweep on the line — appropriate mid-series framing. Story 5 provides the hype hook.

---

### STORY 1: Game 2 Recap — Cubs 12, Nationals 6 (Aug 12)

**Angle selected:** Narrative-led performance angle (Bregman/Swanson/Peterson/Webb) without the final score — per has_score=False insight.

**Hook:** "Bregman and Swanson went to work again last night."
**Context:** Peterson's performance relative to his 6.09 ERA is the contrarian stat hook. Webb as bullpen hero adds specificity.
**Kicker:** "Cubs offense? Relentless." — punchy, brand-voice aligned (bold, passionate)

**Alternatives considered:**
- Score-first: "Cubs 12, Nationals 6 — Chicago keeps rolling." Rejected: violates has_score=False finding.
- Bregman-specific HR count: "Bregman hit 3 HRs in Game 2." Rejected: LOW confidence on that specific claim; BCB headline doesn't lead with Bregman as hero.

---

### STORY 2: Cardinals at .500 / Wild Card update

**Angle selected:** Cardinals roast anchored to standings data — brand-voice "sharp, competitive, historic rivalry energy."
**Hook:** "The Cardinals are 59-59."
**Context:** Cubs at 71-50, currently embarrassing a team on the road (Nationals context).
**Kicker:** "August is here. The NL Central picture couldn't be clearer." — subtle divisional dominance claim.

**Why Cardinals, not Brewers?** Brewers are 74-47 and are actually leading the division — the story there isn't rivalry roast, it's a genuine division chase. The Cardinals at 59-59 are the appropriate roast target today.

---

### STORY 3: PCA MVP — WAR 7.5

**Angle selected:** Analytical take on odds movement as a calibration narrative. The jump from +700 (All-Star break) to -120 (current) is the story.
**Hook:** "Pete Crow-Armstrong's WAR sits at 7.5 — No. 1 in ALL of baseball."
**Context:** The odds shift reflects voters catching up to what the stats have shown since June.
**Kicker:** "The voters are catching up to what Chicago fans already knew." — passionate, confident, brand-voice aligned.

**Avoided:** Specific claims about WAR compared to "franchise records" or "first to X" — no superlative claims that would require two-source verification beyond what search results confirmed.

---

### STORY 4: Game Preview — Gausman vs Cavalli

**Angle selected:** Gausman-as-deadline-acquisition completes his purpose narrative. Framing is "acquired for exactly this moment."
**Hook:** "Kevin Gausman takes the mound at Nationals Park today. First pitch 3:05 PM CT."
**Context:** Gausman's deadline acquisition + 2-0 series lead + sweep opportunity.
**Kicker:** "This lineup has answers." — team confidence framing.

**Avoided:** Gausman's 6-10 record (misleading negative frame; Cubs acquired him to strengthen the rotation for the stretch run). His ERA (4.29) also not included — not relevant to the narrative.

---

### STORY 5: Pre-Game Hype

**Angle selected:** "Two down, one to go" sweep narrative.
**Hook:** "Two down in D.C. One more to go." — direct, punchy.
**Context:** Offensive dominance throughout the series without the score.
**Kicker:** "When this team has momentum, they're impossible to stop." — passionate close.

**Avoided:** Season record since June 10 ("34-34 on June 10") — already covered in Aug 12 Story 3. Fresh angle needed.

---

### Content Mix Check

| Tweet | Type | Pillar |
|-------|------|--------|
| 1 — Game recap | Informative | Passionate |
| 2 — Cardinals roast | Bold/Humor | Rival jab |
| 3 — PCA MVP | Informative/Bold | Stat-backed take |
| 4 — Game preview | Informative | Game day |
| 5 — Hype | Bold | Fan energy |

Mix: 3 informative, 2 bold/hype. Approximately 60/40 informative/bold — within the 50/50 target zone.
