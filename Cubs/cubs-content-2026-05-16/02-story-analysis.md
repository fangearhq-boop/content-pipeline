# Chicago Cubs Fan HQ — Story Analysis
**Date:** May 16, 2026

---

### Insights Applied

The performance insights API at `/api/insights/cubs?days=21` returned a 403 error. The fallback response was `{"tweet_count":0}`, indicating either a cold-start condition or a temporary API/DB issue. With zero tweets analyzed, no statistically meaningful findings are available.

**Decision:** Fall through to `brand-voice.md` defaults for all format decisions. No adjustments were made to:
- Posting time slot selection (defaulted to niche-config.yaml schedule)
- Opening style (defaulted to brand-voice.md: punchy hooks for bold takes, stat-first for informative)
- Hashtag count (defaulted to exactly 3 per tweet per brand-voice.md)
- ALL CAPS emphasis (defaulted to 1-2 words max per brand-voice.md)
- Content mix (defaulted to 50/50 informative/bold split)

**What would change if insights were available:** If `by_has_stat.True.mean` showed lower-than-expected reach, stats would be moved to body rather than hooks. If `by_hour_ct` showed strong evening performance, I'd shift the rival watch tweet from 2:30 PM to later. Without data, standard schedule applied.

---

### Series Context

The series-context API at `/api/cubs/series-context` returned a 403 error. The fallback response was `{"is_series_start_today":false,"off_day":true}`.

**Decision:** The fallback was incorrect. Web research confirmed Cubs are in the middle of a 3-game Crosstown Classic series (May 15-17 at Guaranteed Rate Field). May 16 is Game 2, not an off day. The API failure produced a false negative.

**Action taken:** Treated May 16 as a live game day. Included a game preview (12:00 PM CT) and game-time hype (6:30 PM CT) slot per the `is_series_start_today=false` / mid-series path. Did NOT write a series-preview tweet since Game 1 was already played last night — used game recap + Game 2 preview format instead.

---

### STORY 1: Cubs 10, White Sox 5 — Crosstown Classic Game 1

**Angle:** Game recap. Carson Kelly (3-for-5, 4 RBIs) was the clear hero, delivering the go-ahead single in the 7th and putting the game away with a 2-run double in the 8th. The Cubs' 14-hit attack was the story — this was a team win, not a one-man show, but Kelly gives the tweet a human lead. Cubs snapped the White Sox's 5-game winning streak and improved to 29-16.

**Hook selection:** ALL CAPS "FOURTEEN" as the one punchy word draws the eye. "White Sox streak: OVER." is the knockout close on line 1, inviting readers to find out more. Bregman scoring 3 times reinforces the depth/breadth of the win.

**Tier 1 rationale:** Crosstown Classic game recap — always Tier 1 per research-playbook.md. First slot of the day.

---

### STORY 2: Carson Kelly — The Backup Catcher Who Just Broke Open the Crosstown Classic

**Angle:** Bold take on depth performance. Kelly was acquired as backup catcher depth, not as an offensive centerpiece. A 3-for-5 game with 4 RBIs in the Crosstown Classic is the kind of "depth stepping up" moment that resonates with fans. Voice: understated surprise turning into genuine enthusiasm.

**Hook selection:** "Backup catchers don't usually break open Crosstown Classic games." — subverts expectations before delivering the stat. The kicker ("Depth playing like this makes a 29-16 team look genuinely dangerous") puts the individual performance in season-arc context.

**50/50 mix:** This is the bold-passionate post for the morning block.

---

### STORY 3: Crosstown Classic Game 2 Tonight — Rea vs Fedde, 6:10 PM CT

**Angle:** Preview with a genuine matchup hook. Fedde's 0-4 record despite a 3.77 ERA is the analytical angle — the White Sox simply can't score for him. Rea at 4-2 but 4.68 ERA is the inverse. Cubs are hot offensively (14 hits last night) and the momentum angle makes the preview feel urgent rather than routine.

**Slot:** 12:00 PM CT ("Game preview or midday update") — perfect fit.

**Research-playbook rule:** Game preview must post BEFORE first pitch. 6:10 PM CT first pitch, 12:00 PM preview = 6+ hours of runway. ✓

---

### STORY 4: NL Central Watch — Cards Climbing, Brewers Dangerous, Cubs Leading

**Angle:** Division temperature check. Three data points (Cardinals 25-18, Misiorowski's dominant outing, Yelich working back) paint a picture of a division that won't roll over. The Cubs at 29-16 are leading it, but this isn't a cruise-control story. "Target on their backs" framing turns a standings update into something with edge.

**Why this slot (2:30 PM) over more trade talk:** The trade target story has been covered 3 consecutive days (May 13, 14, 15). The NL Central Watch was last covered May 14. Adding a new name (Misiorowski) and a relevant health storyline (Yelich) makes this fresh. One trade-urgency tweet before deadline is plenty for a day with a live game.

**Dropped claims:** "Cardinals won 7 of 8" — sourced from ~May 5 era, not current. "X games back" — exact current GB not confirmed for all 5 teams with same-day data.

---

### STORY 5: Ben Brown — Next Start Tuesday, Pitch Count Expanding

**Angle:** Season-arc follow-up on the Cubs' rotation answer. Ben Brown has posted identical lines in two straight starts. The "Tuesday vs Brewers" hook grounds this in something specific and near-term rather than vague. The pitch count escalation is the narrative engine — fans tracking his development want to know this is building toward longer outings.

**Voice:** Confident, forward-looking. "He's taking over" is the bold-but-earned claim given back-to-back dominant starts.

**Slot:** 3:45 PM ("Feature / deep-dive / prospect update") — rotation analysis fits perfectly.

**Single-source caveat:** "Tuesday vs Brewers" is MEDIUM confidence (one source, ~20h old). If the rotation shifts, the claim may not hold. Tweet framing is soft enough ("next start: Tuesday") that it can be defended as current reporting.

---

### STORY 6: GAME 2 — Crosstown Classic, Rate Field, 6:10 PM CT

**Angle:** Pure game-time energy. Short, sharp, facts-only plus one emotional beat. The combination of "Cubs won the opener 10-5" and "Crosstown Classic is officially ON" is the minimum viable content for a game-time tweet. 181 characters — intentionally spare.

**No engagement question.** "Let's take the series lead, Chicago." is a declarative rallying cry, not a question. ✓

---

## Content Mix Audit

| Story | Type | Category |
|-------|------|----------|
| 1 | Informative | Game recap |
| 2 | Bold/Passionate | Depth spotlight |
| 3 | Informative | Game preview |
| 4 | Bold/Analysis | Rival watch |
| 5 | Informative | Rotation feature |
| 6 | Bold/Hype | Game time |

Mix: 3 informative / 3 bold-hype = 50/50 ✓

## Posting Cadence Audit

| Slot | Time | Gap from Previous |
|------|------|-------------------|
| Story 1 | 7:00 AM | — |
| Story 2 | 8:15 AM | 75 min ✓ |
| Story 3 | 12:00 PM | 225 min ✓ |
| Story 4 | 2:30 PM | 150 min ✓ |
| Story 5 | 3:45 PM | 75 min ✓ |
| Story 6 | 6:30 PM | 165 min ✓ |

All gaps ≥ 60 min ✓ | No back-to-back within 60 min ✓
