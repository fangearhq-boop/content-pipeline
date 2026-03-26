# FanGear HQ Content Engine: Articles HTML Template Format
**Universal Template** | Niche-specific values from: brand-guide.md, brand-voice.md, niche-config.yaml

---

## Articles Header

```
# {BRAND_NAME} - Articles
**Date:** {PUBLICATION_DATE}
**Story Analysis Reference:** {Link to format-story-analysis.md}
**Prepared By:** FanGear HQ Content Engine
**Article Framework:** HTML5 Standard Template
```

---

## Filename Convention

**Format:** `article-NN-slug-title.html`

**Examples:**
- `article-01-league-playoffs-announcement.html` (Story 1)
- `article-02-player-contract-extension.html` (Story 2)
- `article-07-upcoming-championship-dates.html` (Story 7)

**Rules:**
- NN = Two-digit story number (01-08)
- slug-title = URL-friendly version of article title
- Use hyphens to separate words
- Lowercase only
- No special characters except hyphens
- No spaces or underscores

---

## HTML5 Template Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{Meta description 150-160 characters}">
    <meta property="og:title" content="{Article Title}">
    <meta property="og:description" content="{Meta description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{URL where this will be published}">
    <meta property="og:image" content="{URL to featured image}">
    <title>{Article Title} | {BRAND_NAME}</title>
</head>
<body>
    <article>
        <header>
            <h1>{Article Title}</h1>
            <div class="byline">
                <span class="author">By {BRAND_NAME} Staff</span>
                <span class="date">{Publication Date}</span>
            </div>
            {Optional: <span class="pillar">{Content Pillar}</span>}
        </header>

        <figure>
            <img src="{src left empty for now}" alt="{alt text describing image}">
            <figcaption>
                Photo search suggestion: {Search terms from image-concepts.md}
            </figcaption>
        </figure>

        <section>
            <h2>{Subheading 1}</h2>
            <p>{Paragraph 1 with context and background. Introduce the story, provide necessary context, and set up why this matters.}</p>
            <p>{Paragraph 2 continuing the narrative, adding specific details, facts, and statistics.}</p>
        </section>

        <section>
            <h2>{Subheading 2}</h2>
            <p>{Paragraph exploring angle or perspective 1.}</p>
            <p>{Paragraph exploring angle or perspective 2.}</p>
        </section>

        <section>
            <h2>{Subheading 3}</h2>
            <p>{Paragraph deepening the analysis or adding expert perspective.}</p>
            <p>{Paragraph with specific examples or case studies relevant to {BRAND_NAME} audience.}</p>
        </section>

        {Optional: <section>
            <h2>Quick Reference</h2>
            <table>
                <tr>
                    <th>{Column 1}</th>
                    <th>{Column 2}</th>
                </tr>
                <tr>
                    <td>{Data}</td>
                    <td>{Data}</td>
                </tr>
            </table>
        </section>}

        <section>
            <h2>What's Next</h2>
            <p>{Closing paragraph that summarizes key takeaway and points to future implications or next steps. Avoid ending abruptly.}</p>
        </section>
    </article>
</body>
</html>
```

---

## Article Writing Guidelines

### Word Count
- **Target:** {CONFIG.article_word_count_target} words
- **Acceptable Range:** {CONFIG.article_word_count_min} - {CONFIG.article_word_count_max} words
- **Typical:** 400-1000 words for {BRAND_NAME}
- **Guideline:** Length should match story complexity and Tier (Tier 1 = longer, Tier 3 = shorter)

### Structure

**Header Requirements:**
- `<h1>`: Single, compelling article title (not the same as social post headlines)
- Byline: "By {BRAND_NAME} Staff | {Date}"
- Optional: Content Pillar tag (if niche uses pillars)

**Subheadings (h2):**
- **Target:** 2-4 h2 subheadings per article
- **Placement:** Divide article into logical sections
- **Structure:** Descriptive headings that help readers scan content
- **Avoid:** Vague headings like "Details" or "Analysis"

**Body Paragraphs:**
- **Length:** 4-6 sentences per paragraph (varies)
- **Voice:** Matches {BRAND_NAME} brand-voice.md tone
- **Content:** Mix of facts, analysis, and audience-relevant insights
- **Numbers:** Include specific stats, dates, percentages, scores
- **Specificity:** Avoid generalizations; support with details

**Photo/Figure:**
- `<figure>` with `<img>` (src left empty, filled during image process)
- `<figcaption>` includes photo search suggestions from image-concepts.md
- Placement: After header, before body sections
- Caption guides image selection process

### Voice & Tone

**Editorial Voice:** {From {BRAND_NAME} brand-voice.md}
- {Voice characteristic 1: how to write}
- {Voice characteristic 2: how to write}
- {Voice characteristic 3: how to write}

**Tone Checklist:**
- [ ] Authentic to {BRAND_NAME} brand voice
- [ ] Conversational but professional
- [ ] Avoids jargon without explanation
- [ ] Speaks to {BRAND_NAME} audience directly
- [ ] Avoids generic or marketing-speak language
- [ ] Specific examples and data points included

### Content Requirements

**Specific Numbers & Stats:**
- Every article should include 3-5 specific data points
- Source each statistic if possible (cite in article or link section)
- Avoid round numbers when exact data is available
- Example: "23% improvement" not "significant improvement"

**Relevance to Audience:**
- First paragraph should clearly establish "why this matters" to {BRAND_NAME} audience
- Every section should connect story back to audience needs/interests
- Avoid content that only serves general readers; niche focus

**Cross-References:**
- Mention related stories from same brief if applicable
- Link to previous articles on same topic if they exist
- Provide context for recurring issues or ongoing narratives

### What's Next Section (MANDATORY)

**Purpose:** Closing section that doesn't leave reader hanging

**Structure:** 1-3 sentences that:
- Summarize the key takeaway
- Point to future implications ("What happens next...")
- Provide actionable next step for reader if applicable
- Create continuity with upcoming stories/coverage

**Examples:**
- "Watch for official announcements expected [date]..."
- "The league will [next step], which means [audience impact]..."
- "This sets the stage for [upcoming event/development]..."

**Critical:** Every article MUST end with a "What's Next" section. No abrupt endings.

---

## Optional: Quick Reference Section

**When to use:**
- Stories about events with dates/times/locations/costs
- Stories about decisions with multiple options
- Stories with complex data that benefits from table format

**Format:**
```html
<section>
    <h2>Quick Reference</h2>
    <table>
        <thead>
            <tr>
                <th>{Header 1}</th>
                <th>{Header 2}</th>
                <th>{Header 3}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{Data}</td>
                <td>{Data}</td>
                <td>{Data}</td>
            </tr>
        </tbody>
    </table>
</section>
```

**Table Best Practices:**
- Use for factual, structured data only
- Max 5-6 rows (keep scannable)
- Max 3-4 columns (avoid horizontal scroll)
- Examples: Event schedules, scoring changes, comparison data

---

## HTML Standards & Rules

**Critical Constraints:**
- NO inline styles (style="...")
- NO embedded CSS in `<style>` tags
- NO JavaScript or `<script>` tags
- NO custom classes (structure through semantic HTML only)
- Simple, semantic HTML5 only

**Semantic Elements Required:**
- `<article>`: Wraps entire article
- `<header>`: Contains h1, byline, metadata
- `<figure>`: Contains image and caption
- `<section>`: Groups related content
- `<h2>`: Subheadings within sections
- `<p>`: Body paragraphs

**Meta Tags Required:**
- `<meta charset="UTF-8">`: Character encoding
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: Responsive design
- `<meta name="description">`: 150-160 character summary
- `<meta property="og:*">`: Open Graph tags for social sharing

**Image Attributes:**
- `alt="{descriptive alt text}"`: Always include alt text
- `src=""`: Leave empty for now (filled during image phase)
- `<figcaption>`: Provides photo search guidance

---

## Article Creation Workflow

### Step 1: Template Selection
- [ ] Choose article-NN filename based on story number
- [ ] Create file with correct naming convention

### Step 2: Header & Metadata
- [ ] Write compelling h1 title (different from social headlines)
- [ ] Set byline: "By {BRAND_NAME} Staff | {Date}"
- [ ] Complete all meta tags (description, og tags)
- [ ] Optional: Add content pillar tag if applicable

### Step 3: Structure & Outline
- [ ] Plan 2-4 h2 subheadings
- [ ] Map which story angles/facts go in each section
- [ ] Identify photo placement location
- [ ] Plan "What's Next" closing

### Step 4: Content Writing
- [ ] Write body paragraphs (4-6 sentences each)
- [ ] Include 3-5 specific data points
- [ ] Apply {BRAND_NAME} brand voice consistently
- [ ] Target word count: {CONFIG.article_word_count_target}

### Step 5: Audience Connection
- [ ] Verify each section speaks to {BRAND_NAME} audience
- [ ] Explain "why this matters" to niche readers
- [ ] Include relevant examples/case studies
- [ ] Add cross-references to other stories if applicable

### Step 6: Closing
- [ ] Write "What's Next" section (MANDATORY)
- [ ] Ensure no abrupt ending
- [ ] Connect to future developments/stories

### Step 7: Quality Check
- [ ] Verify HTML structure is semantic
- [ ] Confirm no inline styles or scripts
- [ ] Check all meta tags are complete
- [ ] Validate word count is in range
- [ ] Proofread for brand voice consistency
- [ ] Ensure every h2 subheading is descriptive
- [ ] Verify alt text for image is descriptive

---

## Example: Complete Article Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="New playoff format announced by league, impacting teams and schedules for upcoming season.">
    <meta property="og:title" content="League Announces Major Playoff Format Changes">
    <meta property="og:description" content="New playoff format announced by league, impacting teams and schedules for upcoming season.">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.{niche}.com/article-01-league-playoffs-announcement">
    <meta property="og:image" content="https://cdn.{niche}.com/images/playoff-announcement.jpg">
    <title>League Announces Major Playoff Format Changes | {BRAND_NAME}</title>
</head>
<body>
    <article>
        <header>
            <h1>League Announces Major Playoff Format Changes</h1>
            <div class="byline">
                <span class="author">By {BRAND_NAME} Staff</span>
                <span class="date">February 22, 2026</span>
            </div>
            <span class="pillar">Competition</span>
        </header>

        <figure>
            <img src="" alt="League commissioner announcing playoff format changes at podium">
            <figcaption>Photo search suggestion: League commissioner announcement podium</figcaption>
        </figure>

        <section>
            <h2>What Changed</h2>
            <p>The league announced a restructured playoff format that will take effect next season, affecting how teams qualify and compete. The announcement came after months of deliberation among team owners and league officials, responding to [specific catalyst]. The new format includes [key change 1], [key change 2], and [key change 3], fundamentally altering playoff dynamics.</p>
            <p>According to the official press release, the changes were made to [official rationale]. League Commissioner stated, "[relevant quote]," emphasizing the importance of the update.</p>
        </section>

        <section>
            <h2>How This Affects Teams</h2>
            <p>Under the new format, teams will [impact on seeding]. This means that teams currently positioned [example scenario] could [potential outcome]. Early analysis suggests that [specific team type] stands to [benefit/disadvantage].</p>
            <p>[Specific example of how a notable team or player is affected]. This change particularly impacts teams who [context], as they will now [consequence].</p>
        </section>

        <section>
            <h2>What {BRAND_NAME} Audience Should Know</h2>
            <p>For {BRAND_NAME} audience members, this format change means [direct relevance]. If you're [audience segment], you should [actionable insight]. The key takeaway: [summarize why this matters to niche].</p>
            <p>Looking ahead, this format will affect [future implications], so [audience action or consideration].</p>
        </section>

        <section>
            <h2>What's Next</h2>
            <p>The league will begin implementation planning [timeline]. Teams will submit [required action] by [date], with the new format officially taking effect [future date]. Expect additional details and Q&A sessions from the league in the coming weeks.</p>
        </section>
    </article>
</body>
</html>
```

---

## Article Manifest Integration

Articles are referenced in the content pipeline through:
- **Filename:** Matches story number (article-01, article-02, etc.)
- **Cross-reference:** Linked from X posts and Facebook posts as "Read full story"
- **URL:** Will be generated when articles are published to CMS
- **Status tracking:** Dashboard monitors article completion along with images/posts

---

## SEO & Publishing Considerations

**Before Publishing:**
- [ ] All meta descriptions are 150-160 characters
- [ ] og:image is set to correct featured image URL
- [ ] og:url is set to final article URL
- [ ] Title tag is unique and includes key terms
- [ ] Heading hierarchy is correct (h1 > h2)
- [ ] Alt text on image is descriptive and keyword-aware
- [ ] No broken links or missing images

**During Publishing:**
- [ ] Article URL matches filename convention
- [ ] Featured image is uploaded and linked
- [ ] Open Graph data is verified after publication
- [ ] Social media preview looks correct when shared

---

## Articles Workflow Checklist

### For Each Article:
- [ ] Filename follows convention (article-NN-slug-title.html)
- [ ] HTML5 structure with semantic elements
- [ ] All required meta tags populated
- [ ] h1 title is compelling and unique
- [ ] Byline: "By {BRAND_NAME} Staff | Date"
- [ ] 2-4 h2 subheadings in logical order
- [ ] Body paragraphs written in brand voice
- [ ] Word count in range: {CONFIG.article_word_count_min} - {CONFIG.article_word_count_max}
- [ ] 3-5 specific data points included per article
- [ ] Figure/image included with alt text and photo search suggestions
- [ ] "What's Next" closing section present
- [ ] Optional Quick Reference section if applicable (events/data stories)
- [ ] No inline styles, CSS, or JavaScript
- [ ] Semantic HTML only

### Overall Articles:
- [ ] All 5-8 stories have corresponding articles (or selected stories if not all require articles)
- [ ] Filenames are consistent and numbered correctly
- [ ] All articles follow {BRAND_NAME} brand voice
- [ ] Cross-story references are accurate
- [ ] Articles ready for CMS publishing
- [ ] URLs planned and documented in publishing checklist

---

## Publishing & Archive

**File Organization:**
- Active articles: `/articles/` directory
- Archive: `/articles/archive/YYYY-MM/` (by publish date)
- Template: `/articles/_template/` (this reference document)

**Publishing Process:**
1. Copy article HTML to CMS or publishing platform
2. Upload featured image and update img src URL
3. Publish article and note final URL
4. Update all cross-references (social posts, dashboard)
5. Monitor initial engagement and update if needed
6. Move to archive after 30 days

**Historical References:**
- Articles are archived for SEO and reference
- CMS should maintain URL permanence
- Redirect old URLs if article titles change
