# Cubs Daily Brief — 2026-05-29

## Today's Context
- **Date:** Friday, May 29, 2026 (CT)
- **Platform:** X/Twitter only
- **Series context:** is_series_start_today=TRUE — Cubs at Cardinals, Game 1 of 3, Busch Stadium, 6:15 PM CT
- **Yesterday:** Cubs 7, Pirates 2 — handed Skenes his 3rd straight loss, split the Pittsburgh series 2-2
- **Cubs record:** 31-26 | **Cardinals record:** 29-25
- **Probable pitcher conflict:** Rotation math puts Imanaga on today; one source says Saturday. Use TBD language in tweets.

## Posting Order Conflict Note
The system prompt reserves 7:00 AM CT for a Series Preview when is_series_start_today=true. However, _engine/SKILL.md and Cubs/research-playbook.md both state game recaps go in the FIRST available slot. **Engine docs win per system prompt escalation rule.** Recap at 7:00 AM, series preview at 8:15 AM. (Established precedent: May 22, May 25 runs handled identically.)

---

## Stories Selected (7 Stories)

### STORY 1: Cubs 7, Pirates 2 — Beat Skenes, Split Pittsburgh Series
- **Tier:** 1
- **Type:** NEW STORY (yesterday's game recap)
- **Posting time:** 7:00 AM CT
- **Slot:** Morning news / overnight recap
- **Angle:** Cubs handed 2025 NL Cy Young winner Paul Skenes his 3rd straight loss. Happ 2-run HR, Suzuki 2 hits & 2 RBI. Two Pirates errors in the 6th were the decisive turning point. Cubs split 2-2 at Pittsburgh, leave at 31-26 heading to St. Louis.
- **Insights:** HAS_SCORE ✓, HAS_STAT ✓, content_type=brief ✓

### STORY 2: Cardinals Series Opener — 3 Games at Busch, 6:15 PM CT Tonight
- **Tier:** 1
- **Type:** NEW STORY (series preview; is_series_start_today=true)
- **Posting time:** 8:15 AM CT
- **Slot:** Bold take / fan energy
- **Angle:** Cubs (31-26) riding back-to-back wins into the NL Central rivalry series. Cardinals (29-25). 3 games at Busch Stadium. Lead with matchup+location per engine rule, stakes/rivalry as kicker.
- **Insights:** HAS_STAT (records) ✓, content_type=brief ✓

### STORY 3: NL Central Watch — Cubs 31-26, Cardinals 29-25, Division Race Is Live
- **Tier:** 2
- **Type:** FOLLOW UP (ongoing division race tracking; updated with today's fresh records)
- **Posting time:** 10:45 AM CT
- **Slot:** Analysis / rival watch
- **Angle:** Both clubs within 2 games of each other chasing Milwaukee. This 3-game series at Busch has direct divisional implications.
- **Insights:** HAS_STAT (records + standings context) ✓, content_type=brief ✓

### STORY 4: Ian Happ — 41 Consecutive Games Reaching Base at PNC Park
- **Tier:** 2
- **Type:** FOLLOW UP (yesterday's story noted 40 consecutive; now 41 after Thursday's game)
- **Posting time:** 12:00 PM CT [MIDDAY ✓ — posting_window=midday_12_18 winner]
- **Slot:** Game preview or midday update
- **Angle:** Happ went 3-for-4 with a 2-run HR Thursday. 41 straight games reaching base at PNC Park. He grew up 15 miles from Pittsburgh. Bold/feature take.
- **Insights:** HAS_STAT (41 consecutive, 3-for-4, 2-run HR) ✓, midday window ✓, content_type=brief ✓

### STORY 5: Cubs Offense — Two Straight Wins, Heading to St. Louis with Momentum
- **Tier:** 2
- **Type:** FOLLOW UP (offensive bounce-back from 10-game skid; 2-0 streak after snapping it)
- **Posting time:** 1:15 PM CT [MIDDAY ✓ — posting_window=midday_12_18 winner]
- **Slot:** Bold take / passionate statement
- **Angle:** After the 10-game skid, Cubs went 2-0 (10-4 over Pirates Wed, 7-2 over Skenes Thu). Happ + Suzuki contributing. Offense finding its form at the right time for a Cardinals series.
- **Insights:** HAS_STAT ✓, midday window ✓, content_type=brief ✓

### STORY 6: Iowa Cubs + Farm System — Hartshorn & Ayers Go Deep, Iowa Shutout Win
- **Tier:** 3
- **Type:** NEW STORY (prospect update from May 28 Bleacher Nation report)
- **Posting time:** 3:45 PM CT
- **Slot:** Feature / deep-dive / prospect update
- **Angle:** Iowa Cubs 1-0 shutout Wednesday. Hartshorn and Ayers both homered across affiliates. Farm system producing at multiple levels.
- **Insights:** HAS_STAT (1-0, specific players named) ✓, content_type=brief ✓

### STORY 7: Pre-Game Hype — Cubs at Cardinals, 6:15 PM CT Tonight
- **Tier:** 2 (elevated for rivalry context)
- **Type:** NEW (game-time energy)
- **Posting time:** 5:00 PM CT
- **Slot:** Pre-game hype or evening news
- **Angle:** Cubs carrying 2-game win streak into Busch Stadium. Cardinals fans on notice. Bear down.
- **Insights:** HAS_STAT (records, win streak count) ✓, near midday window ✓, content_type=brief ✓

---

## Publishing Schedule

| Time (CT) | Story | Tier | Type |
|-----------|-------|------|------|
| 7:00 AM | Cubs 7, Pirates 2 — Beat Skenes, Split Series | 1 | Informative |
| 8:15 AM | Cardinals Series Preview — 3 Games at Busch | 1 | Bold |
| 10:45 AM | NL Central Watch — Division Race Live | 2 | Analysis |
| 12:00 PM | Ian Happ — 41 Straight at PNC Park | 2 | Bold/Feature |
| 1:15 PM | Cubs Offense — 2-Game Win Streak, Momentum | 2 | Bold |
| 3:45 PM | Iowa Cubs — Hartshorn/Ayers + Shutout Win | 3 | Informative |
| 5:00 PM | Pre-Game Hype — Cardinals Opener Tonight | 2 | Hype |

**Total:** 7 stories, 7 X posts | **Mix:** 3 informative / 4 bold-hype ≈ 43/57 (within range of 50/50 guidance)
