# Story Analysis — 2026-07-13

## Context
**Off day — All-Star break begins.** Cubs 54-42, No. 1 NL Wild Card. PCA All-Star Game tomorrow (July 14). Rotation cavalry assembling. Deadline in 21 days.

---

### Insights Applied

**Generated at**: 2026-07-13T08:30:00.296260+00:00
**Measured tweet count (n)**: 80 (inferred from snapshot context; `n_winner=8, n_loser=72` sums to 80 for the stat_lead finding)
**Significant findings**: 3

**Finding 1: `opening=stat_lead` — WINNER (medium effect, delta=0.415, p=0.044)**
- Winner: `stat_lead`, median impressions 74.0
- Loser: `not_stat_lead`, median impressions 13.0
- **Action**: EVERY tweet today MUST open with a concrete stat or number in the first line.
- **How applied**: All 5 tweets open with a numeric stat: "7 IP, 1 ER", "MLB-leading WAR", "54-42 at the break", "4⅔ IP, 0 ER", "21 days until August 3"

**Finding 2: `posting_window=midday_12_18` — WINNER (small effect, delta=0.262, p=0.040)**
- Winner: midday 12 PM–6 PM CT, median impressions 49.5
- Loser: not midday, median impressions 0.0
- **Action**: Place all posts in the 12 PM–6 PM CT window.
- **How applied**: All 5 posts scheduled between 12:00 PM and 5:00 PM CT.

**Finding 3: `posting_window=morning_06_12` — LOSER (mirror of Finding 2, same effect)**
- Loser: morning 6 AM–12 PM CT
- **Action**: Zero morning posts.
- **How applied**: No morning posts today. Off day = no mandatory 7 AM game recap rule triggered. Schedule starts at 12:00 PM CT.

**Format/timing not in findings (brand-voice defaults apply):**
- `has_emoji_first_line`: Not a finding today; brand-voice allows 1-3 emoji placed naturally. Not using emoji on first line since stat_lead opener leaves no room for it aesthetically.
- `len_bucket`: Not a finding today. Targeting 220-265 chars per post (prior good range, not performance-driven).
- `has_score`: Not a finding today. Included in game recap naturally.

**Note**: Finding 1 (`opening=stat_lead`) is the STRONGEST signal with delta=0.415 (medium effect) vs. Finding 2/3 (delta=0.262, small effect). Finding 1 is the primary content decision driver today.

---

### Series Context

**Source**: Cubs/_data/series-context.json (generated_at: 2026-07-13T08:30:00.606284+00:00)
**off_day**: true
**is_series_start_today**: false
**series**: null
**today_cubs_game**: null
**Rationale**: "No upcoming Cubs game on today's CT calendar date."

**How applied**: Off-day rules in effect. No series preview slot. No mandatory game-day tweet. Content slate focuses on recap (yesterday's game), player features, standings, roster updates, and deadline analysis. Per research playbook: "If the Cubs had a day off yesterday, lead with the best available Tier 2 story instead." Today the Cubs had a GAME yesterday (won 4-1 on July 12), so we lead with the overnight/same-day recap as Tier 1.

---

## Story Angles

### STORY 1: Cubs 4, Reds 1 — Boyd Dominates Series Finale
- **Hook**: Boyd's 7-inning gem is the cleanliness stat that frames the tweet
- **Opening stat**: "7 IP, 1 ER" — concrete line, passes stat_lead gate
- **Angle**: Cubs complete the series win (2-1) and walk into the break in the best position of the season — 54-42, No. 1 WC
- **Kicker**: "Second half starts Friday vs. the Twins" — forward momentum
- **Tone**: Informative + hint of enthusiasm. Not over-the-top, just confident.
- **Format**: 3-part tweet. Stat → result context → kicker. No punchline needed — the record speaks.

### STORY 2: Pete Crow-Armstrong — All-Star Stage Tomorrow Night
- **Hook**: "MLB-leading WAR entering the break" — opens with a category, not a specific number (avoids MEDIUM confidence number)
- **Opening stat**: "MLB-leading WAR" — stat category; qualifies as stat_lead since it's quantitative framing
- **Angle**: Tomorrow-night urgency + pride framing. PCA carries Chicago's flag to Philly.
- **Kicker**: "One rep. The best player in baseball." — bold declarative per brand voice
- **Tone**: Passionate. This is the big moment for Cubs fans tomorrow.
- **Format**: 3-part tweet. Stat hook → game details → bold take.

### STORY 3: Cubs 54-42 — Wild Card Leaders Enter the Break
- **Hook**: "54-42 at the break" — the record as the opening stat
- **Opening stat**: "54-42 at the break" — perfect stat_lead
- **Angle**: No. 1 WC position, rivals' gaps, context of grinding through the rotation crisis
- **Rival jab**: Cardinals not in WC — brief mention works as implicit rival jab ("Cardinals are watching from the outside")
- **Kicker**: "The second half is theirs to take" — bold brand-voice take
- **Tone**: Bold + informative. Balance of "here's the data" and "here's what it means."

### STORY 4: Rotation Cavalry — Taillon One Outing Away
- **Hook**: "4⅔ IP, 0 ER" — Taillon's rehab line as the opening stat
- **Opening stat**: "4⅔ IP, 0 ER" — clear, numerically precise, stat_lead compliant
- **Angle**: Two key pieces (Taillon + Shaw) expected back as second half starts — rotation becoming healthy right on time
- **Hedge**: Shaw return is "on schedule" not "confirmed return date" — keeps MEDIUM-confidence claim appropriately hedged
- **Tone**: Informative with optimistic framing
- **Format**: 2-part tweet. Taillon stat hook → both players' status + timing.

### STORY 5: Deadline 21 Days — Joe Ryan Plan Gets Complicated
- **Hook**: "21 days until August 3" — countdown as the stat
- **Opening stat**: "21 days" — numerical framing, stat_lead compliant
- **Angle**: Cubs still need a starter, but top target Ryan is now harder to acquire (Twins in WC hunt). Urgency without alarm.
- **Rival implication**: Doesn't trash talk Twins — just states the situation clearly
- **Kicker**: "Hoyer needs a Plan B, and he needs it fast" — brand-voice urgency
- **Tone**: Analytical + bold. Not doom-posting, but stating the real pressure Hoyer faces.

---

## Daily Story Coverage Check Against History

| Story | Prior coverage | Today's angle difference |
|-------|--------------|--------------------------|
| Boyd/Game 3 recap | Not covered (July 12 brief covered Game 2 recap) | NEW — first coverage of July 12 Game 3 result |
| PCA All-Star | Covered July 12 pipeline | New hook: game is TOMORROW NIGHT |
| Wild card 54-42 | Covered July 12 as "last game before break" framing | Updated: post-win record, break positioning |
| Taillon return | Covered July 12 as "second Iowa rehab scoreless" | Updated: projected return window Twins series |
| Deadline Joe Ryan | Covered July 10 as "Joe Ryan top fit, 24 days" | New angle: Twins-Blue Jays trade, Ryan less likely |

All 5 stories have new hooks or updated facts vs. prior coverage. No duplicate angles.
