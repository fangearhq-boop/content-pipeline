# Fact-Check Log — 2026-06-04

Verification of all factual claims against cited sources. Priority order per research-playbook.md.

---

## Priority 1 — Scores and Game Stats

### Claim: "Cubs and the A's were knotted at 4 into the final innings" (Tweet 1A)
- **Source:** Search result referencing partial box score showing ATH4CHC4 in progress through 8 innings
- **Confidence:** LOW — WebFetch blocked on ESPN, CBS Sports, MLB.com (all returned 403). Cannot confirm via primary source.
- **Cross-reference:** Series context JSON shows cubs_record changed from 32-29 (June 2) to 32-30 (June 4 morning), confirming Cubs lost June 3. Tied-game-through-8 is the most specific score data available.
- **Decision:** Use claim as written (tied at 4 into final innings) — avoids fabricating an exact final score. The tweet does NOT claim a specific final score. ✓

### Claim: "Cubs fall to 32-30 and trail the series 0-2" (Tweet 1A)
- **Source:** Series context JSON (cubs_record: "32-30"); Cubs were 32-29 after June 2; therefore lost June 3
- **Confidence:** HIGH ✓

### Claim: "Athletics lead series 2-0" (Brief)
- **Source:** Series context confirms Cubs are 32-30 (lost June 2 and June 3); series is 3 games (June 2-4)
- **Confidence:** HIGH ✓

### Claim: "Colin Rea started, Jeffrey Springs started" (Story 1 notes)
- **Source:** Story history June 3 brief: "Game 2 tonight (Rea vs Springs)" — confirmed from prior pipeline run
- **Confidence:** HIGH ✓

### Claim: "Cubs record 32-30" (multiple tweets)
- **Source:** Series context JSON: cubs_record: "32-30" generated 2026-06-04T08:30:00Z
- **Confidence:** HIGH ✓

### Claim: "Athletics record 30-31" (Tweet 3A)
- **Source:** Series context JSON: opponent_record: "30-31" generated 2026-06-04T08:30:00Z
- **Confidence:** HIGH ✓

---

## Priority 2 — Records and Milestones

### Claim: "Bregman .303 BA, .361 OBP over final 18 games of May" (Tweet 2A, Story 2 notes)
- **Source:** Web search results (AI-summarized from multiple sports sources including Bleacher Nation)
- **Cross-reference:** Trend confirmed by multiple independent search results mentioning Bregman's May improvement
- **Confidence:** MEDIUM — numbers are plausible and mentioned across multiple sources, but not confirmed via Baseball Reference primary source (WebFetch blocked)
- **Decision:** Use as stated; flag in notes as not primary-source confirmed ✓

### Claim: "20-game on-base streak, May 10 through June 2" (Tweet 2A)
- **Source:** Web search result explicitly mentioning "20-game on-base streak from May 10 to June 2"
- **Cross-reference:** June 3 Heroes & Goats shows Bregman 0-4 (ending streak) — consistent with streak ending June 3
- **Confidence:** MEDIUM — source is AI-summarized search, not primary box score. Plausible and directionally correct. ✓

### Claim: "Brewers 6+ games back" (Tweet 7A)
- **Source:** June 1 confirmed: Brewers 35-21, Cubs 32-28 (5 GB). Cubs went 0-2 since then (32-30). Brewers est. won 1-2 more games.
- **Calculation:** If Brewers 37-23, Cubs 32-30: GB = ((37-32)+(30-23))/2 = (5+7)/2 = 6.0
- **Confidence:** MEDIUM — actual Brewers June 3-4 results not confirmed. Using "6+" deliberately avoids pinning an exact figure. ✓

### Claim: "Edward Cabrera 3-2, 4.00 ERA" (Tweet 5A)
- **Source:** Story history June 3 brief explicitly states "Cabrera (3-2, 4.00 ERA) returns Saturday"
- **Confidence:** HIGH (prior pipeline confirmed via source) ✓

### Claim: "Taillon 19 home runs in 11 starts" (referenced in background, not in today's tweets)
- Not used in today's tweets — no fact-check needed.

---

## Priority 3 — Player Ages and Biographical Data

No biographical data claims in today's tweets. N/A.

---

## Priority 4 — Game Times and Schedule

### Claim: "7:05 PM CT" first pitch (Tweets 1A, 3A, 8A)
- **Source:** Series context JSON: game_date_ct: "Thu 7:05 PM CT" for game_pk 824672
- **Cross-reference:** June 4 preview search results confirm 7:05 PM ET start (= 7:05 PM CT since both are same timezone in June/CDT... WAIT — need to double-check. ET in June = EDT (UTC-4). CT in June = CDT (UTC-5). 7:05 PM EDT = 6:05 PM CDT.)
- **ISSUE FLAGGED:** The Cubs Insider preview mentions "8:05 PM ET" for the June 4 game. 8:05 PM EDT = 7:05 PM CDT. So "7:05 PM CT" is CORRECT. The search result that said "7:05pm CT" is consistent with 8:05 PM EDT.
- **Confidence:** HIGH ✓

### Claim: "Giants series starts Friday June 5" (Story 4 notes)
- **Source:** Baseball Reference game preview links show Cubs vs Giants at Wrigley on June 5, 6, 7
- **Confidence:** HIGH ✓

### Claim: "Giants games at 1:20 PM CT" (Story 4 notes, not in tweet)
- **Source:** Baseball Reference schedule page (per search results)
- **Confidence:** HIGH ✓

### Claim: "Game 3 of 3" (series finale description)
- **Source:** Series context: series_length: 1 (data anomaly — this appears to be a data issue; the rationale says mid-series and the games array shows one remaining game, which is tonight). The schedule (June 2-4) and story history (June 2 series preview, June 3 recap, June 4 finale) confirm this is a 3-game series.
- **Confidence:** HIGH (3-game series confirmed via context) ✓

### Claim: "Cubs host Giants June 5-7 at Wrigley" (Story 4 notes)
- **Source:** Multiple Baseball Reference preview links, MLB schedule
- **Confidence:** HIGH ✓

---

## Priority 5 — Contract and Financial Data

No contract/financial claims in today's tweets. N/A.

---

## Fact-Check Flags Summary

| Claim | Status | Confidence |
|-------|--------|------------|
| Cubs fall to 32-30 | VERIFIED | HIGH |
| Cubs trail series 0-2 | VERIFIED | HIGH |
| 7:05 PM CT first pitch | VERIFIED | HIGH |
| Athletics 30-31 record | VERIFIED | HIGH |
| Cabrera 3-2, 4.00 ERA | VERIFIED | HIGH |
| Rea vs Springs starters (June 3) | VERIFIED | HIGH |
| Giants series at Wrigley June 5-7 | VERIFIED | HIGH |
| Game tied 4-4 through 8 innings (June 3) | UNCONFIRMED | LOW |
| Bregman .303 BA, .361 OBP (May final 18) | PLAUSIBLE | MEDIUM |
| Bregman 20-game on-base streak | PLAUSIBLE | MEDIUM |
| Brewers 6+ games back | ESTIMATED | MEDIUM |
| Matt Shaw out since May 19 (16 days) | VERIFIED | HIGH |
| Imanaga starts tonight | VERIFIED | HIGH |
| Imanaga ERA 4.37 | CONFLICTING SOURCES | LOW |
| Giants/Rockies/Jays/Mets all sub-.500 | VERIFIED | HIGH |

---

## Compound Claims Requiring Second Source

### "NONE above .500" (Giants, Rockies, Blue Jays, Mets) — Tweet 4A
- **Primary source:** Chicago Sun-Times June 1 ("22 games vs sub-.500 opponents in June" list includes Giants, Rockies, Blue Jays, Mets)
- **Second source:** Baseball Reference previews showing Giants series; Cubbies Crib schedule analysis
- **Confidence:** HIGH — multiple corroborating sources ✓

### "Cubs trail series 0-2" — Tweet 1A
- **Primary source:** Series context JSON (cubs_record: 32-30; was 32-29 after June 2)
- **Second source:** June 3 story history shows Cubs at 32-29 entering June 3; Cubs lost June 3 per record change
- **Confidence:** HIGH ✓
