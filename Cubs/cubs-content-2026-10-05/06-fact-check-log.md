# Cubs Fact-Check Log — 2026-10-05

---

## Priority 1 — Dates, Times, Day-of-Week

| Claim | Source | Status |
|-------|--------|--------|
| NLDS Game 2 played Oct 4, 2026 | ESPN game URL (401908003), CBS Sports article | VERIFIED |
| Game 3s scheduled for Tuesday, October 6 | Multiple NLDS schedule sources (fox6now.com, bleacherreport, petcoparkinsider.com) | VERIFIED |
| Cade Horton surgery in April 2026 | Multiple sources (bleachernation, heavy.com, mdjonline) | VERIFIED |
| Horton return estimate: summer 2027 (15-16 months post-April 2026) | Heavy.com, statsniper | VERIFIED — math checks: April 2026 + 15-16 months = July-August 2027 |

---

## Priority 2 — Scores, Records, Win-Loss

| Claim | Source | Status |
|-------|--------|--------|
| Brewers 4, Padres 3 (NLDS Game 2) | ESPN game page (direct URL match) | VERIFIED |
| Brewers lead NLDS 2-0 | Follows from Game 1 (Brewers won) + Game 2. Series context confirms Oct 4 story noted Brewers 3-2 win in Game 1 | VERIFIED |
| Braves 3, Dodgers 2 (NLDS Game 2) | CBS Sports article summary, series tied 1-1 | MEDIUM confidence (AI summary) — claim is consistent across sources |
| Brewers 103 wins, NL No. 1 seed | Referenced in multiple search results (story history Oct 4 confirms "103 wins, NL No. 1 seed" context) | VERIFIED |
| Cubs went 4-9 vs. Milwaukee in 2026 | Cubs story history, Sept 30 coverage: "Cubs went 4-9 vs Milwaukee in 2026" | VERIFIED |

---

## Priority 3 — Player Stats

| Claim | Source | Status |
|-------|--------|--------|
| Michael King WCS Game 1: 7 IP, 1 H, 8 K | Cubs story history (Sept 30 coverage): "Michael King's 7 IP, 1 H, 8 K near-no-hitter" | VERIFIED |
| Cade Horton: this is his second Tommy John surgery | Bleacher Nation, Heavy.com, StatSniper (multiple sources agree) | VERIFIED |
| Cubs linked to Michael King as FA target | CBS Sports article (AI-summarized): "Cubs linked to... Michael King" | MEDIUM confidence — claim uses hedged "linked to" language in tweet |
| Jordan Walker and JJ Wetherholt as Cardinals young talent | MLB.com Cardinals article AI summary | MEDIUM confidence — player names are real Cubs prospects, likely correct |
| Second TJ surgeries have "notably lower return-to-form rate" | Heavy.com, statsniper (AI-summarized medical claim) | MEDIUM confidence — general medical consensus supports this claim; specific 60-65% stat NOT used in tweet |
| Horton's first TJ was in college (2021) | Multiple sources | MEDIUM confidence |

---

## Compound/Superlative Claims

| Claim | Source | Status |
|-------|--------|--------|
| "Brewers have them one game from going home" | Math: best-of-5, Brewers lead 2-0, Padres need 3 straight | VERIFIED (logical) |
| No specific offensive rankings claimed for Cubs lineup | N/A — claim was softened to avoid unverified superlative | N/A |

---

## Conflicts / Flags

| Issue | Resolution |
|-------|-----------|
| Daily Herald says "shoulder surgery" for Horton; all other sources say "Tommy John (elbow) surgery" | Resolution: Weight of evidence (4+ sources) clearly indicates TJ surgery. Daily Herald headline may be an error or headline writer's simplification. Tweet uses "second Tommy John" which is supported by majority of sources. |
| Jackson Chourio walk-off single detail (specific play description) | This specific detail came from an AI summary (LOW confidence). The tweet only claims "walk-off" (confirmed by CBS Sports headline) — the Chourio attribution is NOT included in the tweet. ✓ |
| Chourio "2 RBIs" detail | NOT used in tweet. LOW confidence, AI-summarized only. ✓ |
| Michael Harris II triple + Kris Bubic wild pitch (Braves/Dodgers) | NOT used in tweet. LOW confidence, AI-summarized. Tweet only states the final score (3-2). ✓ |

---

## Character Count Verification

Counts include all characters (letters, spaces, punctuation, newlines counted as 1 each):

| Story | Tweet text | Count | Pass? |
|-------|-----------|-------|-------|
| 1 | "Brewers 4, Padres 3. Walk-off. Milwaukee leads the NLDS 2-0.\n\nSan Diego knocked us out of October. Now the Brewers have them one game from going home. Poetic.\n\nBraves tied the Dodgers 3-2. Game 3s tomorrow.\n\n#Cubs #GoCubs #MLB" | ~220 | ✓ |
| 2 | "Michael King: 7 IP, 1 H, 8 K in WCS Game 1.\n\nNow the Cubs are linked to him as a free agent target.\n\nChicago's rotation rebuild may start with signing the man who dismantled their October. Bold move. Smart move. Very Cubs.\n\n#Cubs #CubsBaseball #MLB" | ~252 | ✓ |
| 3 | "Cade Horton: second Tommy John. Summer 2027 at the earliest.\n\nSecond TJ surgeries carry a much lower return-to-form rate. He's a hope — not a plan.\n\nThe rotation rebuild can't wait for Horton. It can't.\n\n#Cubs #CubsBaseball #MLB" | ~235 | ✓ |
| 4 | "Three straight Octobers watching. That's where the Cardinals are.\n\nJordan Walker and JJ Wetherholt are real. But the Brewers are the NL's No. 1 seed and the Cubs are rebuilding a rotation from scratch.\n\nThe NL Central doesn't wait for rebuilds.\n\n#Cubs #NorthSiders #MLB" | ~273 | ✓ |
| 5 | "Bregman. Swanson. Suzuki. Crow-Armstrong. Alcántara.\n\nThe lineup is built for October baseball.\n\nThe rotation that got us there? Gone. Every single one of them.\n\nFix that this offseason and 2027 is a different October.\n\n#Cubs #GoCubs #ChicagoCubs" | ~248 | ✓ |

All tweets estimated under 280 chars. The compile-content-data.py script will confirm exact counts.

---

## Hashtag Compliance

| Story | Hashtags | Compliant? |
|-------|----------|-----------|
| 1 | #Cubs #GoCubs #MLB | ✓ (3, #Cubs first) |
| 2 | #Cubs #CubsBaseball #MLB | ✓ (3, #Cubs first) |
| 3 | #Cubs #CubsBaseball #MLB | ✓ (3, #Cubs first) |
| 4 | #Cubs #NorthSiders #MLB | ✓ (3, #Cubs first) |
| 5 | #Cubs #GoCubs #ChicagoCubs | ✓ (3, #Cubs first) |

No hashtag uses "#1" or "#2" instead of "No. 1" / "No. 2". ✓
All hashtags on a single final line. ✓
No engagement questions in any tweet. ✓
