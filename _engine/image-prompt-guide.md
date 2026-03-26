# FanGear HQ — Image Prompt Engineering Guide

**Purpose:** Reference for the Step 8 (Image Concepts) agent when writing Gemini AI image prompts.
**Model:** gemini-2.5-flash-image (base_only mode)
**Last updated:** February 23, 2026 — based on COS Parenting test run analysis

---

## The Core Principle

**The image must tell the story's emotional truth, not illustrate its setting.**

A scroll-stopping social media image has ~1 second to communicate "this is about YOU" to the viewer. The image should make a parent feel something — urgency, relief, recognition, curiosity — before they read the headline overlay.

---

## The 5-Point Prompt Quality Test

Before finalizing any image prompt, verify it passes all five:

### 1. ACTION TEST: Does the image show someone DOING the story?
- **GOOD:** Parent inspecting a recalled bath seat (Story 2 — the viewer thinks "should I check mine?")
- **BAD:** A nursery with baby products on a shelf (just a setting, no action)
- **Rule:** The subject should be performing the action the story wants the READER to take

### 2. TENSION TEST: Does the image contain the story's core conflict?
- **GOOD:** Mom in work clothes holding toddler outside a FULL daycare (Story 1 — need vs. scarcity)
- **BAD:** A pleasant daycare scene from the sidewalk (setting without conflict)
- **Rule:** For news/crisis stories, the image must show the PROBLEM, not just the topic

### 3. RECOGNITION TEST: Will the target audience see THEMSELVES?
- **GOOD:** Teen sleeping in on weekend morning (Story 4 — every parent of a teen recognizes this)
- **BAD:** A laboratory with sleep study equipment (the science, not the lived experience)
- **Rule:** Show the parent/family experience, not the institution or system

### 4. SINGLE-STORY TEST: Can you describe what the image is "about" in one sentence?
- **GOOD:** "A parent can't find childcare" — clear, one idea
- **BAD:** "A neighborhood with a daycare in it" — no story, just geography
- **Rule:** If you can't state the story in one sentence from the image alone, the prompt is too vague

### 5. DUAL-STORY TEST (for combined stories only): Are BOTH events visually represented?
- **GOOD:** Family on nature trail + charity group in matching shirts in same frame (Story 6)
- **BAD:** Family hiking on trail only (covers one event, ignores the other)
- **Rule:** For combined-event stories, both activities must appear. Use foreground/background or left/right split.

---

## Prompt Structure Template

Use this structure for consistent, high-quality prompts:

```
[STYLE] Photorealistic editorial photograph [TONE MODIFIER if needed]

[SUBJECT] of [specific person description with age, ethnicity, clothing]
[ACTION] [what they are doing — the story's core action]
[EXPRESSION] [emotional state that matches the story's tone]

[SETTING] [specific location grounded in the niche's geography]
[DETAILS] [2-3 contextual details that reinforce the story]
[LIGHTING] [time of day + quality of light]

[COMPOSITION] The upper [third/portion] of the frame is [open sky/clean wall/etc]
for text overlay.

[EXCLUSIONS] No text, no words, no logos, no [story-specific exclusions].
[STYLE REINFORCEMENT] [Warm/Urgent/Peaceful] editorial photography style.
[DIMENSIONS] Shot at [1200x675/1200x630] pixels, [16:9/1.91:1] aspect ratio.
```

---

## Story Type → Prompt Strategy

### Crisis / Urgent News
**Goal:** Communicate urgency and human impact
**Strategy:** Show a person EXPERIENCING the problem, not the system causing it
- Lead with the affected parent/family
- Include one clear visual symbol of the crisis (FULL sign, empty shelf, warning label)
- Expression: concerned but not panicked — empathetic, never exploitative
- **Example prompt element:** "tired but determined mother in work clothes holding her toddler, standing outside a daycare with a FULL sign"

### Safety Alerts / Recalls
**Goal:** Trigger immediate "check your home" response
**Strategy:** Show a parent TAKING the protective action the story recommends
- Subject actively inspecting/checking the product in question
- The product itself should be recognizable
- A child safely in the background = reassurance that action prevents harm
- Expression: focused, protective — serious but not fearful
- **Example prompt element:** "father carefully inspecting a baby bath seat, holding it up to examine the underside"

### Practical Planning Content
**Goal:** Validate the planning chaos parents already feel
**Strategy:** Show the parent mid-planning, surrounded by the tools of the task
- Calendars, schedules, laptops, sticky notes = visual shorthand for "planning overload"
- Use the niche's brand colors in physical objects (colored calendar blocks, sticky notes)
- Expression: slightly amused, slightly overwhelmed — the viewer should think "that's me"
- **Example prompt element:** "mother at a wall calendar with blocks highlighted in different colors including teal, coral, and gold — representing different school district schedules"

### Feel-Good Research / Studies
**Goal:** Make the parent feel reassured or validated
**Strategy:** Show the OUTCOME the study celebrates, not the study itself
- Don't illustrate the research — illustrate what the research says is GOOD
- Warm, golden, peaceful lighting reinforces the positive message
- Expression: serene, content, natural — nothing posed
- **Example prompt element:** "teenage girl sleeping peacefully in a cozy bed, warm golden late-morning sunlight streaming through curtains"

### Community Events
**Goal:** Make the viewer want to attend
**Strategy:** Show people ENJOYING the event, not the venue
- Active participation > empty venue or static building shot
- If covering two events in one image, split the frame (left/right or foreground/background)
- Use matching outfits/gear to signal "organized event" for charity/group events
- Expression: excited, engaged, joyful — community energy
- **Example prompt element:** "family walking along a nature trail on the left, group of adults in matching bright shirts laughing together on the right"

### Humor / Engagement Posts
**Goal:** Trigger the "I need to share this" response
**Strategy:** Show the RELATABLE MOMENT, exaggerated just enough to be funny
- The subject's facial expression carries the joke — it must be readable at thumbnail size
- Physical comedy through props: too many calendars, sticky notes everywhere, tangled headphones
- Expression: the sweet spot between genuinely overwhelmed and laughing at themselves
- **Example prompt element:** "mother sitting at kitchen island looking comically overwhelmed, one hand on forehead, wide eyes with half-smile, surrounded by colorful sticky notes and calendars"

---

## Common Prompt Pitfalls

### 1. "Brochure Syndrome"
**Problem:** The image looks like a marketing photo — pleasant but empty
**Cause:** Describing a SETTING instead of a STORY
**Fix:** Add a human subject performing a specific action with a visible emotional state

### 2. "Split Attention"
**Problem:** Two-event stories where only one event appears
**Cause:** The prompt writer picked the more visually interesting event and forgot the other
**Fix:** Explicitly include both events using spatial composition (left/right, foreground/background)

### 3. "Stock Photo Energy"
**Problem:** The image feels posed, generic, corporate
**Cause:** Vague descriptions like "a happy family" or "parents at a park"
**Fix:** Add 2-3 hyper-specific details: a charging phone on the nightstand, a crumpled sticky note, a hoodie draped over a chair

### 4. "Setting Without Tension"
**Problem:** For conflict/crisis stories, the image shows the location but not the problem
**Cause:** Describing where the story happens instead of what the story IS
**Fix:** Include one visual element that represents the obstacle or conflict (FULL sign, empty lot, long line)

### 5. "Wrong Emotional Register"
**Problem:** The image mood doesn't match the story mood
**Cause:** Using warm/pleasant defaults for stories that need urgency or humor
**Fix:** Explicitly state the desired emotional register in the prompt: "urgent and empathetic, not alarming" or "genuinely funny and relatable, not truly stressed"

---

## Gemini-Specific Technical Notes

### What Works Well
- Detailed scene descriptions with specific props and positioning
- Explicit lighting direction ("late morning winter sunlight from the right")
- Ethnic/age/clothing specifics for subjects (generates more authentic images)
- "Editorial photograph" style instruction (avoids stock photo look)
- Dimension + aspect ratio in the prompt (model respects these)
- "No text, no words, no logos" (model follows this reliably)

### What to Watch For
- Model may generate readable text on signs/papers despite "no text" instruction
  - Exception: single-word signs (like FULL) can be intentionally useful
- Very complex multi-group scenes may merge subjects together
  - Fix: describe spatial separation explicitly ("on the left... on the right...")
- Model defaults to warm/pleasant tone — you must explicitly request tension, urgency, or humor
- Exact pixel dimensions in prompt are respected but actual output varies slightly
  - The 16:9 vs 1.91:1 framing difference between X and Facebook is subtle but real

### Platform Dimensions & Aspect Ratios

**Social Media Posts (ALL platforms):** 1080×1350 (4:5 vertical)
- Used for: X/Twitter posts, Facebook posts, Instagram posts, any social share
- 4:5 vertical dominates mobile feeds — maximum screen real estate
- Gemini base images: request portrait-oriented composition, subject centered
- Compositor overlay: bottom 1/3 text bar, upper 2/3 hero image
- "Upper portion" of frame should have clean space for the image hero area

**Article Hero Images:** 1200×630 (1.91:1 landscape)
- Used for: Article featured image, Open Graph preview, newsletter hero
- NOT for social media posts — only for embedding in articles
- Gemini base images: request landscape composition, "upper third" clean for overlay
- This is the only landscape format in the pipeline

**Key Rule:** One Gemini base image per story, composed for 4:5 vertical. The compositor handles cropping and overlay. Article hero images are a separate generation if needed.

---

## Canva Overlay Rules (Step 11c)

When generating Canva designs with `generate-design`, the `query` parameter must enforce these rules:

### Rule 1: Image-Dominant Layout (2/3 Image, 1/3 Text)
- The photo/image must take up approximately **two-thirds (2/3)** of the total design area
- Text overlay occupies the remaining **one-third (1/3)**
- The image is the hero — it's what stops the scroll. Text supports the image, not the other way around.
- **NEVER** use a template layout where the image is small or crammed into a corner
- The image should be either:
  - Full-bleed background with a text bar/strip overlaid on one edge (preferred), OR
  - Split layout with image filling 2/3 and a solid/semi-transparent text panel on 1/3
- **Why:** The AI-generated image IS the content. Template-style layouts with small images defeat the purpose of custom image generation.

### Rule 2: NO Website URL on the Image
- The final social image must **never** display a website link, URL, or domain name
- Explicitly instruct: "Do NOT include any website URL, web address, link text, or 'reallygreatsite.com' anywhere on the image"
- Also explicitly exclude: placeholder URLs, domain names, "www" anything
- This applies to all platforms (X, Facebook, etc.)
- **Why:** URLs waste precious visual space, are unreadable at thumbnail size, and look like ads rather than content. The link lives in the post text, not the image.

### Rule 3: Maximize Text Size in the 1/3 Text Area
- Within the text area (1/3 of the design), the headline must be **as large as possible**
- Only TWO text elements allowed: headline + subtitle. Nothing else.
- No body paragraphs, no descriptions, no extra copy — just headline + subtitle
- Text should be bold, high-contrast, and readable at mobile thumbnail size
- **Why:** Social images are viewed at thumbnail size on phones. Small text = invisible text.

### Rule 4: Minimal Dead Space
- Leave as little empty/unused space as possible in the entire design
- The image and text together should fill the frame edge to edge
- No large empty margins, no decorative whitespace, no unused corners
- **Why:** Every pixel is real estate on a social feed. Wasted space = wasted attention.

### Standard `query` Template for `generate-design`

```
Create a social media image for [platform] with these specifications:
LAYOUT: The uploaded photo must be the dominant visual element, taking up
approximately two-thirds (2/3) of the total image area. Use the photo as a
large background or hero image. The remaining one-third (1/3) should be a
text overlay area with a semi-transparent dark bar or solid color band.
TEXT: Only two text elements:
- Headline: "[HEADLINE TEXT]" — make this as LARGE and BOLD as possible
  within the text area
- Subtitle: "[SUBTITLE TEXT]" — smaller but still clearly readable
RESTRICTIONS:
- Do NOT include any website URL, web address, domain name, link text, or
  "reallygreatsite.com" anywhere on the image
- Do NOT include any body paragraph or description text — headline and
  subtitle ONLY
- Do NOT use a template layout where the photo is small — the photo must
  dominate the design
- Minimize empty space — the image and text should fill the frame
Use brand kit colors and fonts. [16:9 / 1.91:1] aspect ratio.
```

---

## Quality Bar

An image is ready for Canva overlay when:
- [ ] It passes all 5 quality tests above
- [ ] A parent scrolling at speed would pause on it
- [ ] The emotional register matches the story type
- [ ] There's clean overlay space for headline + subtitle
- [ ] COS-specific grounding is present (for local stories)
- [ ] No unintended text, logos, or watermarks in the base image
- [ ] Diverse representation is tracked across the full daily set

A **final Canva design** passes when:
- [ ] Photo/image takes up ~2/3 of the design area (image-dominant)
- [ ] NO website URL, domain, or link appears anywhere on the image
- [ ] Only headline + subtitle text — no body paragraphs or extra copy
- [ ] Headline text is as large as possible within the text area
- [ ] Text is readable at mobile thumbnail size (scrolling X/Facebook feed)
- [ ] Brand colors/fonts applied consistently
- [ ] Minimal dead space — image and text fill the frame

---

*This guide should be read by the Image Concepts agent (Step 8) before writing any Gemini prompts, and by the Image Production agent (Step 11c) before generating any Canva designs.*
