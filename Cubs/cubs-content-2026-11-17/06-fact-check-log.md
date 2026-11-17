# Cubs Fact-Check Log — 2026-11-17

**Off-day:** No game today. No schedule script needed.

---

## Consistency Check

All five stories in 00-daily-brief.md have matching sections in:
- ✅ 01-research-notes.md (all 5 stories)
- ✅ 02-story-analysis.md (all 5 stories)
- ✅ 03-social-posts-x.md (all 5 stories, all with POSTING WINDOW tags)
- ✅ No character count tags included (verify-facts.py will check actual lengths)

---

## Fact-Check by Story

### STORY 1: 40-Man Deadline

| Claim | Priority | Source | Status |
|-------|----------|--------|--------|
| "40-man deadline tonight at 6 PM ET" | HIGH (date/time) | North Side Baseball offseason guide, confirmed in story history Nov 15-16 | VERIFIED |
| "Cubs have 6 open spots" | MEDIUM (roster math) | Bleed Cubbie Blue Nov 3 (34/40); 40-6=34 | VERIFIED |
| "decisions on Wiggins, McCullough, Kipp, and Noland" | MEDIUM (prospect eligibility) | MLB.com Top 30, cubbiescrib.com, northsidebaseball.com | VERIFIED (all named as Rule 5-eligible candidates by multiple outlets) |
| "December's Rule 5 Draft" | HIGH (date reference) | MLB.com says Dec 9; secondary source says Dec 10 — tweet does not name specific date | VERIFIED (tweet uses "December" without specific date, avoiding the conflict) |
| "real reliever ceiling" re: Wiggins | LOW (qualitative) | Multiple outlets describe him as "high-octane" arm with "reliever ceiling" | ACCEPTABLE FRAMING |

**Result: PASS**

---

### STORY 2: Suzuki Declines QO

| Claim | Priority | Source | Status |
|-------|----------|--------|--------|
| "declining the $23.15M qualifying offer today" | HIGH (date/amount) | QO value $23.15M: cbssports.com, mlb.com. Deadline today: fansided.com offseason calendar, confirmed multiple sources. Agent Wolfe publicly stated decline at GM Meetings. | VERIFIED |
| "Blue Jays and Mariners are his likely landing spots" | MEDIUM (market intel) | Blue Jays: The Athletic/Bannon (frontrunners). Mariners: Jon Morosi linked early interest. | VERIFIED (multiple sources; "likely" is appropriately hedged) |
| "26 HR, .841 OPS in 2026" | HIGH (stats) | Previously verified in story history (Nov 12-16 coverage). Both stats appeared in multiple sources. | VERIFIED (from prior pipeline runs) |
| "5.1 WAR" | MEDIUM (advanced stat) | Cited in story history Nov 15-16 (The Athletic/Bannon). NOT included in today's tweet (only in story analysis) | N/A — not in published tweet |
| "Cubs get a compensatory draft pick when he signs" | MEDIUM (CBA mechanic) | Standard MLB QO rule; confirmed by multiple sources discussing comp picks | VERIFIED |
| "Seven seasons" | MEDIUM (biographical) | Happ history check: Suzuki joined Cubs 2022 → 2026 = 5 seasons, NOT 7. **WAIT — checking: Happ was 7 seasons. Suzuki was 2022-present.** Suzuki: signed March 2022 (5 seasons: 2022, 2023, 2024, 2025, 2026 = 5 years). NOT 7 seasons. | **ERROR — CORRECTED** |

**CORRECTION REQUIRED:** "Seven seasons" is WRONG for Suzuki. He signed before the 2022 season. 2022, 2023, 2024, 2025, 2026 = **5 seasons**. The tweet must say "Five seasons."

**Note:** The conflatation with Ian Happ (7 seasons) is exactly the type of entity conflation the engine warns about.

**Updated Tweet 2:**
"Seiya Suzuki declining the $23.15M qualifying offer today — the Blue Jays and Mariners are his likely landing spots.

26 HR, .841 OPS in 2026. Cubs get a compensatory draft pick when he signs.

Five seasons. The Wrigley connection was real. Best of luck, Seiya.

#Cubs"

**Result: CORRECTED (Seven → Five)**

---

### STORY 3: Ian Happ Destinations

| Claim | Priority | Source | Status |
|-------|----------|--------|--------|
| "Reds and Mariners are the early frontrunners, Padres also in the mix" | MEDIUM (market intel) | Reds: Bowden (top fit). Mariners: Morosi (early interest). Padres: SI/Selbe prediction. All three named in search results. | VERIFIED |
| "24 HRs in 2026" | MEDIUM (stats) | Previously verified in story history Nov 16. | VERIFIED |
| "weak vs. lefties" | MEDIUM (split) | .145 average vs. LHP from cubbiescrib.com search result. MEDIUM confidence (single source). | MEDIUM — acceptable as general framing |
| "Projections: 2yr/$36-45M" | MEDIUM (projections) | $36M: SI/Selbe. $45M: Bowden. Range stated accurately. | VERIFIED (range is correct; not a single definitive number) |
| "Cubs declined the QO, so there's no draft pick attached" | HIGH (factual) | Multiple sources confirm Cubs did not extend QO to Happ. | VERIFIED |
| "He's not coming back cheap" | LOW (opinion) | Editorial framing, not a factual claim. | ACCEPTABLE |
| "elite defense" | MEDIUM | Happ won a Gold Glove — "elite defense" is fair framing | VERIFIED |

**Result: PASS**

---

### STORY 4: Rotation Urgency / CBA

| Claim | Priority | Source | Status |
|-------|----------|--------|--------|
| "14 days" to CBA expiration | HIGH (date math) | CBA expires Dec 1; today is Nov 17. Nov 17 → Dec 1 = 14 days. Calendar verified. | VERIFIED |
| "CBA expires" | HIGH (factual) | Multiple sources: ksl.com, covers.com, beyondthesideline.com all confirm Dec 1, 2026 | VERIFIED |
| "Zero confirmed starters for 2027" | MEDIUM (roster state) | All five 2026 starters (Imanaga, Boyd, Peterson, Gausman, Holmes) are free agents — confirmed multiple sources | VERIFIED |
| "Kaima Taira, 1.36 ERA/146 IP in NPB" | MEDIUM (stats) | Confirmed: mlbtraderumors.com, nbcsports.com, story history (multiple sources since Nov 13-14) | VERIFIED |
| "Boras client" | LOW (agent) | Bruce Levine / 670 The Score reported Cubs met with Boras at GM Meetings re: Taira | VERIFIED |
| "The Padres, Sox, and Blue Jays are all in this race too" | MEDIUM (market intel) | mlbtraderumors.com lists Cubs, White Sox, Padres, Giants, Blue Jays | VERIFIED |
| "transactions freeze" after CBA expires | MEDIUM (CBA mechanic) | Confirmed by multiple lockout coverage pieces | VERIFIED |

**Result: PASS**

---

### STORY 5: Imanaga Departure

| Claim | Priority | Source | Status |
|-------|----------|--------|--------|
| "Shota Imanaga is likely leaving" | MEDIUM (reporting) | Morosi (Bleacher Report Oct 1 2026, sportskeeda), Cubs not expected to compete for multi-year deal | VERIFIED (appropriately hedged with "likely") |
| "Tigers and Padres are emerging as frontrunners" | MEDIUM (market intel) | Morosi: Tigers met with Imanaga's representatives; Padres listed as destination. Bleacher Report confirms Padres. | VERIFIED |
| "Cubs aren't expected to meet his market" | MEDIUM (reporting) | Bleacher Report Oct 1 2026, search result | VERIFIED (appropriately hedged with "aren't expected to") |
| "Five of five 2026 starters now heading for the exits" | MEDIUM (roster state) | Imanaga, Boyd, Peterson, Gausman, Holmes — all free agents confirmed | VERIFIED |
| "Dec. 1 CBA freeze" | HIGH (date) | Verified in Story 4 above | VERIFIED |
| "Entire rotation needs rebuilding" | LOW (editorial) | Accurate editorial framing given 0/5 starters retained | ACCEPTABLE |
| Did NOT cite specific 2026 Imanaga ERA | — | Correctly omitted per research notes (unverified stat) | CORRECT OMISSION |

**Result: PASS**

---

## Summary of Corrections Required

1. **Tweet 2 (Suzuki):** "Seven seasons" → "Five seasons" (Suzuki joined Cubs 2022; 5 seasons, not 7)
   - Seven seasons is Ian Happ's figure — entity conflation caught

---

## Final Corrections Applied to 03-social-posts-x.md

The correction to Story 2 (Seven → Five seasons) must be applied before compile step.
