# Story Analysis — June 6, 2026

---

### Series context

**is_series_start_today:** false
**off_day:** false
**Series:** Cubs (33-31) vs. San Francisco Giants (26-38), 2-game set at Wrigley Field
**Rationale from snapshot:** "Same opponent (San Francisco Giants) as yesterday — this is mid-series, not a series opener."
**Today's game:** Game 2 of 2, 1:20 PM CT, Wrigley Field

Implication: No dedicated series-preview tweet slot needed. Reference the opponent and series stakes in game-related tweets as context, but no standalone preview is mandated.

---

### Insights applied

**Source:** Cubs/_data/insights.json (generated_at: 2026-06-06T08:30:00Z, n=71 measured tweets)

**Finding 1: has_allcaps=True wins (medium effect, Cliff's delta=0.407, p=0.0275)**
- Winner: allcaps present. Loser: no allcaps.
- Applied: Every tweet has 1-2 ALL CAPS emphasis words. Examples used: "EIGHTEEN," "TORCHED," "WORST," "BOTH," "SMOKING," "REAL."
- Brand voice allows "1-2 words max" ALL CAPS — this finding confirms that ceiling. No changes to the brand-voice ceiling; finding reinforces existing practice.

**Finding 2: posting_window=morning_06_12 loses (medium effect, p=0.0076)**
- Loser: morning 6–12 AM CT. Winner: not-morning.
- Applied: Reduced morning slots to 1 (the 7:00 AM game-recap slot). The research playbook mandates game recaps in the "first available slot" — overriding the loser-window preference for this one post. All other content shifted to midday window. 8:15 AM, 9:30 AM, and 10:45 AM slots all skipped.

**Finding 3: posting_window=midday_12_18 wins (medium effect, p=0.0076)**
- Winner: midday 12 PM–6 PM CT.
- Applied: 5 of 6 tweets scheduled in the 12:00 PM–5:00 PM CT range. Story 2 (12:00 PM), Story 3 (1:15 PM), Story 4 (2:30 PM), Story 5 (3:45 PM), Story 6 (5:00 PM). Evening slots (6:30 PM+) skipped because game outcome is unknown.

**Finding 4: has_stat=True wins (medium effect, p=0.0159)**
- Winner: stat present. Loser: no stat.
- Applied: Every tweet contains at least one specific stat.
  - Story 1: "8 runs," "19 of their last 25," "2 HRs"
  - Story 2: "1.92 ERA," "4.22 ERA," "18-3"
  - Story 3: ".181," "$177M"
  - Story 4: "33-31"
  - Story 5: ".455 BA," "1.409 OPS"
  - Story 6: "33-31," "37-23," "32-28"

**Findings NOT in significant_findings today:**
- has_emoji_first_line: not measured/not significant → follow brand-voice defaults (1-3 emojis placed naturally)
- content_type=brief: not appearing as a finding (all posts are briefs per platform, no change)
- len_bucket: no finding → no character-length adjustment beyond brand-voice guidance

**Conclusion:** 4 findings applied. No findings were empty; full adjustment made to allcaps, timing, and stat inclusion. No brand-voice prescriptions were contradicted by the findings (brand voice already allows ALL CAPS and recommends stats).

---

### STORY 1: Giants 18, Cubs 3 — Cabrera Shelled on IL Return

**Tier:** 1
**Angle:** Reset framing — don't dwell on the carnage, pivot to Brown on the mound today. Lead with the score (has_score=TRUE isn't in significant_findings but it's always good practice for recaps).
**Hook:** "EIGHTEEN to 3" — leads with the brutal number, no softening. ALL CAPS on "EIGHTEEN" for the biggest emphasis moment.
**Stats used:** 8 runs allowed, 19 of last 25 losses, 2 HRs each for Chapman and Adames.
**Slot rationale:** Morning window is a performance loser, but game recaps are mandated in "first available slot" by research playbook. Posting priority rule (game recaps first) overrides the loser-window avoidance.
**Follow-up:** Tomorrow morning — today's game result (Brown vs. Roupp).

---

### STORY 2: Ben Brown Takes the Mound

**Tier:** 1
**Angle:** The cleanup crew. After last night's disaster, Brown's 1.92 ERA (6th in baseball) is the antidote. He's having the best season by a Cubs starter in years. Preview positions him as a difference-maker.
**Hook:** Stat-led with Brown and Roupp ERAs front and center. "Giants TORCHED the Cubs 18-3 last night" grounds the context without leading with negativity.
**Stats used:** 1.92 ERA, 4.22 ERA, 18-3 (yesterday's score for contrast)
**Slot:** 12:00 PM CT — midday winner window, 80 minutes before first pitch.
**Follow-up:** Tomorrow morning — Brown's stat line and outcome.

---

### STORY 3: Dansby Swanson Slump

**Tier:** 2
**Angle:** Accountability take, stat-backed. Third-lowest BA among qualified hitters on a $177M deal. Counsell isn't benching him. Walk rate is genuinely career-best, xwOBA is better than the BA — so this is a real slump but not necessarily a permanent decline.
**Hook:** ".181. On a $177M contract." — contrast drives engagement without being doom-posting.
**Stats used:** .181 BA, $177M contract
**Slot:** 1:15 PM CT — midday winner window, game already underway.
**Follow-up:** Swanson June numbers as sample builds.

---

### STORY 4: Shaw and Boyd Returns

**Tier:** 2
**Angle:** Good news for a team that badly needs reinforcements. Two significant pieces — a batting lineup depth piece (Shaw) and a rotation anchor (Boyd). Frame as cavalry arriving at a critical juncture.
**Hook:** "The cavalry is coming." — clear, punchy.
**Stats used:** "33-31" team record — grounds the urgency.
**Slot:** 2:30 PM CT — midday winner window.
**Follow-up:** Boyd activation announcement (expected June 7-8); Shaw return to active roster.

---

### STORY 5: PCA Hot Streak

**Tier:** 2
**Angle:** Positive, stat-backed, forward-looking. The early-season cold Cubs fans worried about is clearly over. Walk-off June 4 as anchor; last-5-games numbers as proof.
**Hook:** "Pete Crow-Armstrong in his last 5 games: .455 BA, 1.409 OPS."
**Stats used:** .455 BA, 1.409 OPS, walk-off June 4 reference.
**Slot:** 3:45 PM CT — midday winner window.
**Follow-up:** PCA June stats as they accumulate.

---

### STORY 6: NL Central Standings

**Tier:** 2
**Angle:** Context and urgency. Cubs are in a hole but not out of contention. 22 sub-.500 opponents in June is the window. Need consistency.
**Hook:** All three records up front — Cubs, Brewers, Cardinals.
**Stats used:** 33-31, 37-23, 32-28 (standings), "1 game back of St. Louis."
**Slot:** 5:00 PM CT — midday winner window.
**Follow-up:** Weekly NL Central check-in.
