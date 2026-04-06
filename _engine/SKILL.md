---
name: fangearhq-content-engine
description: >
  **FanGear HQ Content Engine**: The shared pipeline that powers all FanGear HQ niche
  content brands. This engine defines the universal 15-step daily content production process
  including research, story selection, multi-platform content creation, fact-checking,
  image production, and review dashboard generation.

  DO NOT invoke this skill directly. Each niche has its own thin skill that reads this
  engine first, then applies brand-specific configuration (colors, voice, sources, etc.).
  See the niche's SKILL.md for triggers and brand config.
---

# FanGear HQ — Shared Content Engine

This is the universal content pipeline that powers every FanGear HQ niche brand.
Each niche skill reads this engine file first, then layers on its own brand configuration.

**Before executing any step**, you must have already read the niche's SKILL.md, which
provides the `niche-config.yaml` values referenced throughout this document as `{CONFIG.*}`.

## How Niche Config Works

Each niche folder contains a `niche-config.yaml` that defines:
- `brand_name` — display name (e.g., "I Love Softball")
- `content_prefix` — folder prefix (e.g., "softball-content")
- `photo_source` — where images come from (e.g., "imagn" or "stock")
- `brand_colors` — hex codes for text overlays
- `brand_fonts` — typography for graphics
- `canva_brand_kit_id` — Canva brand kit to apply
- `content_pillars` — topic categories (if the niche uses them)
- `claim_types` — niche-specific fact-check claim patterns
- `github_pages_url` — where dashboards are published
- `platforms` — which social platforms this niche publishes to

Read the niche's `niche-config.yaml` and `brand-guide.md` before starting the pipeline.

## Pipeline Overview

The pipeline has 15 steps. Execute them in order — each step builds on the previous ones.

| Step | Output File | Description |
|------|------------|-------------|
| 1 | — | Research current news via web search |
| 2 | — | Read `story-history.md` to identify follow-ups and avoid duplicates |
| 3 | `00-daily-brief.md` | Select 5-7 stories, assign tiers, write publishing schedule |
| 4 | `01-research-notes.md` | Document sources, stats, freshness verification per story |
| 5 | `02-story-analysis.md` | Deep analysis with angles, engagement hooks, headlines |
| 6 | `03-social-posts-x.md` | X/Twitter text posts and image post concepts |
| 7 | `04-social-posts-facebook.md` | Facebook long-form posts and image captions |
| 8 | `05-image-concepts.md` | Photo search terms, text overlay specs, composition notes |
| 9 | `articles/*.html` | Website-ready HTML articles for Tier 1-2 stories |
| 10 | `06-fact-check-log.md` | Verification of all factual claims against web sources |
| 10b | `07-content-data.json` | Run `compile-content-data.py` — compiles markdown into structured JSON |
| 11 | `07-image-manifest.md` | Image production: search → select → design → export (interactive) |
| 12 | `story-history.md` | Append today's stories to the running history |
| 13 | `review-dashboard.html` | Run `generate-review-dashboard.py` |
| 14 | — | Review dashboard, approve content, export PostPlanner upload |
| 15 | — | Publish dashboard to GitHub Pages |

Content goes into dated subfolders: `{CONFIG.content_prefix}-YYYY-MM-DD/`

## Step 1: Research

Search the web for current news relevant to this niche. The niche's `api-reference.md`
lists the primary sources to search. The niche's `seasonal-calendar.md` provides context
for what's timely right now.

The niche SKILL.md specifies the exact search strategies for its topic area.

### Mandatory Research Protocol

You MUST run at least **10 distinct web searches** covering a minimum of **6 of the 8
categories** below. Do not stop after finding 2-3 obvious stories — dig deeper.

| # | Category | Example Search Queries |
|---|----------|-----------------------|
| 1 | **Scores & Results** | "{sport} scores today {year}", "{sport} results yesterday" |
| 2 | **Tournament/Event Coverage** | Search EACH active tournament from `seasonal-calendar.md` by name |
| 3 | **Rankings & Polls** | "{sport} rankings poll this week {year}", "NFCA poll {month} {year}" |
| 4 | **Upsets & Surprises** | "{sport} upset {year}", "unranked beats ranked {sport}" |
| 5 | **Individual Performances** | "{sport} no-hitter {year}", "{sport} record {month} {year}", "milestone" |
| 6 | **Coaching & Program News** | "{sport} coaching change {year}", "milestone win", "{sport} hire fire" |
| 7 | **Injury & Roster Updates** | "{sport} injury report {year}", "{sport} transfer portal {month} {year}" |
| 8 | **Preview & Lookahead** | "{sport} weekend preview {year}", "{sport} conference play preview" |

Replace `{sport}`, `{year}`, `{month}` with the niche's sport and current date context.

### Research Minimums

- **10+ web searches** across **6+ categories**
- **8+ candidate stories** identified before moving to Step 2
- Each candidate needs at least 1 source URL and 3+ key facts
- Save all findings to `00-research.md` in the content folder — do NOT just save them
  mentally. This file is required for fact-checking.

### Research Quality Checks

- **HARD RULE: REJECT any story whose source article is more than 48 hours old.** Sports stats, standings, and streaks change daily. A story from 3+ days ago is stale and likely contains outdated numbers. Do NOT write articles about events or stats from earlier in the week unless there is a NEW development today that references them.
- Every fact must have a source published within the last 48 hours
- Cross-reference key stats across at least 2 sources for Tier 1 stories
- If a story only has 1 source and cannot be verified, demote it to Tier 3 or drop it
- Note any conflicting information between sources
- If a stat (batting average, win streak, record) appeared in a source from 2+ days ago, verify it is STILL accurate today before using it. Players play games every day and stats change.

### WebFetch Warning (CRITICAL)

WebFetch returns AI-summarized content, NOT raw page text. The summarizer can distort facts.
**Never save a WebFetch output directly into research notes as a verified fact.** Instead:
- Treat all WebFetch outputs as LOW confidence leads
- Compound claims (e.g., "X joins Y and Z in...") must be verified against a 2nd source
- Biographical facts (age, birthday, draft position) must be verified from a reference site
- Superlative claims ("first to...", "only player to...", "record for...") need 2nd-source confirmation
- See `_engine/CLAUDE.md` → Fact Verification Protocol for the full ruleset

## Step 2: Story History Check

Read `story-history.md` in the niche's project root. For each potential story, determine:
- **NEW STORY**: Never covered before
- **FOLLOW UP**: Previously covered, with new developments
- **SKIP**: Already covered with no material update

For follow-ups, note the previous date and angle so today's content adds new information
rather than repeating what was already published.

## Step 3: Daily Brief

Read `_engine/references/format-daily-brief.md` for the universal structure, then read
the niche's brand-guide for voice and pillar assignments.

Key decisions at this step:
- Select 5-7 stories (occasionally up to 8 if news warrants)
- Assign each story a **tier**: Tier 1 (lead/breaking), Tier 2 (developing), Tier 3 (evergreen/informational)
- If the niche uses content pillars, assign each story a pillar
- Tier determines which platforms get content (see Platform Assignment below)
- Write a publishing schedule with specific posting windows

**CRITICAL: Every social post MUST have a posting window.** No post goes out without
a scheduled time in the daily brief.

### Posting Order Rule (MANDATORY)

**Game results and today's games go FIRST.** When building the publishing schedule:

1. **Earliest time slots** → Yesterday's game recaps and scores
2. **Next slots** → Today's game preview/hype (if there's a game today)
3. **Remaining slots** → All other news, analysis, roster moves, features, evergreen

This applies to ALL sports niches. Fans check their feed in the morning wanting to know
what happened last night and what's coming today. Lead with that, then layer in everything else.

### Story Count Gate (MANDATORY)

After completing the Daily Brief, count the stories. If you have **fewer than 5 stories**:

1. **STOP** — do not proceed to Step 4
2. Return to Step 1 and run additional searches in underrepresented categories
3. Check which of the 8 research categories you missed and search those
4. Repeat until you have at least 5 stories (target 7)

Required tier mix:
- At least 1-2 Tier 1 stories (breaking, major results, records)
- At least 2-3 Tier 2 stories (notable performances, developing storylines)
- At least 1-2 Tier 3 stories (features, previews, engagement content)

If a slow news day genuinely has fewer than 5 stories, you may proceed with a minimum
of 5 by adding evergreen/preview content as Tier 3 stories (e.g., conference play
previews, historical comparisons, fan engagement posts).

## Step 4: Research Notes

Read `_engine/references/format-research-notes.md` for the universal structure.

This is the most research-intensive file. For each story, document:
- Decision justification (NEW STORY vs FOLLOW UP)
- Sources with publication dates (minimum 2 per Tier 1 story)
- Key facts and stats (with specific, verifiable numbers)
- Freshness verification explaining why the tier is justified
- Why the story matters to this niche's audience

## Step 5: Story Analysis

Read `_engine/references/format-story-analysis.md` for the universal structure.

For each story, produce:
- Freshness tag (3 keywords)
- Summary paragraph
- Relevance paragraph (why this niche's audience cares)
- 5 unique angles with talking points
- 2 engagement hooks (question-based + opinion/hot-take)
- Audience sentiment (3 perspectives representing different audience segments)
- 3 headline options (news-style, engagement-driven, voice-specific)

## Step 6: X/Twitter Posts

Read `_engine/references/format-x-posts.md` for the universal structure, then
read the niche's `brand-guide.md` and `brand-voice.md` for voice rules.

**Exemplar posts:** If the niche has a `top-posts.md` file, read it now. These are real
posts that performed well — study the tone, hooks, structure, and energy. Your goal is
to sound like the brand's best work, not just follow rules. Match what actually connects
with the audience.

Content by tier:
- **Tier 1**: 2 Text Posts (different angles — e.g., informative + bold take) + Image Post Concept
- **Tier 2**: 1-2 Text Posts + Image Post Concept
- **Tier 3**: 1 Text Post + Image Post Concept

**EMOJI REQUIREMENT**: Every X/Twitter post must include 1-3 relevant emojis. Place them
naturally — at the end of a line, start of a line, or between sections. Don't overdo it.
Facebook TOBI posts inherit emojis from the tweet text automatically.

**CHARACTER COUNT CHECK**: Do NOT manually estimate character counts — they are unreliable.
Instead, omit the `[CHARACTER COUNT: X/280]` tag from tweets entirely. The `verify-facts.py`
script (Step 10) will calculate accurate counts for every tweet and flag any that exceed 280.
URLs count as 23 characters on X regardless of actual length. Hashtags, newlines, and emojis
each count as characters. If Step 10 reports any over 280, fix them before generating the dashboard.

**SPACING (hard requirement)**: Every social media post (X and Facebook) must use blank lines for visual breathing room. Never write a post as one continuous block of text.
- Blank line between the hook and the supporting detail
- Blank line before any punchline or kicker
- Blank line before hashtags (X/Twitter — hashtags on their own line)
- See the niche's `brand-voice.md` for examples

## Step 7: Facebook Posts

Read `_engine/references/format-facebook-posts.md` for the universal structure, then
read the niche's `brand-guide.md` and `brand-voice.md` for voice rules.

**Exemplar posts:** If the niche has a `top-posts.md` file and you haven't already read
it in Step 6, read it now. Match the voice, structure, and hooks of proven winners.

Each story gets:
- **Long-Form Post**: 3-5 short paragraphs with blank lines between each, conversational, explains story for the niche's audience
- **Image Post Caption**: 1-2 sentences, punchy, platform-appropriate emoji usage

**SPACING (hard requirement)**: Facebook long-form posts must have a blank line between every paragraph. Short paragraphs (1-3 sentences) with breathing room perform far better than dense blocks. See the niche's `brand-voice.md` for examples.

The niche's brand voice guide defines the specific tone, emoji policy, and engagement tactics.

## Step 8: Image Concepts

Read `_engine/references/format-image-concepts.md` for the universal structure, then
read the niche's `brand-guide.md` for colors, fonts, and composition rules.

Each story gets image specs for each output format:
- **Social Image** (1080×1350, 4:5 vertical) — used for ALL social media posts (X, Facebook, Instagram, etc.)
- **Article Hero** (1200×630, 1.91:1 landscape) — only for article featured images and Open Graph

The 4:5 vertical format maximizes screen real estate on mobile feeds. One Gemini base image
per story, composed for 4:5 vertical. Article hero images are a separate generation if needed.

Each spec includes: Visual Description, Photo Search Terms (4-5), Text Overlay Copy
(with exact color hex codes from the niche's brand kit), and Composition Notes.

### Photo Search Rules / Gemini Image Prompts

The image sourcing approach depends on `{CONFIG.photo_source}`:

**If `imagn` (licensed sports photography):**
- Search terms are ONLY: **player/person name + team/organization name**
- NO years, NO event context, NO action descriptions in search terms
- Example: "Reese Atwood Texas" — NOT "Reese Atwood Texas 2026 batting"
- Search URL: `https://www.imagn.com/search?q=SEARCH+TERMS`
- Credit: "(USA TODAY Sports Images)" or "(Imagn Images)"

**If `stock` (free stock photos):**
- Search terms can be descriptive: topic + mood + subjects
- Use Unsplash first (higher quality), Pexels as backup
- Example: "family playground kids summer"
- Prioritize authentic-feeling photos over posed stock shots
- Ensure diversity in family representation

**If `gemini` (AI-generated images):**
- **REQUIRED READING:** Before writing ANY prompts, read `_engine/image-prompt-guide.md`
  for the full prompt engineering framework, quality tests, and story-type strategies.
- Instead of photo search terms, write a **detailed Gemini image prompt** for each image
- The prompt replaces the "Photo Search Terms" section in image concepts
- Read `{CONFIG.gemini_config.mode}` to determine prompt style:
  - **`base_only`**: Write prompts for clean background images with NO text. Request open
    visual space where text overlays will be added in Canva. Focus on scene, subjects,
    mood, lighting, color palette, and art style.
  - **`complete`**: Write prompts that include the headline text, font description, brand
    colors (hex codes from brand-guide), overlay bar style, and text placement. The
    generated image will be the final graphic — no Canva step.
- **Apply the 5-Point Quality Test** from the prompt guide to every prompt:
  1. ACTION — subject is DOING the story, not just in a setting
  2. TENSION — for crisis/news stories, the conflict is visible
  3. RECOGNITION — target audience sees themselves
  4. SINGLE-STORY — you can describe the image's story in one sentence
  5. DUAL-STORY — for combined stories, both events appear in frame
- Use consistent art style across all story images for visual cohesion
- Include brand color guidance in prompts (reference hex codes from brand-guide.md)
- See `format-image-concepts.md` for detailed prompt examples and guidelines

## Step 9: Articles

**Minimum 5 articles per day** for any niche where `article_word_count_min > 0` in the
niche config. Start with Tier 1 stories (all get articles), then Tier 2, then Tier 3
until you reach at least 5. If fewer than 5 stories exist for the day, write an article
for every story.

Create HTML article files in an `articles/` subfolder. The dashboard script also detects
`article-*.html` files placed in the content root, but the subfolder is preferred.

Read `_engine/references/format-articles.md` for the **mandatory HTML template**.
Every article MUST use this template structure — no exceptions.

Articles should be written in the niche's editorial voice (see `brand-voice.md`):
- Include subheadings (h2 tags)
- Always end with a "What's Next" section
- Leave img src="" empty — images are sourced separately
- Figcaption should suggest a photo search term for the editor
- Meta description under 160 characters
- No inline styles, no CSS, no JavaScript

Article length is defined in the niche config (typically 400-800 or 500-1000 words).

## Step 10: Fact-Check & Consistency Verification

**This is the critical quality gate.** Before finalizing any content, run the
universal verification script:

```bash
python _engine/scripts/verify-facts.py --niche {NICHE_FOLDER_NAME} YYYY-MM-DD
```

This runs two checks:

### 10a: Consistency Check
The script validates that every story from the daily brief has matching sections in all
downstream files (X posts, Facebook posts, image concepts, story analysis, articles).
It also checks **every tweet** for:
- Character count violations (>280 chars) — catches tweets that are over the limit
- Character count tag mismatches — flags when a `[CHARACTER COUNT: X/280]` tag disagrees
  with the actual count (this catches LLM estimation errors)
Fix any CHAR LIMIT or CHAR MISMATCH issues before proceeding to the dashboard.

### 10b: Fact-Check Claims
The script extracts factual claims from all content files using the niche's
`claim-patterns.py` module, groups them by story, and assigns verification priorities.

Each niche defines its own HIGH/MEDIUM/LOW claim types in `claim-patterns.py`.
Universal priorities that apply to ALL niches:
- **HIGH (Priority 1):** Dates, times, day-of-week claims — always the most error-prone
- **HIGH (Priority 1):** Player/person ages — NEVER calculate ages from birth dates. Always
  verify the current age from a reliable source (e.g., Baseball Reference, MLB.com player page,
  team roster page). LLM birth year knowledge is unreliable and off-by-one errors are common.
- **HIGH (Priority 1):** Compound claims linking multiple named entities (e.g., "X joins Y and Z
  as the only players to..."). These are the highest-risk category for AI summarization errors.
  Must be verified against 2 independent sources. See `_engine/CLAUDE.md` → Fact Verification Protocol.
- **HIGH (Priority 1):** Superlative/historical claims ("first to...", "only player to...",
  "franchise record...", "ties the record for..."). Verify against the actual record book or a
  second source — AI summaries commonly inflate or distort these.
- Everything else is niche-specific (sports stats, event prices, study findings, etc.)

### 10c: WebFetch / AI Summary Verification (MANDATORY)

**Any fact that originated from a WebFetch summary or AI-processed web page must be treated
as UNVERIFIED until cross-referenced.** WebFetch uses an AI model to summarize page content,
and that model can distort facts in predictable ways:

- **Entity conflation**: Merges separate people/teams into one false statement
- **Scope creep**: An NFL-wide stat gets attributed to a single team
- **Date/age drift**: Birth dates shifted, ages off by one
- **Superlative inflation**: "one of the best" becomes "the best"

**Before any fact from web research enters the verified-facts file or article content:**
1. Check: Is this a compound claim, biographical fact, or superlative? → Requires 2 sources.
2. Check: Did this come from a WebFetch summary (not raw page text)? → Treat as LOW confidence.
3. Verify ages/birthdays from a reference site (Pro Football Reference, Baseball Reference, Wikipedia).
4. For any "X joins Y and Z" claim, independently confirm Y and Z actually belong in that category.

See `_engine/CLAUDE.md` → Fact Verification Protocol for the full confidence tagging system.

**Triage guidance for verification:**
1. Fix all consistency issues first (missing stories, character count violations)
2. Verify all compound/entity claims and biographical facts (Step 10c)
3. Web-verify all HIGH priority claims for Tier 1 stories
4. Web-verify HIGH priority claims for Tier 2 stories
5. Verify MEDIUM claims for Tier 1 stories
6. Spot-check remaining claims as time allows

For each claim, search the specific source and mark the result in the log as
VERIFIED, CORRECTED, or UNVERIFIED.

If a claim is wrong, fix it in ALL content files before proceeding.

Cross-reference claims against:
- The story history (for consistency with previous coverage)
- At least one web source (for accuracy)
- A second web source for any compound, biographical, or superlative claim

**If a claim cannot be verified, mark it UNVERIFIED — never guess.**

## Step 11: Image Production (Interactive)

Read `_engine/references/format-image-manifest.md` for the manifest schema.

This step produces finished social media graphics by sourcing photos and
creating branded designs in Canva. It's **interactive** — the user selects photos and
approves designs. Process Tier 1 stories first, then Tier 2. Tier 3 is optional.

### 11a: Initialize Manifest

Create `07-image-manifest.md` in the content folder with all stories in `not_started` state.
Copy text overlay lines from `05-image-concepts.md` into each story entry.

### 11b: For Each Story — Photo Search & Selection / Gemini Generation

The image sourcing workflow depends on `{CONFIG.photo_source}`:

**Imagn workflow (sports niches):**
1. Read image concepts — get the 4-5 Imagn search terms
2. Navigate to `https://www.imagn.com/search?q=SEARCH+TERMS` using Chrome browser tools
3. Screenshot results for user to see thumbnails
4. User picks an image
5. Click selected image, capture direct image URL via `javascript_tool`
6. Confirm with user, update manifest

**IMAGN SEARCH TERM RULES (MANDATORY):**
- Terms are ONLY: player/person name + team/organization
- NO years, NO context words, NO event names
- Example: "Reese Atwood Texas" — correct
- Example: "Reese Atwood Texas 2026 batting Clearwater" — WRONG
- If first term doesn't yield results, try next term from the list

**Imagn Auth Fallback:** If login is required, tell user to log in and paste the
direct image URL. Resume from Canva upload step.

**Stock photo workflow (non-sports niches):**
1. Read image concepts — get the 4-5 stock photo search terms
2. Navigate to Unsplash or Pexels with search terms
3. Screenshot results for user
4. User picks an image
5. Click selected, capture download URL
6. Confirm with user, update manifest

**Gemini workflow (AI-generated niches):**

Requires: `GEMINI_API_KEY` environment variable set.
Script: `_engine/scripts/generate-gemini-image.py`

1. Read image concepts — get the Gemini image prompt for each platform image
2. Run the generation script for both X and Facebook images:
   ```bash
   python _engine/scripts/generate-gemini-image.py \
     --prompt "{GEMINI_PROMPT_FROM_IMAGE_CONCEPTS}" \
     --story-number {N} \
     --content-folder ./{CONFIG.content_prefix}-YYYY-MM-DD \
     --mode {CONFIG.gemini_config.mode} \
     --model {CONFIG.gemini_config.model}
   ```
   This generates 1080x1350 (4:5 vertical) social images and saves them
   to `{content_folder}/generated-images/story-{N}-social.png`
   For article heroes, use `--platform article` to generate 1200x630 (1.91:1 landscape)
3. Show the generated images to the user for approval
4. If user approves:
   - Update manifest: set `photo_source: gemini`, `gemini_prompt`, `gemini_image_path`
   - Update status to `gemini_generated`
5. If user rejects: adjust the prompt and regenerate (repeat from step 2)
6. **If `base_only` mode:** Continue to Step 11c (Canva upload + text overlay + export)
   - Use the local file path as the upload source for `upload-asset-from-url`
   - The rest of the Canva workflow is identical to stock/imagn photos
7. **If `complete` mode:** The image is already finished
   - Copy the `gemini_image_path` to `exported_url` in the manifest
   - Update status directly to `exported`
   - Skip the Canva upload/design/export steps entirely

**Gemini generation tips:**
- Process all stories first (generate all images), then review with user in batch
- If rate limited (HTTP 429), the script auto-retries with backoff
- For higher quality results, switch to `gemini-3-pro-image-preview` model
- If an image has text artifacts in `base_only` mode, regenerate with stronger
  "no text" instructions in the prompt

### 11c: For Each Selected Image — Composite Final Image

Once a base image is selected, use the **Python compositor script** to create the
final social media image. Do NOT use Canva's `generate-design` for overlays — it
doesn't give reliable layout control.

**Script:** `_engine/scripts/composite-social-image.py`

1. **Run the compositor** for each image:
   ```
   python _engine/scripts/composite-social-image.py <base_image> <output_path> \
       --headline "Headline Text" --subtitle "Subtitle Text" \
       --platform x|facebook \
       [--subtitle-color "#F4C542"] \
       [--bar-opacity 0.85]
   ```
   Or call `composite_image()` directly from Python.

2. **Layout rules** (enforced by the script):
   - Base image fills the full frame (resized to exact platform dimensions)
   - Semi-transparent dark overlay bar covers the bottom 1/3
   - Headline: Poppins Bold, white, as LARGE as possible in the bar
   - Subtitle: Nunito, accent color (gold default, coral for urgent/safety)
   - **NO website URL**, no body text, no extra elements — headline + subtitle only
   - Minimal dead space — image and text fill the frame edge to edge

3. **Subtitle colors by story type:**
   - Default: Soft Gold `#F4C542` (most stories)
   - Urgent/Safety: Warm Coral `#FF6F61` (recalls, crisis alerts)

4. **Output:** Final composited PNG saved to `images/final/` subfolder
   - Naming: `{brand}-Story{N}-{X|FB}-final-{date}.png`
   - Update manifest status to `composited`

5. **Show final graphic to user** for approval

6. **Optional Canva upload:** If the image needs further editing or team
   collaboration, upload the final composite to Canva using `upload-asset-from-url`
   and `import-design-from-url`.

**Required fonts:** `_engine/fonts/Poppins-Bold.ttf`, `_engine/fonts/Nunito-Variable.ttf`
(downloaded from Google Fonts on first setup). See `_engine/image-prompt-guide.md`
→ "Canva Overlay Rules" for the full layout specification.

### 11d: Skip or Defer

Image production is **optional per-story**. If time is limited:
- Prioritize Tier 1 stories
- Mark skipped stories as `not_started` in manifest
- The dashboard and PostPlanner export handle missing images gracefully
- Come back later to produce remaining images

## Step 12: Update Story History

Append today's stories to `story-history.md` following the existing format. Each entry needs:
- Story title
- Content pillar (if niche uses pillars)
- Angle (NEW STORY or FOLLOW UP with reference)
- Content Produced (list of platforms/formats)
- Follow-Up Opportunities (3-5 bullet points for future coverage)

## Step 10b: Compile Content Data

After fact-check, compile all markdown content into structured JSON. This is the single source of truth for the dashboard and PostPlanner export — it separates publishable post text from metadata (posting times, types, hashtags).

```bash
python _engine/scripts/compile-content-data.py --niche {NICHE_FOLDER_NAME} YYYY-MM-DD
```

This produces `07-content-data.json` in the content folder. Review the validation output — it reports character count violations, missing posts, and gaps.

## Step 13: Generate & Publish Review Dashboard

Generate the dashboard and publish it live in one step:

```bash
python _engine/scripts/generate-review-dashboard.py --niche {NICHE_FOLDER_NAME} YYYY-MM-DD
python _engine/scripts/publish-dashboard.py --niche {NICHE_FOLDER_NAME} YYYY-MM-DD
```

**Always run both commands together.** The first creates `review-dashboard.html` inside
the content folder. The second publishes it to GitHub Pages so the user can review live.
The index page shows only the **5 most recent dashboards** — older ones stay on disk
but are not linked.

Report the item count and the live URL from `{CONFIG.github_pages_url}`.

## Step 14: Review & Export

The dashboard is now live. The user reviews content at the GitHub Pages URL:
1. Review each card — approve, edit, or reject
2. Check fact-check badges on each story card
3. Check image production badges (if Step 11 was completed)
4. For any images not yet sourced, paste photo URLs into the dashboard input fields
5. Once all social posts are approved, generate the PostPlanner upload file:

```bash
python _engine/scripts/generate-postplanner-export.py --niche {NICHE_FOLDER_NAME} YYYY-MM-DD
```

This generates a **PostPlanner Bulk Upload V3.1 XLSX** file at
`{niche}/postplanner-imports/postplanner-upload-YYYY-MM-DD.xlsx`.

6. Also generate the **Facebook TOBI export** (text on background image):

```bash
python _engine/scripts/generate-postplanner-export.py --niche {NICHE_FOLDER_NAME} YYYY-MM-DD --tobi
```

This generates `{niche}/postplanner-imports/postplanner-tobi-upload-YYYY-MM-DD.xlsx`.
TOBI posts use Column H (`true-black`) for automatic background styling. Rules:
- TOBI text is IDENTICAL to the tweet — no stripping, no truncation
- Only change: `#NUMBER` rankings → `No. NUMBER` to avoid Facebook hashtag links

See `_engine/references/format-postplanner-export.md` for the exact column format.

**CRITICAL**: PostPlanner requires XLSX (not CSV) with `BULK UPLOAD VERSION 3.1` in cell B1.
The script handles this automatically — do NOT manually create or modify the export format.

Report the final approval count and any items that need manual attention.

## Platform Assignment by Tier

- **Tier 1**: Article + 2 X Text Posts (different angles) + Facebook Long-Form + Facebook Image Caption + Image Concepts (X + FB)
- **Tier 2**: Article + 1-2 X Text Posts + Facebook Long-Form + Facebook Image Caption + Image Concepts
- **Tier 3**: 1 X Text Post + Facebook Long-Form + Facebook Image Caption + Image Concepts. Article if needed to meet the 5-article daily minimum.

## Parallelization

Steps 6, 7, and 8 (X posts, Facebook posts, Image concepts) can be written in parallel
using subagents since they're independent of each other. Steps 5 and 9 (analysis and articles)
can also be parallelized. Use the Task tool to run these concurrently when possible.

Steps 1-4 must be sequential. Step 10 (fact-check) must come after all content is written.
Step 11 (image production) is interactive and cannot be parallelized with other steps.
Steps 12-14 come last.

## Error Recovery

If the dashboard script fails, check the path — make sure the dated content folder
exists and contains the expected files.

If web searches return no results for a story, note it as UNVERIFIED in the fact-check log
rather than guessing. Flag it for the user's manual review.

If the verify-facts.py script reports consistency issues, fix them before running the dashboard
generator — missing stories will show as empty cards in the dashboard.

## Story Count Guidelines

- Aim for 7 stories per day (5-8 range acceptable)
- At least 1-2 Tier 1 stories
- 3-4 Tier 2 stories
- 1-2 Tier 3 stories

## Platform Expansion (Future)

The current pipeline covers X/Twitter and Facebook. Natural next platforms:
- **Instagram**: Carousel posts (reuse image concepts), Stories, Reels scripts
- **TikTok**: Short-form video scripts
- **Email Newsletter**: Weekly digest
- **Pinterest**: Evergreen content pins

When adding a platform, create a new format reference file in `_engine/references/`
and add a corresponding step to the pipeline.
