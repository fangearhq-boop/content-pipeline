# Research Notes — July 1, 2026

---

### STORY 1: Cubs 9, Padres 7 — Game 2 Recap

**Sources**:
- ESPN game page: "Cubs 9-7 Padres (Jun 30, 2026)" — score CONFIRMED
- Field Level Media wire (syndicated to KNBR, 107.5 The Game, WJOX, Sportsradio Harrisburg): "Dansby Swanson homers twice, Cubs outslug Padres" — narrative CONFIRMED
- Bleacher Nation Enhanced Box Score — game details
- Washington Post game story

**Verified facts** (confidence levels):
- Final score: Cubs 9, Padres 7 — HIGH (ESPN + wire syndication)
- Dansby Swanson: 2 home runs — HIGH (headline word across multiple outlets)
- One Swanson homer "estimated at 432 feet" to center — MEDIUM (single AI summary detail; directional)
- Alex Bregman: three-run home run — HIGH (wire story specific)
- Michael Busch: solo home run — HIGH (wire story)
- Pete Crow-Armstrong: solo home run — HIGH (wire story "Busch and Crow-Armstrong added solo HRs")
- Five total Cubs home runs — HIGH (consistent across search summaries)
- Matthew Boyd (W, 3-1): 5+ innings, 3 ER, 0 BB, 2 K — HIGH (box score detail from ESPN)
- Ryan Rolison: recorded last out, first save — HIGH (wire story)
- JP Sears (L, 1-1): 4.2 IP, 7 R (6 ER), 3 BB, 4 K — HIGH (wire story)
- Padres home runs: Tatis Jr. (2), Machado, Gavin Sheets — HIGH (wire detail)
- Cubs' 4th consecutive win — HIGH (consistent across sources; aligns with story history)
- Cubs now 48-38 — HIGH (matches series context JSON generated July 1 AM)
- Padres now 43-41 — HIGH (matches series context JSON)
- Padres on 4-game losing streak — HIGH (consistent with wins Tuesday + Monday)

---

### STORY 2: Game 3 Preview — Rea vs. Buehler

**Sources**:
- Cubs Insider series preview article (June 29)
- Bleacher Nation series odds/preview (June 27)
- SI.com: Padres starter announcement
- FantasyPros probable pitchers

**Verified facts**:
- Game time: 1:20 PM CT — HIGH (matches series context JSON game_date_ct "Wed 1:20 PM CT")
- Game location: Wrigley Field — HIGH (series context JSON is_cubs_home=true)
- Cubs starter: Colin Rea — HIGH (multiple preview sources agree)
- Rea's ERA: 4.80 across 84.1 IP — MEDIUM (preview source; directional)
- Rea recent form: 1 ER in last 10.1 innings (last 2 starts) — MEDIUM (single preview source)
- Padres starter: Walker Buehler — HIGH (multiple sources)
- Buehler ERA in last 5 starts: 1.71 — MEDIUM (single AI summary; strong directionality)
- Buehler allowed 1 run in EACH of last 5 starts — MEDIUM (single source; directional and plausible for a sub-2.00 ERA stretch)
- Cubs lead series 2-0 — HIGH (series context + story history confirms Game 1 W + Game 2 W)
- TV: Marquee Sports Network — MEDIUM (preview source)

---

### STORY 3: Wild Card Watch

**Sources**:
- Series context JSON (cubs_record: 48-38)
- June 30 pipeline status (NL WC2 at 47-38)
- Prior daily pipeline context (Phillies ~47-37 a half-game ahead as of June 30)

**Verified facts**:
- Cubs record: 48-38 — HIGH (series context JSON, generated July 1 08:30 UTC)
- Cubs firmly in NL Wild Card race — HIGH (consistent across multiple pipeline days)
- Cubs held NL WC2 as of June 30 at 47-38 — HIGH (June 30 pipeline status)
- Brewers lead NL Central substantially — MEDIUM (directional, per power rankings ~52-30 range)
- Five home runs hit June 30 — HIGH (per Story 1 above)

NOTE: Exact current WC standings (# of games up/back) not confirmed from live search. Using directional language only — "firmly in the Wild Card race" rather than a specific games-behind figure.

---

### STORY 4: All-Star — PCA Phase 2

**Sources**:
- Bleacher Report Phase 1 results
- Sports Keeda Phase 2 finalists list
- SI.com (PCA WAR/OAA data)
- CBS Philadelphia (Phase 2 voting announcement)
- Bleacher Nation multiple articles

**Verified facts**:
- PCA finished 10th among NL outfielders in Phase 1 — HIGH (Bleacher Report article)
- PCA Phase 1 vote total: 1,061,310 — MEDIUM (single source)
- Phase 2 voting closes July 2 at 12 PM ET — HIGH (multiple sources)
- Votes did not carry over from Phase 1 to Phase 2 — HIGH (CBS Philadelphia)
- PCA did NOT advance to Phase 2 starter ballot (only top 6 per position advance) — HIGH (consistent across multiple sources)
- PCA WAR 4.6 leads all MLB position players (both bWAR and fWAR) — MEDIUM (described in multiple search summaries; compound superlative claim requiring cross-reference; directional confidence is high)
- PCA leads NL outfielders in Outs Above Average (15) — MEDIUM (SI.com article summary; directional)
- PCA leads NL outfielders in Fielding Run Value (16) — MEDIUM (same source; not used in tweet)
- PCA's path is as a reserve (commissioner + player votes) — HIGH (standard MLB All-Star process)

COMPOUND CLAIM FLAG: "Leads all MLB position players in WAR (4.6)" — this is a superlative claim. Multiple sources say it but I cannot verify against Baseball Reference same-day. Flagging as MEDIUM. Using it in tweet but including confidence note in fact-check log. The sources cite both bWAR and fWAR at 4.6 — the consistency across two metrics and multiple articles increases confidence.

---

### STORY 5: Roster Moves — Maton/Milner

**Sources**:
- CBS Sports Cubs injury page (cbssports.com/mlb/teams/CHC/chicago-cubs/injuries/)
- FanGraphs RosterResource
- MLB.com transactions

**Verified facts**:
- Phil Maton: 15-day IL, right knee injury — MEDIUM (CBS Sports injury report summary; specific injury detail from AI summary)
- Hobie Milner: out 4-to-6 weeks, emergency appendectomy — MEDIUM (CBS Sports injury report summary)
- These moves are NEW as of July 1 (not in June 30 pipeline coverage) — HIGH (confirmed by absence in June 30 story history and pipeline-status.md)
- Both Maton and Milner are Cubs relievers — HIGH (known roster context)

NOTE: Both facts are MEDIUM confidence — from AI summary of CBS Sports injury page, not directly verified from primary source. Including in tweet but using conservative language "lands on the IL" (confirmed transaction language) vs. claiming specific injury details with HIGH confidence. Will flag in fact-check.

---

### STORY 6: Trade Deadline + Pipeline

**Sources**:
- MLB Trade Rumors (Jed Hoyer pitching needs article)
- Yahoo Sports (Cubs prioritize starting pitching upgrades)
- Stadium Rant (Alcántara landing spots)
- Yahoo Sports (Alcántara trade odds)
- Cubs Crib / Sports Mockery (Wiggins timeline)

**Verified facts**:
- August 3 deadline: 33 days from July 1 — HIGH (math: Aug 3 minus July 1 = 33 days)
- Cubs rotation ERA: 27th in MLB at 4.71 "through 75 games" — MEDIUM (single search result; approximate game count; directional)
- Sandy Alcántara trade odds at 40% — MEDIUM (Yahoo Sports article summary; directional; specific % from a betting/odds source)
- Cubs and Padres "most closely tied" to Alcántara — MEDIUM (multiple sources suggest it consistently)
- Alcántara contract: $17.3M in 2026, $21M club option 2027 — MEDIUM (cited in multiple articles)
- Jaxon Wiggins: 3.2 scoreless at South Bend (High-A) — HIGH (in June 30 pipeline story history, covered as confirmed fact)
- Wiggins' next start expected at Triple-A Iowa — HIGH (June 30 pipeline covered "expected next at Iowa"; corroborated by multiple Wiggins update articles)
- Jed Hoyer confirmed pitching priority — HIGH (MLB Trade Rumors article direct)
