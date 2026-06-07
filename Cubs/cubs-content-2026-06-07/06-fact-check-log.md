# Fact-Check Log — June 7, 2026

## Priority 1 — Scores and Game Stats

| Claim | Tweet | Verdict | Source(s) | Confidence |
|-------|-------|---------|-----------|------------|
| Cubs 3, Giants 2 (June 6, 2026) | Post 1A | ✓ VERIFIED | ESPN gameday (gameId/401815653), MLB.com gameday (game 824669), CBS Sports box score | HIGH — 3 independent sources |
| Cubs record: 34-31 | Posts 1A, 5A, 6A | ✓ VERIFIED | Multiple preview sources (NBC Sports, Baseball-Reference preview) | HIGH |
| "torched 18-3" (June 5 loss context) | Post 1A | ✓ VERIFIED | Established in June 5/6 pipelines; not reinvestigated today | HIGH (carry-forward) |

---

## Priority 2 — Records and Standings

| Claim | Tweet | Verdict | Source(s) | Confidence |
|-------|-------|---------|-----------|------------|
| Cubs 19-14 at home | Post 6A | ✓ VERIFIED | Multiple preview sources (NBC Sports, Baseball-Reference) | HIGH |
| Giants record: 26-39 | Post 6A | ✓ VERIFIED | Series context snapshot (generated_at 2026-06-07T08:30:00Z) | HIGH — snapshot is authoritative |
| "Trailing Milwaukee in the division" | Post 5A | ✓ VERIFIED (direction) | Cubs 34-31 vs Brewers (37-23+ per June 6 pipeline) | HIGH direction; MEDIUM exact GB |
| "Most of the remaining schedule is sub-.500" | Post 5A | ✓ PLAUSIBLE | From June 1 pipeline: Athletics, Giants, Rockies, Blue Jays, Mets all sub-.500 in June schedule. Directionally accurate. | MEDIUM — schedule was confirmed June 1; today's opponents match but did not re-verify each team's current record |

---

## Priority 3 — Player Stats

| Claim | Tweet | Verdict | Source(s) | Confidence |
|-------|-------|---------|-----------|------------|
| Dansby Swanson .180 BA | Post 2A | ✓ VERIFIED | ESPN, Chicago Sun-Times, Yahoo Sports all cite .180 | HIGH |
| "Six hits in his last 46 at-bats" | Post 2A | ✓ VERIFIED | Sun-Times / ESPN cite 6 hits in 46 AB = .130 in last 14 games | HIGH |
| Swanson contract: $177M | Post 2A | ✓ VERIFIED | Well-established public contract figure (7 years, $177M signed before 2023 season) | HIGH |
| Taillon: 2-5, 5.13 ERA | Post 6A | ✓ VERIFIED | Multiple June 7 preview sources (NBC Sports, Baseball-Reference, CubsInsider) | HIGH |
| McDonald: 2-3, 4.50 ERA | Post 6A | ✓ VERIFIED | Same preview sources | HIGH |
| Boyd: final rehab start Saturday (June 6) | Post 3A, 4A | ✓ VERIFIED | Bleacher Nation, ESPN, Fox Sports all confirm Boyd's rehab arc and final start Saturday | HIGH |
| Shaw: 2-for-4 in recent rehab | Post 4A | ✓ VERIFIED | CBS Sports, Bleacher Nation, RotoWire | HIGH |

---

## Priority 4 — Dates, Times, Day of Week

| Claim | Tweet | Verdict | Source(s) | Confidence |
|-------|-------|---------|-----------|------------|
| "tonight at 7:30 PM CT" (June 7 game) | Posts 1A, 5A, 6A | ✓ VERIFIED | Series context snapshot (`game_date_ct: "Sun 7:30 PM CT"`), NBC Sports preview | HIGH |
| "Wrigley" as venue | Posts 1A, 5A, 6A | ✓ VERIFIED | Series context: `is_cubs_home: true`, `venue: "Wrigley Field"` | HIGH |
| "Series tied 1-1" | Posts 1A, 5A | ✓ VERIFIED | Game 1: Giants won 18-3 (June 5), Game 2: Cubs won 3-2 (June 6) | HIGH |
| Boyd final rehab start "Saturday" (June 6) | Post 4A | ✓ VERIFIED | Prior pipeline + research confirmation | HIGH |
| Kelly acquired "on Saturday" | Post 3A | ✓ VERIFIED | Research confirms transaction June 6 | MEDIUM-HIGH — transaction date from single source |

---

## Priority 5 — Roster / Transactions

| Claim | Tweet | Verdict | Source(s) | Confidence |
|-------|-------|---------|-----------|------------|
| Antoine Kelly is LHP | Post 3A | ✓ VERIFIED | Research agent confirmed "LHP Antoine Kelly" | MEDIUM-HIGH (single explicit source) |
| Horton (Tommy John) | Post 3A | ✓ VERIFIED | Multiple pipelines + research ("Tommy John surgery Thursday") | HIGH |
| Steele: 60-day IL (elbow) | Post 3A | ✓ VERIFIED | Established in prior pipelines | HIGH |

---

## Flags / Omissions

| Item | Reason for Flag/Omission |
|------|--------------------------|
| Ben Brown's June 6 pitching line | NOT included in any tweet — Box score data not retrieved. Ben Brown was the scheduled starter per June 6 pipeline and ERA may have improved to ~1.74 (research snippet), but specific IP/ER/K numbers NOT confirmed. Writing around it was the correct decision. |
| Brewers exact current record | Omitted exact figure — Brewers were 37-23 entering June 6; today's record unconfirmed. Tweet says "trailing Milwaukee" without a specific GB number — appropriate hedge. |
| Cardinals current record | Not used in any tweet — was 32-28 entering June 6; June 6 result unknown. |
| "Most of the remaining schedule is sub-.500" | Carry-forward from June 1 pipeline. Directionally accurate (Rockies, Blue Jays, Mets all sub-.500 in June schedule) but individual team records not re-verified today. Flagged MEDIUM. |
| "3rd worst batting average" ranking for Swanson | Single-source ranking — tweet uses absolute stat (.180 BA) and specific recent slump numbers instead of the ranking claim. Correct decision. |

---

## Summary
- **Total claims checked:** 22
- **HIGH confidence:** 17
- **MEDIUM-HIGH confidence:** 3
- **MEDIUM (flagged):** 2
- **Failures / corrections:** 0
- **Omissions (claims removed from tweets):** 4 (Brown line, Brewers exact record, Cardinals record, Swanson ranking)
