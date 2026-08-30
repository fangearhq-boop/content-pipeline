# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-08-30 |
| Writing | Complete (all steps) | 2026-08-30 |
| Fact-check | Complete (verify-facts.py run — 5 stories, 41 claims) | 2026-08-30 |
| Compile | Complete (07-content-data.json — 5 stories, 7 X posts, 5 articles, 22 items) | 2026-08-30 |
| Dashboard | Complete (review-dashboard.html, 22 items) | 2026-08-30 |
| PostPlanner Export | 0 posts (parser compat known issue) | 2026-08-30 |
| WordPress Publish | Attempted — proxy blocks WordPress API (same as all prior runs) | 2026-08-30 |
| Dashboard Push | Attempted — proxy lacks write access to content-dashboards repo (same as all prior runs) | 2026-08-30 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-08-30 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Elena Voss [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** 0 posts (known parser compat issue — same as prior runs)
- **Key stories:** Buse wins Winston-Salem 6-3, 6-2 over Fery (youngest champion at 22y 5m, first Peruvian since 2004); US Open Day 1 opens (Djokovic vs. Navone tonight 7 PM ET, Rybakina vs. Frodin, Pegula vs. Ruse, Venus Williams vs. Kenin); Venus Williams eliminated R1 by Kenin (focuses on doubles with Serena — Serena's first Grand Slam since 2022 retirement, 14-time Grand Slam doubles champs); Rybakina entered singles draw despite not practicing since Cincinnati ankle injury; Alcaraz returns Monday vs. Safiullin (first match since April), Eala opens Monday vs. Stoiana (historic No. 17 seed)
- **Issues:** image manifest all not_started (expected for imagn source); compile posting-window warnings cosmetic (known); PostPlanner 0 posts (known parser issue); WordPress blocked by proxy; dashboard push blocked by proxy (content-dashboards not in session authorized repos)
- **Story history:** Updated with all 5 stories

### 2026-08-29 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 5 FB posts (5 long-form + 5 captions) = 12 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** 0 posts (known parser compat issue — same as prior runs)
- **Key stories:** Winston-Salem final Fery (GBR) vs. Buse (PER) at 4 PM ET — first ATP final for both, first Peruvian finalist since 2004; US Open main draw preview (starts Aug 30, Zverev No. 1, Alcaraz No. 2 returning from 4+ months, Sabalenka three-peat bid, Rybakina ankle doubt); Rybakina still not practicing (MRI done, "hasn't been on court yet"); Roger Federer Hall of Fame induction tonight 6:30 PM ET Newport RI (Tennis Channel); Eala No. 17 seed opens US Open vs. qualifier Sunday
- **Issues:** image manifest all not_started (expected for imagn source); compile posting-window warnings cosmetic (known); PostPlanner 0 posts (known parser issue); WordPress blocked by proxy; dashboard push blocked by proxy (content-dashboards not in session authorized repos)
- **Story history:** Updated with all 5 stories

### 2026-08-28 — Full Pipeline Run
- **Steps completed:** All 15
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 8 X posts + 5 FB posts = 13 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **Key stories:** US Open 2026 full preview; Rybakina ankle injury follow-up; Winston-Salem SF day; Eala No. 17 seed; Arthur Fils Cincinnati champion draws Tsitsipas R1

## Known Issues (Recurring)
- WordPress publish: 403 proxy block — articles queued as drafts, pending manual publish or proxy fix
- PostPlanner export: parser compat issue returns 0 posts every run
- content-dashboards push: 403 proxy block (not in session authorized repo set)
- Image manifest warnings from dashboard generator: expected (imagn images are sourced separately)
