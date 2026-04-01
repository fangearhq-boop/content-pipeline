# Golf Fanrecap — Pipeline Status

Dashboard subfolder: `gfr`
Dashboard URL: https://fangearhq-boop.github.io/content-dashboards/gfr/

## Current Pipeline

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-04-01 |
| Writing | Complete (all 7 files + 5 articles) | 2026-04-01 |
| Fact-check | Complete (verify-facts.py run — 36 claims, 66 HIGH) | 2026-04-01 |
| Scripts | Complete (all 6 scripts run) | 2026-04-01 |
| PostPlanner | Complete (standard + TOBI exports) | 2026-04-01 |
| Dashboard | Generated locally (push blocked — see notes) | 2026-04-01 |
| Published | Pending upload | — |

## Queue

(No items in queue.)

## Pipeline Run: 2026-04-01
- **Research:** 8 web searches covering Tiger Woods DUI not-guilty plea + Masters withdrawal + treatment announcement, Valero Texas Open field/odds/Morikawa withdrawal, Masters odds update, Spieth course history at Valero, Masters bubble players world rankings, Fleetwood TGL win, Masters Grand Slam chasers, Chevron/Kim LPGA update
- **Stories (7):** Tiger withdraws Masters/seeks treatment (T1), Valero final preview Fleetwood/Åberg (T1), Masters 8 days out without Tiger (T1), Spieth at Valero 2021 champion (T2), Masters bubble watch Fowler/Horschel/Kim/Zalatoris (T2), Grand Slam chasers Schauffele/Morikawa/Koepka (T2), Kim/Chevron Championship (T3)
- **X Posts:** 10 written, all under 280 characters
- **Facebook Posts:** 14 (long-form + caption for each of 7 stories)
- **Articles:** 5 (Stories 1-5)
- **PostPlanner exports:** gfr-postplanner-2026-04-01.xlsx (10 posts) + gfr-postplanner-tobi-2026-04-01.xlsx (10 TOBI posts)
- **Dashboard:** Generated at Golf/golf-content-2026-04-01/review-dashboard.html (29 items)
- **Key facts:** Tiger pleaded not guilty (DUI + property damage + test refusal), withdrew from Masters, announced treatment. Augusta's Ridley expressed support. Arraignment April 23. Valero: Fleetwood/Åberg +1500 co-favorites, Spieth +1600 (2021 champion), Morikawa WD. Bubble players: Fowler No. 65, Horschel No. 94, Finau No. 107, Tom Kim No. 126, Zalatoris No. 299. Masters April 9-12, Scheffler +480 (3-peat bid). Grand Slam chasers: Schauffele, Morikawa, Koepka.
- **Fact concerns:** All core facts HIGH. DeChambeau/Rahm Masters odds MEDIUM (fluctuate daily). Tiger Senior Open registration MEDIUM (single source). Saturday Valero thunderstorm forecast MEDIUM.

## Pipeline Run: 2026-03-31
- **Research:** 7 web searches covering Tiger Woods Masters status/DUI update, Valero Texas Open start/field/odds, Masters 2026 countdown (9 days), Chevron Championship/Hyo Joo Kim, LIV Golf 2026 format change, Fowler/Spieth Valero storyline, Gary Woodland Masters debut
- **Stories (7):** Tiger Masters status 9 days (T1), Valero Texas Open starts Thursday (T1), Masters countdown 9 days (T2→T1), Chevron Championship/Kim (T2), LIV Golf 72-hole format (T2), Fowler/Spieth at Valero (T3), Woodland Masters debut (T3)
- **X Posts:** 10 written, all under 280 characters
- **Facebook Posts:** 14 (long-form + caption for each of 7 stories)
- **Articles:** 5 (Stories 1-5)
- **PostPlanner exports:** gfr-postplanner-2026-03-31.xlsx (24 posts) + gfr-postplanner-tobi-2026-03-31.xlsx (17 TOBI posts)
- **Dashboard:** Generated at Golf/golf-content-2026-03-31/review-dashboard.html (29 items)
- **Key facts:** Tiger in Masters field but status TBD (DUI charges pending). Valero starts Thursday, Fleetwood +1400 favorite, winner gets final Masters spot. Masters is 90th edition, Scheffler +480, McIlroy defending. Kim enters Chevron on back-to-back wins, shot two 61s at Ford Championship. LIV moves from 54 to 72 holes for 2026, Doral dropped. Woodland earns first Masters invite off Houston Open win.
- **Fact concerns:** Tiger Masters participation (MEDIUM — conflicting signals; Trump quote sourced, official confirmation pending). All other key facts HIGH confidence.

## Pipeline Run: 2026-03-30
- **Research:** 5 web searches covering Houston Open final results, LPGA Ford Championship final, Tiger Woods DUI charges update, Masters field update, Valero Texas Open preview
- **Stories (7):** Woodland wins Houston (T1), Tiger DUI charges/mugshot (T1), Hyo Joo Kim back-to-back LPGA wins (T1), Masters 10 days out (T2), Valero Texas Open preview (T2), Lydia Ko 4th (T3), Grand Slam chasers (T3)
- **X Posts:** 10 written, all under 280 characters
- **Facebook Posts:** 14 (long-form + caption for each of 7 stories)
- **Articles:** 5 (Stories 1-5)
- **PostPlanner exports:** gfr-postplanner-2026-03-30.xlsx + gfr-postplanner-tobi-2026-03-30.xlsx (10 posts each)
- **Dashboard:** Generated at Golf/golf-content-2026-03-30/review-dashboard.html
- **Key facts:** Woodland 21-under 259 (new course record, wins by 5). Kim first LPGA player with two 61s in same tournament. Tiger mugshot released, formal DUI charges. Masters field ~92 players, Scheffler +480. Valero Texas Open starts April 2.
- **Fact concerns:** All published facts HIGH or MEDIUM confidence. Gary Player Grand Slam year (1965) marked MEDIUM — consistently stated in sources but single-source for this session.

## Notes

### Pipeline Run: 2026-03-29
- **Research:** 12 web searches covering PGA Tour (Houston Open R4), LPGA (Ford Championship final day), LIV Golf (South Africa recap), Masters preview, Tiger Woods DUI arrest, Rory McIlroy injury/documentary, Scottie Scheffler withdrawal, Jon Rahm, ball rollback
- **Stories:** 7 stories tiered (3x T1, 3x T2, 1x T3)
- **Coverage:** PGA Tour (2), LPGA (1), LIV Golf (1), Masters Preview (1), Tiger/breaking (1), Rules (1)
- **X Posts:** 8 posts across 7 stories (8 AM – 8:30 PM ET), all verified under 280 chars
- **Facebook Posts:** 14 posts (7 long-form + 7 image captions)
- **Articles:** 6 HTML5 articles (Stories 1–6)
- **Scripts run:**
  - `verify-facts.py`: 24 claims, 63 HIGH confidence; image warnings expected (not_started)
  - `compile-content-data.py`: 7 stories, 8 tweets, 6 articles compiled to JSON
  - `generate-review-dashboard.py`: Dashboard HTML generated (28 items)
  - `publish-unified-dashboard.py`: Push to content-dashboards failed (PAT scope limited to content-pipeline)
  - `generate-postplanner-export.py`: `gfr-postplanner-2026-03-29.xlsx` (22 posts)
  - `generate-postplanner-export.py --tobi`: `gfr-postplanner-tobi-2026-03-29.xlsx` (15 TOBI posts)
- **Key facts note:** Houston Open R4 was in progress at research time; articles cover Woodland leading entering Sunday — final result not confirmed. Tiger Woods DUI arrest: all facts from ABC/NPR/CNN — HIGH confidence.
- **Files created:**
  - `golf-content-2026-03-29/00-daily-brief.md` through `07-image-manifest.md`
  - `golf-content-2026-03-29/articles/article-01` through `article-06`

### Pipeline Run: 2026-03-28
- **Research:** Web searches across PGA Tour (Houston Open), LPGA (Ford Championship, Founders Cup), LIV Golf (Singapore/South Africa)
- **Stories:** 7 stories tiered (2x T1, 4x T2, 1x T3)
- **Coverage:** PGA Tour (2), LPGA (2), LIV Golf (1), Masters Preview (2)
- **X Posts:** 9 posts across 6 time slots (8 AM - 8:30 PM ET), all verified under 280 chars
- **Facebook Posts:** 14 posts (7 long-form + 7 image captions)
- **Articles:** 5 HTML5 articles written with semantic structure and "What's Next" sections
- **Scripts run:**
  - `verify-facts.py`: 36 claims, 80% HIGH confidence; advisory warnings (missing article for Story 6 — expected, 5 articles per instructions)
  - `compile-content-data.py`: 7 stories, 9 tweets, 5 articles compiled to JSON
  - `generate-review-dashboard.py`: Dashboard HTML generated (28 items)
  - `publish-unified-dashboard.py`: Push to content-dashboards failed (PAT scope limited to content-pipeline)
  - `generate-postplanner-export.py`: `gfr-postplanner-2026-03-28.xlsx` (23 posts)
  - `generate-postplanner-export.py --tobi`: `gfr-postplanner-tobi-2026-03-28.xlsx` (16 TOBI posts)
- **Files created:**
  - `golf-content-2026-03-28/00-daily-brief.md`
  - `golf-content-2026-03-28/01-research-notes.md`
  - `golf-content-2026-03-28/02-story-analysis.md`
  - `golf-content-2026-03-28/03-social-posts-x.md`
  - `golf-content-2026-03-28/04-social-posts-facebook.md`
  - `golf-content-2026-03-28/05-image-concepts.md`
  - `golf-content-2026-03-28/06-fact-check-log.md`
  - `golf-content-2026-03-28/07-content-data.json`
  - `golf-content-2026-03-28/07-image-manifest.md`
  - `golf-content-2026-03-28/review-dashboard.html`
  - `golf-content-2026-03-28/articles/article-01-woodland-leads-houston-open-brain-surgery-comeback.html`
  - `golf-content-2026-03-28/articles/article-02-lydia-ko-shoots-60-ford-championship.html`
  - `golf-content-2026-03-28/articles/article-03-dechambeau-liv-back-to-back-march-dominance.html`
  - `golf-content-2026-03-28/articles/article-04-masters-2026-preview-scheffler-mclroy-grand-slam.html`
  - `golf-content-2026-03-28/articles/article-05-scheffler-wd-houston-open-grand-slam-chasers.html`
  - `Golf/postplanner-imports/gfr-postplanner-2026-03-28.xlsx`
  - `Golf/postplanner-imports/gfr-postplanner-tobi-2026-03-28.xlsx`
- **Key events covered:** Texas Children's Houston Open (PGA Tour, Moving Day), Ford Championship (LPGA, Phoenix), DeChambeau LIV March sweep, Masters 2026 preview

### Pipeline Run: 2026-03-20 (First Run)
- **Research:** 10+ web searches across PGA Tour, LIV Golf, LPGA, OWGR, merger news, injuries
- **Stories:** 7 stories tiered (1x T1, 5x T2, 1x T3)
- **Coverage:** PGA Tour (2), LIV Golf (1), LPGA (1), Business (1), Injuries (1), Rankings (1)
- **X Posts:** 10 posts across 6 time slots (8 AM - 8:30 PM ET), all verified under 280 chars
- **Files created:**
  - `golf-content-2026-03-20/00-daily-brief.md`
  - `golf-content-2026-03-20/01-verified-facts.md`
  - `golf-content-2026-03-20/02-story-analysis.md`
  - `golf-content-2026-03-20/03-social-posts-x.md`
- **Also updated:** `story-history.md`, `pipeline-status.md`
- **Remaining steps:** FB posts, image concepts, articles, fact-check script, dashboard generation, publishing
- **Key events this week:** Valspar Championship (PGA Tour, R2 today), LIV Golf South Africa (R2 today), Fortinet Founders Cup (LPGA, R2 today)
