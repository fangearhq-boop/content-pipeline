# Cubs Research Notes — 2026-06-02

Per-story facts and sources verified before drafting.

---

## STORY 1: Cubs vs Athletics — Game 1 of 3 at Wrigley, 7:05 PM CT

**Key Facts:**
| Fact | Source | Confidence |
|------|--------|------------|
| Cubs record: 32-28 | Cubs/_data/series-context.json (game-monitor, generated 2026-06-02T08:30Z) | HIGH |
| Athletics record: 28-31 | Cubs/_data/series-context.json | HIGH |
| Wrigley Field, is_cubs_home=true | Cubs/_data/series-context.json | HIGH |
| Game 1: Tue June 2, 7:05 PM CT | Cubs/_data/series-context.json (game_date_ct "Tue 7:05 PM CT", ISO 2026-06-03T00:05Z = 7:05 PM CDT) | HIGH |
| 3-game series | Cubs/_data/series-context.json (series_length: 3) | HIGH |
| June 2 = Tuesday | Calendar check: June 1 2026 = Monday → June 2 = Tuesday ✓ | HIGH |
| Cubs' next 22 games vs under-.500 opponents | Chicago Sun-Times (May 31): "Cubs will benefit from June schedule filled with games against teams under .500" | HIGH |
| Combined 41 games under .500 | Chicago Sun-Times (same article) | MEDIUM (WebFetch blocked, from search snippet) |
| Cardinals took 2-of-3 from Cubs (May 29-31) | ESPN recaps, CBS Sports box scores (multiple) | HIGH |

**Story status check (story-history.md):** No Cubs vs Athletics series preview in recent story history (last Athletics content in spring training only). NEW STORY ✓

---

## STORY 2: Bregman 11-Game Hitting Streak

**Key Facts:**
| Fact | Source | Confidence |
|------|--------|------------|
| 11-game hitting streak entering June | ESPN (May 31 recap): "extended his hitting streak to 11 games" | HIGH |
| Hit safely in 14 of last 16 games | Chicago Sun-Times (May 30): reported as context for Bregman feature | MEDIUM (search snippet) |
| .316 average (12-for-38) over 9-game stretch | Chicago Sun-Times (May 30): "came into play with a nine-game hitting streak in which he was batting .316 (12-for-38)" — describes streak entering May 30 | MEDIUM (search snippet) |
| Bregman homered in May 31 game | ESPN recap (gameId=401815572): "Alex Bregman homered for the Cubs" | HIGH |
| Season BA: .255 | ESPN player page (as of late May) | MEDIUM |
| Cubs season record 32-28 | Series-context.json | HIGH |

**Note on streak math:** May 30 article described 9-game streak. After May 30 game (Cubs win 6-1, Bregman had hits per recap) = 10 games. After May 31 (Bregman HR) = 11 games. ✓ Streak count verified through game-by-game logic.

**No duplicate in story history:** Bregman's streak not covered as standalone story. Cardinals recap (June 1) briefly mentioned Bregman HR but no dedicated streak post. ✓

---

## STORY 3: Ben Brown — From Bullpen to De Facto Ace

**Key Facts:**
| Fact | Source | Confidence |
|------|--------|------------|
| 1.92 ERA in 17 appearances | RotoWire / CBS Sports (cited in multiple search results) | HIGH |
| Opened 2026 in bullpen | Yardbarker, Last Word on Sports, ChiCitySports | HIGH |
| 0.99 WHIP | ChiCitySports / Last Word on Sports | MEDIUM (search snippet) |
| 47 K in 44.2 IP (bullpen + starts) | ChiCitySports / Last Word on Sports | MEDIUM (search snippet) |
| 0 HR allowed in 51.2 IP | June 1 pipeline (Ben Brown story, from yesterday's research) | MEDIUM |
| 1.73 ERA in 5 starts specifically | Multiple search results | MEDIUM |
| 29 K, 7 BB in 26 IP as starter | Multiple search results | MEDIUM |
| Four starters unavailable: Horton, Steele, Boyd, Cabrera | FanGraphs Roster Resource, MLB.com injuries (June 1 update) | HIGH |

**Differentiation from June 1 content:** June 1 tweet focused on ERA + 0 HR stat as a standalone feat ("Cy Young credentials"). Today's angle is the ROLE TRANSFORMATION narrative — from bullpen arm to rotation stabilizer — and its implications. Angle is fresh. ✓

---

## STORY 4: Rotation Crisis and Trade Deadline

**Key Facts:**
| Fact | Source | Confidence |
|------|--------|------------|
| Cade Horton: right UCL revision repair with internal brace, April 16 | CBS Sports injury report, June 1 update | HIGH |
| Horton timetable: 15-16 months → ~July 2027 | Multiple sources (CBS, FTA) | HIGH |
| Justin Steele: 60-day IL (left elbow) | FanGraphs Roster Resource | HIGH |
| Matthew Boyd: Iowa rehab (4 IP, 2 ER, one more start then Chicago) | June 1 pipeline research | HIGH |
| Edward Cabrera: 15-day IL (right finger blister) | FanGraphs Roster Resource | HIGH |
| Freddy Peralta: Cubs trade target, on Mets | MLB Trade Rumors URL: "mets-trade-rumors-freddy-peralta-cubs"; Bleacher Nation May 31 | MEDIUM |
| Sonny Gray (Red Sox): Cubs target | Heavy.com: "$75M Red Sox SP as Viable Target"; The Athletic named | MEDIUM |
| Logan Webb (Giants): Cubs target | Multiple outlets | MEDIUM |
| Cubs still 4 games above .500 (32-28) | Series-context.json | HIGH |
| Craig Counsell knows Peralta from Milwaukee | Bleacher Nation, multiple sources | HIGH |
| Trade deadline approaching | Bleacher Nation: "The 2026 MLB Trade Deadline is August 3" | MEDIUM (one source; not stated in tweet) |

**Note:** Tweet references "trade deadline is coming" without specific date, to avoid low-confidence August 3 claim. ✓

---

## STORY 5: Game 1 Pre-Game Hype

**Key Facts:**
| Fact | Source | Confidence |
|------|--------|------------|
| First pitch 7:05 PM CT at Wrigley | Series-context.json | HIGH |
| Cubs 32-28 | Series-context.json | HIGH |
| Bregman 11-game hitting streak (carried from Story 2) | ESPN (May 31 recap) | HIGH |
| Favorable June schedule ("easiest stretch of the schedule") | Sun-Times article (May 31) | HIGH |

**Probable pitcher note:** Game 1 probable listed as TBD. Imanaga confirmed for Game 3 (Thu June 4) per search snippet ("Imanaga scheduled to pitch Thursday, June 4 at 7:05 PM CDT"). Game 1 likely Taillon or Rea based on rotation order (Imanaga May 29, Brown May 30, one more May 31 → Taillon most likely for June 2). NOT stating probable in tweets due to TBD status in official snapshot. ✓
