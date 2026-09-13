# Story Analysis — 2026-09-13

## ### Insights applied

**Insights snapshot:** Generated 2026-09-13T08:30:00 UTC (today's fresh snapshot). 3 significant findings from 115 measured tweets over the past 21 days.

### Finding 1: `opening=statement` (LOSER)
- **Effect:** not_statement beats statement, p=0.025, small effect (Cliff's delta 0.252)
- **Median impressions:** not_statement = 112.5 vs statement = 74.0
- **Action taken:** ALL five tweets drafted with stat leads or narrative action openers — NOT declarative statements. Examples: "Two solo home runs off Skenes" (stat-action lead), "Cubs 83-66. Phillies 82-66." (standings stat lead), "Matthew Boyd's ERA since returning from the IL: 2.08" (explicit stat lead), "Clay Holmes: 5⅔ innings, six strikeouts, two earned runs" (stat line lead).

### Finding 2: `has_score=False` (WINNER)
- **Effect:** tweets without game scores beat those with, p=0.033, small effect (Cliff's delta 0.234)
- **Median impressions:** no-score = 114.0 vs has-score = 75.5
- **Action taken:** The game recap tweet (Story 1) does NOT state the "4-3" final score. Story is framed through game events — HRs, O'Hearn bomb, 8th-inning comeback — without leading with or explicitly calling out the final score. The game preview and standings tweets are not game recaps, so the finding is less directly applicable there (standings include records, not game scores).

### Finding 3: `has_stat=True` (WINNER)
- **Effect:** tweets with stats beat those without, p=0.037, small effect (Cliff's delta 0.226)
- **Median impressions:** has-stat = 109.0 vs no-stat = 73.5
- **Action taken:** Every tweet contains at least one concrete stat: Holmes 5⅔ IP / 6 K / 2 ER, Boyd 2.08 ERA, Chandler 10-10 / 4.25 ERA, Cubs 83-66, Holmes ~1.82 ERA since deadline. The first-pitch hype tweet (Story 5) is intentionally lean but still includes the game time as a hard data point.

### Summary
All three findings were directly actionable today. No findings were empty or bypassed. The combination of stat-led openers + no final score + embedded stats represents the strongest signal alignment possible from this dataset.

---

## ### Series context

**Source:** Cubs/_data/series-context.json (generated 2026-09-13T08:30:00 UTC)

- `is_series_start_today`: false
- `off_day`: false
- **Case:** Mid-series. Cubs vs Pittsburgh Pirates at Wrigley Field. Today is Game 3 (series finale).
- Cubs record: 83-66. Pirates record: 74-75.
- Game time: 1:20 PM CT
- Probables: TBD per snapshot (confirmed via WebSearch as Boyd vs Chandler)

**Action:** No mandatory series-preview slot required. Series context informs game preview framing (sweep opportunity = narrative hook). Boyd vs Chandler serves as the preview story at 9:30 AM.

---

## Story Selection and Angles

### STORY 1: Game Recap — Clutch Comeback in the 8th
- **Status:** FOLLOW UP (continuation of Pirates series coverage)
- **Tier:** 1
- **Angle:** Built through the game arc without stating the final score. Two solo HRs off Skenes → Holmes dominant but O'Hearn 3-run bomb flips it → 8th inning clutch rally (Shaw walk, Hoerner HBP, Bregman scores). Drama without spoiling it with a score. Two-game winning streak.
- **Insights:** Stat-action lead. No score. Has stats (HRs, 8th inning sequence).
- **Slot:** 7:00 AM CT

### STORY 2: Wild Card Watch — Cubs Own the WC1 Seat
- **Status:** FOLLOW UP
- **Tier:** 1
- **Angle:** Cubs 83-66, lead Phillies ~82-66 by 1 game for home-field in Wild Card Series. Cardinals eliminated. 15 games left. Cubs vs Phillies framing with mild Cardinals jab. 
- **Insights:** Stat lead (records). Has stats. Not a statement opener.
- **Slot:** 8:15 AM CT

### STORY 3: Game Preview — Boyd vs Chandler, Sweep on the Line
- **Status:** NEW STORY
- **Tier:** 1 (game-day preview, must post before 1:20 PM first pitch)
- **Angle:** Boyd's 2.08 ERA since returning from IL makes him the strongest Cubs starter right now. Chandler is 10-10 with above-average stuff but hittable. Sweep = 3-0 Pirates series at home, massive momentum boost for wild card race.
- **Insights:** Explicit stat lead (Boyd ERA). Has stats. Not a statement opener.
- **Slot:** 9:30 AM CT

### STORY 4: Holmes — The Rotation's October Anchor
- **Status:** NEW STORY
- **Tier:** 1
- **Angle:** Holmes 5⅔ IP, 6 K last night, with a calculated ~1.82 ERA in 6 starts since the deadline. One O'Hearn 3-run bomb but otherwise command was there. Bold take: this is what ace-level starting looks like.
- **Insights:** Stat lead (IP, K, ERA). Has stats. Bold take rather than statement opener.
- **Slot:** 10:45 AM CT

### STORY 5: First Pitch Hype
- **Status:** NEW STORY
- **Tier:** 2
- **Angle:** Wrigley Sunday, 1:20 PM CT, sweep in the air. Short, punchy, passionate.
- **Insights:** Slight stats (game time). Minimal filler framing.
- **Slot:** 12:00 PM CT

**Total: 5 tweets** — appropriate for a Sunday game day. No filler. Five genuine stories.

---

## Publishing Schedule

| Time (CT) | Story | Type |
|-----------|-------|------|
| 7:00 AM | Game Recap — Comeback in the 8th | Informative/Dramatic |
| 8:15 AM | Wild Card Watch — WC1 Seat | Analysis/Standings |
| 9:30 AM | Boyd vs Chandler Preview | Informative/Bold |
| 10:45 AM | Holmes Deadline Resume | Bold Take |
| 12:00 PM | First Pitch Hype | Passionate |
