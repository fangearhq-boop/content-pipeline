# Chicago Cubs Fan HQ — Research Playbook

How to research, tier, and fact-check Cubs/MLB stories for daily content.

## HARD RULE — First pitch and ballpark

Game start times and ballparks come from MLB's official schedule, not from a national listing with "CT" typed on the end.

1. Before writing a first pitch or a ballpark, run:

```bash
python Cubs/mlb_schedule.py --date YYYY-MM-DD
```

2. Paste that output into `00-research.md` and `01-research-notes.md`.
3. Copy the clock and the venue name from that output into the brief, the story files, and the posts. The clock is already Central. It is the Stats API `gameDate` (UTC) converted with the `America/Chicago` time zone, so daylight time and standard time are both handled. Do not subtract 5 or 6 hours by hand.
4. CBS, Yahoo, ESPN, Fox, and TV listings are not a source for a first pitch or a ballpark. They often print an Eastern clock with no zone. Two of them agreeing does not make the clock Central.

The same rule covers the park. A best-of-five flips parks after Game 2. Use `venue.name` on that date's game. Do not reuse the Game 1 park for Game 3 because a preview or a local listing still names it.

If the script cannot reach the Stats API, leave the first pitch and the ballpark out. Do not fill them from a secondary site.

Scores, inning lines, and player game stats follow the same official-source rule. Use the box score URL the script prints (`/api/v1/game/{gamePk}/boxscore`), or the MLB.com box score for that game. Two recap articles agreeing is not verification when that box score exists. Season-long stats still come from Baseball Reference or FanGraphs, as in the tables below.

Fact-check runs the comparison again. `verify-facts.py` calls this script. A mismatch fails the fact-check. You can also run it directly:

```bash
python Cubs/mlb_schedule.py --date YYYY-MM-DD --check Cubs/cubs-content-YYYY-MM-DD
```

Exit code 2 means do not mark the fact-check PASS. Fix the copy so it matches the official line.

What this caught: on Oct 4, 2026 the brief labeled NLDS Game 2 as 4:00 PM CT and 8:00 PM CT because CBS and Yahoo agreed. Official `gameDate` values were `2026-10-04T20:00:00Z` and `2026-10-05T00:00:00Z`, which are 3:00 PM CT and 7:00 PM CT. On Oct 6, 2026 the brief put Brewers at Padres Game 3 at American Family Field. The official venue was Petco Park, 8:30 PM CT.

## Research Categories

Run **8-10 web searches** across these categories before writing content.

| # | Category | Example Search Queries |
|---|----------|----------------------|
| 1 | Game Results | "Cubs score last night", "Cubs game recap [date]", "Cubs box score" |
| 2 | Roster & Transactions | "Cubs roster moves", "Cubs trade rumors", "Cubs DFA", "MLB Trade Rumors Cubs" |
| 3 | Injury Updates | "Cubs injury report", "[player name] injury update", "Cubs IL moves" |
| 4 | Starting Rotation | "Cubs probable pitchers", "Cubs pitching matchups this week", "Cubs rotation order" |
| 5 | Prospect Pipeline | "Iowa Cubs results", "Cubs prospects", "Cubs top prospects [year]", "Tennessee Smokies" |
| 6 | Standings & Playoff Race | "NL Central standings", "MLB wild card standings", "Cubs playoff chances" |
| 7 | Rivalry Watch | "Cardinals news today", "NL Central news", "Brewers roster moves", "Cubs Cardinals series" |
| 8 | Preview & Lookahead | "Cubs schedule this week", "Cubs next series", "Cubs probable starters this week" |

Also run **2-4 fan sentiment searches** (see api-reference.md for details):
- "Bleed Cubbie Blue" or "Bleacher Nation Cubs Bullets" for fan blog reactions
- "site:reddit.com/r/CHICubs" for community hot takes
- Podcast recaps: "Cubs Related podcast", "Under the Ivy podcast"

## Story Tiering

### Tier 1 — Lead Stories (7:00 AM, 8:30 AM slots)

Must-cover content. Anchors the day and drives engagement.

| Story Type | Why Tier 1 |
|-----------|-----------|
| Cubs game results (W or L) | The game is always the story. Recap goes in the first available slot. |
| Walk-offs and extra-inning games | Peak fan emotion — always lead with these |
| Cardinals series (any game) | Rivalry games are minimum Tier 2, series openers/finales are Tier 1 |
| Major injury news (key players) | Starter hits the IL, ace needs surgery — fans need to know immediately |
| Trades and signings | Any completed transaction involving the Cubs roster |
| Playoff clinching/elimination | Highest-stakes moments of the season |
| No-hitters, combined no-hitters | Rare historic achievements — always Tier 1 |
| Opening Day / Home opener | Once-a-year events, always the lead |

### Tier 2 — Developing Stories (10:00 AM, 1:00 PM slots)

Strong content that builds out the day.

| Story Type | Why Tier 2 |
|-----------|-----------|
| Spring training standouts | Breakout performers in camp generate buzz |
| Roster battles and option decisions | Who makes the 26-man roster matters to fans |
| Prospect performances (AAA/AA) | Iowa Cubs and Tennessee Smokies results with top prospect highlights |
| NL Central rival news | Brewers/Reds/Pirates moves that affect the division race |
| Win/loss streaks developing | 5+ game streaks in either direction |
| Monthly/weekly awards | Cubs players winning NL Player of the Week, etc. |
| Trade deadline rumors (late July) | Speculation content 2 weeks before the deadline |
| All-Star selections | Cubs players named to the team |

### Tier 3 — Supporting Content (3:00 PM, 5:30 PM slots)

Fills out the schedule with evergreen and analysis content.

| Story Type | Why Tier 3 |
|-----------|-----------|
| Historical comparisons | "Last time the Cubs started 20-10..." type features — always anchored to a specific stat |
| Evergreen stat breakdowns | Advanced metrics explainers, Statcast highlights, season-to-date analysis |
| Minor league roundups (non-top prospects) | South Bend Cubs results, system-wide updates |
| Offseason minor signings | Low-profile free agent additions, minor league deals |
| Bold takes and season analysis | Opinion-backed takes on team trajectory, standings context |

**DISABLED — Do NOT use for Tier 3:**
- ~~Fan culture content~~ — No generic Wrigley history posts, 7th inning stretch trivia, or fan engagement filler
- ~~Engagement questions~~ — No "What do you think?", polls, or question-based posts of any kind
- ~~Standalone countdowns~~ — No "X days until Opening Day" posts without a real news hook attached

## Slow News Day Strategies

When breaking news is thin and there aren't 5 stories, fill Tier 3 slots with these — **never with engagement questions or fan polls**:

- Historical stat comparisons ("Last time a Cubs pitcher did X was...")
- Season-arc analysis (rotation health, lineup depth, standings context)
- Prospect pipeline updates (Iowa Cubs results, minor league standouts)
- NL Central rival analysis (what Brewers/Cardinals moves mean for the division race)
- Upcoming series preview with specific matchup angles (pitching splits, historical H2H)

**Explicitly banned on slow days:** Do NOT use "fan engagement posts", polls, questions like "Who's your favorite Cub?", or any content that asks followers for their opinion. These posts perform poorly and dilute the brand. If news is genuinely that thin, use fewer tweets that day — 4 good posts beat 7 with filler.

## Posting Priority

This order is non-negotiable. All times are CT.

1. **Game recaps** — always in the first available slot (7:00 AM for night games, 10:00 PM for just-ended games).
2. **Today's game preview** — must post BEFORE first pitch. If a 1:20 PM CT game, preview goes no later than 10:00 AM.
3. **Injury and roster news** — time-sensitive, post as early as confirmed.
4. **Everything else** — analysis, evergreen, hype posts fill remaining slots.

If the Cubs had a day off yesterday, lead with the best available Tier 2 story instead.

## Fact-Check Requirements

Every post must be verified before publishing. Priority order:

### Priority 1 — Scores and Game Stats

| Check | How to Verify |
|-------|--------------|
| Final score | ESPN box score AND MLB.com/Cubs game recap — cross-reference both |
| Innings pitched / line score | Verify from box score — never assume 9 innings (extras, rain delays) |
| Winning/losing/save pitcher | Box score decision column — do not guess from starter |
| Key play details | Verify home run distances, exit velo from Baseball Savant if citing Statcast |

### Priority 2 — Records and Milestones

| Check | How to Verify |
|-------|--------------|
| Career stats / milestones | Baseball Reference player page — the definitive source |
| Franchise records | Baseball Reference franchise page or Cubs media guide |
| Season stats (BA, ERA, HR) | Baseball Reference or FanGraphs — stats update daily, verify same-day |
| Win-loss records | Baseball Reference team schedule page — count manually if claiming a streak |

### Priority 3 — Player Ages and Biographical Data

| Check | How to Verify |
|-------|--------------|
| Player age | Look up birth date on Baseball Reference, calculate from today's date |
| Service time / years in MLB | Baseball Reference player page — count debut year to present |
| Draft history | Baseball Reference or MLB.com draft tracker |

### Priority 4 — Game Times, Ballparks, and Schedule

| Check | How to Verify |
|-------|--------------|
| First pitch | `python Cubs/mlb_schedule.py --date YYYY-MM-DD`. The clock is `gameDate` converted to America/Chicago. Always publish CT. Two secondary sites agreeing is not verification. |
| Ballpark | `venue.name` from that same script output. Do not carry a park forward from an earlier game in the series. |
| Score and game line | Stats API box score for the `gamePk` the script prints. Two recap sites agreeing is not verification. |
| TV/streaming broadcast | MLB.com schedule. Broadcasts change, and a TV listing is still not the first-pitch source. |
| Day of week | Cross-reference the calendar — never say "tonight's game" for an afternoon start |
| Series length | Verify 3-game vs 4-game vs 2-game series from the official schedule output |

### Priority 5 — Contract and Financial Data

| Check | How to Verify |
|-------|--------------|
| Contract values (AAV, total, years) | Spotrac Cubs page — the definitive payroll source |
| Arbitration projections | MLB Trade Rumors arbitration tracker |
| Luxury tax / payroll figures | Spotrac team payroll page |
| Free agent contract comparisons | Spotrac or MLB Trade Rumors — never estimate from memory |

## Special Rules

### Cardinals Content

- Any Cubs vs Cardinals game is **minimum Tier 2**, with series openers and finales at **Tier 1**
- Cardinals roster moves that affect the NL Central race are worth covering as Tier 2
- Rivalry jabs and fan energy posts perform well during and around Cardinals series
- Check Cardinals news as part of every daily research sweep, not just during series

### Walk-offs and Extras

- Cubs walk-off wins are **always Tier 1** — these are peak emotional moments for fans
- Extra-inning games (win or loss) are **always Tier 1** — the drama and bullpen usage are both story-worthy
- Walk-off losses are still Tier 1 if they involve a significant game situation (playoff race, rivalry)

### Time Zone Reminder

- All game times posted in **CT (Central Time)** — the label is always CT, including during daylight time
- The number comes from `America/Chicago`, not from an Eastern listing and not from a fixed 5-hour or 6-hour offset. Chicago is CDT (UTC−5) from the second Sunday in March until the first Sunday in November, and CST (UTC−6) otherwise. The schedule script applies that.
- A West Coast first pitch is still written in CT. A 9:10 PM CT game is not "7:10 PM" with CT added.
- Never post a bare "7:00 PM". If the official start is TBD, say TBD and do not invent a clock.

## NL Central Quick Reference

| Team | Affiliate (AAA) | Key Rivalry Note |
|------|-----------------|-----------------|
| Cubs | Iowa Cubs (Des Moines) | — |
| Cardinals | Memphis Redbirds | Primary rival. Every series is content. |
| Brewers | Nashville Sounds | Division threat. Always check standings gap. |
| Reds | Louisville Bats | Competitive rebuilds create storylines. |
| Pirates | Indianapolis Indians | Prospect-heavy; watch for callups that affect Cubs. |
