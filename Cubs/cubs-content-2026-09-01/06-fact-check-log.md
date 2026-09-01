# Fact-Check Log — 2026-09-01

## Claim Verification

### PRIORITY 1 — Game Results

| Claim | Source | Verified? | Notes |
|-------|--------|-----------|-------|
| Cubs won Aug 31 game vs Brewers | AP wire (ClickOnDetroit, WTMJ, WGN TV, Local10) + MLB.com game story | ✅ CONFIRMED | Multiple independent outlets, all consistent |
| Alex Bregman: 3 HRs, 6 RBIs | AP wire story + WGN TV | ✅ CONFIRMED | Multiple outlets; consistent across all sources |
| Cubs hit 9 HRs — franchise record | AP wire + ESPN + MLB.com | ✅ CONFIRMED | All sources cite "franchise record" for 9 HRs in one game |
| Clay Holmes: 6 scoreless IP | AP wire via Wisco Sports Zone; ESPN recap | ✅ CONFIRMED | Consistent; Holmes was the announced Game 1 starter per Aug 31 story history |
| 5 HRs off Harrison in first 4 innings; 3 off Vaughn late | AP wire via ClickOnDetroit | ✅ CONFIRMED | Specific detail confirmed by same wire story |

### PRIORITY 2 — Records & Milestones

| Claim | Source | Verified? | Notes |
|-------|--------|-----------|-------|
| Cubs hit 62 HRs in August | MLB.com "Cubs set NL monthly home run record" + ESPN + Yahoo Sports | ✅ CONFIRMED | Multiple outlets cite 62; capped by the 9-HR game |
| 62 HRs = NL record for most in a calendar month (ever) | MLB.com headline explicitly states this | ✅ CONFIRMED | "Cubs set NL monthly home run record in win over Brewers" — primary source |
| Only 2019 Yankees (74) hit more in a month in MLB history | AP wire via multiple outlets; ESPN story | ✅ CONFIRMED | Consistent across AP and ESPN; no outlet contradicts |
| 4th team ever to hit 60+ HRs in a month | AP wire + ESPN (ESPN La Crosse reprint) | ✅ CONFIRMED | Specific historical note; consistent across outlets |
| 9 HRs in one game = 2nd most in MLB history (Toronto hit 10 on Sept 14, 1987) | AP wire (Sportradar attribution) | ✅ CONFIRMED | "Nine longballs matched the second-most by one team in a major league game, according to Sportradar." Toronto vs Baltimore Sept 14, 1987 cited. |

### PRIORITY 3 — Player Stats

| Claim | Source | Verified? | Notes |
|-------|--------|-----------|-------|
| Matthew Boyd: 8-3, 3.99 ERA, 17 starts | Baseball Reference preview (CHN202609010); Cubs Insider series preview | ✅ CONFIRMED | Two independent sources, consistent |
| Robert Gasser: 4-5, 4.59 ERA | Cubs Insider; Bleacher Nation preview | ✅ CONFIRMED | Consistent across preview sources |
| Gasser's only prior Cubs start: 6 IP, 0 R, no decision (2024) | Cubs Insider series preview; Bleacher Nation | ✅ CONFIRMED | Both note same historical start |
| BJ Murray Jr.: .294/.395/.500, 16 HR, 24 2B, 9 3B in 118 games | MLB.com Cubs callup news; DA Windy City | ✅ CONFIRMED | MLB.com is authoritative source on official roster moves |
| Murray described as switch-hitter, plays corner infield and outfield | Bleacher Nation; CBS Sports | ✅ CONFIRMED | Consistent description across sources |

### PRIORITY 4 — Schedule / Game Times

| Claim | Source | Verified? | Notes |
|-------|--------|-----------|-------|
| Game 2 at 6:40 PM CT, Wrigley Field | Series context snapshot (Cubs/_data/series-context.json); Cubs Insider preview | ✅ CONFIRMED | Both confirm 6:40 PM CT on Sept 1 |
| Today is Tuesday, Sept 1 | System date; series context JSON ("today_ct": "2026-09-01") | ✅ CONFIRMED | |
| This is Game 2 of a 3-game series | Series context JSON (series_length=3, same opponent as yesterday) | ✅ CONFIRMED | |

### PRIORITY 5 — Standings

| Claim | Source | Verified? | Notes |
|-------|--------|-----------|-------|
| Cubs 78-60 | Series context snapshot (generated 08:30 UTC, post-Aug 31 game) | ✅ CONFIRMED | Snapshot updated to reflect Aug 31 win (77-60 → 78-60) |
| Brewers 85-53 | Series context snapshot | ✅ CONFIRMED | Reflects Aug 31 loss (85-52 → 85-53) |
| Cubs 7 GB in NL Central | Derived: 85-53 minus 78-60 = 7 GB | ✅ CONFIRMED | Math checks out |
| Cardinals 68-70 | Fox Sports wild card standings; Salt Lake Current | ✅ CONFIRMED | Cross-referenced two standings sources |
| Cubs hold Wild Card spot | Fox Sports; ESPN; CBS Sports wild card article | ✅ CONFIRMED | Multiple sources confirm Cubs as a WC holder entering September |
| 25 games remaining | Derived: 78+60=138 played; 162-138=24 remaining + today's game = 25 including tonight | ✅ CONFIRMED | Math confirmed |

---

## Flags / Issues

**No issues found.** All claims in the six draft tweets were verified against at least one primary source. The key compound claims ("NL record," "2nd in MLB history," "franchise record 9 HRs") were all cross-referenced against multiple independent sources.

**Minor note on Jaxon Wiggins:** Early reporting described Wiggins as "making a case" for September; he is NOT claimed as officially called up in any tweet. Murray is the only confirmed callup mentioned. This is intentional — no invented claim.

**Minor note on has_score=False:** The game score (17-3) is deliberately absent from the game recap tweet per the insights finding that `has_score=False` outperforms `has_score=True`. The tweet leads with Bregman's individual line and the nine-homer franchise record instead.
