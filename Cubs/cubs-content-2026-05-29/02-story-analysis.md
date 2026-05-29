# Cubs Story Analysis — 2026-05-29

---

### Insights Applied

**Source:** Cubs/_data/insights.json — generated_at: 2026-05-29T08:30:00.192773+00:00
**Measured tweet count:** 90 tweets
**Significant findings count:** 6

| # | Finding | Effect Size | Applied Today |
|---|---------|-------------|---------------|
| 1 | content_type=brief wins (vs not_brief) | medium, Δ=0.453 | All 7 posts are brief-type ✓ |
| 2 | rss_news loses (vs not_rss_news) | medium, Δ=0.453 | All 7 posts are editorial takes, no wire-style dumps ✓ |
| 3 | has_stat=True wins | medium, Δ=0.380 | Stat in every tweet: scores, records, streak counts, RBI totals ✓ |
| 4 | posting_window=midday_12_18 wins | small, Δ=0.320 | Stories 4 (12 PM) and 5 (1:15 PM) both land in midday window; Stories 6 (3:45 PM) and 7 (5:00 PM) also near-midday. 4 of 7 slots in or near 12–6 PM CT window. ✓ |
| 5 | len_bucket=260+ wins | small, Δ=0.254 | All 7 tweets targeted at 260–279 chars ✓ |
| 6 | has_score=True wins | small, Δ=0.246 | Story 1 (game recap) leads with "Cubs 7, Pirates 2" ✓ |

**Findings NOT in today's snapshot (notable changes from prior runs):**
- `has_emoji_first_line=True loser` — NOT in today's findings → brand-voice.md defaults apply; emojis used naturally, not specifically avoided at line starts
- `len_bucket=140-200 loser` — NOT in today's findings → no explicit penalty for mid-range; still targeting 260+
- `has_allcaps winner` — NOT in today's findings → ALL CAPS used per brand-voice (1-2 words for emphasis), not driven by insights signal

**Overall application:** 6/6 significant findings applied. No findings conflict with brand-voice.md; brand-voice defaults used where findings are silent.

---

### Series Context

**Source:** Cubs/_data/series-context.json — generated_at: 2026-05-29T08:30:00.406346+00:00

**Case: is_series_start_today = TRUE**

Cubs at St. Louis Cardinals — Game 1 of 3 at Busch Stadium
- Cubs record: 31-26
- Cardinals record: 29-25
- Rationale: "Yesterday vs Pittsburgh Pirates; today vs St. Louis Cardinals → game 1 of 3 (on the road)."
- Game 1: Fri 6:15 PM CT | Game 2: Sat 6:15 PM CT | Game 3: Sun 6:20 PM CT
- Both probable pitchers: TBD (snapshot at 3:30 AM CT before lineup announcement)

**Action taken:** Story 2 (8:15 AM CT slot) is the Series Preview post, with opponent+length+location in the lead and rivalry/stakes as kicker. Engine rule conflict resolved (see below).

**Posting-Order Conflict Resolution:**
System prompt: "RESERVE the 7:00 AM CT slot for a 'Series Preview' story" when is_series_start_today=true.
Engine docs (_engine/SKILL.md + Cubs/research-playbook.md): Game recaps go in FIRST available slot (7:00 AM for night games).
**Resolution:** Engine docs win (per system prompt escalation: "the niche+engine docs win — flag the conflict in your output and follow the docs"). Game recap → 7:00 AM. Series preview → 8:15 AM. (Same precedent as May 22 and May 25 runs.)

---

### STORY 1: Cubs 7, Pirates 2 — Beat Skenes, Split the Series

**Freshness tags:** Skenes-loss, series-split, Happ-HR

**Summary:** The Cubs closed out their Pittsburgh road trip with a clean 7-2 win Thursday, handing Paul Skenes his third straight loss. Ian Happ went 3-for-4 with a 2-run HR in the 8th; Seiya Suzuki added 2 hits and 2 RBI. Two throwing errors by Pittsburgh infielders in the 6th inning turned a 1-0 game into a 3-0 Cubs lead. Skenes was dominant (10 Ks, only 1 ER) but took the loss. Cubs split the 4-game series 2-2 and leave Pittsburgh at 31-26.

**Relevance:** This is the morning's lead story. Cubs fans wake up wanting to know what happened. The result — beating the reigning NL Cy Young winner — is a confidence-building win going into the Cardinals series.

**Angle selected:** Score-first recap + key contributors + decisive play (errors) + record heading to next series. Informative with a bold finish ("Cubs leave Pittsburgh at 31-26. 🔥").

---

### STORY 2: Cardinals Series Preview

**Freshness tags:** rivalry-series, division-race, Busch-Stadium

**Summary:** Cubs open a 3-game series at Busch Stadium tonight at 6:15 PM CT. Cubs arrive at 31-26 on a 2-game win streak. Cardinals are 29-25. This series has NL Central implications: Cubs lead Cardinals by 1.5 games in the standings, both chasing the division-leading Brewers. The Cubs-Cardinals rivalry is the NL Central's most charged matchup.

**Angle selected per prompt rule:** Lead with opponent + series length + location. Kicker = momentum angle and rivalry stakes.

**Engine note:** The system prompt mandates the opener tweet "lead with the matchup itself (opponent + length + location)." Applied exactly: "Cubs at Cardinals. 3 games at Busch Stadium, 6:15 PM CT tonight."

---

### STORY 3: NL Central Race Update

**Freshness tags:** NL-Central, standings, division-race

**Summary:** NL Central standings as of today: Cubs 31-26, Cardinals 29-25, Brewers leading the division (~33-20 estimated). Cubs and Cardinals are separated by 1.5 games, both chasing Milwaukee. This weekend's 3-game set at Busch Stadium is a meaningful divisional contest between two teams within striking distance of each other.

**Angle selected:** Clean standings context tweet — state records, describe the race, frame the weekend's stakes without an engagement question.

---

### STORY 4: Ian Happ's PNC Park Mastery

**Freshness tags:** Happ-streak, PNC-Park, hometown-angle

**Summary:** Ian Happ has now reached base in 41 consecutive games at PNC Park, extending a streak that started well before the 2026 season. He grew up in Mt. Lebanon, PA — about 15 miles from PNC Park — and the numbers reflect it. Thursday he went 3-for-4 with a 2-run HR in the 8th inning, his second consecutive game homering at Pittsburgh.

**Angle selected:** Bold/feature take. Lead with the 41-game streak stat, frame with the hometown origin story, close with Thursday's performance. Does NOT claim "longest active streak in MLB" (superlative; not independently verified with second source today).

---

### STORY 5: Cubs Offense — Two-Game Win Streak, Heading to St. Louis

**Freshness tags:** offensive-momentum, win-streak, Cardinals-preview

**Summary:** After a brutal 10-game losing streak (ending May 27), the Cubs went 2-0 to close out Pittsburgh. Happ: 5 RBI Wednesday (10-4 blowout), 2-run HR Thursday. Suzuki: 2 hits, 2 RBI Thursday. The Cubs arrive in St. Louis having found their offensive footing at exactly the right time heading into a rivalry series with divisional implications.

**Angle selected:** Bold momentum take. Stats (Happ 5 RBI Wednesday + HR Thursday, Suzuki 2 RBI Thursday) anchor the claim that the offense is back. Does NOT say they've "fixed" anything permanently — just notes the 2-game run.

---

### STORY 6: Iowa Cubs + Farm System

**Freshness tags:** Iowa-Cubs, prospects, farm-system

**Summary:** Iowa Cubs won 1-0 in a shutout Wednesday. Hartshorn and Owen Ayers both homered in their respective affiliates (Hartshorn at Myrtle Beach, Ayers at Tennessee). The Cubs' prospect pipeline is producing at multiple levels heading into June.

**Angle selected:** Informative prospect roundup. Careful NOT to say "Hartshorn and Ayers went deep for Iowa" — they're at different affiliates. Uses "across the farm system" framing.

---

### STORY 7: Pre-Game Hype

**Freshness tags:** game-day, rivalry, Cardinals

**Summary:** Cubs at Cardinals, Busch Stadium, 6:15 PM CT. Cubs arrive riding a 2-game win streak fresh off splitting Pittsburgh. Rivalry series. First pitch in ~75 minutes from the 5:00 PM tweet time.

**Angle selected:** Energetic pre-game hype. States the stakes (2-game win streak, coming into Cardinals territory), punchy closer ("Bear down").
