# Research Notes — Cubs June 14, 2026

Per-story facts, source confidence, and freshness verification.

---

## STORY 1: Cubs 6, Giants 1 — PCA First-Pitch HR, Brown Wins Third (Game Recap)

**Source freshness:** <24h (game played June 13, 2026)
**Source confidence:** HIGH — multiple independent wire reports confirm

**Key facts confirmed:**
- Final score: Cubs 6, Giants 1 ✓ (AP wire, multiple outlets)
- PCA homered on first pitch ✓ (AP, TSN, ABC7, beloitdailynews, MLB.com video)
- PCA's HR = 12th of season ✓ (AP report: "connected off Trevor McDonald for his 12th home run")
- Losing pitcher: Trevor McDonald (2-4) ✓ (AP report)
- Ben Brown: W (3-2), 5 IP, 7 H, 1 R ✓ (multiple sources)
- Ian Happ solo HR in 5th ✓ (AP report)
- Pedro Ramírez solo HR in 5th ✓ (AP report)
- Cubs now 37-34 ✓ (series-context.json, generated 8:30 AM today)
- Giants now 28-43 ✓ (series-context.json)

**Flagged for fact-check:**
- Ben Brown zero HRs allowed in starts — unconfirmed after June 13 start (7 H, 1 R with no specific HR mention, but not explicitly confirmed HR-free). FLAG: Do not claim in tweets without verification or use hedge language.
- Series game numbering: Game 2 of 3 confirmed (series-context.json: "same opponent as yesterday, mid-series")

---

## STORY 2: Game 3 Preview — Colin Rea vs Logan Webb, 2:10 PM CT

**Source freshness:** Published June 12-14 previews from cubsinsider.com, Bleed Cubbie Blue, MLB.com, Baseball-Reference
**Source confidence:** HIGH for pitching matchup facts; MEDIUM for Webb injury return details

**Key facts confirmed:**
- First pitch: 2:10 PM CT ✓ (series-context.json: game_date_ct = "Sun 2:10 PM CT"; Baseball-Reference preview)
- Venue: Oracle Park, San Francisco ✓ (series-context.json)
- Cubs SP: Colin Rea ✓ (multiple sources)
- Rea record/ERA: 5-4, 5.19 ERA ✓ (actionnetwork.com odds preview)
- Giants SP: Logan Webb ✓ (multiple sources)
- Webb record/ERA: 3-4, 3.88 ERA ✓ (actionnetwork.com)
- TV: ABC, ESPN App ✓ (MLB.com Cubs news article title confirmed national TV)
- Cubs series lead: 2-0 ✓ (6-1 win June 13, 5-1 win June 12)

**Flagged for fact-check:**
- Webb returning from right knee bursitis — one source (cubsinsider.com search result) — MEDIUM confidence. Do not cite specific injury if using "returning to form" framing.
- Win probability: 53% (actionnetwork.com) — betting model, LOW-MEDIUM; OK to cite as "slight edge"

---

## STORY 3: Bold Take — Cubs on the Sweep

**Source freshness:** N/A (opinion piece)
**Source confidence:** Facts underlying it are HIGH (Cubs 2-0, Giants 28-43)

**Key facts:**
- Cubs lead series 2-0 ✓
- Giants record 28-43 ✓ (series-context.json)
- Cubs record 37-34 ✓ (series-context.json)
- A sweep today would mean Cubs take all 3 from a team 9+ games under .500

---

## STORY 4: Standings / Wild Card Analysis

**Source freshness:** MEDIUM — standings data from ~June 10-11 (multiple searches)
**Source confidence:** MEDIUM — no live standings page accessible today

**Key facts available:**
- Cubs: 37-34 ✓ (HIGH — series-context.json, this morning)
- Brewers: ~41-25 per Great Bend Tribune/deepmetricanalytics from ~June 10; actual Brewers record by June 14 may be slightly different (~43-27 estimated). Using "~41-25 as of recent data" is the correct framing.
- Cubs games behind Brewers: ~7.5 GB (calculated from 41-25 vs 35-34 baseline; with Cubs at 37-34 and Brewers possibly 43-27 = 7.5 GB as well — roughly consistent)
- Cardinals: ~37-29 per one search result (~June 10 data)
- Cubs are over .500 — wild card is the story

**Tweet framing:** Use "Cubs 37-34" (confirmed) and note Brewers lead comfortably; wild card path. Do NOT claim an exact Brewers record or GB figure as current without hedging.

---

## STORY 5: Trade Deadline Countdown

**Source freshness:** Multiple pieces from June 2026 (fresh)
**Source confidence:** HIGH on deadline date; MEDIUM on specific rumors

**Key facts confirmed:**
- Deadline: August 3, 2026 ✓ (mlb.com)
- Days to deadline from June 14: 50 days ✓ (calendar math: June 14 → August 3 = 50 days)
- Hoyer confirmed Cubs looking for rotation help ✓ (MLB.com headline)
- Horton: Tommy John, out through ~2027 ✓
- Steele: 60-day IL, left elbow ✓
- Taillon: 15-day IL, out through All-Star break ✓
- Boyd: on IL (status uncertain mid-June) ✓
- Angels cited as possible trade partner — LOW confidence (single outlet)

**Tweet framing:** Lead with rotation crisis facts (confirmed) + deadline countdown. No specific trade rumors unless at least two sources confirm.

---

## STORY 6: Prospect Pipeline — Ayers & Hartshorn at Knoxville

**Source freshness:** June 11-12 Bleacher Nation reports (<72h)
**Source confidence:** MEDIUM (fan/beat blog, not official MiLB)

**Key facts:**
- Owen Ayers (Tennessee Smokies/Knoxville): hitting hot streak in June — multiple 2-hit games per Bleacher Nation June 11 and 12 reports
- Josiah Hartshorn (Iowa/Knoxville): HR and multi-hit games, also mentioned in same reports
- Jefferson Rojas (Knoxville): back-to-back 3-hit games per North Side Baseball
- Will Sanders (Iowa): 5 scoreless IP on return (Bleed Cubbie Blue, June 13 minor league wrap)

**Flagged:** Hartshorn's exact affiliate (Iowa or Knoxville) unclear from search results. The Bleacher Nation reports mention both "Ayers & Hartshorn" together in Knoxville-themed write-ups. Do NOT claim a specific affiliate for Hartshorn without more confirmation. Use "in the Cubs system" or "in Knoxville" if the report is labeled Smokies.

---

## Sources List

1. AP Wire (multiple local affiliates) — Cubs 6, Giants 1 game recap
2. TSN.ca — PCA first-pitch HR article
3. Baseball-Reference preview page (SFN202606140.shtml) — June 14 game details
4. cubsinsider.com — Cubs-Giants series preview (June 12-14)
5. actionnetwork.com — Cubs vs Giants betting odds, team records
6. Bleed Cubbie Blue — Cubs vs Giants game threads and minor league wraps
7. Bleacher Nation — Cubs prospect reports June 11-12
8. MLB.com — Cubs news, Ben Brown all-star piece, trade deadline piece
9. Chicago Sun-Times — Ben Brown all-star article (June 4, 2026)
10. FanGraphs RosterResource — Injury updates
11. Great Bend Tribune / deepmetricanalytics — MLB standings 2026
12. chicitysports.com — Cubs trade deadline direction article
13. North Side Baseball — Cubs minor league report
14. series-context.json (generated 2026-06-14T08:30:00 UTC) — today's game data, records
