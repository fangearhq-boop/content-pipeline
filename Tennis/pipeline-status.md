# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-08-27 |
| Writing | Complete (all steps) | 2026-08-27 |
| Fact-check | Complete (verify-facts.py run — 5 stories, 38 claims, 64 HIGH) | 2026-08-27 |
| Compile | Complete (07-content-data.json — 5 stories, 6 X posts, 5 articles, 26 items) | 2026-08-27 |
| Dashboard | Complete (review-dashboard.html, 26 items) | 2026-08-27 |
| PostPlanner Export | 0 posts (parser compat known issue — posts exported to social files but not picked up by exporter) | 2026-08-27 |
| WordPress Publish | Attempted — proxy blocks WordPress API (same as all prior runs) | 2026-08-27 |
| Dashboard Push | Attempted — proxy lacks write access to content-dashboards repo (same as all prior runs) | 2026-08-27 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-08-27 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** 0 posts (known parser compat issue — same as prior runs)
- **Key stories:** US Open 2026 draw revealed (Zverev No. 1, Alcaraz No. 2, Sabalenka No. 1, Eala historic first Filipino Grand Slam seed, 14+ withdrawals, Sinner absent, main draw Sunday Aug 30); Alcaraz confirms US Open return skipping Winston-Salem (tenosynovitis right wrist, missed French Open/Wimbledon/Toronto/Cincinnati, going directly to US Open as No. 2 seed); Jordan Lee + American teens all fall in qualifying R2 (Lee lost to Rincon 6-3, 4-6, 6-1, Antonius + Johnson also out); Qualifying final day (Day 4, 32 qualifiers complete the field); Winston-Salem Open SF day (final Aug 29, Alcaraz not in draw)
- **Issues:** image manifest all not_started (expected for imagn source); posting window warnings cosmetic (known issue); FB posts 0 in compile (known parser issue); PostPlanner 0 posts (known parser issue); WordPress blocked by proxy; dashboard push blocked by proxy (content-dashboards not in session authorized repos)
- **Story history:** Updated with all 5 stories
- **Key correction:** Alcaraz did NOT compete at Winston-Salem — confirmed going directly to US Open (prior pipeline Aug 25 S3, Aug 26 S5 assumed Winston-Salem based on reports; updated based on official confirmation today)

### 2026-08-26 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts (6 in PostPlanner) + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-08-26.xlsx (6 posts 13:10–20:30 ET), tfr-postplanner-tobi-2026-08-26.xlsx (6 TOBI posts)
- **Key stories:** Serena/Alcaraz out in mixed doubles QF (lost to Cobolli/Bencic 5-4(4), 4-1 after winning R1 5-3, 4-1 same day); Federer exhibition recap (def. Roddick 6-3 singles, Federer/McEnroe def. Roddick/Agassi 7-5 doubles; Wintour coin toss, McConaughey hype reel, Serena/Ruud/Eala/Auger-Aliassime courtside); US Open draw ceremony today noon ET (Zverev/Sabalenka No. 1, Eala first Grand Slam seed, 14+ withdrawals, Alcaraz No. 2); Qualifying Day 3 (Jordan Lee R2 vs Rincon, Fearnley R2, Andreescu in women's qualifying); Winston-Salem QF/SF (Alcaraz wildcard first tournament since April wrist injury)
- **Issues:** image manifest all not_started (expected for imagn source); posting window warnings cosmetic (known issue); FB posts 0 in compile (known parser issue); WordPress blocked by proxy; dashboard push blocked by proxy (content-dashboards not in session authorized repos)
- **Story history:** Updated with all 5 stories
