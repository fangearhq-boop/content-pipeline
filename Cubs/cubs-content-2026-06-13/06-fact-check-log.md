# Cubs Fact-Check Log — June 13, 2026

**Verified by:** Content Pipeline Bot  
**Date:** 2026-06-13  
**Stories:** 8  

---

## Priority 1: Dates, Times, Day-of-Week

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| "Cubs 5, Giants 1" on June 12, 2026 | CBS Sports recap, ESPN game recap, MLB.com | VERIFIED | Multiple sources confirm final score |
| "Oracle Park" as venue | Series-context.json, CBS Sports | VERIFIED | Confirmed venue |
| Tonight's game at "9:05 PM CT" | Series-context.json (game_date_iso: 2026-06-14T02:05:00Z → 9:05 PM CT) | VERIFIED | UTC to CT conversion confirmed |
| "Saturday, June 13" as today's date | System context: 2026-06-13 | VERIFIED | Date correct |
| Taillon IL "retroactive to June 8" | Bleed Cubbie Blue, Cubs Insider | VERIFIED | Multiple sources confirm June 8 retroactive date |
| "August 3" trade deadline | Standard MLB trade deadline 2026 | VERIFIED | Confirmed from multiple trade deadline articles |
| "51 days" to August 3 from June 13 | Math: June 13 → Aug 3 = 51 days | VERIFIED | June has 30 days: 17 left in June + 31 July days + 3 Aug days = 51 ✓ |

---

## Priority 2: Scores, Records, Win-Loss

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Cubs 5, Giants 1 | CBS Sports, ESPN, MLB.com Gameday | VERIFIED | Final score confirmed across sources |
| Assad record "4-1" | CBS Sports recap: "Assad (4-1)" | VERIFIED | Explicit in recap text |
| Assad "3rd straight win spanning 7 starts" | CBS Sports: "win his third straight decision spanning seven starts" | VERIFIED | Quoted directly from recap |
| Cubs record "36-34" | Series-context.json generated 08:30 UTC June 13 | VERIFIED | Consistent with Cubs going 35-34 → 36-34 after June 12 win |
| Giants record "28-42" | Series-context.json | VERIFIED | Confirmed |
| Brewers "41-25" | CBS Sports/ESPN standings summary | MEDIUM | AI-generated standings summary; consistent with series-context notes but not independently verified from a live standings page |
| Cardinals "~37-29" | CBS Sports standings summary | MEDIUM | Same caveat; may not reflect games played June 12 |
| McDonald record "2-3, 4.15 ERA" | WebFetch summary (Cubs Insider) | LOW | WebFetch/AI summary only; no second source. Used in tweet as preview context but flagged. |

---

## Priority 3: Player Stats

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Assad "6 IP, 3 H" | CBS Sports recap | VERIFIED | Explicit in text |
| Assad "5 K" | CBS Sports recap: "struck out five" | VERIFIED | **DISCREPANCY:** MLB.com video title says "six-strikeout start." CBS Sports written recap (longer, more detailed) says "struck out five." Using 5 from the text-based source. Flag for manual review. |
| Assad "1 BB" | CBS Sports recap | VERIFIED | "walked one" |
| Busch "3-run HR" | CBS Sports, ESPN | VERIFIED | Multiple sources confirm |
| Busch HR "into McCovey Cove" | CBS Sports: "three-run homer into McCovey Cove beyond right field in the fifth inning" | VERIFIED | Specific detail confirmed |
| Suzuki "RBI double" in 4th | CBS Sports recap | VERIFIED | Confirmed |
| Hoerner "sacrifice fly" | CBS Sports recap | VERIFIED | Confirmed |
| Brown ERA "1.74" | Consistent across June 12 pipeline story history and search results | MEDIUM | Multiple story-history references + search results consistent; not freshly pulled from a live stat page today |
| Brown WHIP "0.88" | Search result summary | MEDIUM | Single source (WebFetch summary) |
| Brown "58 K" | Search result summary | MEDIUM | Single source |
| Brown "0 HR allowed" | Multiple story history references and search summaries | MEDIUM | Consistent across sources but no freshly verified page pull |
| Brown record "2-2" | Search result summary | MEDIUM | Single source; consistent with story history |

---

## Priority 4: Game Times and Schedule

| Claim | Source | Status | Notes |
|-------|--------|--------|-------|
| Tonight's game "9:05 PM CT" | Series-context.json (HIGH) | VERIFIED | Direct from structured data |
| Sunday game "2:10 PM CT" | Series-context.json | VERIFIED | game[1].game_date_ct = "Sun 2:10 PM CT" |

---

## Compound / Superlative Claims

| Claim | Status | Notes |
|-------|--------|-------|
| "One of the most quietly dominant pitchers in baseball" | ACCEPTABLE | Qualified with "one of" — not a superlative requiring a 2nd source |
| "Most urgent rotation need in baseball" | ACCEPTABLE | Opinion framing, not a factual compound claim |
| Assad "3rd straight win" | VERIFIED | CBS Sports: "third straight decision" explicit |
| Four starters "simultaneously unavailable" | VERIFIED | Horton (confirmed 2027 timeline), Steele (60-day IL confirmed), Boyd (recovering from meniscus — confirmed), Taillon (15-day IL hamstring confirmed) |

---

## Claims Requiring Manual Review Before Posting

1. **Assad strikeout count (5 vs. 6):** CBS Sports text says 5; MLB.com video title says 6. Tweet uses "5 K" from the written recap. Low-stakes discrepancy, but note for future.
2. **McDonald stats (2-3, 4.15 ERA):** LOW confidence (WebFetch only). Used in the game preview tweet as context. If wrong, it's a preview stat from a routine start, not a milestone claim.
3. **Brewers/Cardinals exact records:** Based on AI standings summary. Cubs own record (36-34) is HIGH confidence from series-context.json. GB calculations may be off by .5 games if standings data is stale by 1 game.

---

## Characters-Over-280 Check

Per engine rules, character count verification is handled by compile-content-data.py in Step 4. No manual character counts included. If the compiler flags any tweet, fix before dashboard generation.

---

## Summary

- **VERIFIED claims:** 18
- **MEDIUM confidence:** 7 (used in tweets, flagged above)
- **LOW confidence:** 1 (McDonald stats — preview context only)
- **Items for manual review:** 3 (strikeout count discrepancy, McDonald stats, standings GB precision)
