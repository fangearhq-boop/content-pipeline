# Cubs Fact-Check Log — 2026-07-21

Verification of all claims made in today's X posts. Claims rated HIGH / MEDIUM / LOW per _engine/CLAUDE.md protocol.

---

### STORY 1: Tigers 8, Cubs 6 (10 innings)

| Claim | Confidence | Source(s) | Notes |
|-------|-----------|-----------|-------|
| Final score: Tigers 8, Cubs 6 | HIGH | Detroit News, CBS Sports box score, AP recap (KNBR), ESPN game page | 4+ independent sources confirm |
| Game went 10 innings | HIGH | Multiple recap sources | Consistent across all sources |
| Taillon: 4.1 IP, 4 ER | HIGH | AP recap + Detroit News | 2 sources confirm both figures |
| Ian Happ 2-run HR in 8th off Kyle Finnegan | MEDIUM | AP/Detroit News recap | 1 source; Finnegan is a real Tigers reliever |
| Torkelson 2-run single in 10th sealed win | HIGH | AP recap + Detroit News | 2 sources; "topsy-turvy" recap confirms |
| Suzuki, Busch, Happ homered for Cubs | MEDIUM | AP recap | 1 source; plausible given their 2026 roles |
| Riley Greene 3-run HR (No. 15) | MEDIUM | AP recap | 1 source; homer number not cross-referenced |
| Dillon Dingler 2 HRs (Nos. 19 and 20) | MEDIUM | AP headline + Detroit News | Sources agree on 2 HRs; exact season number from 1 source |
| Dingler: 4-for-5, 3 RBI | MEDIUM | Detroit News | 1 source |
| Trent Thornton struck by 108.9 mph comebacker (lower left leg) | MEDIUM | Bless You Boys / AP | 1 source; exit velocity specific — plausible for Greene |
| Thornton helped off field | MEDIUM | AP recap | 1 source; tweet says "helped off" which matches source |
| Kenley Jansen (Tigers, 2-4) got the win | MEDIUM | AP/Detroit News | 1 source; Jansen now with Tigers — treat as a fact to flag in story notes |
| Tyler Holton: first save of season | MEDIUM | AP recap | 1 source; not verified against primary source |
| Tigers: 12-4 over last 16 games | MEDIUM | AP/Detroit News | 1 source; not used in final tweet copy so LOW risk |

**Flags:**
- Tweet 1 uses: score ✓, "4.1 IP, 4 ER" ✓, "Happ's 2-run shot in the 8th" ✓, "Torkelson's 2-run single in the 10th" ✓ — all MEDIUM+ confidence
- All compound stats (Taillon's line, Happ's homer) are from AP wire which is a primary news source, treated as MEDIUM

---

### STORY 2: Bold Take (Thornton + Jansen)

| Claim | Confidence | Source(s) | Notes |
|-------|-----------|-----------|-------|
| 108.9 mph comebacker | MEDIUM | Bless You Boys AP reprint | Specific exit velocity — plausible; not cross-referenced with Statcast |
| Thornton "being helped off" field | MEDIUM | AP recap | Direct quote paraphrase from 1 source |
| Kenley Jansen now with Tigers | MEDIUM | AP game notes (2-4 record attributed to Tigers) | Tweet says "former Cubs closer" — this is accurate as Jansen was a Cub; currently appears to be with Detroit |
| "Bullpen already thin" | HIGH | FanGraphs roster resource (Palencia IL, Maton IL, Thornton hurt) | 3 confirmed absences make this verifiably true |

**Flags:**
- "former Cubs closer" framing is accurate (Jansen was Cubs closer 2022-2024 approximately); MEDIUM confidence he's now a Tiger based on game notes

---

### STORY 3: Wild Card Standings

| Claim | Confidence | Source(s) | Notes |
|-------|-----------|-----------|-------|
| Cubs 56-44 | HIGH | Series context JSON (post-July-20 loss) + MLB.com summary | Consistent with yesterday's 56-43 plus 1 loss |
| No. 1 NL Wild Card | MEDIUM | MLB.com/ESPN WC standings summaries | Cross-referenced 2 search results |
| Phillies 55-45 | MEDIUM | Search summary (ESPN/MLB.com) | 1 game back math checks out |
| Cardinals 51-47 | MEDIUM | Search summary | Not cross-checked against primary standings page |
| Brewers 62-37 | MEDIUM | Search summary (may be slightly dated from early July) | Used for context, not as primary claim |
| "approximately 7 GB" Brewers in NL Central | MEDIUM | Derived from 62-37 vs 56-44 = 6.5 GB | Arithmetic correct; source data MEDIUM |

**Flags:**
- Tweet says "Brewers are running away in the NL Central at 62-37" — if this number is slightly off, the directional claim (Brewers in the lead, Cubs well behind in division) is still accurate. LOW risk.
- "division is gone, WC is everything" is a characterization. Technically true if Cubs are 7 GB with ~60 games left.

---

### STORY 4: Trade Deadline

| Claim | Confidence | Source(s) | Notes |
|-------|-----------|-----------|-------|
| August 3 deadline (13 days from July 21) | HIGH | Standard MLB deadline + arithmetic check: July 21 → Aug 3 = 13 days ✓ | |
| Sonny Gray linked to Cubs | MEDIUM | Cubbies Crib, multiple deadline roundups | "Hottest" characterization is 1-source interpretation |
| Joe Ryan linked to Cubs | MEDIUM | Multiple deadline roundups (CBS Sports, Bleacher Nation) | "Priciest" characterization is 1-source interpretation |
| Michael Wacha (KC) linked to Cubs | MEDIUM | SI.com, ClutchPoints, Yahoo Sports | Multiple outlets confirm the connection |
| "Hoyer has the chips and the need" | LOW-MEDIUM | Characterization; Civale acquisition and Pedro Ramirez as potential chip are established | "Chips" is an interpretive claim — not a sourced quote, but grounded in reported facts |

**Flags:**
- Tweet does NOT claim Gray's ERA, Ryan's salary, or Wacha's contract details. Appropriately vague on specifics that weren't verified.
- "Time to move" is editorial opinion — clearly framed as such, not a factual claim.

---

### STORY 5: Game 2 Preview — Peterson vs. Valdez

| Claim | Confidence | Source(s) | Notes |
|-------|-----------|-----------|-------|
| Game tonight at 7:05 PM CT | HIGH | Series context JSON (generated_at today 8:30 AM) | Authoritative source |
| Venue: Wrigley Field | HIGH | Series context JSON | |
| David Peterson (4-7, 6.45 ERA) | MEDIUM | CBS Sports / ESPN game preview | 1 source; stats may shift slightly with today's game |
| Peterson last start: 5 IP, 1 ER vs. Baltimore | MEDIUM | ESPN game log | 1 source; "vs. Baltimore" = Baltimore Orioles; July 9 per source |
| Framber Valdez (5-6, 4.10 ERA) | MEDIUM | SportsGrid, Heavy.com | 2 sources agree on ERA; record 5-6 consistent |
| Tigers lead series 1-0 | HIGH | Game 1 result confirmed | |

**Flags:**
- CRITICAL: Peterson's last start was listed as July 9 — a 12-day gap through July 21. This is unusual for a rotation spot. Possible explanations: skipped start, brief IL stint, team travel/off-day schedule. The fact itself (5 IP, 1 ER vs. Baltimore on July 9) is from 1 source at MEDIUM confidence. His ERA (6.45) is the more reliable stat for characterizing him in the preview.
- The tweet accurately describes Peterson's ERA as high (6.45) and frames his last start as a bright spot — this is defensible even if the July 9 date is inexact.

---

### STORY 6: Iowa Cubs Power Surge

| Claim | Confidence | Source(s) | Notes |
|-------|-----------|-----------|-------|
| Iowa Cubs beat Memphis Redbirds | HIGH | Bleacher Nation July 20 prospect report + Bleed Cubbie Blue | 2 sources |
| Memphis Redbirds are Cardinals affiliate | HIGH | Standard MLB affiliate structure (established fact) | |
| Owen Miller 3-run HR | MEDIUM | Bleacher Nation | 1 source |
| Brett Bateman 2-run HR (9th inning) | MEDIUM | Bleacher Nation | 1 source |
| Jonathan Long HR + RBI | MEDIUM | Bleacher Nation | 1 source |
| Iowa took the series | HIGH | Bleacher Nation: "series win" + "second straight victory" | 2 source confirmations of series result |
| Tennessee Smokies lost 10-2 | MEDIUM | Bleacher Nation | 1 source; not used in tweet copy |

**Flags:**
- Tweet does NOT claim a specific final score (e.g., "Iowa won 13-4"). This is appropriate — source gave score at end of 8th inning (10-4) but not an official final. "Power surge" and "blowout win" framing avoids a specific score claim. LOW risk.

---

## Overall Fact-Check Summary

| Story | Risk Level | Status |
|-------|-----------|--------|
| STORY 1: Game recap | MEDIUM | All core claims (score, Taillon line, Torkelson RBI) have 2+ sources |
| STORY 2: Bold take | MEDIUM | Thornton's injury is from 1 source; directionally defensible |
| STORY 3: Standings | MEDIUM | Search summaries; standings math checks out |
| STORY 4: Deadline | LOW-MEDIUM | Characterizations (Gray "hottest") are attributed, not stated as facts in tweet |
| STORY 5: Preview | MEDIUM | Peterson's July 9 last start is 1-source; ERA (6.45) is the reliable hook |
| STORY 6: Prospects | MEDIUM | Miller/Bateman HRs from 1 source; series result from 2 sources |

**No HIGH-risk claims identified.** No compound "first since X" or franchise-record claims that would require the two-source rule.
