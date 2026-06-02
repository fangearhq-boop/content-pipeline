# Cubs Fact-Check Log — 2026-06-02

All factual claims from 03-social-posts-x.md verified against source material.

---

## TWEET 1A (7:00 AM): Series Preview

| Claim | Verification | Source | Confidence | Status |
|-------|-------------|--------|------------|--------|
| Cubs host the Athletics | is_cubs_home=true | Cubs/_data/series-context.json | HIGH | ✅ PASS |
| 3-game series | series_length: 3 | Cubs/_data/series-context.json | HIGH | ✅ PASS |
| Wrigley Field | venue: "Wrigley Field" | Cubs/_data/series-context.json | HIGH | ✅ PASS |
| Game 1 tonight at 7:05 PM CT | game_date_ct: "Tue 7:05 PM CT"; ISO 2026-06-03T00:05Z = June 2 7:05 PM CDT | Cubs/_data/series-context.json | HIGH | ✅ PASS |
| Chicago (32-28) | cubs_record: "32-28" | Cubs/_data/series-context.json | HIGH | ✅ PASS |
| Athletics (28-31) | opponent_record: "28-31" | Cubs/_data/series-context.json | HIGH | ✅ PASS |
| 22 straight games against under-.500 opponents | "Cubs will benefit from June schedule filled with games against teams under .500 — 22 games" | Chicago Sun-Times (May 31, 2026) | MEDIUM (snippet, WebFetch blocked) | ✅ PASS |
| Cardinals just took 2-of-3 | Game 1: STL 6-5; Game 2: CHC 6-1; Game 3: STL 5-1 | ESPN recaps (gameIds 401815542, 401815557, 401815572) + CBS Sports | HIGH | ✅ PASS |
| "June has to be different" | Editorial take — not a factual claim | N/A | N/A | ✅ OPINION OK |

**Priority 1 check (date/time):** June 2, 2026 = Tuesday ✓ (Jan 1, 2026 = Thu; count forward: June 2 = Tue). First pitch 7:05 PM CT ✓. Game 1 of series (not Game 2 or 3) ✓.

---

## TWEET 2A (12:00 PM): Bregman Streak

| Claim | Verification | Source | Confidence | Status |
|-------|-------------|--------|------------|--------|
| Alex Bregman | Cubs third baseman, confirmed | MLB.com player page | HIGH | ✅ PASS |
| 11-game hitting streak | "extended his hitting streak to 11 games" in May 31 recap | ESPN recap (gameId 401815572) | HIGH | ✅ PASS |
| Safely in 14 of his last 16 games | "had hit safely in 14 of his last 16 games" | Chicago Sun-Times (May 30, 2026) | MEDIUM (snippet) | ✅ PASS |
| "Enters June" | Streak active through May 31; June 1 off day; entering June 2 = 11 games | Logic from game schedule | HIGH | ✅ PASS |
| "Alex Bregman the Cubs signed" | Bregman signed with Cubs in 2026 offseason | Multiple sources | HIGH | ✅ PASS |
| "Better late than never" | Editorial take | N/A | N/A | ✅ OPINION OK |

**Cross-reference:** Streak math check: Sun-Times (May 30) said 9-game streak entering May 30 → May 30 game (Cubs 6-1 win, PCA 4-hit game) → 10 games → May 31 HR (ESPN confirmed) → 11 games. ✓

---

## TWEET 3A (1:15 PM): Ben Brown Ace Arc

| Claim | Verification | Source | Confidence | Status |
|-------|-------------|--------|------------|--------|
| Ben Brown opened 2026 in bullpen | "Brown opened 2026 in the bullpen" (12 bullpen appearances before rotation) | Yardbarker, Last Word on Sports, ChiCitySports | HIGH | ✅ PASS |
| 1.92 ERA | Cited in multiple sources: "1.92 ERA in 17 appearances" | CBS Sports player page, RotoWire | HIGH | ✅ PASS |
| 17 appearances | "through seventeen appearances" | CBS Sports, Yardbarker | HIGH | ✅ PASS |
| FOUR starters lost to injury | Horton (TJ), Steele (60-day IL), Boyd (Iowa rehab), Cabrera (15-day IL) = 4 | FanGraphs Roster Resource, MLB.com injuries (June 1 update) | HIGH | ✅ PASS |
| "most reliable arm" | Subjective by ERA: Brown 1.92, Imanaga 4.37, Rea 4.70, Taillon 5.37 | Multiple pitching stat sources | HIGH | ✅ PASS |
| "bullpen reclamation project" | Brown was in bullpen, moved to rotation — confirmed | Multiple sources | HIGH | ✅ PASS |

---

## TWEET 4A (3:45 PM): Rotation Crisis / Trade

| Claim | Verification | Source | Confidence | Status |
|-------|-------------|--------|------------|--------|
| Horton is out until 2027 | April 16 surgery + 15-16 month timetable = ~July 2027 | CBS Sports injury report, FTA (June 1 update) | HIGH | ✅ PASS |
| Steele on the 60-day IL | Listed on 60-day IL, left elbow | FanGraphs Roster Resource | HIGH | ✅ PASS |
| Boyd rehabbing | 4 IP, 2 ER Iowa rehab start; one more start planned | June 1 pipeline research + MLB.com injuries | HIGH | ✅ PASS |
| Cabrera rehabbing/IL | 15-day IL (right finger blister) | FanGraphs Roster Resource | HIGH | ✅ PASS |
| Four starters down | Horton + Steele + Boyd + Cabrera = 4 | Enumerated above | HIGH | ✅ PASS |
| Cubs still 4 games above .500 | 32-28 = +4 | Series-context.json | HIGH | ✅ PASS |
| "trade deadline is coming" | Deadline exists; stated without specific date (one source cited August 3 — not verified against official MLB announcement, so date omitted) | MLB Trade Rumors (one source) | MEDIUM | ✅ PASS (hedged) |
| Peralta (trade target) | "Cubs exploring early market... Freddy Peralta" — on Mets | MLB Trade Rumors URL + Bleacher Nation (May 31) | MEDIUM | ✅ PASS (rumor labeled implicitly) |
| Gray (trade target) | "Sonny Gray [Red Sox] named by The Athletic as viable target" | Heavy.com (May 2026) | MEDIUM | ✅ PASS (rumor labeled implicitly) |
| Webb (trade target) | "Logan Webb" mentioned in multiple trade target roundups | North Side Baseball, Last Word on Sports | MEDIUM | ✅ PASS (rumor labeled implicitly) |
| Counsell knows what rotation needs | Editorial conclusion from factual premise (4 starters down) | N/A | N/A | ✅ OPINION OK |

**⚠ FLAG — Trade deadline date:** One source (Bleacher Nation, from search snippet) cited "August 3" as the 2026 deadline. Standard deadline is July 31. This discrepancy was NOT resolved; specific date was therefore OMITTED from tweet. Tweet says "trade deadline is coming" — appropriately hedged. ✓

---

## TWEET 5A (5:00 PM): Pre-Game Hype

| Claim | Verification | Source | Confidence | Status |
|-------|-------------|--------|------------|--------|
| First pitch at Wrigley in two hours (from 5 PM post) | 7:05 PM CT - 5:00 PM CT = 2:05 hrs. "In two hours" is accurate | Series-context.json | HIGH | ✅ PASS |
| Athletics at Cubs, Game 1 of 3 | Same as Tweet 1A verification | Series-context.json | HIGH | ✅ PASS |
| Chicago (32-28) | Same as Tweet 1A | Series-context.json | HIGH | ✅ PASS |
| "easiest stretch of the schedule" | Sun-Times called it 22 straight vs under-.500 | Chicago Sun-Times (May 31) | MEDIUM | ✅ PASS |
| Bregman on 11-game hit streak | Same as Tweet 2A verification | ESPN recap | HIGH | ✅ PASS |
| "Time to start a run" | Editorial take | N/A | N/A | ✅ OPINION OK |

---

## Compound Claims Cross-Check

No "first since XXXX", "career-high", or "led MLB" claims were used in any tweet. No compound claims requiring second-source cross-reference. ✓

## Priority 1 (Date/Time) Summary
- Game is tonight (June 2, 2026 = Tuesday) ✓
- First pitch 7:05 PM CT ✓
- "Game 1" confirmed ✓
- "in two hours" from 5 PM post ✓ (7:05 PM CT - 5:00 PM CT = 2:05 hours)

## Character Count Verification

| Tweet | Approximate Count | Limit | Status |
|-------|------------------|-------|--------|
| 1A | ~277 chars | 280 | ✅ PASS |
| 2A | ~212 chars | 280 | ✅ PASS |
| 3A | ~258 chars | 280 | ✅ PASS |
| 4A | ~270 chars | 280 | ✅ PASS |
| 5A | ~244 chars | 280 | ✅ PASS |

## Hashtag Check

| Tweet | Hashtags | Count | #Cubs Present | Status |
|-------|----------|-------|--------------|--------|
| 1A | #Cubs #GoCubs #WrigleyField | 3 | ✅ | ✅ PASS |
| 2A | #Cubs #GoCubs #MLB | 3 | ✅ | ✅ PASS |
| 3A | #Cubs #CubsBaseball #MLB | 3 | ✅ | ✅ PASS |
| 4A | #Cubs #MLB #CubsBaseball | 3 | ✅ | ✅ PASS |
| 5A | #Cubs #GoCubs #WrigleyField | 3 | ✅ | ✅ PASS |

## Style Rules Check
- "No. 1" vs "#1": No rankings used — not applicable ✓
- Score format (winner first): No scores in today's tweets (preview day) — not applicable ✓
- Contractions used: "he's" not used, "that's" used in Tweet 2A ✓
- ALL CAPS max 1-2 words: "FOUR" in Tweet 3A ✓; no ALL CAPS in other tweets ✓
- No engagement questions: No "?" marks anywhere in tweet copy ✓
- No filler/non-news tweets: All 5 anchored to specific news angles ✓
- Time format: "7:05 PM CT" used ✓
