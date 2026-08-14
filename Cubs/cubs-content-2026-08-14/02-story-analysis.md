# Cubs Story Analysis — 2026-08-14

---

### Series context

**Snapshot file:** Cubs/_data/series-context.json (generated 2026-08-14T08:30:00Z)
**Status:** `is_series_start_today: true` | `off_day: false`
**Series:** Cardinals (61-60) at Cubs (71-51), Game 1 of 3 at Wrigley Field
**First pitch:** 1:20 PM CT, Apple TV+
**Cubs probable:** Clay Holmes (TBD per snapshot; confirmed Holmes via search)
**Cardinals probable:** Matthew Liberatore (TBD per snapshot; confirmed via search)
**Rationale (from snapshot):** "Yesterday vs Washington Nationals; today vs St. Louis Cardinals → game 1 of 3 (home)."

**Applied rule:** `is_series_start_today=true` → 7:00 AM CT slot RESERVED for Cardinals Series Preview. This is the highest-priority slot of the day and overrides any other story (per STEP 0.5). Game recap (from yesterday's Nationals loss) moves to 8:15 AM.

---

### Insights applied

**Snapshot file:** Cubs/_data/insights.json (generated 2026-08-14T08:30:00Z)
**Measured tweet count:** 126 (up from 125 Aug 13; implies one new tweet now in the measured pool)

**Finding 1 — has_score=False beats has_score=True**
- Dimension: `has_score`
- Winner: False | Loser: True
- Effect: **medium** (Cliff's delta=0.376, p=0.0004)
- Medians: 123 (no score) vs 78 (with score) impressions
- n: 79 (no score) vs 47 (with score)
- **Applied:** Zero game scores in all 6 tweets. Yesterday's recap leads with Cavalli's near no-hitter and Gausman's IP/ER line — not "Cubs lost 7-0." Pre-game and hype tweets use team W-L records (71-51 vs 61-60), which are standings records not game scores. H2H tweet uses win differential (10 more wins), not scores.

**Finding 2 — posting_window=midday_12_18 wins**
- Dimension: `posting_window=midday_12_18`
- Winner: midday_12_18 | Loser: not_midday_12_18
- Effect: **small** (Cliff's delta=0.217, p=0.0426)
- Medians: 123 (midday) vs 92 (other windows)
- **Applied:** Two slots placed in the 12-18 CT window: 12:00 PM (pre-game hype) and 1:15 PM (bold H2H take). Both carry high-engagement Cubs vs Cardinals content, capitalizing on the performance-winning window. Morning slots (7-11 AM) held only for time-sensitive content (series preview must post before first pitch; game recap rolls from yesterday).

**Finding 3 — posting_window=morning_06_12 loses**
- Dimension: `posting_window=morning_06_12`
- Winner: not_morning_06_12 | Loser: morning_06_12
- Effect: **small** (Cliff's delta=0.217, p=0.0426)
- Medians: 123 (outside morning) vs 92 (morning) impressions
- **Applied:** Morning slots (7:00, 8:15, 9:30, 10:45 AM) used only for time-sensitive or mandatory content: series preview (7 AM, mandatory per STEP 0.5 rule), game recap (8:15 AM, time-sensitive news), PCA milestone angle (9:30 AM, strong enough to warrant morning slot), Bregman hot streak (10:45 AM, provides Cardinals series context before first pitch). Non-time-sensitive bold takes pushed to 12:00 PM and 1:15 PM slots where possible.

**Finding 4 — has_stat=True wins**
- Dimension: `has_stat`
- Winner: True | Loser: False
- Effect: **small** (Cliff's delta=0.21, p=0.0465)
- Medians: 123 (with stat) vs 93 (without stat) impressions
- **Applied:** Every tweet includes at least one stat:
  - Story 1: Holmes 2.86 ERA, Liberatore 5-9, 5.15 ERA
  - Story 2: Gausman 4.2 IP, 6 R; no-hit bid through 7th
  - Story 3: PCA 30 SB, 27 HR, 72 RBI
  - Story 4: Bregman .394/.460/.788, 6 HR in 16 games; Liberatore 5-9, 5.15 ERA
  - Story 5: 71-51 vs 61-60 records
  - Story 6: 4-2 H2H, 10-win differential

**No findings were empty.** All four findings were actionable. No brand-voice prescription was directly contradicted by a finding (brand voice already encourages stat-backed takes, and morning vs midday is a scheduling preference, not a voice attribute).

---

### STORY 1: Cardinals Series Preview
**Tier:** 1 | **Slot:** 7:00 AM CT
**Angle:** Mandatory series preview for Game 1 of 3. Lead with matchup (opponent + length + location) per rule. Pitcher angle second. Rivalry/stakes kicker.
**Hook:** Cubs vs. Cardinals — Game 1 of 3 at Wrigley Field, 1:20 PM CT
**Kicker:** Cardinals won 7 of 10 recently but are still a .500 club walking into Wrigley
**Insight adjustments:** Stats included (Holmes 2.86 ERA, Liberatore 5-9, 5.15 ERA). No game score. Midday rule: morning slot necessary (preview must precede first pitch, scheduled 7 AM series start per rule).

---

### STORY 2: Nationals Shutout Recap
**Tier:** 1 | **Slot:** 8:15 AM CT
**Angle:** Honest recap of yesterday's 7-0 loss. Cavalli was the story — his near no-hit bid, not a Cubs collapse. Gausman's rough second start is a genuine concern but framed as "outlier." Cubs still won the series 2-1. Now the bounce back begins vs Cardinals.
**Hook:** Cavalli was near untouchable through 7 innings in Washington
**Kicker:** Cardinals are in town — time to move on fast
**Insight adjustments:** No score lead (finding 1 — don't say "Nationals 7, Cubs 0"). Lead with Cavalli's near no-hitter instead. Stat included (Gausman 4.2 IP, 6 R). Morning slot justified by time-sensitive news.

---

### STORY 3: PCA 30-30 Watch
**Tier:** 2 | **Slot:** 9:30 AM CT
**Angle:** PCA has 30 stolen bases and 27 home runs — he's three HR from back-to-back 30-30 seasons. He also leads ALL of MLB in WAR. This is a historic Cubs season happening in real time.
**Hook:** PCA has 30 steals, 27 HR, leads MLB in WAR
**Kicker:** "This isn't just an MVP race. This is a historic Cubs season happening in real time."
**Insight adjustments:** Has_stat=True — three stats in lead. No score. Morning slot justified by the story's strong analytics content (drives engagement even in underperforming window).
**Avoided:** Not covering MVP odds again (covered Aug 13). Fresh angle = the 30-30 milestone milestone approach.

---

### STORY 4: Bregman Entering Cardinals Series on Fire
**Tier:** 2 | **Slot:** 10:45 AM CT
**Angle:** Bregman has been the hottest hitter in baseball since July 27 (.394/.460/.788, 6 HR in 16 games). He faces Liberatore (5-9, 5.15 ERA) today. This matchup is very favorable for him. Cardinals jab is the kicker.
**Hook:** Bregman's slash line since July 27
**Kicker:** Cardinals, you've made this easy (facing a 5.15 ERA starter with the hottest bat in baseball)
**Insight adjustments:** Has_stat=True — slash line + Liberatore ERA. No game score. Morning slot: pre-game context has time value (before 1:20 PM first pitch).
**Avoided:** Not re-covering the general "Bregman hot streak" arc that was covered Aug 8-9. Fresh angle = framing as Cardinals series context + favorable matchup.

---

### STORY 5: Pre-Game Hype
**Tier:** 2 | **Slot:** 12:00 PM CT (midday window winner — applying insight)
**Angle:** Rival game day energy. Cubs 71-51 vs Cardinals 61-60 — the record tells the story. Cards are at Wrigley for a Friday afternoon rivalry game.
**Hook:** Records (71-51 vs 61-60)
**Kicker:** "That's why the Cubs are in first place in the Wild Card race and the Cardinals are on the outside looking in."
**Insight adjustments:** Midday slot (12-18 CT winner per finding 2). Has records as stats. No game score.

---

### STORY 6: H2H vs Standings Bold Take
**Tier:** 2 | **Slot:** 1:15 PM CT (midday window winner)
**Angle:** Cardinals lead the 2026 H2H series 4-2, but Cubs have 10 more wins overall. One stat tells a short story; the other tells the playoff picture. October matters.
**Hook:** H2H 4-2 vs 10-win differential
**Kicker:** "Only one of them matters for October."
**Insight adjustments:** Midday slot (1:15 PM is in the 12-18 CT window — capitalizing on best-performing window per finding 2). Has two stats. No game score. Sharp rivalry angle.
