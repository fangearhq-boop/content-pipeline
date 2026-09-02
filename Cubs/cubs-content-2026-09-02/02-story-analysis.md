# Cubs Story Analysis — 2026-09-02

---

### Insights applied

**Findings read (from Cubs/_data/insights.json, generated 2026-09-02T08:30:00 UTC):**

3 significant findings cleared all three gates (n≥8, p<0.05, |Cliff's delta|≥0.20):

1. **`has_stat=True` beats `has_stat=False`** — median impressions 109 vs. 82, Cliff's delta 0.276 (small effect), p=0.0102.
   - **Applied:** Every tweet bakes in at least one hard number. No abstract takes without a stat anchor. Game recap leads with "Brewers 9, Cubs 4." Preview leads with Misiorowski's ERA/record/SO. Wild Card tweet includes Cubs record and Cardinals record. Swanson tweet includes the IL date. PCA tweet leads with the stat line. Pre-game tweet includes Misiorowski's ERA.

2. **`posting_window=midday_12_18` wins** — median impressions 111 vs. 83, Cliff's delta 0.221 (small effect), p=0.0395.
   - **Applied:** Five of six tweets scheduled between 12:00 PM and 5:00 PM CT (the upper edge of midday). The 7:00 AM slot is kept only because the game recap is time-anchored to morning. Morning slots 8:15, 9:30, and 10:45 AM are skipped entirely — content that would have gone there (Wiggins callup push, a standalone roster note) is either deferred to midday or omitted.

3. **`posting_window=morning_06_12` is the LOSER** — winner is "not_morning_06_12," median impressions 111 vs. 83, Cliff's delta 0.221 (small effect), p=0.0395.
   - **Applied:** Only one tweet in this window: the 7:00 AM game recap (anchored by timing convention and audience expectation — fans check overnight recap first thing). The three other morning slots are skipped.

**No changes from raw_buckets:** Raw bucket data was not used to make any decisions. Significant findings exclusively drove adjustments.

**No overrides of brand-voice prescriptions:** No significant finding directly contradicts brand-voice defaults today. Emoji guidance remains per brand-voice (1-3 per post, placed naturally) — no findings on emoji presence in significant_findings.

---

### Series context

**`is_series_start_today=false`** — This is Game 2 of a 2-game series against the Milwaukee Brewers (series started September 1). No dedicated series-preview slot today.

**Mid-series context used:**
- Cubs (78-61) host Brewers (86-53) at Wrigley Field
- Cubs lost Game 1 last night, 9-4
- Tonight: Jacob Misiorowski (14-5, 1.73 ERA) vs. David Peterson (7-7, 5.11 ERA), 6:40 PM CT
- Series clinch/split math informs the game preview and pre-game hype framing

**Off day: false** — Cubs play tonight.

---

### Story Selection Rationale

**Story 1: Game recap (loss)** — Tier 1, mandatory. Game losses still get the recap slot. Angle: accountability framing. Boyd's third-time-through trap in the 6th is the mechanism; Palencia's bad relief compounded it. Not doom-posting — "fix it tonight" closer.

**Story 2: Game 2 preview (Misiorowski)** — Tier 1. This is the most compelling story of the day: Misiorowski's 1.73 ERA is the best in baseball. Cubs draw him in a must-split situation. High-stakes, stat-rich, naturally compelling. Scheduled at 12:00 PM (midday window winner).

**Story 3: Wild Card watch / Cardinals** — Tier 2 follow-up. Last covered Sept 1. Today's angle: Cubs 78-61 with 23 games left, Cardinals effectively eliminated. Rival jab at Cardinals. Fresh numbers validate the update.

**Story 4: Swanson + Steele** — Tier 2 follow-up. New developments since last coverage: Swanson swinging for the first time (Sept 1), Steele Iowa rehab assignment this week. Genuinely new status for both. Scheduled at 2:30 PM to stay in midday window.

**Story 5: PCA 40-40 / MVP** — Tier 2. Stats moved since last dedicated PCA feature (Aug 30 — MVP odds). Now at 36 HR / 32 SB; the 40-40 angle is mathematically fresh (4 HR + 8 SB in 23 games = realistic and exciting). Stat-heavy tweet fits the has_stat winner insight perfectly.

**Story 6: Pre-game hype** — Tier 1. Tonight's game stakes (must split vs. the best pitcher in baseball) create natural hype. 5:00 PM slot is at the edge of midday window (within 12-6 PM range), appropriately placed for pre-game energy.

**Stories skipped:**
- Jaxon Wiggins callup push — genuinely worth covering but no new information beyond "still not called up." Last covered Aug 30. Would require morning slot (loser window) or displace a stronger midday story. Will revisit if he's officially called up.
- BJ Murray MLB debut performance — Murray was called up Sept 1 and was in the lineup, but no box-score detail available on his debut performance. Would need specific stats to be worth a tweet. Follow-up when stats are confirmed.
- Tyrone Taylor individual game performance — role in the loss unclear from searches; leaving out rather than speculating.

---

### Angles, Hooks, Headlines

| Story | Angle | Hook |
|-------|-------|------|
| Game 1 recap | Accountability/bounce-back | Boyd's 6th-inning trap; Palencia compounded it |
| Game 2 preview | Best pitcher in baseball + must-split | Misiorowski's 1.73 ERA as the obstacle |
| Wild Card / Cardinals | Rival elimination + Cubs position | Cardinals effectively dead at 68-71 |
| Swanson + Steele | Two October weapons on track | First swings, Iowa rehab same week |
| PCA 40-40 | Closing argument for NL MVP | 4 HR + 8 SB = historic territory |
| Pre-game hype | Must crack the best ERA in baseball | Wrigley atmosphere as the Cubs' edge |
