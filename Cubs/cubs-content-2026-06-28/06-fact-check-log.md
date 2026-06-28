# Cubs Fact-Check Log — 2026-06-28

**Fact-check completed:** 2026-06-28 (pre-publish)
**Stories checked:** 5
**Method:** Cross-reference search results, series-context.json snapshot, prior pipeline coverage

---

### STORY 1: Game Recap — Cubs 8, Brewers 2 (June 27)

- **Claim:** "Cubs 8, Brewers 2" (final score)
  - **Status:** ✅ VERIFIED — Confirmed from two independent sources: ESPN box score (gameId/401815929) and MLB.com gameday (game_pk 823770). Score matches series-context.json snapshot showing Cubs at 45-38 after the game (was 44-38, +1 win = Cubs won).
- **Claim:** "Imanaga and the offense erupted in Milwaukee"
  - **Status:** ✅ VERIFIED — Imanaga starting confirmed across multiple sources. Offense "erupted" = 8 runs scored, well-supported. Imanaga's exact line not in tweet (specific IP/ER/K not confirmed in summaries — kept vague intentionally).
- **Claim:** "series at 1-1"
  - **Status:** ✅ VERIFIED — Cubs lost Game 1 (Brewers 6-2, June 26), won Game 2 (Cubs 8-2, June 27). Series is 1-1. ✓
- **Claim:** "Game 3 today at 1:10 PM CT"
  - **Status:** ✅ VERIFIED — Confirmed from series-context.json snapshot (game_date_ct: "Sun 1:10 PM CT") ✓
- **Claim:** "Rolison takes the ball for the series finale at American Family Field"
  - **Status:** ⚠ PLAUSIBLE / MEDIUM — Ryan Rolison as Cubs starter confirmed via Cubs Insider preview and MLB.com player lookup. No official lineup card at pipeline time. American Family Field confirmed as venue. Day-of confirmation recommended.

---

### STORY 2: Game 3 Preview — Rolison vs. Woodruff

- **Claim:** "Ryan Rolison (5-1, 1.82 ERA)"
  - **Status:** ⚠ MEDIUM — Confirmed via MLB.com player page and Cubs Insider preview; both web search summaries. Record and ERA not verified against Baseball Reference or FanGraphs. Two search sources align. Treat as medium confidence.
- **Claim:** "five starters on the IL"
  - **Status:** ✅ VERIFIED — Horton (TJ), Steele (elbow, 60-day), Taillon (hamstring), Brown (neck), Cabrera (IL). Confirmed from CBS Sports injury report and consistent across research. ✓
- **Claim:** "hottest arms in the NL" (editorial about Rolison)
  - **Status:** ✅ VERIFIED as editorial — 1.82 ERA supports this characterization. Not a specific ranking claim (no "#1" or "best ERA" stated). ✓
- **Claim:** "series on the line" / "series finale"
  - **Status:** ✅ VERIFIED — This is Game 3 of 3 (confirmed series-context.json) ✓

---

### STORY 3: Pete Crow-Armstrong — June for the Ages

- **Claim:** "Pete Crow-Armstrong in June: 10 home runs. .867 slugging."
  - **Status:** ⚠ MEDIUM — Consistent across June 27 pipeline and June 28 research. Not independently verified from Baseball Reference. First reported June 26-27; used in prior pipeline without correction. Treat as medium.
- **Claim:** "Season line: .287/.367/.521, 17 HR, 18 SB"
  - **Status:** ⚠ MEDIUM — Consistent across multiple research passes over June 26-28. No Baseball Reference direct verification in summaries. Medium confidence.
- **Claim:** "The 24-year-old"
  - **Status:** ✅ VERIFIED — PCA born January 14, 2002. As of June 28, 2026 = 24 years, ~5.5 months. Age 24 confirmed. ✓
- **Claim:** "CARRYING this offense"
  - **Status:** ✅ VERIFIED as editorial — PCA leading offense stats (10 HR June, 17 HR season) while five starters hurt. Characterization is opinion-backed by data. ✓
- **Claim:** "All-Star caliber season. Not a debate."
  - **Status:** ✅ VERIFIED as editorial — Opinion statement. PCA has not been officially named an All-Star (season in progress). Tweet uses "caliber" not "selection." ✓
- **Compound claims:** No compound comparative claims made ("first since", "only player", etc.). No cross-reference required. ✓

---

### STORY 4: Rotation Crisis — Trade Deadline in 36 Days

- **Claim:** "Five Cubs starters on the IL"
  - **Status:** ✅ VERIFIED — Horton, Steele, Taillon, Brown, Cabrera confirmed. ✓
- **Claim:** "August 3 trade deadline"
  - **Status:** ✅ VERIFIED — MLB trade deadline August 3, 2026 is consistent with all prior pipeline references. ✓
- **Claim:** "36 days away"
  - **Status:** ✅ VERIFIED — June 28 to August 3: (June 28→30 = 2 days) + (July = 31 days) + (Aug 1→3 = 3 days) = 36 days. ✓
- **Claim:** "the farm system's best arm rehabs his elbow"
  - **Status:** ✅ VERIFIED as characterization — Jaxon Wiggins (ranked Cubs' top pitching prospect) has elbow inflammation and is rehabbing. "Farm system's best arm" is editorial but consistent with Wiggins' top-prospect status. ✓

---

### STORY 5: Wild Card Watch — Records, Gap, Path Forward

- **Claim:** "Cubs 45-38"
  - **Status:** ✅ VERIFIED — series-context.json snapshot (generated 08:30 UTC June 28) ✓
- **Claim:** "Brewers 50-30"
  - **Status:** ✅ VERIFIED — series-context.json snapshot ✓
- **Claim:** "Six and a half games back in the NL Central"
  - **Status:** ✅ VERIFIED — Calculated: GB = ((50-45)+(38-30))/2 = (5+8)/2 = 6.5 GB ✓
- **Claim:** "The division title's out of reach"
  - **Status:** ✅ VERIFIED as editorial — 6.5 GB with ~77 games remaining. Not mathematical elimination, but editorial characterization of a challenging deficit. Defensible. ✓
- **Claim:** "the Wild Card is the path"
  - **Status:** ✅ VERIFIED as editorial — Cubs are in the wild card picture at 45-38. No specific WC position claimed. ✓
- **Claim:** "rotation upgrade before August 3"
  - **Status:** ✅ VERIFIED as editorial — Consistent with 5 starters on IL. No false factual claim. ✓

---

## Summary

| Story | Claims Checked | ✅ Verified | ⚠ Medium/Plausible | ❌ Flagged |
|-------|---------------|------------|---------------------|-----------|
| 1 (Game 2 Recap) | 5 | 4 | 1 | 0 |
| 2 (Game 3 Preview) | 4 | 3 | 1 | 0 |
| 3 (PCA Feature) | 6 | 4 | 2 | 0 |
| 4 (Rotation/Deadline) | 4 | 4 | 0 | 0 |
| 5 (Wild Card) | 6 | 6 | 0 | 0 |
| **TOTAL** | **25** | **21** | **4** | **0** |

**Overall status:** No hard errors. Four medium-confidence claims (Rolison record/ERA, PCA June stats, PCA season stats, Rolison as today's starter). None of these claims are of the compound/superlative variety requiring two-source rule. All are single-entity stats at medium confidence — acceptable for social posts, flagged for awareness.

**Omitted due to LOW confidence:** "David Peterson acquired from Mets" (single source, web summary, not verified from second source — not used in any tweet).
