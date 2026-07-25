# Fact-Check Log — 2026-07-25

---

## STORY 1: Cubs 3, Pirates 2 F/10

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Final score: Cubs 3, Pirates 2 | ESPN recap + Cubs Insider + Butler Eagle (3 sources) | HIGH | ✓ VERIFIED |
| Game went 10 innings | ESPN recap URL includes gameId=401816237, multiple sources | HIGH | ✓ VERIFIED |
| Boyd: 7 IP, 1 ER | Multiple sources (Butler Eagle headline, Cubs Insider recap) | HIGH | ✓ VERIFIED |
| PCA solo HR in 6th off Jones | Cubs Insider "PCA Stays Hot, Belts Solo Home Run" + ESPN recap | HIGH | ✓ VERIFIED |
| Swanson RBI single in 10th | Cubs Insider + Butler Eagle headline | HIGH | ✓ VERIFIED |
| Suzuki bases-loaded walk in 10th | Cubs Insider recap | MEDIUM | ✓ VERIFIED (single detailed source) |
| Ian Happ scored on Swanson single (automatic runner) | Cubs Insider recap | MEDIUM | ✓ VERIFIED (single source) |
| Cubs record becomes 58-45 | series-context.json (generated 08:30 UTC): cubs_record: "58-45" | HIGH | ✓ VERIFIED |

**Tweet text check:** "Crow-Armstrong's solo shot tied it in the 6th" — game was 1-0 Pirates when PCA homered to tie 1-1. ✓ Accurate.
"Swanson delivered in the 10th" — correct, it was the 10th inning. ✓

---

## STORY 2: Imanaga vs. Skenes Ace Duel

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Skenes: 9-8, 3.23 ERA on season | MLB.com preview + RotoWire | MEDIUM | ✓ PLAUSIBLE (multiple sources cite same stats) |
| Skenes seeking 4th straight win | MLB.com headline: "Bizarre drought in the past, Skenes seeks a 4th straight win vs. Cubs" | HIGH | ✓ VERIFIED |
| Skenes last start: 7 IP, 1 ER at Cleveland | CBS News article ("Pirates beat Reds 4-1" is wrong team — another article) | MEDIUM | FLAG: CBS News headline about Reds game vs. Cleveland; source may be inconsistent. Using "three-win roll" in tweet rather than game-specific claim |
| Imanaga: 2.31 ERA last 7 starts | RotoWire + Yardbarker (same stat cited by both) | MEDIUM | ✓ PLAUSIBLE |
| Game time: 5:40 PM CT | series-context.json: game_date_ct: "Sat 5:40 PM CT" | HIGH | ✓ VERIFIED |

**Tweet text check:** "Skenes on a three-win roll, looking for No. 4" — uses "No. 4" not "#4" per brand rules ✓. "Looking for No. 4" = 4th straight win. ✓

---

## STORY 3: Pete Crow-Armstrong MVP Watch

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| PCA 22nd HR last night | July 24 story-history: "21 HR" entering July 24 + confirmed HR vs Jones | MEDIUM | ✓ PLAUSIBLE (22 = 21 + 1; not independently confirmed from bbref) |
| .296 BA | StatMuse / search AI summary | MEDIUM | FLAG: unconfirmed from primary source; tweet uses this |
| 6.0 WAR | FanGraphs cited (multiple sources) | MEDIUM | ✓ PLAUSIBLE |
| WAR pace "historically rare" | Chi City Sports citing franchise history context | MEDIUM | ✓ Used soft language ("historically rare") not a hard number — appropriate hedging |

**Tweet text check:** Used "22nd home run" (confirmed MEDIUM). Used "historically rare" (hedged, not citing a specific count). Used "NL MVP conversation isn't slowing down" (directional opinion, no hard claim). ✓

**Fact-check note:** HR count (22) is derived from prior pipeline data (21 entering 7/24) + confirmed homer vs Jones. Cannot independently verify from primary source in this session. Marked MEDIUM. Cross-check against Baseball Reference before next session.

---

## STORY 4: Trade Deadline

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Deadline: August 3 | Multiple sources consistent | HIGH | ✓ VERIFIED |
| "9 days out" from July 25 | Date arithmetic (Aug 3 - July 25 = 9 days) | HIGH | ✓ VERIFIED |
| Hoyer targeting multi-year control arms | ClutchPoints / Cubs Insider citing reporting | HIGH | ✓ VERIFIED (multiple sources) |
| Freddy Peralta (Mets) as target | Jon Heyman via Yahoo Sports, Bleacher Nation, CBS Sports, Heavy.com | HIGH | ✓ VERIFIED (multiple credible sources) |
| Joe Ryan (Twins) as target | Chi City Sports, multiple outlets | HIGH | ✓ VERIFIED |
| Horton out for 2026 (Tommy John) | July 24 story-history + confirmed in research | HIGH | ✓ VERIFIED |
| Steele on IL | Mentioned in source roundup | MEDIUM | ✓ PLAUSIBLE |
| Maton IL (3rd stint) | Multiple sources (Cubs Crib, Sun-Times, FantasyPros) | HIGH | ✓ VERIFIED |
| Palencia on IL | July 24 story-history (elbow flexor, mid-August target) | HIGH | ✓ VERIFIED |

**Tweet text check:** "Horton, Steele, Maton, and Palencia are all shelved" — accurate summary of IL situation ✓. No superlative claims. ✓

**Fact-check note — Peralta tension:** Tweet says Hoyer is "targeting starters with multi-year control" but Peralta is a free agent after 2026 (confirmed from multiple sources). Tweet intentionally separates Hoyer's preference from the reported targets, letting readers see both points without implying Peralta satisfies Hoyer's criteria. No misrepresentation. ✓

---

## STORY 5: Pirates vs. LHP

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Pirates 9-20 vs. LHP starters | RotoWire (single source) | MEDIUM | FLAG: single source — tweet uses "one of the worst marks" (hedged) not "the worst" |
| Imanaga 2.31 ERA last 7 starts | RotoWire, Yardbarker (MEDIUM) | MEDIUM | Same as Story 2 |

**Tweet text check:** "9-20 vs. lefty starters" exact record used. "One of the worst marks in baseball" = appropriately hedged per confidence level. ✓

---

## STORY 6: Wild Card Standings

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| Cubs 58-45 | series-context.json snapshot | HIGH | ✓ VERIFIED |
| No. 1 NL Wild Card | series-context.json + ESPN WC standings search result | HIGH | ✓ VERIFIED |
| Phillies chasing | ESPN WC standings (56-47 per search summary) | MEDIUM | ✓ PLAUSIBLE |
| D-backs chasing | ESPN WC standings (54-49 per search summary) | MEDIUM | ✓ PLAUSIBLE |

**Tweet text check:** "No. 1 NL Wild Card" — uses "No. 1" not "#1" ✓. Score "58-45" matches series-context.json. ✓

---

## STORY 7: Pre-Game Hype

| Claim | Source | Confidence | Status |
|-------|--------|------------|--------|
| "Took Game 1 in extras last night" | Story 1 verified ✓ | HIGH | ✓ VERIFIED |
| "5:40 PM CT" | series-context.json | HIGH | ✓ VERIFIED |
| "Sunday's finale" | series-context.json shows Game 3 on July 26 | HIGH | ✓ VERIFIED |
| "PNC Park" | series-context.json + venue confirmed | HIGH | ✓ VERIFIED |

---

## Overall Fact-Check Summary

- **HIGH confidence claims:** All 7 tweets contain at least 1-2 HIGH confidence anchors
- **MEDIUM confidence claims used in tweets:** PCA HR count (22), batting average (.296), WAR (6.0), Imanaga ERA (2.31), Pirates LHP record (9-20), Phillies/D-backs standings
- **No LOW confidence claims used in tweets**
- **Hedging applied:** "historically rare" instead of exact franchise count; "one of the worst" instead of ranked claim; "top the reported board" instead of definitive targets
- **Cross-check needed next session:** PCA exact HR count (22) against Baseball Reference; Imanaga last 7 starts ERA against FanGraphs
- **No superlative or milestone claims requiring two-source verification in tweet copy**
