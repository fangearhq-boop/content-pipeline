# Story Analysis — Cubs 2026-09-10

## Series Context

**Case: `off_day=true`, `is_series_start_today=false`**

Today is a Cubs off day. No game scheduled in CT. The series-preview reserved 7:00 AM slot does NOT apply — there is no `is_series_start_today=true` trigger. Instead: lean into prospect news, division watch, roster recovery, and previewing the upcoming home stand (Pirates start tomorrow).

The Pittsburgh Pirates series begins September 11 at Wrigley (1:20 PM CT) — that is tomorrow's is_series_start story. Today we can tease it but do not lead with it.

---

## Insights Applied

### Significant Findings Read (generated_at: 2026-09-10T08:30 UTC)

**Finding 1 — has_score=False WINS (effect: small, Cliff's delta=0.282, p=0.0094)**
- Winner: tweets WITHOUT a score → median 110 impressions
- Loser: tweets WITH a score → median 75.5 impressions
- **Impact on today's drafts:** Do NOT lead with "Cubs lost 8-6" or embed the final score in the tweet. Frame the sweep reaction around the narrative (Gausman shelled, three HRs allowed) rather than the scoreline. Also applies to standings tweets — avoid "Cubs 81-66" as a lead stat.

**Finding 2 — posting_window=midday_12_18 WINS (effect: small, delta=0.229, p=0.0338)**
- Midday 12–6 PM CT slots outperform: median 107 vs 76.5
- **Impact:** Bias today's freshest stories toward 12:00 PM–5:00 PM slots. The 7:00 AM sweep-reaction slot is used because its purpose requires it (off-day lead story, recap delivery), but midday gets the analytical and milestone stories.

**Finding 3 — posting_window=morning_06_12 LOSES (mirror of Finding 2)**
- Morning 6–12 AM CT slots underperform: median 76.5 vs 107
- **Impact:** Only use the 7:00 AM slot if the story has no better home (sweep recap is essential content fans will check first thing). Keep the 7 AM tweet tight and strong. Do NOT double up in the morning — skip 8:15 AM and 9:30 AM slots today (off day, less urgency).

**No finding on emoji_first_line** — all 116 measured tweets had False; no contrast possible. Brand voice default applies: no emoji in the first line.

**No finding on len_bucket** — the 260+ bucket (n=50) and 200-260 bucket (n=63) exist but neither cleared significance gates (no contrast in `significant_findings`). Brand voice default: target 200-260 chars (where top performers cluster in raw_buckets — diagnostic only, not directive).

**No finding on has_allcaps, has_stat** — these appear in raw_buckets only. Not actionable per the rules (raw_buckets bypass significance gates). Fall through to brand-voice defaults: stat-backed takes, ALL CAPS on 1-2 words for emphasis.

---

## Stories Selected — 5 Tweets (Off Day)

### STORY 1: Sweep Reaction — Gausman Gets Shelled
- **Angle:** Narrative framing — Gausman allowed 3 HRs in 4 innings (Yelich, Chourio, Contreras); Cubs swept 3-0 in Milwaukee. Not about the score — about a 9th-inning rally that came too late and what this means for the rotation heading into October.
- **Hook:** "Three home runs in four innings. That's not Gausman at his best." vs. "Cubs lost 8-6" (avoid score per insights)
- **Tier:** 1
- **Slot:** 7:00 AM CT (purpose-required morning slot — off day lead story)
- **Type:** Game reaction / narrative take
- **Tone:** Honest, not doom-posting; acknowledge the bad start while noting 9th-inning resilience

### STORY 2: NL Wild Card Standing — Cubs Still Hold WC2
- **Angle:** Informative standings update. Cubs 81-66, WC2, 0.5 GB of Phillies (WC1). The sweep hurt but didn't knock them out. Padres/D-backs still fighting for WC3. 15 games to solidify home-field in Wild Card round.
- **Hook:** Lead with the position ("Cubs hold WC2") not the record number (avoid score/record-number lead per insights)
- **Tier:** 2
- **Slot:** 12:00 PM CT (midday preferred window)
- **Type:** Informative standings
- **Tone:** Steady, analytical

### STORY 3: PCA 40-40 Watch — 41 HR / 35 SB
- **Angle:** Bold milestone framing. PCA needs 5 SBs in 15 games to join the 40-40 club. Only a handful of players have done it in MLB history. No Cub ever.
- **Hook:** Lead with "41 HR / 35 SB" (stat lead — top performers pattern from raw_buckets qualitative observation)
- **Tier:** 1
- **Slot:** 1:15 PM CT (midday preferred)
- **Type:** Bold milestone take
- **Tone:** Excitement, urgency, historical weight

### STORY 4: Wiggins + Steele — Bullpen Help Coming
- **Angle:** Double-barrel prospect/rehab update. Wiggins: 8 scoreless Iowa bullpen innings, September callup overdue. Steele: 2 Iowa outings in, targeting October bullpen role. This bullpen got hurt in September — reinforcements are on the way.
- **Hook:** Lead with the tension: "The bullpen gave up 5 in the 9th last night. Help is on the way."
- **Tier:** 2
- **Slot:** 2:30 PM CT (midday preferred)
- **Type:** Roster news / prospect update
- **Tone:** Informative, forward-looking

### STORY 5: Pirates Series Preview — Wrigley Homestand Starts Tomorrow
- **Angle:** The Cubs just got swept on the road. Now they come home. Three games vs the Pirates (71-73) starting tomorrow at Wrigley. This is a mandatory-win series before the Braves come to town Sept 14.
- **Hook:** Lead with the opportunity, not the record ("Wrigley Field. Three games. Pirates (below .500). This is how you bounce back.")
- **Tier:** 2
- **Slot:** 5:00 PM CT (early evening, teasing tomorrow)
- **Type:** Series preview / hype
- **Tone:** Confident, restorative energy after the sweep

---

## Skipped Slots (Off Day — No Game Tonight)
- 6:30 PM — first pitch hype (no game)
- 8:00 PM — in-game reaction (no game)
- 9:30 PM — post-game recap (no game)
- 8:15 AM — morning energy (morning window underperforms; no breaking news to justify it)
- 9:30 AM — stat breakdown (folded into 1:15 PM PCA story instead)
- 10:45 AM — analysis (folded into 12:00 PM standings story)
- 3:45 PM — prospect (combined with 2:30 PM Wiggins/Steele)
