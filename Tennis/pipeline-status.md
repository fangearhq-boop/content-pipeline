# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-06-19 |
| Writing | Complete (all steps) | 2026-06-19 |
| Fact-check | Complete (verify-facts.py passed — 5 stories, 43 claims, 86 HIGH; image not_started warnings cosmetic/expected for imagn) | 2026-06-19 |
| Compile | Complete (07-content-data.json — 5 stories, 6 X posts, 0 FB posts, 5 articles, 5 images; posting window warnings cosmetic) | 2026-06-19 |
| Dashboard | Complete (review-dashboard.html, 21 items) | 2026-06-19 |
| PostPlanner Export | Complete (standard 6 posts; TOBI 6 posts) | 2026-06-19 |
| WordPress Publish | Attempted — proxy blocks WordPress API (same as all previous runs) | 2026-06-19 |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | 2026-06-19 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-06-19 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Elena Voss [S1, S4], Marcus Cole [S2, S5], Ryan Calloway [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-19.xlsx (6 posts), tfr-postplanner-tobi-2026-06-19.xlsx (6 TOBI posts)
- **Coverage:** Fritz vs Shelton Halle QF rematch (5 days after Stuttgart final; Shelton 6-win streak, Fritz 5-1 grass); Queen's Club QF Day — de Minaur vs Nakashima, Paul vs Davidovich Fokina (both unbeaten in sets), Fery vs Cerundolo, Hijikata (who upset Lehecka 4-6, 7-5, 7-6(7)) in draw; Berlin WTA QF — Sabalenka vs Bartunkova, Badosa vs Noskova, Pegula vs Keys (final Sunday June 21); Wimbledon countdown — draw June 26, qualifying Monday June 22, Sinner cold (no ATP grass warm-ups), Alcaraz out (wrist), Williams sisters doubles wildcard, £64.2M prize; Nottingham QF — Fernandez upset by Sonmez 6-4, 7-6(1)
- **Notes:**
  - CORRECTION from June 18: Paul was NOT upset by van de Zandschulp (as reported). Multiple June 19 sources confirm Paul is alive in QF vs Davidovich Fokina. Real upset: Hijikata def. Lehecka (No. 2 seed) 4-6, 7-5, 7-6(7). This was a WebFetch distortion in June 18 pipeline.
  - verify-facts.py: passed; 43 claims, 86 HIGH; image not_started warnings cosmetic (imagn source, expected)
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images; posting window warnings cosmetic
  - dashboard: 21 items
  - PostPlanner exports: standard (6 posts) and TOBI (6 posts) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

### 2026-06-18 — Full Pipeline Run
- **Steps completed:** All 15
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 6 X posts + 5 FB posts (5 long-form + 5 captions) = 11 total
- **Articles:** 5 (bylines: Marcus Cole [S1, S4], Ryan Calloway [S2, S5], Elena Voss [S3])
- **PostPlanner exports:** tfr-postplanner-2026-06-18.xlsx (6 posts), tfr-postplanner-tobi-2026-06-18.xlsx (6 TOBI posts)
- **Coverage:** Halle R16 sweep; Badosa stuns Gauff 1-6, 6-3, 6-2 in Berlin; van de Zandschulp result noted as incorrect on June 19; Berlin QF set; Wimbledon countdown 11 days
- **Notes:** WordPress proxy error; Dashboard push failed; Correction: Paul vs van de Zandschulp story was inaccurate — Paul alive in QF per June 19 sources

### 2026-06-16 — Full Pipeline Run
- **Steps completed:** All 15
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Articles:** 5 (bylines: Ryan Calloway [S1, S4], Elena Voss [S2, S5], Marcus Cole [S3])
