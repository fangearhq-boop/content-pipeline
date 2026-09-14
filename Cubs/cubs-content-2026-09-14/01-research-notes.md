# Research Notes — 2026-09-14

---

### STORY 1: Series Preview — Cubs vs Braves, Game 1 at Wrigley

**Verified Facts**
- **[HIGH]** Cubs are 83-67 (per series-context.json, generated 2026-09-14T08:30:00Z)
- **[HIGH]** Atlanta Braves are 88-62 (per series-context.json)
- **[HIGH]** Series is 3 games, Sept 14-16, at Wrigley Field (home for Cubs)
- **[HIGH]** Game 1 first pitch: 6:40 PM CT (23:40 UTC per series-context.json game_date_iso)
- **[HIGH]** Braves lead NL East — NL East leaders per multiple search results (CBS Sports, Fox Sports, MLB.com)
- **[MEDIUM]** Probable pitchers: David Peterson (Cubs, 7-8, 5.28 ERA) vs. Reynaldo Lopez (Braves, 4-4, 4.13 ERA) — from search AI summaries, not primary-source box score; MLB.com gameday preview URL confirmed
- **[MEDIUM]** Reynaldo Lopez return from injury, had 7 ER in 4.2 IP vs. Rays on Sept 9 — multiple sources (Clutchpoints, MLB Trade Rumors) confirm Lopez activation from IL and poor return start; specific line (7 ER / 4.2 IP) from search AI summary (MEDIUM until verified from box score)
- **[MEDIUM]** 2026 H2H: Braves lead Cubs 2-1 entering series — from StatMuse search AI summary; MEDIUM

Sources:
- Cubs/_data/series-context.json (generated_at 2026-09-14T08:30:00Z) — primary source for series structure
- https://www.mlb.com/gameday/braves-vs-cubs/2026/09/14/824629/preview
- https://www.mlbtraderumors.com/2026/09/braves-to-activate-reynaldo-lopez-on-wednesday.html
- https://clutchpoints.com/mlb/atlanta-braves/braves-news-atlanta-to-give-reynaldo-lopez-another-chance-vs-cubs-after-disastrous-return-start

---

### STORY 2: Game Recap — Pirates 4, Cubs 3 (Series Finale)

**Verified Facts**
- **[HIGH]** Final score: Pirates 4, Cubs 3 — confirmed by ESPN URL title "Pirates 4-3 Cubs (Sep 13, 2026)", Yahoo Sports headline, Bleed Cubbie Blue headline, MLB.com game story URL
- **[HIGH]** Series result: Cubs won 2-1 over Pittsburgh — Games 1 and 2 wins per pipeline-status.md; Game 3 loss confirmed above
- **[MEDIUM]** Miguel Amaya HR (his 6th of the year) giving Cubs a 2-1 lead — from search AI summary of Bleed Cubbie Blue article; BCB article title confirms Amaya; "sixth" unverified from primary source
- **[MEDIUM]** Matthew Boyd started and left with runners on base — consistent across Yahoo Sports ("Boyd deserved better"), BCB summary; specific IP not confirmed
- **[MEDIUM]** Two-run single in 6th inning turned 2-1 Cubs lead to 4-2 — from search AI summary; search attributed to "Brandon Lowe" but Lowe's 2026 team not confirmed (historically Rays; possibly traded); elected NOT to name the batter in tweet to avoid potential misattribution
- **[LOW]** Aaron Civale named as Cubs reliever who allowed the rally — from AI summary; could not verify Civale is on the 2026 Cubs roster; not used in tweet

Sources:
- https://www.espn.com/mlb/boxscore/_/gameId/401816929 (Pirates 4-3 Cubs, Sep 13)
- https://sports.yahoo.com/articles/pirates-4-cubs-3-matthew-221001813.html
- https://www.bleedcubbieblue.com/chicago-cubs-scores/233184/cubs-pirates-score-matthew-boyd-miguel-amaya-mlb
- https://www.mlb.com/stories/game/824628

---

### STORY 3: Wild Card Standings — Cubs Lead WC1 by 1 Game

**Verified Facts**
- **[HIGH]** Cubs record: 83-67 (series-context.json primary source)
- **[HIGH]** Cubs hold WC1 (confirmed consistent across all standings search results entering Sept 14)
- **[HIGH]** Cardinals eliminated from contention (confirmed prior pipeline; consistent)
- **[HIGH]** Brewers won NL Central (93-56 per search)
- **[MEDIUM]** Games remaining: 12 (calculated: 83+67=150 games played; 162-150=12; assumes no doubleheaders yet unplayed; MEDIUM)
- **[MEDIUM]** Cubs lead Phillies by ~1 game for WC1 — from NL WC search results; Phillies exact record not confirmed after Sept 13 games; estimated ~82-67
- **[MEDIUM]** Magic number to clinch: ~9 — from cubsmagicnumber.net (most recent page title "The Chicago Cubs Magic Number: 9"); MEDIUM, not cross-referenced

Sources:
- Cubs/_data/series-context.json
- https://www.cbssports.com/mlb/news/2026-mlb-playoff-picture-standings-bracket/
- https://www.cubsmagicnumber.net/
- https://sportsbrackets.net/2026/05/23/2026-mlb-standings/

---

### STORY 4: PCA 40-40 Watch — 41 HR / 36 SB

**Verified Facts**
- **[HIGH]** PCA: 41 HR / 36 SB entering Sept 14 — consistent across pipeline-status.md (Sept 13 update), CBS Sports search result, multiple search summaries
- **[HIGH]** No Cub has ever achieved 40-40 in a season — consistent claim in pipeline since Sept 9; no conflicting source found
- **[MEDIUM]** Six players in MLB history have done 40-40 — from CBS Sports search result quote ("The 40-40 club has six members in all of MLB history"); consistent with prior pipeline; MEDIUM because specific membership list not verified from primary source for this run
- **[MEDIUM]** 12 games remaining — calculated (150 played, 162-150=12); MEDIUM
- **[MEDIUM]** PCA season stats (context): .948 OPS, 111 runs, 98 RBI — from CBS Sports search result; not cross-referenced

Sources:
- Cubs/pipeline-status.md (Sept 13 run update, PCA 41 HR / 36 SB)
- https://www.cbssports.com/mlb/players/26615365/pete-crow-armstrong/splits/
- https://www.si.com/mlb/cubs/where-pete-crow-armstrong-2026-season-ranks-among-best-in-cubs-history

---

### STORY 5: Braves Stakes — Lopez's Last Start

**Verified Facts**
- **[HIGH]** Braves are NL East leaders (88-62) — consistent across all standings search results
- **[MEDIUM]** Reynaldo Lopez's last start (Sept 9 vs. Rays): 7 earned runs in 4.2 innings — from Clutchpoints article and search AI summary; consistent across two sources (Clutchpoints + Field Level Media); MEDIUM because specific pitching line from AI summary
- **[MEDIUM]** Lopez returned from IL — MLB Trade Rumors article confirms "Braves To Activate Reynaldo Lopez On Wednesday"; consistent
- **[MEDIUM]** Braves 7-3 in last 10 games — from thedatastreak.com search summary; MEDIUM (single source AI summary)
- **[MEDIUM]** Possible NLDS matchup between Cubs and Braves in October — from CBS Sports playoff picture; ESPN playoff tracker; multiple consistent sources confirm Braves as NL East division winners

Sources:
- https://clutchpoints.com/mlb/atlanta-braves/braves-news-atlanta-to-give-reynaldo-lopez-another-chance-vs-cubs-after-disastrous-return-start
- https://fieldlevelmedia.com/mlb/braves-reynaldo-lopez-likely-to-return-for-clash-vs-rays/
- https://www.mlbtraderumors.com/2026/09/braves-to-activate-reynaldo-lopez-on-wednesday.html
- https://www.cbssports.com/mlb/news/2026-mlb-playoff-picture-standings-bracket/

---

### STORY 6: Swanson Return — Closing In

**Verified Facts**
- **[HIGH]** Dansby Swanson placed on IL Aug 17 with Grade 2 left oblique strain — consistent across Yahoo Sports, Clutchpoints, Athlonsports, Cubs pipeline-status.md
- **[HIGH]** Swanson has not played since Aug 16 — confirmed per search ("hasn't played since August 16") and pipeline-status.md
- **[MEDIUM]** 22 games missed — from Yahoo Sports search summary; consistent with pipeline-status.md note
- **[MEDIUM]** Nearing return; Cubs targeting this week — from multiple search results (clutchpoints.com, sportsmockery.com, yardbarker.com confirm "near-term return"); specific Cincinnati trip target (Sept 18) from pipeline-status.md

Sources:
- Cubs/pipeline-status.md (Sept 13 run: "targeting activation Sept 18 in Cincinnati")
- https://sports.yahoo.com/articles/cubs-news-dansby-swanson-injury-031459522.html
- https://clutchpoints.com/mlb/chicago-cubs/cubs-news-dansby-swanson-injury-timeline-return-near
- https://athlonsports.com/mlb/chicago-cubs/cubs-dansby-swanson-injury-rehab-assignment-update

---

### STORY 7: Pre-Game Hype — Wrigley Tonight

**Verified Facts**
- **[MEDIUM]** David Peterson: 7-8, 5.28 ERA — from search AI summary (CBS Sports search; FanGraphs link); MEDIUM (specific W-L and ERA from summary, not primary source lookup this run)
- **[HIGH]** Game tonight at Wrigley, 6:40 PM CT — confirmed by series-context.json
- **[MEDIUM]** Lopez coming off worst start of season — referenced across multiple sources; "7 ER in 4.2 IP" claim MEDIUM per Story 5 notes

Sources:
- Cubs/_data/series-context.json
- https://www.mlb.com/player/david-peterson-656849
- Reynaldo Lopez sources (see Story 5)
