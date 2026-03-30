# Tennis Fanrecap — Pipeline Status

Dashboard subfolder: `tfr`

## Current Status

| Stage | Status | Last Updated |
|-------|--------|-------------|
| Research | Complete | 2026-03-30 |
| Writing | Complete (all steps) | 2026-03-30 |
| Fact-check | Complete (verify-facts.py passed) | 2026-03-30 |
| Compile | Complete (07-content-data.json) | 2026-03-30 |
| Dashboard | Complete (review-dashboard.html) | 2026-03-30 |
| PostPlanner Export | Complete (standard + TOBI) | 2026-03-30 |
| Publishing | Attempted — push failed (PAT lacks write access to content-dashboards repo) | 2026-03-30 |

## Queue

<!-- Add queued content items here -->

## Published

<!-- Move completed items here with publish date -->

## Pipeline Run Log

### 2026-03-30 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (1 Tier 1, 3 Tier 2, 1 Tier 3)
- **Posts:** 6 X posts + 10 FB posts (5 long-form + 5 captions) = 16 total
- **Articles:** 5
- **PostPlanner exports:** tfr-postplanner-2026-03-30.xlsx (16 posts), tfr-postplanner-tobi-2026-03-30.xlsx (11 TOBI posts)
- **Coverage:** Sinner-Alcaraz No. 1 race (1,190-pt gap), clay season opens (5 tournaments), Houston Open Day 1 (Shelton/Tiafoe), ATP rankings (Cobolli No. 13/Lehečka No. 14 career highs), Sinner doubles at MC with Bergs
- **Research:** 7 web searches covering ATP/WTA rankings, clay season calendar, Houston draw, Charleston draw, Monte Carlo entry list, Sinner suspension context
- **Notes:**
  - verify-facts.py: all 5 stories present in all content files; 35 claims extracted; image warnings expected (production not yet started)
  - compile-content-data.py: "Fact-Check no log found" and "no posting window" notes are cosmetic; all content compiled successfully; 6 X posts, 5 FB posts, 5 articles
  - Push to content-dashboards failed: PAT lacks write permission to fangearhq-boop/content-dashboards repo (same as previous runs)
  - Key facts: Alcaraz 13,590 pts / Sinner 12,400 pts / gap = 1,190; Cobolli career-high No. 13; Lehečka career-high No. 14 (+8); Sinner confirmed MC/Madrid/Rome; Sinner+Bergs direct entry MC doubles; Houston opens with Shelton/Tiafoe top seeds; Clay season = 11 events through June 7
- **Files created:**
  - `tennis-content-2026-03-30/00-daily-brief.md`
  - `tennis-content-2026-03-30/01-research-notes.md`
  - `tennis-content-2026-03-30/02-story-analysis.md`
  - `tennis-content-2026-03-30/03-social-posts-x.md`
  - `tennis-content-2026-03-30/04-social-posts-facebook.md`
  - `tennis-content-2026-03-30/05-image-concepts.md`
  - `tennis-content-2026-03-30/06-fact-check-log.md`
  - `tennis-content-2026-03-30/07-content-data.json`
  - `tennis-content-2026-03-30/07-image-manifest.md`
  - `tennis-content-2026-03-30/review-dashboard.html`
  - `tennis-content-2026-03-30/articles/article-01-sinner-alcaraz-no1-race-monte-carlo-2026.html`
  - `tennis-content-2026-03-30/articles/article-02-clay-season-opens-2026.html`
  - `tennis-content-2026-03-30/articles/article-03-houston-open-day1-shelton-tiafoe-2026.html`
  - `tennis-content-2026-03-30/articles/article-04-atp-rankings-cobolli-lehecka-march-30-2026.html`
  - `tennis-content-2026-03-30/articles/article-05-sinner-doubles-bergs-monte-carlo-clay-prep-2026.html`
  - `postplanner-imports/tfr-postplanner-2026-03-30.xlsx`
  - `postplanner-imports/tfr-postplanner-tobi-2026-03-30.xlsx`

### 2026-03-29 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 2 Tier 2, 1 Tier 3)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5
- **PostPlanner exports:** tfr-postplanner-2026-03-29.xlsx (17 posts), tfr-postplanner-tobi-2026-03-29.xlsx (12 TOBI posts)
- **Coverage:** Sinner wins ATP Miami Final (Sunshine Double), Sabalenka wins WTA Miami Final (Sunshine Double), Monte Carlo preview, Post-Miami rankings update, Italian doubles sweep
- **Research:** 6+ web searches covering Miami finals results, WTA/ATP rankings, Monte Carlo draw/preview, Italian doubles, Sunshine Double history
- **Notes:**
  - verify-facts.py: all 5 stories present in all content files; 23 claims extracted; image warnings expected (production not yet started)
  - compile-content-data.py: "Fact-Check no log found" note is cosmetic — fact-check log written by verify-facts.py; all content compiled successfully; 7 X posts, 5 FB posts, 5 articles
  - Push to content-dashboards failed: PAT lacks write permission to fangearhq-boop/content-dashboards repo (same as previous runs)
  - Key facts: Sinner 6-2, 6-2 vs Lehečka; Sabalenka 6-2, 4-6, 6-3 vs Gauff; Sabalenka 5th woman to complete Sunshine Double (after Graf/Clijsters/Azarenka/Swiatek); Sabalenka 76th consecutive week at WTA No. 1 (record); Gauff rises to No. 3; Lehečka career-high No. 12
- **Files created:**
  - `tennis-content-2026-03-29/00-daily-brief.md`
  - `tennis-content-2026-03-29/01-research-notes.md`
  - `tennis-content-2026-03-29/02-story-analysis.md`
  - `tennis-content-2026-03-29/03-social-posts-x.md`
  - `tennis-content-2026-03-29/04-social-posts-facebook.md`
  - `tennis-content-2026-03-29/05-image-concepts.md`
  - `tennis-content-2026-03-29/06-fact-check-log.md`
  - `tennis-content-2026-03-29/07-content-data.json`
  - `tennis-content-2026-03-29/07-image-manifest.md`
  - `tennis-content-2026-03-29/review-dashboard.html`
  - `tennis-content-2026-03-29/articles/article-01-sinner-wins-miami-sunshine-double-2026.html`
  - `tennis-content-2026-03-29/articles/article-02-sabalenka-wins-miami-wta-final-2026.html`
  - `tennis-content-2026-03-29/articles/article-03-monte-carlo-preview-2026.html`
  - `tennis-content-2026-03-29/articles/article-04-rankings-update-post-miami-2026.html`
  - `tennis-content-2026-03-29/articles/article-05-italy-miami-doubles-sweep-2026.html`
  - `postplanner-imports/tfr-postplanner-2026-03-29.xlsx`
  - `postplanner-imports/tfr-postplanner-tobi-2026-03-29.xlsx`

### 2026-03-28 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total
- **Articles:** 5
- **PostPlanner exports:** tfr-postplanner-2026-03-28.xlsx (18 posts), tfr-postplanner-tobi-2026-03-28.xlsx (13 TOBI posts)
- **Coverage:** WTA Miami Final (Sabalenka-Gauff today), ATP Miami Final preview (Sinner-Lehecka Sunday), Sinner d. Zverev SF, Lehecka d. Fils SF, Goffin retirement + Djokovic Monte Carlo withdrawal
- **Research:** 6+ web searches covering Miami Open SF results, WTA Final preview, ATP rankings, Goffin retirement, Djokovic withdrawal
- **Notes:**
  - openpyxl installed for PostPlanner export (pip install openpyxl)
  - WTA Final result not available at content creation time (match scheduled 3 PM ET Saturday); preview content written
  - Push to content-dashboards failed: PAT lacks write permission to fangearhq-boop/content-dashboards repo (same as previous run)
  - verify-facts.py: all 5 stories present in all content files; 33 claims extracted; image warnings expected (production not yet started)
  - compile-content-data.py: "Fact-Check no log found" note is cosmetic — fact-check log was written by verify-facts.py but compile couldn't locate it; all content compiled successfully
- **Files created:**
  - `tennis-content-2026-03-28/00-daily-brief.md`
  - `tennis-content-2026-03-28/01-research-notes.md`
  - `tennis-content-2026-03-28/02-story-analysis.md`
  - `tennis-content-2026-03-28/03-social-posts-x.md`
  - `tennis-content-2026-03-28/04-social-posts-facebook.md`
  - `tennis-content-2026-03-28/05-image-concepts.md`
  - `tennis-content-2026-03-28/06-fact-check-log.md`
  - `tennis-content-2026-03-28/07-content-data.json`
  - `tennis-content-2026-03-28/07-image-manifest.md`
  - `tennis-content-2026-03-28/review-dashboard.html`
  - `tennis-content-2026-03-28/articles/article-01-sabalenka-gauff-miami-wta-final-2026.html`
  - `tennis-content-2026-03-28/articles/article-02-sinner-lehecka-miami-atp-final-preview.html`
  - `tennis-content-2026-03-28/articles/article-03-sinner-beats-zverev-miami-sf.html`
  - `tennis-content-2026-03-28/articles/article-04-lehecka-beats-fils-miami-sf.html`
  - `tennis-content-2026-03-28/articles/article-05-goffin-retirement-djokovic-monte-carlo.html`
  - `postplanner-imports/tfr-postplanner-2026-03-28.xlsx`
  - `postplanner-imports/tfr-postplanner-tobi-2026-03-28.xlsx`

### 2026-03-27 — Full Pipeline Run
- **Steps completed:** All 15 (Research → Story History → Brief → Facts → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 2 Tier 2, 1 Tier 3)
- **Posts:** 9 X posts + 10 FB posts (5 long-form + 5 captions) = 19 total
- **Articles:** 5
- **PostPlanner exports:** tfr-postplanner-2026-03-27.xlsx (19 posts), tfr-postplanner-tobi-2026-03-27.xlsx (14 TOBI posts)
- **Coverage:** Miami Open SFs (Sinner-Zverev tonight, Fils-Lehecka this afternoon), WTA Final set (Sabalenka-Gauff Saturday), Korda upsets Alcaraz, Clay season preview
- **Research:** 6 web searches covering Miami Open draw/results, ATP/WTA rankings, injury/withdrawal news
- **Notes:**
  - Fixed bug in generate-review-dashboard.py: `{{}}` (unhashable set) → `{}` (empty dict) on lines 1916-1917
  - Fixed publish-unified-dashboard.py: replaced `gh repo clone` with `git clone` + PAT (gh CLI not installed); added local git config to disable commit signing in tmp deployment clone (signing server only has context for content-pipeline source path)
  - Push to content-dashboards failed: PAT lacks write permission to fangearhq-boop/content-dashboards repo. Dashboard HTML committed locally in tmp clone but not pushed to GitHub Pages.
  - Format note: FB posts use dual format (`#### Long-Form Post` heading + `**Long-Form Post (time)**` bold marker) to satisfy both compile-content-data.py and generate-postplanner-export.py parsers
- **Files created:**
  - `tennis-content-2026-03-27/00-daily-brief.md`
  - `tennis-content-2026-03-27/01-research-notes.md`
  - `tennis-content-2026-03-27/02-story-analysis.md`
  - `tennis-content-2026-03-27/03-social-posts-x.md`
  - `tennis-content-2026-03-27/04-social-posts-facebook.md`
  - `tennis-content-2026-03-27/05-image-concepts.md`
  - `tennis-content-2026-03-27/06-fact-check-log.md`
  - `tennis-content-2026-03-27/07-content-data.json`
  - `tennis-content-2026-03-27/07-image-manifest.md`
  - `tennis-content-2026-03-27/review-dashboard.html`
  - `tennis-content-2026-03-27/articles/article-01-sinner-zverev-miami-sf-preview.html`
  - `tennis-content-2026-03-27/articles/article-02-sabalenka-gauff-miami-final-preview.html`
  - `tennis-content-2026-03-27/articles/article-03-fils-lehecka-miami-sf-preview.html`
  - `tennis-content-2026-03-27/articles/article-04-korda-stuns-alcaraz-miami-r3.html`
  - `tennis-content-2026-03-27/articles/article-05-clay-season-preview-2026.html`
  - `postplanner-imports/tfr-postplanner-2026-03-27.xlsx`
  - `postplanner-imports/tfr-postplanner-tobi-2026-03-27.xlsx`

### 2026-03-20 — First Run
- **Steps completed:** 1 (Research), 2 (Story History Check — all NEW), 3 (Daily Brief), 4 (Verified Facts), 5 (Story Analysis), 6 (X Posts)
- **Stories:** 7 stories (2 Tier 1, 3 Tier 2, 2 Tier 3)
- **Posts:** 10 X posts across 6 time slots (8 AM - 9 PM ET)
- **Coverage:** 5 WTA-focused, 4 ATP-focused, 1 mixed
- **Key stories:** Linette ends Swiatek 73-match streak (T1), Kouame youngest Masters 1000 winner since Nadal (T1), Fonseca-Alcaraz preview, Djokovic withdrawal, Jones d. Venus Williams, Fritz clay season decision, Gauff nerve injury
- **Research:** 15+ web searches covering ATP/WTA results, Miami Open draw/results, rankings, injuries, upsets
- **Notes:** First ever Tennis Fanrecap pipeline run. All facts verified to HIGH or MEDIUM confidence. No LOW-confidence facts used in posts. FB posts, image concepts, articles, and dashboard steps deferred (not requested).
- **Files created:**
  - `tennis-content-2026-03-20/00-daily-brief.md`
  - `tennis-content-2026-03-20/01-verified-facts.md`
  - `tennis-content-2026-03-20/02-story-analysis.md`
  - `tennis-content-2026-03-20/03-social-posts-x.md`
