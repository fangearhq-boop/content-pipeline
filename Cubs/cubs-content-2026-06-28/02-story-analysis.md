# Cubs Story Analysis — 2026-06-28

---

## ### Insights Applied

**Source:** Cubs/_data/insights.json (generated_at: 2026-06-28T08:30:00 UTC)
**Findings count:** 2 (significant_findings — all three gates cleared: n≥8, Mann-Whitney U p<0.05, |Cliff's delta|≥0.20)

| Rank | Dimension | Winner | Loser | Delta | p | Applied |
|------|-----------|--------|-------|-------|---|---------|
| 1 | posting_window=midday_12_18 | midday (12–6 PM CT) | not-midday | 0.275 (small) | 0.049 | 4 of 5 slots placed in 12:00–6:30 PM CT window |
| 2 | posting_window=morning_06_12 | not-morning | morning | 0.275 (small) | 0.049 | Only 7:00 AM slot retained (mandatory game recap); 8:15/9:30/10:45 AM skipped |

**No significant findings** for: has_emoji_first_line, has_allcaps, len_bucket, has_score, content_type.

**How findings changed today's drafts:**
- The 7:00 AM game recap slot was retained because it is mandatory (overnight game results always post in first available slot per research-playbook.md). No other morning slots were used.
- The Game 3 preview was pushed from 10:45 AM (typical pre-game slot) to 12:00 PM, placing it inside the midday winner window while still posting 70 minutes before first pitch.
- PCA feature, rotation deadline, and wild card analysis all placed in 3:45 PM, 5:00 PM, and 6:30 PM respectively — maximum concentration in the midday_12_18 window.
- No other brand-voice prescriptions were overridden by the findings (emoji guidance, ALLCAPS, content_type all remain at brand-voice defaults).

---

## ### Series Context

**Source:** Cubs/_data/series-context.json (generated_at: 2026-06-28T08:30:00 UTC)

**is_series_start_today:** false
**off_day:** false
**Opponent:** Milwaukee Brewers (50-30, American Family Field)
**Today:** Game 3 of 3 (series finale)

Cubs split the first two games of this road series at Milwaukee: lost Game 1 on June 26 (Brewers 6, Cubs 2 — Jacob Misiorowski dominant) and won Game 2 on June 27 (Cubs 8, Brewers 2 — Imanaga started). Today is the decisive series finale at 1:10 PM CT.

**No dedicated series-preview tweet required** (is_series_start_today=false). Series context informs the Game 3 preview framing (series tied 1-1, winner takes it).

---

## Story Angles and Hooks

### STORY 1: Game Recap — Cubs 8, Brewers 2 (June 27)

**Angle:** Bounce-back narrative. After Misiorowski shut them down in Game 1, the Cubs erupted for eight runs to even the series. Imanaga delivered the start they needed. Now it comes down to a Game 3 today.

**Hook:** "Cubs 8, Brewers 2." — score first, then the bounce-back context, then the teaser for Game 3. Short, punchy opening. Score format (winner first per brand-voice).

**Tweet tone:** Informative with a hint of momentum energy. Not triumphant — the series is tied and Game 3 determines the winner.

---

### STORY 2: Game 3 Preview — Rolison vs. Woodruff

**Angle:** Rolison-as-surprise-ace framing. With five starters on the IL, Ryan Rolison (5-1, 1.82 ERA) has quietly become one of the better arms in the NL. Today's matchup pits him against Woodruff returning from injury. Series on the line.

**Hook:** Lead with Rolison's numbers immediately — "Ryan Rolison (5-1, 1.82 ERA) takes the ball at 1:10 PM CT." Stat-backed opener, then context.

**Tweet tone:** Informative — game preview with confidence in Rolison's ability. Not hype, not doom. Matter-of-fact with quiet pride.

**Scheduling note:** Pushed from 10:45 AM to 12:00 PM per midday_12_18 winner finding. Still well before 1:10 PM first pitch.

---

### STORY 3: Pete Crow-Armstrong — June for the Ages

**Angle:** PCA as the engine of this Cubs team — doing it while five starters are hurt, on a 10-HR June pace that's simply historic for a 24-year-old center fielder. All-Star caliber season framed as editorial take, not a factual claim about selection.

**Hook:** "Pete Crow-Armstrong in June: 10 home runs. .867 slugging." — numbers first. Let the stats make the argument, then add the context about carrying the offense while the rotation is in pieces.

**Tweet tone:** Bold/Passionate. This is a player feature. Use CARRYING in all-caps per brand voice (1-2 words max). End with a strong editorial statement ("All-Star caliber season. Not a debate.").

---

### STORY 4: Rotation Crisis — Trade Deadline in 36 Days

**Angle:** The math is simple: five starters on the IL + August 3 deadline in 36 days = Jed Hoyer has to act. Rolison can't carry this rotation alone indefinitely. Wiggins is rehabbing an elbow and isn't a solution in the near-term. This is the defining challenge of the 2026 Cubs season.

**Hook:** "Five Cubs starters on the IL. The August 3 trade deadline is 36 days away." — plain statement of stakes. Counts up the problem, then makes the demand.

**Tweet tone:** Bold/Analysis. Declarative sentences. End with "The deadline defines this season." — a genuine editorial stake that the brand is willing to plant.

---

### STORY 5: Wild Card Watch — Records, Gap, Path Forward

**Angle:** Cubs 45-38, Brewers 50-30, 6.5 GB in the NL Central. The division isn't the path — the Wild Card is. But even the Wild Card requires a rotation fix before August 3. Every result in this division series matters.

**Hook:** "Cubs 45-38. Brewers 50-30. Six and a half games back in the NL Central." — honest accounting of the gap. Don't sugarcoat. Then pivot to the Wild Card framing.

**Tweet tone:** Bold/Analysis. Honest assessment of the standings without doom. The Wild Card path is real; don't make it sound impossible. End with the deadline urgency callback.

---

## Content Mix Assessment

| Story | Type | Tone |
|-------|------|------|
| Story 1 (recap) | Informative | Matter-of-fact/momentum |
| Story 2 (preview) | Informative | Confident/stat-backed |
| Story 3 (PCA) | Bold/Passionate | Pride/conviction |
| Story 4 (rotation) | Bold/Analysis | Urgent/declarative |
| Story 5 (standings) | Bold/Analysis | Honest/forward-looking |

**50/50 balance:** 2 informative / 3 bold-analytical. Acceptable for a game day with a 1:10 PM CT first pitch — the morning slot is locked informative (mandatory recap), and the analytical/bold content clusters in the midday winner window where it performs better.
