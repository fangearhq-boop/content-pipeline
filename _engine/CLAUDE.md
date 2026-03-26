# FanGear HQ Content Engine — Project Rules

## Architecture
- This is the SHARED engine powering ALL FanGear HQ niche content brands. Do NOT modify it for niche-specific behavior.
- Each niche has its own thin SKILL.md that reads this engine first, then applies brand-specific configuration.
- Niche-specific values come from `niche-config.yaml` — referenced throughout as `{CONFIG.*}`.
- Always read the niche's `niche-config.yaml` and `brand-guide.md` before starting the pipeline.

## Pipeline Order (15 Steps — Sequential)
Steps must execute in order. Each step depends on the previous:
1. Research (web search)
2. Story History Check (NEW STORY / FOLLOW UP / SKIP)
3. Daily Brief → `00-daily-brief.md`
4. Research Notes → `01-research-notes.md`
5. Story Analysis → `02-story-analysis.md`
6. X/Twitter Posts → `03-social-posts-x.md`
7. Facebook Posts → `04-social-posts-facebook.md`
8. Image Concepts → `05-image-concepts.md`
9. Articles → `articles/article-NN-slug-title.html`
10. Fact-Check → `06-fact-check-log.md` (run `verify-facts.py`)
10b. Compile Content Data → `07-content-data.json` (run `compile-content-data.py`)
11. Image Production → `07-image-manifest.md`
12. Story History Update → append to `story-history.md`
13. Generate Dashboard → `review-dashboard.html` (run `generate-review-dashboard.py`)
14. Review & Export (interactive dashboard, PostPlanner XLSX export)
15. Publish to GitHub Pages (run `publish-dashboard.py`)

Steps 6-8 (X posts, FB posts, image concepts) CAN run concurrently.

## Content Folder Structure
```
{content_prefix}-YYYY-MM-DD/
├── 00-daily-brief.md
├── 01-research-notes.md
├── 02-story-analysis.md
├── 03-social-posts-x.md
├── 04-social-posts-facebook.md
├── 05-image-concepts.md
├── 06-fact-check-log.md
├── 07-content-data.json    ← compiled from markdown by compile-content-data.py
├── 07-image-manifest.md
├── articles/
│   └── article-NN-slug-title.html
├── generated-images/ (for Gemini niches)
└── review-dashboard.html
```

## Tier Assignment Rules
- **Tier 1** (Breaking/Trending): Article + 2 X Text Posts (different angles) + FB Long-Form + FB Image Caption + 2 image concepts.
- **Tier 2** (Today/Upcoming): 1-2 X Text Posts + FB Long-Form + FB Image Caption + 2 image concepts. Optional article.
- **Tier 3** (Evergreen): 1 X Text Post + FB Long-Form + FB Image Caption + 1-2 image concepts.
- Every social post MUST have a posting window assigned.

## X/Twitter Character Rules
- Absolute limit: 280 characters.
- URLs count as 23 characters regardless of actual length.
- Hashtags count as written (e.g., #ParentingTips = 14 chars).
- After writing, always verify character count with URLs normalized to 23.

## Photo Source Rules (Config-Driven)
- **imagn** (sports): ONLY "PlayerName Organization" search terms. NO years, NO context, NO event names. Credit: "(USA TODAY Sports Images)" or "(Imagn Images)".
- **stock** (Unsplash/Pexels): Descriptive search terms, diverse representation, no credit needed.
- **gemini** (AI-generated): Detailed visual prompts with scene, mood, lighting, style. Mode `base_only` = clean backgrounds for Canva text overlay. Mode `complete` = finished graphic with text baked in.

## Article Format
- Filename: `article-NN-slug-title.html` (NN = two-digit story number, slug = lowercase hyphenated, no spaces/underscores).
- Semantic HTML5: `<article>`, `<header>`, `<figure>`, `<section>` tags. NO inline styles, NO CSS, NO JavaScript.
- Must include "What's Next" closing section — MANDATORY.
- Word count: `{CONFIG.article_word_count_min}` to `{CONFIG.article_word_count_max}`.

## Image Manifest (07-image-manifest.md)
- Format: YAML with header (pipeline_date, brand_kit_id, photo_source).
- Status lifecycle: `not_started` → `photo_selected`/`imagn_selected`/`gemini_generated` → `canva_uploaded` → `design_created` → `exported`.
- Social image dimensions: 1080x1350 (4:5 vertical) for ALL social platforms (X, Facebook, Instagram).
- Article hero dimensions: 1200x630 (1.91:1 landscape) — only for articles and Open Graph.

## Story Headers
All pipeline markdown files use `### STORY N:` headers to delimit stories. Scripts parse by this pattern.

## Scripts (in `scripts/`)
- `verify-facts.py` — Consistency + fact-check + image manifest validation. Generates `06-fact-check-log.md`. Auto-detects niche from cwd or uses `--niche` flag.
- `compile-content-data.py` — Reads all markdown content files and produces `07-content-data.json`. Must run AFTER fact-check (Step 10) and BEFORE dashboard generation (Step 13). Auto-detects niche or uses `--niche` flag. Validates completeness and reports char-count violations.
- `generate-review-dashboard.py` — Creates interactive review dashboard HTML. Auto-detects niche. Prefers `07-content-data.json` (v2.0) when available; falls back to markdown parsing.
- `generate-gemini-image.py` — AI image generation via Gemini API. Requires `GEMINI_API_KEY` env var. Tracks daily cost. Has `--dry-run` and `--budget` flags.
- `publish-dashboard.py` — Publishes dashboards to GitHub Pages. Generates index.html, git add/commit/push.
- `query-fanrumor-traffic.py` — Queries GA4 for fanrumor.com traffic, filters to softball content, outputs `fanrumor-traffic.json`. Requires `GA4_SERVICE_ACCOUNT_JSON` env var. Dashboard generator auto-loads this file to render Content Performance panel.

## Daily Operations

### Session Start (EVERY session before any content work)
1. Read `{NICHE}/pipeline-status.md` — check if today's pipeline already started, resume from last step
2. Read `{NICHE}/niche-config.yaml` and `_engine/CLAUDE.md`
3. Verify git health: `git fetch origin main && git status` in each niche dashboard repo
4. Verify GitHub Pages: `gh api repos/{ORG}/{REPO}/pages --jq '{build_type, status}'` — must be `"workflow"` not `"legacy"`

### Operational Runbook
Full step-by-step checklist: `_engine/daily-runbook.md`

### Per-Niche State Tracking
Each niche has `pipeline-status.md` at its root. Update after every pipeline run:
- Last run date and steps completed
- Deploy info (repo, build type, Pages URL)
- Issues encountered and their fixes
- Pipeline run log (newest at top)

This is the cross-session recovery mechanism — if context runs out mid-pipeline, the next session reads this file and resumes.

### Multi-Niche Sequence
When running multiple niches: **Softball first** (more complex — FB + images + articles), then **Cubs** (simpler — X-only).

### GitHub Pages Deployment
`publish-dashboard.py` handles all deployment automatically:
- Creates `.nojekyll` and `.github/workflows/deploy-pages.yml` if missing
- Switches legacy Jekyll builds to workflow mode via `gh` CLI
- Verifies deployment after push (polls build status, checks content)
- See `_engine/daily-runbook.md` Troubleshooting section for manual fixes

## Quality Gates
- All HIGH priority claims for Tier 1 stories must be verified before dashboard generation.
- Consistency check (Step 10) must pass before generating the dashboard (Step 13).
- Every story in the daily brief must have entries in ALL downstream files.
- All facts in verified-facts files must meet the confidence requirements below before use in articles.

## Fact Verification Protocol (MANDATORY)

WebFetch and web search AI summaries can distort, merge, or hallucinate facts from source pages.
**Never treat a WebFetch summary as a verified fact.** Treat it as a lead to investigate.

### Three Rules

**1. Two-Source Rule for Compound Claims**
Any fact linking multiple named entities (e.g., "X joins Y and Z as the only players to...") MUST be verified against a second independent source before being marked as verified. This is the highest-risk category for AI summarization errors — the summarizer may conflate separate comparisons into one false statement.

**2. Biographical Facts Get Primary-Source Verification**
Ages, birthdays, birth places, draft positions, and career timelines must be verified from a reference source (Pro Football Reference, Baseball Reference, Wikipedia, official team bio page). Never infer these from a summarized article or calculate ages from estimated birth years.

**3. Superlative and Historical Claims Need Explicit Verification**
Claims containing "first to...", "only player to...", "franchise record...", "ties the record for..." must be verified against the actual record book or a second source. These are the most commonly distorted claims in AI summaries.

### Confidence Tagging for Fact Sheets

When building a verified-facts file (or equivalent research document), tag each fact:

| Confidence | Meaning | Use in Articles |
|------------|---------|-----------------|
| **HIGH** | Verified from 2+ independent sources | Use freely |
| **MEDIUM** | Single source, not cross-referenced | Use, but flag for review during fact-check step |
| **LOW** | Inferred from AI summary or calculated | Do NOT use in articles without upgrading to HIGH first |

### Common WebFetch Distortion Patterns
- **Entity conflation**: "X and Y are both Broncos QBs who..." when Y never played for that team
- **Scope creep**: An NFL-wide stat gets attributed to a single team
- **Date/age drift**: Birth dates shifted by a month or year, ages off by one
- **Superlative inflation**: "one of the best" becomes "the best" or "the only"
- **Quote misattribution**: A quote from one person gets attached to another, or the context changes

<!-- GSD-inspired: 2026-02-23 — Project-specific verification and decisions -->
<!-- To remove: delete everything between the GSD-inspired comment tags -->

## Verification Checklist
For any engine change, confirm:
- [ ] Change is niche-agnostic — no niche-specific behavior in the engine (use `{CONFIG.*}` references)
- [ ] Pipeline step ordering preserved (steps are sequential except 6-8 which can be concurrent)
- [ ] All `### STORY N:` header patterns maintained — scripts parse by this pattern
- [ ] `verify-facts.py` still passes on existing content after changes
- [ ] Article format: semantic HTML5, no inline styles/CSS/JS, "What's Next" section present
- [ ] Image manifest YAML structure unchanged (status lifecycle intact)
- [ ] X/Twitter posts verified under 280 chars with URLs normalized to 23
- [ ] Tier assignment rules followed (Tier 1/2/3 content requirements)
- [ ] Dashboard generation (`generate-review-dashboard.py`) still produces valid HTML

## Decision Log
Append-only. Record WHY, not just WHAT.

- **2026-02-23:** Engine is shared, niches are thin — avoids duplicating pipeline logic across brands. Niche-specific config lives in `niche-config.yaml` and `brand-guide.md` only.
- **2026-02-23:** Three photo source modes (imagn/stock/gemini) — different niches have different image needs. Config-driven so engine code doesn't branch on niche name.
- **2026-03-05:** Added daily-runbook.md, pipeline-status.md per niche, and hardened publish-dashboard.py — daily pipeline was running into different errors each day (Pages build failures, stale Jekyll, missing .nojekyll). Solution: pre-flight checks, auto-fix infrastructure, post-deploy verification, and cross-session state tracking.
- **2026-03-17:** Added Fact Verification Protocol — WebFetch AI summary of a Broncos team article said "Joins Peyton Manning and Justin Herbert as Broncos QBs" when the actual stat was NFL-wide (Herbert is a Charger, never a Bronco). The bad fact propagated from a verified-facts file into 2 of 5 articles. Also caught age/birthday errors from AI summaries. Solution: two-source rule for compound claims, primary-source verification for biographical data, confidence tagging (HIGH/MEDIUM/LOW) for fact sheets, and explicit warning about WebFetch distortion patterns.
- **2026-03-22:** Added Content Performance panel to softball dashboard — queries GA4 for fanrumor.com traffic, filters to softball articles by keyword matching on page titles. Pipeline-time bake-in approach (query GA4 during pipeline run, embed data into static dashboard HTML) chosen over client-side API calls because the dashboard is static GitHub Pages and data freshness from daily pipeline runs is sufficient. Softball dominates fanrumor.com traffic (~68% of all pageviews). Uses the sports-digest service account (`sports-digest@sports-news-digest.iam.gserviceaccount.com`) which has Viewer access on the GA4 property. GA4 property ID for fanrumor.com: 377089089.

<!-- /GSD-inspired: 2026-02-23 -->
