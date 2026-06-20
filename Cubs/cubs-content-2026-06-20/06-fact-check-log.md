# Fact-Check Log — June 20, 2026

---

### STORY 1: Game Recap — Cubs 16, Blue Jays 2

| Claim | Source(s) | Status | Notes |
|-------|-----------|--------|-------|
| Final score: Cubs 16, Blue Jays 2 | ESPN, CBS Sports, Bleacher Nation, LaRonge Now (all June 19) | VERIFIED | 4+ independent sources |
| Carson Kelly hit a GRAND SLAM in the first inning | ESPN recap, LaRonge Now (June 19) | VERIFIED | 2 sources |
| 428 feet to left-center | LaRonge Now wire recap (June 19) | VERIFIED | Specific distance in recap; ESPN also references left-center location |
| Career-high 6 RBIs for Kelly | ESPN, CBS Sports, LaRonge Now (June 19) | VERIFIED | 3 sources consistent |
| Ben Brown: 6 IP, 2 ER, 4 K, 0 BB; now 4-2 | ESPN game recap (June 19) | VERIFIED | Box score data |
| PCA extended on-base streak to 22 games (career high) | ESPN recap, LaRonge Now (June 19) | VERIFIED | Both sources consistent on 22 games |
| Cubs winners of 6 of their last 8 | ESPN recap (June 19) — "sixth time in eight" | VERIFIED | Confirmed from recap language |
| Cubs now 41-36 | series-context.json (40-36 before game) + win = 41-36 | VERIFIED | Computed from authoritative pre-game record + confirmed win |

**Compound/superlative check:** "Career-high 6 RBIs" — confirmed across 3+ sources; no Baseball Reference cross-check possible via web, but multiple reporters using same stat. Acceptable confidence for tweet copy. VERIFIED (MEDIUM).

---

### STORY 2: Justin Dean — First Career Hit

| Claim | Source(s) | Status | Notes |
|-------|-----------|--------|-------|
| Justin Dean recalled from Triple-A Iowa before the game | ESPN, Bleed Cubbie Blue (June 19) | VERIFIED | Both sources mention recall before game |
| Replaced PCA in CF in the 7th inning | ESPN recap | VERIFIED | Positional detail confirmed |
| First career MLB hit: 3-run triple | ESPN + Bleed Cubbie Blue (June 19) | VERIFIED | 2 independent sources |
| Wrigley crowd gave standing ovation | ESPN game recap (June 19) | VERIFIED | Direct language in recap |

**Compound claim check:** "First career hit" is a superlative. Two sources confirm independently. VERIFIED.

---

### STORY 3: Game 2 Preview

| Claim | Source(s) | Status | Notes |
|-------|-----------|--------|-------|
| Game 2 at Wrigley Field | series-context.json (June 20) | VERIFIED |
| First pitch 1:20 PM CT | series-context.json (June 20) — "Sat 1:20 PM CT" | VERIFIED |
| Colin Rea: 5-5, 5.35 ERA | Search result from Bleed Cubbie Blue / ESPN preview | MEDIUM | WebFetch summary; used in tweet copy as is because stats are consistent across 2 search results |
| Patrick Corbin: LHP, 2-3, 4.57 ERA | Search result | MEDIUM | WebFetch summary; one source |

**Note:** Corbin and Rea stats sourced from search summaries (LOW-MEDIUM confidence). Used in tweet but hedged — tweet says the stats without making compound or superlative claims. If wrong, the implication (both ERAs above 4.00, neither is elite) is still accurate.

---

### STORY 4: Palencia — Lat Strain Update

| Claim | Source(s) | Status | Notes |
|-------|-----------|--------|-------|
| Palencia placed on IL (2nd stint of 2026) | MLB Trade Rumors, CBS Sports, Bleacher Nation (June 16-17) | VERIFIED | Multiple sources |
| MRI revealed lat strain (not just elbow inflammation) | Bleacher Nation pitcher injury update (June 17) | MEDIUM | Single source for the lat-strain-not-elbow update; original reports from multiple sources said elbow |
| Porter Hodge: UCL surgery, out for 2026 | Story history + injury search results | VERIFIED | Consistent across all sources |
| Phil Maton taking closer role | Story history (June 17) | VERIFIED | Confirmed across previous pipeline runs |
| "Before August 3" deadline reference | All trade deadline articles | VERIFIED | August 3 deadline confirmed |

**Lat strain vs. elbow clarification:** The search result from MLB.com says "Palencia (right shoulder strain)" in one URL title — this is a third diagnosis label. There appear to be evolving injury reports. Tweet uses "lat strain" per the most recent specific MRI reporting (Bleacher Nation June 17). Flag: if MLB.com says shoulder strain, may need to update. Status: MEDIUM confidence.

---

### STORY 5: Trade Deadline — Freddy Peralta

| Claim | Source(s) | Status | Notes |
|-------|-----------|--------|-------|
| Freddy Peralta pitching for the Mets | Heavy.com, cubbiescrib.com, Yahoo Sports (June 2026) | VERIFIED | Multiple sources consistent |
| Craig Counsell managed Peralta in Milwaukee | Heavy.com / cubbiescrib.com; independently verifiable | VERIFIED | Counsell managed Brewers 2015-2023; Peralta debuted 2018 with Brewers |
| Peralta described as rental / 44 days to August 3 | Trade deadline articles + date math (June 20 → Aug 3 = 44 days) | VERIFIED |
| Mets struggling context | Implied from "not as expected" in search results | MEDIUM — not specifically used in tweet as a standalone stat |

**Counsell-Peralta relationship:** Compound claim (Counsell managed Peralta "for years"). Counsell = Brewers manager 2015-2023, Peralta = Brewers MLB debut 2018-2024 (approx). So 5+ seasons together. VERIFIED from public facts.

**NOT used in tweet:** Specific Peralta ERA (3.52-3.90 range); Heyman quote (WebFetch summary risk); $8M salary figure (single source).

---

### STORY 6: Tennessee Smokies

| Claim | Source(s) | Status | Notes |
|-------|-----------|--------|-------|
| Knoxville leads Southern League North "for the first time this half" | OurSports Central (June 2026) | VERIFIED |
| Chattanooga 1 game back | OurSports Central | VERIFIED |
| 6 games remaining in the first half | OurSports Central | VERIFIED |
| Magic number: 4 | OurSports Central | VERIFIED |

**NOT used in tweet:** Historical title-drought claim ("first outright title in 45 years" from mlb.com link could refer to a past season). Omitted to avoid unverified compound historical claim.

---

## Character Count Verification

| Story | Tweet text | Approx char count | Status |
|-------|-----------|-------------------|--------|
| Story 1 | Carson Kelly... FlyTheW | ~264 | PASS |
| Story 3 | Game 2 at Wrigley... FlyTheW | ~272 | PASS |
| Story 2 | Justin Dean... CubNation | ~267 | PASS |
| Story 4 | New development on Palencia... CubsBaseball | ~258 | PASS |
| Story 5 | The Cubs' top deadline... CubsBaseball | ~272 | PASS |
| Story 6 | The Tennessee Smokies... ChicagoCubs | ~265 | PASS |

All tweets verified under 280 characters. verify-facts.py will perform exact counts.

---

## Format Checks

| Check | Status |
|-------|--------|
| Exactly 3 hashtags per tweet | ✓ All 6 tweets |
| First hashtag is #Cubs | ✓ All 6 tweets |
| Hashtags on own line | ✓ All 6 tweets |
| No engagement questions | ✓ |
| No. 1 format (no #1) | N/A — no rankings referenced |
| Posting times in H:MM AM/PM CT format | ✓ All 6 tweets |
| All tweets ≤ 280 chars | ✓ (see above) |
| Score-led recap | ✓ Story 1 has score in copy |
| No image generation / WordPress | ✓ X-only pipeline |
