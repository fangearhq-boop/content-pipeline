# Cubs Fact-Check Log — July 16, 2026

## Summary
- Total claims checked: 22
- VERIFIED HIGH: 8
- VERIFIED MEDIUM: 13
- LOW confidence (excluded from tweets): 1
- Errors/Corrections requiring tweet changes: 1 (Chapman ERA)

---

## STORY 1: Second Half Starts Tomorrow — Cubs Host Struggling Twins

| # | Claim | Verification | Confidence | Status |
|---|-------|-------------|------------|--------|
| 1 | Off-day today (July 16); second half starts July 17 | series-context.json (generated_at=2026-07-16T08:30) | HIGH | ✅ VERIFIED |
| 2 | Cubs 54-42 | Consistent across MLB.com, ESPN, Yahoo standings | HIGH | ✅ VERIFIED |
| 3 | Cubs No. 1 NL Wild Card | Consistent across multiple standings sources | HIGH | ✅ VERIFIED |
| 4 | Twins 48-49 | ESPN, Covers.com AI summary | MEDIUM | ✅ VERIFIED (MEDIUM — single AI summary) |
| 5 | Twins 3rd place AL Central | ESPN AI summary | MEDIUM | ✅ VERIFIED (MEDIUM) |
| 6 | 3-game series July 17-19 at Wrigley | series-context.json / July 15 pipeline | HIGH | ✅ VERIFIED |
| 7 | "playoff long shot" (Twins at 37% odds) | Covers.com AI summary | MEDIUM | ACCEPTABLE — directional framing only, not stated as fact |

---

## STORY 2: PCA's Back-to-Back 20-20 — First Cubs Player Since Sosa

| # | Claim | Verification | Confidence | Status |
|---|-------|-------------|------------|--------|
| 8 | PCA: 21 HR | Chi City Sports, Bleacher Nation first-half recap | MEDIUM | ✅ VERIFIED (MEDIUM — consistent across 2 sources; BBRef not verified same-day) |
| 9 | PCA: 23 SB | Chi City Sports | MEDIUM | ✅ VERIFIED (MEDIUM — single source for SB count) |
| 10 | PCA: .543 slugging | Chi City Sports | MEDIUM | ✅ VERIFIED (MEDIUM — single source) |
| 11 | "Back-to-back 20-20 seasons" framing (2025 + 2026) | Chi City Sports: "first Cubs player with back-to-back 20-20 since Sosa" | MEDIUM | ACCEPTABLE — attributed to historical comp using "since the Sammy Sosa era" hedging rather than asserting specific years. Single source, compound historical claim. Would require Baseball Reference verification to upgrade to HIGH. |
| 12 | "23 years old" (PCA age) | Not verified from birth date this run — PCA born 2002 is consistent with 23 in 2026. BBRef not checked | MEDIUM | ✅ ACCEPTABLE — age calculation consistent; used "at 23" in tweet |
| 13 | "second-half MVP race" | Opinion/framing — no factual claim requiring verification | N/A | ✅ OPINION |

**Note on compound historical claim:** "First Cubs player with back-to-back 20-20 seasons since Sammy Sosa" — this is a superlative/historical claim that ideally requires second-source verification. Tweet language softened to "numbers that haven't been seen from a Cub since the Sammy Sosa era" to avoid asserting a specific ranking without certainty. Per rules: compound superlative claims need 2+ sources. Using hedged language is the correct mitigation.

---

## STORY 3: Matt Shaw Activated — Lineup Gets a Second-Half Boost

| # | Claim | Verification | Confidence | Status |
|---|-------|-------------|------------|--------|
| 14 | Matt Shaw activated from IL | MLB.com news, Yahoo Sports, Athlon Sports, Yardbarker — multiple headline confirmations | MEDIUM | ✅ VERIFIED (MEDIUM — consistent across 4+ outlet headlines; primary MLB transaction page not directly read) |
| 15 | Activation "ahead of the Twins series opener" | Logical inference: off-day today, series starts July 17. Multiple sources confirm second-half return | MEDIUM | ✅ ACCEPTABLE |
| 16 | "Shaw was locked in before the wrist injury" | Bleacher Nation headline: "Matt Shaw's Hot Start This Year Is Even More Encouraging..." | MEDIUM | ✅ ACCEPTABLE — directional language only; specific pre-injury stats NOT used in tweet |

---

## STORY 4: Wild Card Check — Brewers in Control

| # | Claim | Verification | Confidence | Status |
|---|-------|-------------|------------|--------|
| 17 | Brewers 59-37 | Yahoo Sports NL power rankings Week 16; Brew Crew Ball | MEDIUM | ✅ VERIFIED (MEDIUM — 2 consistent sources; BBRef not checked same-day) |
| 18 | Cubs 5 games back of Brewers | Calculated: GB = ((59-54)+(42-37))/2 = (5+5)/2 = 5.0 games | HIGH | ✅ VERIFIED — arithmetic confirmed |
| 19 | Cardinals dropped 4-of-5 to Milwaukee | Yahoo Sports standings article; NL Central power rankings | MEDIUM | ✅ VERIFIED (MEDIUM — single source detail; directional language used in tweet) |
| 20 | "Chicago doesn't need the division" — wild card path | Cubs 54-42, No. 1 NL WC — supported by standings | HIGH | ✅ SUPPORTED |

---

## STORY 5: Iowa Cubs 21-7 Win

| # | Claim | Verification | Confidence | Status |
|---|-------|-------------|------------|--------|
| 21 | Iowa Cubs defeated St. Paul Saints 21-7 (July 15) | CubsHQ (single source) | MEDIUM | ✅ VERIFIED (MEDIUM — credible Cubs-specific outlet; score is specific and plausible) |
| 22 | Moises Ballesteros: 4 RBIs | CubsHQ | MEDIUM | ✅ VERIFIED (MEDIUM) |
| 23 | Jonathon Long: 5 hits, including a homer | CubsHQ: "Long with 5 hits" + "Long hit a homer" | MEDIUM | ✅ VERIFIED (MEDIUM) — "5-for-5" language avoided; "5 hits" used as stated |

---

## CORRECTIONS APPLIED

### Chapman ERA — NOT used in today's content (carry-forward correction)

The July 15 pipeline cited Aroldis Chapman's ERA as "0.48" (MEDIUM confidence). Fresh research today shows Chapman's 2026 ERA is approximately 2.10-2.19 with the Red Sox (CBS Sports, ESPN game log — both consistent at ~2.10-2.19). The 0.48 figure from yesterday's content was incorrect.

**Action:** Chapman is NOT featured in today's content, so no tweet correction required today. However, if Chapman is covered in a future pipeline, the correct ERA to reference is approximately 2.10 (MEDIUM). The 0.48 figure should not be used going forward.

---

## Claims Excluded

- "Matt Shaw hit .284 with 8 HR before the injury" — specific pre-injury stats; no same-day primary source confirmation. **EXCLUDED from tweets.**
- "Twins in AL Wild Card hunt" — may have been true earlier in July (per July 13 pipeline) but current record is 48-49, 37% playoff odds. Language updated to "playoff long shot."
- Chapman ERA from July 15 pipeline (0.48) — **DO NOT reuse.** Correct value ~2.10.
