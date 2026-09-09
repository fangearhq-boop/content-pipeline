# Story Analysis — Cubs 2026-09-09

## Series Context

**is_series_start_today:** false
**off_day:** false
**Series:** Cubs @ Milwaukee Brewers (mid-series — Game 3 of 3)
- Cubs record: 81-65
- Brewers record: 90-56
- Venue: American Family Field
- Game time: 6:40 PM CT
- Rationale: "Same opponent (Milwaukee Brewers) as yesterday — this is mid-series, not a series opener."
- No series-preview slot reserved (not Game 1)
- Story angle: Cubs have lost Games 1 and 2; tonight is a must-win to avoid a sweep by the NL's best team with 16 games left.

---

## Insights Applied

**Snapshot loaded:** Cubs/_data/insights.json (generated_at=2026-09-09T08:30:00 UTC, measured_tweet_count=116)

### Significant Findings (effect-size order, strongest first):

**Finding 1 — has_score=False beats has_score=True**
- Winner median impressions: 107 | Loser median: 79 | Effect: small (Cliff's δ=0.268, p=0.013)
- **Applied:** Do NOT lead any tweet with a final score. Where game results are referenced, the score appears mid-body or is implied by context (e.g., "drop Game 2"), never as the hook or opening line. The game recap at 7:00 AM opens with the dramatic play (Chourio's HR), not "Brewers 4, Cubs 3."

**Finding 2 — opening=not_statement beats opening=statement**
- Winner median impressions: 115 | Loser median: 79 | Effect: small (Cliff's δ=0.227, p=0.047)
- **Applied:** For every tweet, the opening line is either a stat_lead (e.g., "Pete Crow-Armstrong: 41 HR / 35 SB.") or a specific event/allcaps hook — not a plain declarative statement like "The Cubs lost last night." The 7:00 AM tweet opens with a named play; the 1:15 PM tweet opens with the PCA stat line; the 5:00 PM tweet opens with an allcaps/urgency hook.

**Finding 3 — posting_window=midday_12_18 beats all other windows**
- Winner median impressions: 107 | Loser median: 79 | Effect: small (Cliff's δ=0.224, p=0.038)
- **Applied:** Best content placed in 12 PM–6 PM slots. PCA milestone tweet (1:15 PM), Game preview (12:00 PM), and pre-game hype (5:00 PM) are all in the midday window. Game recap at 7:00 AM is required by the playbook (game recaps always go in the first slot) but is the only morning post.

**Finding 4 — posting_window=morning_06_12 is a loser**
- Loser median impressions: 79 | Effect: small (Cliff's δ=0.224, p=0.038)
- **Applied:** Only ONE morning post today (7:00 AM game recap — mandatory per playbook). No 8:15 AM or 9:30 AM posts this run; those slots left empty. All optional content pushed to midday.

**Finding 5 — has_stat=True beats has_stat=False**
- Winner median impressions: 106 | Loser median: 79 | Effect: small (Cliff's δ=0.223, p=0.039)
- **Applied:** Every tweet includes at least one concrete stat. Game recap: Cubs 81-65 record. Game preview: Henderson 9-3, 2.48 ERA / Gausman 9-11, 4.38 ERA. PCA tweet: 41 HR / 35 SB, 16 games remain. Happ tweet: .275 over last 15 games, 13 RBI. Pre-game: Henderson's ERA.

**No additional findings** — no has_emoji, has_allcaps, or len_bucket findings cleared the gates.

---

## Story Selection & Angles

### STORY 1 — Game 2 Recap: Walkoff Misery in 10 (Tier 1)
**Slot:** 7:00 AM CT
**Angle:** Cubs had a lead through much of Game 2. Jackson Chourio's two-out HR in the 9th inning erased it; Luis Lara walked it off in the 10th. Peterson was outdueled by Misiorowski. Cubs now 0-2 in the series headed into tonight's Game 3.
**Hook:** Open with the devastating play (Chourio's HR), not the score. End with the urgency (Gausman tonight).
**Insight adjustments:** No score in the opening. Stat included (81-65 record + 16 games).

### STORY 2 — Game 3 Preview: Gausman vs Henderson (Tier 1)
**Slot:** 12:00 PM CT
**Angle:** Cubs need a win to avoid the sweep. Henderson (9-3, 2.48 ERA) is one of baseball's best right now — the Cubs' offense will have to grind against him. Gausman goes for Chicago with his reputation on the line in a big-stakes road game.
**Hook:** Lead with Henderson's stats as the challenge, then pivot to Gausman's answer. Midday slot = best impression window.
**Insight adjustments:** Stat_lead opening (Henderson's record/ERA), stats throughout.

### STORY 3 — PCA 40-40 Watch: 41/35, Five Away (Tier 1)
**Slot:** 1:15 PM CT
**Angle:** PCA went from 40/33 (Sept 7) to 41/35 (Sept 8). He's now just 5 stolen bases from joining the most exclusive club in baseball. No Cub has ever done it. 16 games left — it's doable.
**Hook:** Stat_lead exactly like the top-performing PCA tweets. "Pete Crow-Armstrong: 41 HR / 35 SB." Period. Then build the historical context.
**Insight adjustments:** Stat_lead opening, rich stats throughout, midday prime slot.

### STORY 4 — Ian Happ Knee: October Stakes (Tier 2)
**Slot:** 2:30 PM CT
**Angle:** Happ has been out since Sept 6 with left knee discomfort. Day-to-day, but an IL move at this point would threaten his October availability. He's been hitting .275 over his last 15 games — the Cubs need him healthy. Counsell monitoring closely.
**Hook:** Frame the urgency with the playoff angle; include his recent stats to satisfy has_stat.
**Insight adjustments:** Not a stat_lead opening (hard to frame injury news as a stat), but includes stats in body. Classified as a reasonable exception — injury updates require narrative context.

### STORY 5 — Pre-Game Hype: Must-Win Tonight (Tier 2)
**Slot:** 5:00 PM CT
**Angle:** With 16 games left and an 0-2 series deficit, tonight is a character test. Henderson is elite; Gausman has to match him. The Cubs don't want to enter the final stretch with a sweep by the NL leaders on their record.
**Hook:** Allcaps_lead urgency opener to push outside the statement zone. Stats: Henderson's ERA.
**Insight adjustments:** Allcaps_lead (not_statement), has_stat (Henderson ERA), midday window (5 PM = 17:00, in the 12-18 window).

### STORY 6 — First Pitch Tweet (Tier 3)
**Slot:** 6:30 PM CT
**Angle:** Brief game-time tweet. Minimal, punchy. Stakes established earlier in the day.
**Hook:** Game-time plus urgency close.

---

## Duplicate/Overlap Check (vs story-history.md last 30 days)

- PCA 40-40 Watch: Covered on Sept 7 and Sept 8 — but PCA went from 40/33 to 41/35. Fresh update with new numbers — proceed. Fans want this daily at this pace.
- Game Recaps: Daily, always fresh.
- Wiggins prospect: Covered Sept 8. Not repeating today unless new news (it's repetitive enough).
- Matt Shaw activation: Covered Sept 8. Skip today unless he had a notable debut stat.
- NL Wild Card Standings: Covered Sept 8. Skip as standalone today (folded into game urgency context instead).

---

## Posting Schedule

| Time | Story | Type |
|------|-------|------|
| 7:00 AM CT | Game 2 Recap | Tier 1 |
| 12:00 PM CT | Game 3 Preview | Tier 1 |
| 1:15 PM CT | PCA 40-40 Watch | Tier 1 |
| 2:30 PM CT | Ian Happ Injury | Tier 2 |
| 5:00 PM CT | Pre-game Hype | Tier 2 |
| 6:30 PM CT | First Pitch | Tier 3 |

**Total posts: 6** (within the 12-post max; all posts have genuine news value)
