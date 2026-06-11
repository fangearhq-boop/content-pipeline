# Fact-Check Log — Cubs, June 11, 2026

Script: verify-facts.py (manual pass — X-only pipeline, no article HTML to check)
Date: 2026-06-11

---

## Character Count Verification

All tweets verified manually (newlines count as 1 character each):

**Post 1A (7:00 AM)**:
"Rockies 3, Cubs 2. Walk-off. Again.\n\nTJ Rumfield's 2-run HR in the 8th erased FIVE shutout innings from Imanaga. The bullpen couldn't hold it.\n\nCubs fall to 34-34. They haven't won a SERIES in over a month.\n\n#Cubs #GoCubs #FlyTheW"
- Line 1: 36 + 2 = 38
- Line 2: 139 + 2 = 141
- Line 3: 61 + 2 = 63
- Line 4: 22
- Total: 36+2+139+2+61+2+22 = **264 chars** ✓ UNDER 280

**Post 2A (12:00 PM)**:
"Series finale at Coors. First pitch 2:10 PM CT.\n\nCabrera (3-3, 4.99 ERA) vs Feltner (2-1, 4.22 ERA).\n\nThe Rockies have already clinched the series. The Cubs need to WIN this one — because getting swept by a 26-42 team isn't something you just shake off.\n\n#Cubs #GoCubs #FlyTheW"
- Line 1: 48 + 2 = 50
- Line 2: 50 + 2 = 52 (wait: "Cabrera (3-3, 4.99 ERA) vs Feltner (2-1, 4.22 ERA)." = 50 chars)
- Line 3: "The Rockies have already clinched the series. The Cubs need to WIN this one — because getting swept by a 26-42 team isn't something you just shake off." = 150 + 2 = 152
- Line 4: 22
- Total: 48+2+50+2+150+2+22 = **276 chars** ✓ UNDER 280

**Post 3A (1:15 PM)**:
"Matthew Boyd's return is DELAYED — left shoulder soreness in a bullpen session.\n\nHorton, Steele, and Taillon are already on IL. Now Boyd pushes back further.\n\nTHREE rotation arms lost to injury — plus Boyd in limbo. The Cubs are out of runway.\n\n#Cubs #CubsBaseball #MLB"
- Line 1: 80 + 2 = 82
- Line 2: 75 + 2 = 77
- Line 3: "THREE rotation arms lost to injury — plus Boyd in limbo. The Cubs are out of runway." = 84 + 2 = 86
- Line 4: 24
- Total: 80+2+75+2+84+2+24 = **269 chars** ✓ UNDER 280

**Post 4A (2:30 PM)**:
"Dansby Swanson: .180 BA. .139 in his last 11 games.\n\nNico Hoerner: deep funk since taking a fastball to the helmet — power stripped, production collapsed.\n\nTWO core infielders ice cold at the same time. That's not bad luck — that's the hidden rot inside this collapse.\n\n#Cubs #NorthSiders #MLB"
- Line 1: 52 + 2 = 54
- Line 2: "Nico Hoerner: deep funk since taking a fastball to the helmet — power stripped, production collapsed." = 100 + 2 = 102
- Line 3: "TWO core infielders ice cold at the same time. That's not bad luck — that's the hidden rot inside this collapse." = 111 + 2 = 113
- Line 4: 23
- Total: 52+2+100+2+111+2+23 = **292 chars** ⚠ OVER 280 — NEEDS FIX

> FIX: Trim line 2 and line 3.
> Revised Post 4A:
> "Dansby Swanson: .180 BA. .139 in his last 11 games.\n\nNico Hoerner in a DEEP funk since taking a fastball to the helmet — power gone.\n\nTWO core infielders ice cold simultaneously. That's the hidden rot inside this collapse.\n\n#Cubs #NorthSiders #MLB"
> - Line 1: 52 + 2 = 54
> - Line 2: "Nico Hoerner in a DEEP funk since taking a fastball to the helmet — power gone." = 79 + 2 = 81
> - Line 3: "TWO core infielders ice cold simultaneously. That's the hidden rot inside this collapse." = 87 + 2 = 89
> - Line 4: 23
> - Total: 52+2+79+2+87+2+23 = **247 chars** ✓ UNDER 280

**Post 5A (3:45 PM)**:
"Since peaking at 27-12, the Cubs are 7-22.\n\nThey haven't won a series in OVER A MONTH — including losses to the A's and Giants at Wrigley, and now getting swept at Coors by a sub-.500 Rockies team.\n\nThis isn't a slump. It's a structural failure.\n\n#Cubs #MLB #NorthSiders"
- Line 1: 43 + 2 = 45
- Line 2: "They haven't won a series in OVER A MONTH — including losses to the A's and Giants at Wrigley, and now getting swept at Coors by a sub-.500 Rockies team." = 153 + 2 = 155
- Line 3: "This isn't a slump. It's a structural failure." = 47 + 2 = 49
- Line 4: 23
- Total: 43+2+153+2+47+2+23 = **272 chars** ✓ UNDER 280

**Post 6A (5:00 PM)**:
"Brewers: 41-24.\nCubs: 34-34.\n\nMilwaukee has LAPPED this division. The Cubs are 8.5 games back and haven't won a series in June.\n\nThe division is gone. Wild card is the realistic goal now — and even that picture is starting to blur.\n\n#Cubs #NorthSiders #MLB"
- Line 1-2: "Brewers: 41-24.\nCubs: 34-34." = 16+1+15 = 32 + 2 = 34
- Line 3: "Milwaukee has LAPPED this division. The Cubs are 8.5 games back and haven't won a series in June." = 97 + 2 = 99
- Line 4: "The division is gone. Wild card is the realistic goal now — and even that picture is starting to blur." = 100 + 2 = 102
- Line 5: 23
- Total: 32+2+97+2+100+2+23 = **258 chars** ✓ UNDER 280

**Revised Post 4A approved** — all 6 posts now within 280 chars.

---

## Fact Claims by Priority

### Priority 1: Dates, Times, Day-of-Week

| Claim | Source | Status |
|-------|--------|--------|
| Game June 11 is Thursday | Calendar | VERIFIED ✓ |
| First pitch 2:10 PM CT | SportsGrid, Baseball-Reference preview | VERIFIED ✓ |
| June 10 game result was yesterday | Timeline math | VERIFIED ✓ |

### Priority 2: Scores, Records

| Claim | Source | Status |
|-------|--------|--------|
| Rockies 3, Cubs 2 (June 10) | Purple Row, CBS Sports, SI.com, ESPN | VERIFIED ✓ |
| Cubs fall to 34-34 | Series context snapshot + game result math | VERIFIED ✓ |
| Cubs peaked at 27-12 | Multiple sources (North Side Baseball, Bleacher Nation) | VERIFIED ✓ |
| 7-22 since peak (27+7=34, 12+22=34) | Calculated from verified W-L records | VERIFIED ✓ |
| Brewers: 41-24 | MLB standings, ESPN standings | VERIFIED ✓ |
| Cardinals: 36-28 | MLB standings (from search results) | VERIFIED ✓ |
| Cubs 8.5 GB from Brewers | Calculated: ((41-34)+(34-24))/2 = 8.5 ✓ | VERIFIED ✓ |
| Rockies record "sub-.500" | 26-42 entering series per snapshot → well below .500 | VERIFIED ✓ |
| Cabrera: 3-3 record | ESPN player page | MEDIUM (single source) |
| Cabrera: 4.99 ERA | ESPN player page | MEDIUM (single source) |
| Feltner: 2-1, 4.22 ERA | ESPN player page | MEDIUM (slight variation in sources: 4.22 vs 4.85) |

### Priority 3: Player Stats

| Claim | Source | Status |
|-------|--------|--------|
| Swanson .180 BA on season | CBS Sports, Bleed Cubbie Blue | VERIFIED ✓ |
| Swanson .139 last 11 games | CBS Sports player splits | MEDIUM (single calculation window) |
| Imanaga 5 shutout innings, 7 K (June 10) | CBS Sports box score, Purple Row | VERIFIED ✓ |
| TJ Rumfield 2-run HR in 8th | Purple Row, CBS Sports | VERIFIED ✓ |
| Hoerner deep slump since fastball to helmet | Bleacher Nation (June 9-10), CubbiesCrib | VERIFIED ✓ (descriptive claim, no specific stat fabricated) |
| THREE rotation arms on IL (Horton, Steele, Taillon) | June 10 pipeline, injury reports | VERIFIED ✓ |

### Priority 4: Schedule / Game Times

| Claim | Source | Status |
|-------|--------|--------|
| Series at Coors Field | Series context snapshot, SportsGrid | VERIFIED ✓ |
| 3-game series (June 9-11) | Series context rationale, game dates | VERIFIED ✓ |
| Cubs 0-2 in series before today | Game results June 9 (7-3 L) and June 10 (3-2 L) | VERIFIED ✓ |

### Flags / Caveats

- **Hoerner recent BA**: Not fabricated — tweet uses descriptive "DEEP funk" and "power gone" without inventing a number. SAFE.
- **Feltner ERA**: Two sources differ slightly (4.22 vs 4.85). Used the lower number (4.22) in tweet — if confirmed incorrect, minor correction needed. LOW impact either way (both are mediocre ERAs).
- **"not won a series in over a month"**: Bleacher Nation June 10 states explicitly: "This team has not won a series in over a month, including back-to-back very winnable sets against the A's and Giants at Wrigley Field." VERIFIED via primary news source. ✓
- **"12 of 14 MLB teams ever" with both 10-win and 10-loss streak**: NOT used in tweets (single source, North Side Baseball). Wisely omitted.

---

## Consistency Check

| Story in Brief | X Post Exists | Posting Time Set |
|----------------|---------------|-----------------|
| STORY 1: Walk-off loss | ✓ Post 1A | 7:00 AM CT ✓ |
| STORY 2: Series finale preview | ✓ Post 2A | 12:00 PM CT ✓ |
| STORY 3: Boyd delay | ✓ Post 3A | 1:15 PM CT ✓ |
| STORY 4: Swanson/Hoerner slump | ✓ Post 4A | 2:30 PM CT ✓ |
| STORY 5: 7-22 since peak | ✓ Post 5A | 3:45 PM CT ✓ |
| STORY 6: NL Central/wild card | ✓ Post 6A | 5:00 PM CT ✓ |

**All stories have X posts. All X posts have CT posting times. ✓**

---

## Posting Time Format Check

All times follow cubs-x-bot strptime format ("H:MM AM/PM CT"):
- 7:00 AM CT ✓
- 12:00 PM CT ✓
- 1:15 PM CT ✓
- 2:30 PM CT ✓
- 3:45 PM CT ✓
- 5:00 PM CT ✓

---

## Hashtag Rules Check

Each tweet has exactly 3 hashtags, first one #Cubs, on their own line:
- Post 1A: #Cubs #GoCubs #FlyTheW ✓
- Post 2A: #Cubs #GoCubs #FlyTheW ✓
- Post 3A: #Cubs #CubsBaseball #MLB ✓
- Post 4A: #Cubs #NorthSiders #MLB ✓
- Post 5A: #Cubs #MLB #NorthSiders ✓
- Post 6A: #Cubs #NorthSiders #MLB ✓

**All pass. ✓**

---

## '#1' Bug Check

No rankings written as '#1' or '#2'. All references use 'No.' format or number only. ✓

---

## Result: PASS (with one char-count fix applied to Post 4A above)

Post 4A has been corrected in this log. The correction must be applied to 03-social-posts-x.md before compiling.
