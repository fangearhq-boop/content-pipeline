# Research Notes — 2026-07-05

Per-story verified facts and source attributions.

---

### STORY 1: Cardinals 3, Cubs 0 — Game 2 Recap

- **[HIGH]** Final score: Cardinals 3, Cubs 0 — Sun-Times headline ("Cubs lose 3-0") + STL Today ("rousing shutout win") independently confirm shutout
- **[HIGH]** Shota Imanaga took the loss; record now 5-7 — multiple sources
- **[MEDIUM]** Imanaga's line: 4 2/3 IP, 4 H, 2 ER, 3 BB — from AI summary of CBS Sports gametracker
- **[MEDIUM]** Jake Leahy win (7-4), 6 K, 2 BB, 3 singles allowed — AI summary of gametracker
- **[MEDIUM]** Riley O'Brien save No. 22 — AI summary; plausible given Palencia on IL
- **[MEDIUM]** JJ Wetherholt leadoff HR on first pitch — reported in multiple search results; STL Today story confirms it
- **[LOW]** Cardinals rookie record: 4 leadoff HRs — NOT used in any tweet; flagged as single-source, not verified
- **[MEDIUM]** Cardinals won 5 of last 6 games — AI summary claim; consistent with series results (won G1 17-1, G2 3-0)
- **[HIGH]** PCA reached base 4 times (H + 2 BB + HBP) — consistent across multiple sources

Sources:
- Chicago Sun-Times: "Cubs lose 3-0 to Cardinals on foggy Wrigley night"
- STL Today: "Cardinals keep Cubs in a fog, follow JJ Wetherholt's leadoff homer to rousing shutout win"
- ESPN gametracker
- CBS Sports gametracker
- Bleed Cubbie Blue (alternate score "3-2" noted but deprioritized vs. shutout confirmation from two beat outlets)

---

### STORY 2: PCA Named Cubs' Lone All-Star — Second Straight Year

- **[HIGH]** PCA named to 2026 All-Star Game — MLB.com headline: "Pete Crow-Armstrong earns second straight All-Star nod for Cubs"; Chicago Sun-Times: "Pete Crow-Armstrong named Cubs' lone All-Star"; FOX 32 Chicago confirms
- **[HIGH]** Second consecutive All-Star selection — confirmed in headline text of multiple sources
- **[MEDIUM]** All-Star Game date: July 14 in Philadelphia — AI summary; plausible for 2026 but not independently verified with primary source
- **[MEDIUM]** 2026 season stats: .287 BA, 19 HR, 21 SB, .900 OPS — AI summary of MLB.com player page; used with MEDIUM confidence
- **[MEDIUM]** Cubs payroll approaching $230M — AI summary; not independently verified; used as narrative color only
- **[LOW]** PCA tracking to join Sosa/Sandberg as only Cubs with consecutive 20/20 — AI summary compound claim; NOT used in any tweet per two-source rule

Sources:
- MLB.com: "Pete Crow-Armstrong earns second straight All-Star nod for Cubs"
- Chicago Sun-Times: "Pete Crow-Armstrong named Cubs' lone All-Star"
- FOX 32 Chicago: "Why a 2026 MLB All-Star nod is special to Cubs CF Pete Crow-Armstrong"

---

### STORY 3: Series Finale Preview — Assad vs. Liberatore

- **[MEDIUM]** Javier Assad record: 6-1, 4.53 ERA — AI summary; cross-ref with story from Cubs Insider mentioning Assad as one of only three active starters (Imanaga, Assad, Rea)
- **[MEDIUM]** Matthew Liberatore record: 4-5, 5.33 ERA — AI summary of SportsGrid prediction piece
- **[HIGH]** Game time: 1:30 PM CT — confirmed in series-context.json (game_date_ct: "Sun 1:30 PM CT")
- **[HIGH]** Venue: Wrigley Field — confirmed in series-context.json
- **[HIGH]** Cardinals won Games 1 (17-1) and Game 2 (3-0) — established facts from this pipeline and prior pipeline

Sources:
- series-context.json (game time, venue, records)
- SportsGrid prediction piece (Liberatore ERA)
- MLB.com probable pitchers (Assad confirmed as starter)
- Cubs Insider series preview

---

### STORY 4: Taillon Begins Rehab at Iowa — Rotation Update

- **[MEDIUM]** Taillon begins rehab assignment at Triple-A Iowa on July 5 — FantasyPros news item "Jameson Taillon (hamstring) to begin rehab assignment Sunday"; Sun-Times piece confirms rehab imminent
- **[HIGH]** Injury type: hamstring strain — confirmed across multiple sources
- **[MEDIUM]** Could return before All-Star break — per Sun-Times: "Around the All-Star break is when the Cubs can expect to have Jameson Taillon back"
- **[HIGH]** Five starters lost: Steele, Brown, Horton, Cabrera, Taillon — consistent across multiple search results and prior pipeline context
- **[MEDIUM]** Matt Shaw: 10-day IL, left hand sprain, June 29; eligible July 9 if minimum stay — per Chicago Sun-Times
- **[MEDIUM]** Ethan Roberts: 15-day IL, right forearm inflammation — per MLB.com news
- **[MEDIUM]** Kevin Alcántara recalled from Iowa — per MLB.com

Sources:
- FantasyPros: "Jameson Taillon (hamstring) to begin rehab assignment Sunday"
- Chicago Sun-Times: "Jameson Taillon might make injury return before All-Star break"
- Chicago Sun-Times: "More Cubs injuries as Matt Shaw hits IL with sprained hand"
- MLB.com: "Cubs place Shaw (left hand), Roberts (right forearm) on IL"
- Bleacher Nation: "Cubs Injury Updates: Taillon, Cabrera, Palencia..."

---

### STORY 5: Wild Card Stakes — Cubs 49-40, Cardinals 47-39

- **[HIGH]** Cubs record: 49-40 — confirmed in series-context.json
- **[HIGH]** Cardinals record: 47-39 — confirmed in series-context.json
- **[HIGH]** GB calculation: ((49-47) + (39-40)) / 2 = 0.5 — mathematical derivation from HIGH-confidence records
- **[MEDIUM]** Brewers record: 54-32 — AI summary of NL Central standings search
- **[MEDIUM]** Phillies in wild card picture at ~49-39 — from WC standings search; exact current record not confirmed

Sources:
- series-context.json (Cubs 49-40, Cardinals 47-39 — HIGH confidence)
- ESPN/CBS Sports WC standings (supplemental context)

---

### STORY 6: Pre-Game Bold Take — Assad, Stop the Sweep

- **[MEDIUM]** Assad record 6-1 this season — same source as Story 3
- **[HIGH]** Cardinals going for the series sweep — established from Game 1 and 2 results
- **[HIGH]** Wild card gap: 0.5 games — same math as Story 5
- **[HIGH]** First pitch 1:30 PM CT — per series-context.json

Sources: Same as Stories 3 and 5

---

### STORY 7: Prospect Pipeline — Kelly, Dean, Farm Update

- **[MEDIUM]** Antoine Kelly: 0.84 ERA at Triple-A Iowa — per Bleacher Nation Cubs Prospects Report July 3 (AI summary): "Antoine Kelly tossed two scoreless innings... lowered his ERA to 0.84"
- **[MEDIUM]** Nick Dean: 6 IP, 4 H, 7 K, 1 BB in Knoxville's 1-0 win (July 3) — per Bleacher Nation Cubs Prospects Report
- **[MEDIUM]** Nick Dean's innings were scoreless — the final was 1-0 Smokies and no other pitcher was credited with the run, making Dean's shutout innings consistent; MEDIUM because not directly stated as "scoreless"

Sources:
- Bleacher Nation: "Cubs Prospects Report | July 3, 2026: Iowa Wins Late, Smokies Shut Out Win, More"
