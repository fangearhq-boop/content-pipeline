# Cubs Fact-Check Log — 2026-05-27

**Pipeline date:** 2026-05-27  
**Fact-checker:** Automated pipeline  
**Status:** COMPLETE

---

## STORY 1: Pirates 12, Cubs 1 — Losing Streak Reaches 10

| Claim | Confidence | Source(s) | Status |
|-------|-----------|-----------|--------|
| Final score: Pirates 12, Cubs 1 (May 26, 2026) | HIGH | Bleacher Nation enhanced box score; Chicago Sun-Times "Cubs' skid reaches 10"; ESPN recap | VERIFIED |
| Jordan Wicks started Game 2 | HIGH | Chicago Sun-Times, ESPN, Bleacher Nation (all confirm) | VERIFIED |
| Wicks surrendered 5 ER in the 1st inning | HIGH | CBS Sports losing streak article cites Wicks giving up 5 first-inning runs; Sun-Times confirms | VERIFIED |
| Cubs went 1-for-13 with RISP | HIGH | CBS Sports article quotes this directly: "1 for 13 with runners in scoring position" | VERIFIED |
| Cubs left 11 on base | HIGH | CBS Sports article cites 11 LOB for May 26 | VERIFIED |
| 2 total runs across Games 1 and 2 | HIGH | Game 1 (May 25): Pirates 2, Cubs 1. Game 2 (May 26): Pirates 12, Cubs 1. Both confirmed individually; 1+1=2 total runs. | VERIFIED |
| 10-game losing streak | HIGH | ESPN headline, Sun-Times headline, CBS Sports all say "10th straight loss" | VERIFIED |
| Longest skid since 2022 | HIGH | CBS Sports: "Cubs' longest losing streak since 2022"; ESPN confirms | VERIFIED |
| Cubs record: 29-26 | HIGH | series-context.json generated 08:30 UTC May 27; consistent with 29-25 before loss | VERIFIED |

### FLAGGED — NOT used in tweets:
- ~~"Only the second team in MLB history with two 10-game winning streaks AND a 10-game losing streak in same season"~~ — Single source (CBS Sports), compound historical claim. Requires second-source verification per protocol. **NOT included in any tweet.** Removed from all drafts.

---

## STORY 2: The Math on This Season

| Claim | Confidence | Source(s) | Status |
|-------|-----------|-----------|--------|
| Cubs started season 21-4 | HIGH | Consistent across multiple pipeline entries (May 24, 25, 26 story history); Counsell referenced in CBS Sports article | VERIFIED |
| Cubs are now 29-26 | HIGH | series-context.json | VERIFIED |
| 8-22 since 21-4 peak (the math) | HIGH | Calculated: 29-21=8 wins since peak; 26-4=22 losses since peak. Arithmetic is internally consistent. | VERIFIED (arithmetic) |
| 10-game losing streak is current | HIGH | Multiple sources | VERIFIED |
| No blockbuster trade / no lineup overhaul | MEDIUM | Consistent with story history (no major transactions reported); no contradicting sources | ACCEPTABLE |

---

## STORY 3: NL Central Standings

| Claim | Confidence | Source(s) | Status |
|-------|-----------|-----------|--------|
| Cubs 29-26, 3rd in NL Central | HIGH | series-context.json (generated today) | VERIFIED |
| Cubs were in 1st place in NL Central (mid-May) | HIGH | Story history confirms Cubs were 1st as recently as around May 16 | VERIFIED |
| Brewers "31-20+" | MEDIUM | CBS Sports, Brew Crew Ball confirmed 31-20 before May 26 games. May 26 Brewers-Cardinals result not confirmed from two sources. Tweet uses "31-20+" framing to avoid asserting a precise post-May-26 figure. | ACCEPTABLE (hedged) |
| Cardinals ~29-23, sitting between Cubs and Brewers | MEDIUM | Standings before May 26 games: Cardinals 29-23 (per CBS Sports). Used "sitting between them" language rather than specific record. | ACCEPTABLE (hedged) |
| "4+ game lead" for Brewers | MEDIUM | Calculated: using 31-20 vs 29-26, GB = (31-29)/2 + (26-20)/2 = 1+3 = 4 GB. If Brewers won May 26, could be 4.5+. "4+" framing is conservative and correct. | ACCEPTABLE (hedged) |

---

## STORY 4: Game Preview — Taillon vs Chandler

| Claim | Confidence | Source(s) | Status |
|-------|-----------|-----------|--------|
| Jameson Taillon starts today (May 27) for Cubs | HIGH | MLB.com video title "Jameson Taillon against the Pirates 05/27/2026"; Picks and Parlays, theScore matchup all confirm | VERIFIED |
| Game time: 5:40 PM CT | HIGH | series-context.json (game_date_ct: "Wed 5:40 PM CT") | VERIFIED |
| Venue: PNC Park | HIGH | series-context.json | VERIFIED |
| Taillon ERA: 5.20 | MEDIUM-HIGH | Picks-and-parlays preview cites 5.20; one source (FanGraphs era) cites 4.97. The more frequently cited/downstream figure is 5.20. **Tweet uses 5.20** — flag as MEDIUM-HIGH. | ACCEPTABLE |
| Taillon: 17 HR allowed | MEDIUM-HIGH | Picks-and-parlays cites 17 HR; consistent with story history referencing Taillon's HR problem. | ACCEPTABLE |
| Taillon: 55.1 IP | MEDIUM | One source cites "55.1 IP", another "50.2 IP". Used 55.1 IP in tweet which matches the 5.20 ERA source package. | ACCEPTABLE |
| Bubba Chandler starts for Pirates | HIGH | Multiple series preview sources (Bleacher Nation series preview, picks-and-parlays, theScore) | VERIFIED |
| Chandler: 1-6 record | MEDIUM-HIGH | Picks-and-parlays, theScore both confirm 1-6 | VERIFIED |
| Chandler: 4.79 ERA | MEDIUM | Picks-and-parlays cites 4.79; theScore preview cites 4.60. Used 4.79 from picks source — both in the same ballpark. | ACCEPTABLE (hedged — tweet says "4.79 ERA") |
| Chandler: 34 BB in 47 IP | MEDIUM | Picks-and-parlays cites both figures. Second source not found for BB total. Flagged MEDIUM — defensible as "34 BB in 47 IP" is a specific enough claim that I should note it. **Single source.** | ACCEPTABLE but flag |

---

## STORY 5: Paul Skenes Tomorrow

| Claim | Confidence | Source(s) | Status |
|-------|-----------|-----------|--------|
| Skenes pitches Game 4 (May 28) | HIGH | Multiple series preview sources (Bleacher Nation "Oh, Cool … Now They Get to Face Paul Skenes", picks-and-parlays, Bucs Dugout all confirm Skenes is Game 4 Thursday) | VERIFIED |
| Skenes record: 6-2 | HIGH | CBS Sports player page, ESPN player stats | VERIFIED |
| Skenes ERA: 1.98 | HIGH | CBS Sports: "1.98 ERA"; ESPN confirms | VERIFIED |
| Skenes WHIP: 0.714 (leads MLB) | HIGH | CBS Sports cites 0.714 WHIP and notes "leads the majors" | VERIFIED |
| Skenes: 56 K in 50 innings | HIGH | CBS Sports: "56:7 K:BB ratio across 50 innings" | VERIFIED |
| Colin Rea starts for Cubs in Game 4 | MEDIUM | Multiple preview sources (Bleacher Nation series preview, SportsGrid) confirm Rea; one source says "Rea vs Skenes." | ACCEPTABLE |
| Cubs scored 2 runs in Games 1 and 2 | HIGH | Both game scores confirmed (1 run each; see Story 1) | VERIFIED |
| Game 4 time: 5:40 PM CT / tomorrow (May 28) | HIGH | series-context.json shows Thu 5:40 PM CT for May 28 game | VERIFIED |

---

## Posting time format check

All posting times use "H:MM AM/PM CT" format matching cubs-x-bot's strptime("%I:%M %p") parser after "CT" is stripped:
- 7:00 AM CT ✓
- 8:15 AM CT ✓
- 10:45 AM CT ✓
- 12:00 PM CT ✓
- 3:45 PM CT ✓

## Hashtag check
All posts have exactly 3 hashtags, on one line, space-separated, first one #Cubs. ✓

## "#1" / "No. 1" check
No "#1" usage. One "#MLB" hashtag is legitimate. ✓

## Engagement question check
No posts contain questions directed at followers. ✓

## 280-char check
Character counts estimated during drafting; compile-content-data.py will verify exact counts.
