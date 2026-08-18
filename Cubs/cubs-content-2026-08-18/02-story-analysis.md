# Story Analysis — 2026-08-18

---

### Insights applied

**Significant findings from insights.json (generated_at: 2026-08-18T08:30:00Z, measured_tweet_count: 124):**

| Dimension | Winner | Loser | Median (winner) | Median (loser) | p-value | Cliff's delta | Label |
|-----------|--------|-------|-----------------|----------------|---------|---------------|-------|
| has_score | False | True | 109.5 | 81.0 | 0.0069 | 0.289 | small |

**One significant finding applies to today's drafts:**

1. **has_score=False beats has_score=True (small effect, p=0.007, delta=0.289, n=76 vs 48)**
   - Tweets WITHOUT embedded game scores get median 35% more impressions than tweets WITH scores.
   - **Applied to all 8 posts today:** The game score (Cubs 7, White Sox 5) is intentionally omitted from every tweet. Story 1 leads with PCA's walk-off and milestone, NOT the final score. Story 5 (game preview) describes the match without embedding past scores.
   - This directly contradicts the brand-voice Score Format rule ("Cubs won 7-5"). Per the pipeline prompt, a significant_findings entry overrides any brand-voice prescription it directly contradicts. The has_score finding overrides score inclusion today.

**No other significant findings.** The `has_emoji_first_line`, `len_bucket`, `posting_window`, and `content_type` dimensions were NOT in significant_findings — meaning no adjustment is made to those dimensions beyond the brand-voice defaults.

---

### Series context

**Source:** Cubs/_data/series-context.json (generated_at: 2026-08-18T08:30:00Z)

- **off_day:** false — Cubs play tonight
- **is_series_start_today:** false — this is Game 2 (mid-series), not a series opener
- **Series:** Cubs vs Chicago White Sox, 2 remaining games (tonight and tomorrow)
- **is_cubs_home:** true — Wrigley Field
- **Game tonight:** 7:05 PM CT (Aug 19 00:05 UTC = Aug 18 7:05 PM CDT ✓)
- **Cubs record:** 73-53 | **White Sox record:** 65-59
- **Rationale in snapshot:** "Same opponent (Chicago White Sox) as yesterday — this is mid-series, not a series opener."

**Decision:** No series-preview slot reserved (is_series_start_today=false). The 7:00 AM slot goes to the game recap (game-1 result), not a series preview. Tonight's matchup is referenced in the 12:00 PM preview and 5:00 PM / 6:30 PM hype slots.

---

### STORY 1: PCA Walk-off / 30-30 Club — Game 1 Recap

**News hook:** Game 1 result (last night, Aug 17). Cubs 7, White Sox 5 in 10 innings. PCA hit a leadoff HR AND a walk-off HR — reaching 30 HR + 31 SB. First Cub ever with back-to-back 30-30 seasons.

**Angle:** Lead with PCA milestone, NOT score (insight applied). Walk-off is inherently dramatic; the score is secondary.

**Tier:** 1

**Posting window:** 7:00 AM CT (game recap slot)

**Style decision:** Informative/emotional blend. Three sentences, dramatic pacing. No emoji leading (not contraindicated — has_emoji_first_line was NOT a significant finding today — but brand voice leads with stat/action, not emoji, for game recaps).

**Hashtags:** #Cubs #GoCubs #FlyTheW (game day)

---

### STORY 2: PCA Franchise History

**News hook:** Same game; franchise history angle is a second, deeper take on PCA's achievement.

**Angle:** "First Cub ever with back-to-back 30-30 seasons." Sammy Sosa comparison. Bold/celebratory. Stat-backed.

**Tier:** 2

**Posting window:** 8:15 AM CT (bold take slot)

**Style decision:** Lead with exclusivity ("two-person club"). Reference Sosa for historical scale.

**Hashtags:** #Cubs #GoCubs #ChicagoCubs

---

### STORY 3: Wild Card Standings

**News hook:** Post-game standings update. Cubs lead NL Wild Card by 5 games. Brewers still lead division.

**Angle:** "Holding the line" frame. After a rough Cards series, Cubs are still WC1. Also sets up Brewers division gap.

**Tier:** 2

**Posting window:** 9:30 AM CT (stat breakdown/informative)

**Style decision:** Understated lead ("still holding the line"), then context. No records in tweet body per has_score insight spirit (avoiding raw numbers that read like scores).

**Hashtags:** #Cubs #NorthSiders #MLB

---

### STORY 4: Cardinals Reality Check

**News hook:** Cardinals are playing Reds tonight while sitting 13.5 GB in the division. Rival jab.

**Angle:** "They won a battle in August. Cubs still own October." Punchy, confident, not mean-spirited.

**Tier:** 2

**Posting window:** 10:45 AM CT (analysis/rival watch)

**Style decision:** Short, punchy sentences. Three beats: Cardinals swept Wrigley → but they're 13.5 GB → receipts.

**Hashtags:** #Cubs #GoCubs #ChicagoCubs

---

### STORY 5: Tonight's Game 2 Preview — Gausman

**News hook:** Kevin Gausman (6-11, 4.53 ERA) starts tonight. Game 2 of Crosstown Classic at Wrigley, 7:05 PM CT.

**Angle:** Deadline acquisition narrative. Cubs lead series 1-0. Gausman has the ball to potentially clinch the series win tonight.

**Tier:** 1

**Posting window:** 12:00 PM CT (game preview slot)

**Style decision:** Informative first (who's pitching), then context, then kicker.

**Hashtags:** #Cubs #GoCubs #FlyTheW

---

### STORY 6: Swanson MRI / Silver Lining

**News hook:** MRI confirmed Grade 2 oblique strain. 4-6 weeks. Could return Sept. 15.

**Angle:** Silver lining framing: bad news (grade 2, not minor), but he should be back for October. Counsell confident.

**Tier:** 2

**Posting window:** 2:30 PM CT (roster news/injury update slot)

**Style decision:** Lead with the diagnosis, then timeline, then the hopeful kicker.

**Hashtags:** #Cubs #CubsBaseball #MLB

---

### STORY 7: Pre-Game Hype

**News hook:** 5 hours before first pitch. Gausman starts. Cubs riding walk-off energy.

**Angle:** High-energy, fan-forward. Call to action (don't let Sox get comfortable).

**Tier:** 1

**Posting window:** 5:00 PM CT (pre-game hype slot)

**Hashtags:** #Cubs #GoCubs #FlyTheW

---

### STORY 8: First Pitch Hype

**News hook:** 90 minutes before first pitch.

**Angle:** Ultra-short, punchy. PCA recap callback + tonight's mission.

**Tier:** 1

**Posting window:** 6:30 PM CT (first pitch slot)

**Hashtags:** #Cubs #GoCubs #FlyTheW
