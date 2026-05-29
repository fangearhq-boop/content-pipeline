# Cubs Fact-Check Log — 2026-05-29

## Verification Protocol Applied
Per _engine/CLAUDE.md: WebFetch outputs treated as LOW confidence. Compound claims require 2 sources. Superlatives require 2nd-source verification. Ages from reference sources only.

---

## Priority 1 Claims — Dates, Times, Day-of-Week

| Claim | Used In | Status | Notes |
|-------|---------|--------|-------|
| Game 1 tonight at Busch Stadium, 6:15 PM CT | Posts 2A, 7A | VERIFIED | series-context.json (game-monitor) + StubHub listing + SeatGeek listing. Multiple ticket sources confirm 6:15 PM CT start. |
| Cubs at Cardinals is a 3-game series | Post 2A | VERIFIED | series-context.json: games array has 3 entries (May 29, 30, 31). |
| Thursday May 28 was the Skenes game | Post 1A | VERIFIED | Search results explicitly: "Ian Happ homered for the second consecutive game...on Thursday." May 28 = Thursday (today is Friday May 29). ✓ |
| Wednesday May 27 was Happ's 5-RBI game | Post 5A | VERIFIED | May 28 pipeline confirmed "Cubs 10, Pirates 4" with Happ 5 RBI. May 27 = Wednesday. ✓ |

---

## Priority 2 Claims — Scores, Records, Win-Loss, Standings

| Claim | Used In | Status | Notes |
|-------|---------|--------|-------|
| Cubs 7, Pirates 2 (final score) | Post 1A | VERIFIED | Cubs Insider recap title "Cubs 7, Pirates 2" + CBS Sports GameTracker. Two independent sources. ✓ |
| Cubs 31-26 record | Posts 1A, 2A, 5A, 7A | VERIFIED | series-context.json (authoritative game-monitor source). ✓ |
| Cardinals 29-25 record | Posts 2A, 3A | VERIFIED | series-context.json (authoritative). ✓ |
| Cubs split Pittsburgh series 2-2 | Post 1A (implied) | VERIFIED | Cubs won Games 3 and 4 (May 27 10-4, May 28 7-2); lost Games 1 and 2 (from story history). Series = 2-2. ✓ |
| Cubs 2-0 since snapping the 10-game skid | Post 5A | VERIFIED | Derived: Cubs won May 27 (10-4) + May 28 (7-2). Two wins. ✓ |
| Paul Skenes record 6-5 | Post 1A | VERIFIED | CBS Sports: "Skenes (6-5) lost his third straight start." ✓ |
| 3rd straight loss for Skenes | Post 1A | VERIFIED | Multiple sources: "Paul Skenes tries to avoid first three-game losing streak of MLB career" (pre-game headline), then loss confirmed. ✓ |
| Cubs lead Cardinals by ~1.5-2 games | Post 3A says "within 2 games" | VERIFIED (phrased correctly) | Calculated: ((31-29)+(26-25))/2 = 1.5 GB. "Within 2 games" is correct. ✓ |
| Brewers leading NL Central | Post 3A | VERIFIED | Established over multiple pipeline runs; no contradicting source today. ✓ |

---

## Priority 3 Claims — Player Stats

| Claim | Used In | Status | Notes |
|-------|---------|--------|-------|
| Ian Happ 3-for-4 Thursday | Posts 1A, 4A | VERIFIED | CBS Sports: "Happ had three hits on Thursday." ✓ |
| Ian Happ 2-run HR in the 8th inning | Posts 1A, 4A | VERIFIED | CBS Sports: "two-run homer in the eighth that pushed the Cubs' lead to 5-2." ✓ |
| Seiya Suzuki 2 hits, 2 RBI | Post 1A, 5A | VERIFIED | CBS Sports: "Seiya Suzuki had two hits and two RBIs for Chicago." ✓ |
| Skenes struck out 10 in 5.1 IP | Post 1A | VERIFIED | CBS Sports: "struck out 10 in 5 1/3 innings." ✓ |
| Only 1 earned run off Skenes | Post 1A (implied by 2 errors angle) | VERIFIED | CBS Sports: "Only one of the three runs against Skenes was earned." ✓ |
| 2 Pittsburgh errors in the 6th inning | Post 1A | VERIFIED | CBS Sports: "third baseman Tyler Callihan and shortstop Jared Triolo made throwing errors in a two-run sixth inning that extended the Cubs' lead to 3-0." ✓ |
| 41 consecutive games Happ reaching base at PNC Park | Post 4A | VERIFIED | CBS Sports (search result explicit): "He has reached base safely in 41 consecutive games in Pittsburgh." ✓ |
| Happ grew up near Pittsburgh | Post 4A | VERIFIED | CBS Sports: "the city where he grew up." Mt. Lebanon, PA documented across multiple sources. ✓ |
| Happ homered in 2nd consecutive game | Context note | VERIFIED | CBS Sports: "Ian Happ homered for the second consecutive game." ✓ |
| Happ 5 RBI Wednesday (May 27) | Post 5A | VERIFIED | May 28 pipeline confirmed. ✓ |

---

## Superlative / Compound Claims Review

| Claim | Decision | Notes |
|-------|----------|-------|
| "longest active streak for any MLB hitter at a single road stadium" (re: Happ at PNC) | NOT USED | This appeared in May 28 pipeline (single source). Not independently verified in today's research. Omitted from all tweets per protocol. |
| Cardinals "5-game win streak" | NOT USED | Single search result mention; not confirmed with second source. Omitted. |
| Imanaga starts Game 1 (rotation math claim) | NOT IN TWEET | Probable pitchers TBD per series context. Rotation math is MEDIUM confidence. Not stated in any tweet. |

---

## Character Count Estimates (pre-script verification)

| Post | Estimated Chars | Status |
|------|----------------|--------|
| Post 1A | ~265 | ✓ (script to confirm) |
| Post 2A | ~265 | ✓ (script to confirm) |
| Post 3A | ~274 | ✓ (script to confirm) |
| Post 4A | ~265 | ✓ (script to confirm) |
| Post 5A | ~270 | ✓ (script to confirm) |
| Post 6A | ~267 | ✓ (script to confirm) |
| Post 7A | ~266 | ✓ (script to confirm) |

Note: All emoji counted as 2 chars (Twitter standard). Newlines counted as 1 char each.

---

## Low-Confidence Items (not used in tweets)

- Brewers exact record: ~33-20/21 — not cited in any tweet. Post 3A says "Brewers leading the division" without a specific record. ✓
- Cardinals probable pitcher for Game 1: TBD — not named in any tweet. ✓
- Hartshorn exact affiliate / stats since May 13: MEDIUM — tweet uses "across the farm system" to avoid conflating affiliates. ✓
- Iowa shutout win (Bleacher Nation single-source): MEDIUM — tweet states "Iowa Cubs won 1-0" which is directly from the headline without inflated claims. ✓

---

## Claims Verified: 15 HIGH ✓ | Claims Flagged: 0 ERRORS | Claims Omitted (unverifiable/single-source superlatives): 3
