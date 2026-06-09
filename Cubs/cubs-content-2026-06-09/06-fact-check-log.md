# Cubs Fact-Check Log — 2026-06-09

Generated: 2026-06-09
Pipeline step: Step 10 (manual fact-check — verify-facts.py run after)

---

## Priority 1: Dates, Times, Day-of-Week Claims

| Claim | Source | Status |
|-------|--------|--------|
| Game tonight June 9 = Tuesday | Calendar verified (June 9 = Tuesday) | VERIFIED |
| First pitch 7:40 PM CT | series-context.json game_date_ct="Tue 7:40 PM CT" | VERIFIED |
| Game at Coors Field | series-context.json venue="Coors Field" | VERIFIED |
| 3-game series | series-context.json series_length=3 | VERIFIED |
| Boyd missed ~4 weeks (May 7 → June 9) | Calculated: May 7 surgery date (WaPo), June 9 activation = 33 days. "Four weeks" is accurate. | VERIFIED |
| Game 2 June 10 (Wednesday) | series-context.json game_date_iso for game 2 | VERIFIED |

---

## Priority 2: Scores, Records, Win-Loss Records

| Claim | Source | Status |
|-------|--------|--------|
| Cubs record 34-32 | series-context.json cubs_record="34-32" | VERIFIED |
| Rockies record 24-42 | series-context.json opponent_record="24-42" | VERIFIED |
| Cubs 14-17 on the road | Covers.com game preview summary | MEDIUM — single source (betting site). Not cross-referenced. Flagged for review. |
| Brewers 40-23 | Brew Crew Ball Week 11 Power Rankings/Review | MEDIUM — fan blog, not MLB.com primary standings. Used in Tweet 5. |
| Cardinals 35-28 | Brew Crew Ball Week 11 | MEDIUM — fan blog. Used in Tweet 5. |
| Cubs 7.5 GB from Brewers | Calculated: ((40-34)+(32-23))/2 = 7.5 | VERIFIED (calculation confirmed) — depends on MEDIUM-confidence Brewers record |
| Colin Rea 5-3, 4.59 ERA | Covers.com game preview (multiple search results consistent) | MEDIUM — not pulled from primary stat page (Baseball Reference/Fangraphs). Used in Tweets 1 and 3. |
| Tomoyuki Sugano 5-4, 3.98 ERA | Covers.com game preview | MEDIUM — not from primary stat page. Used in Tweet 3. |
| Sugano = Rockies pitcher | Denver Gazette "Rockies' Tomoyuki Sugano shines in first Coors Field start" (April 5, 2026) | VERIFIED (team affiliation confirmed) |
| Michael Lorenzen 2-8, 8.01 ERA | Probables search result | MEDIUM — AI summary only. NOT used in final tweets (mentioned in analysis only). |

---

## Priority 3: Player Stats

| Claim | Source | Status |
|-------|--------|--------|
| Dansby Swanson batting .180 | Multiple sources (Athlon Sports, Bleacher Nation, ClutchPoints, all cite .180) | VERIFIED |
| Swanson "mental reset, not an injury" / Counsell said "He's healthy" | Athlon Sports, ClutchPoints reporting Craig Counsell's confirmed statement | VERIFIED |
| Swanson benched June 6 | Bleacher Nation lineup note June 6, June 7 story history | VERIFIED |
| Ben Brown ERA "under 2.00" | Sun-Times June 4 (1.92 ERA); June 6 start (5.1 scoreless) would lower ERA further | VERIFIED directionally — current exact ERA not re-pulled. "Under 2.00" is accurate based on available data. NOT USED IN TODAY'S TWEETS (Ben Brown not covered today — no material new angle) |
| Rockies have worst rotation ERA in baseball | FanSided, MLB Trade Rumors articles both confirm "only Rockies starters performing worse" than Cubs | VERIFIED as qualitative claim — specific ERA number NOT cited in tweets to avoid LOW-confidence specifics |
| Boyd = Cubs' Opening Day starter | Widely reported, multiple sources | VERIFIED |
| Taillon hamstring strain → IL | WaPo June 7 article: "Taillon set to go on the IL after straining his hamstring" | MEDIUM — sourced from one AI summary. Not pulled from MLB transactions page directly. |

---

## Priority 4: Compound / Historical Claims

No compound claims ("X joins Y and Z as the only...") present in today's tweets. No superlative historical claims requiring two-source verification.

**"WORST ERA in baseball" (Rockies rotation):** This is a superlative. Two sources confirm independently (FanSided: "with only Rockies' starters performing worse" than Cubs; MLB Trade Rumors article context). Used as qualitative claim without citing a specific number. VERIFIED (two sources).

---

## Priority 5: Schedule / Series Claims

| Claim | Source | Status |
|-------|--------|--------|
| Series is 3 games at Coors Field | series-context.json confirmed | VERIFIED |
| Game 1 tonight (June 9) | series-context.json | VERIFIED |
| Cubs at Coors (visiting) | series-context.json is_cubs_home=false | VERIFIED |
| June schedule features 22+ sub-.500 opponents | Referenced from June 5 pipeline research (Sun-Times June 2 article). NOT cited in today's tweets (folded into general "favorable schedule" language) | BACKGROUND ONLY |

---

## Character Count Pre-Check (manual estimates — verify-facts.py will confirm)

| Tweet | Est. Character Count | Status |
|-------|---------------------|--------|
| Tweet 1 (Series Preview, 7:00 AM) | ~269 | Under 280 ✓ |
| Tweet 2 (Boyd Activated, 12:00 PM) | ~253 | Under 280 ✓ |
| Tweet 3 (Pitching Preview, 1:15 PM) | ~239 | Under 280 ✓ |
| Tweet 4 (Swanson, 3:45 PM) | ~224 | Under 280 ✓ |
| Tweet 5 (Division Stakes, 5:00 PM) | ~244 | Under 280 ✓ |

All tweets manually checked against 280-char limit. verify-facts.py will produce exact counts.

---

## Hashtag Compliance Check

| Tweet | Hashtag Count | First Hashtag = #Cubs | Result |
|-------|--------------|----------------------|--------|
| Tweet 1 | 3 (#Cubs #GoCubs #FlyTheW) | Yes | PASS |
| Tweet 2 | 3 (#Cubs #MLB #CubsBaseball) | Yes | PASS |
| Tweet 3 | 3 (#Cubs #GoCubs #FlyTheW) | Yes | PASS |
| Tweet 4 | 3 (#Cubs #GoCubs #CubsBaseball) | Yes | PASS |
| Tweet 5 | 3 (#Cubs #NorthSiders #MLB) | Yes | PASS |

---

## "#1 / No. 1" Rule Check

No rankings or "No. X" claims in today's tweets. PASS.

---

## Engagement Question Check

No tweets contain questions posed to followers. PASS.

---

## Flags for Manual Review

1. **Brewers 40-23 and Cardinals 35-28**: Sourced from Brew Crew Ball fan blog Week 11 review. Recommend spot-checking against MLB.com standings before the 5:00 PM tweet posts.
2. **Colin Rea stats (5-3, 4.59 ERA)**: Sourced from betting site AI summary. Should be confirmed against ESPN or Fangraphs if possible before 7:00 AM.
3. **Taillon hamstring IL**: Sourced from WaPo AI summary. If this is wrong and Taillon is not actually on the IL, Tweet 2 would need adjustment.
4. **Cubs road record (14-17)**: Single source (betting site). Minor stat used in analysis only, not in final tweet text.
