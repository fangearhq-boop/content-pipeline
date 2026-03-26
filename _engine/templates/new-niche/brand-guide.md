# {BRAND_NAME} — Brand Guide

<!-- INSTRUCTIONS:
     This file defines HOW your brand looks — colors, fonts, image specs,
     composition rules, and photo sourcing workflow.
     The engine reads this before image production (Steps 8, 11) and
     article generation (Step 9).

     Fill in every section. The hex codes and font names you choose here
     must match your Canva Brand Kit.
-->

## Brand Identity

- **Brand Name:** {BRAND_NAME}
- **Parent Company:** FanGear HQ
- **Tagline:** "{ONE_LINE_TAGLINE}"
- **Logo:** {Description of logo and filename, e.g., "Softball with colorful fireworks (file: logo.png in project root)"}
- **Canva Brand Kit ID:** {CANVA_BRAND_KIT_ID}


## Colors

<!-- Choose 4-6 colors that define your visual identity.
     Every color needs a hex code and a clear usage description.
     The compositor script and image concepts reference these by name.

     SPORTS EXAMPLE (Softball):
     | Primary Orange | #FF8A00 | Headlines, player names, key stats |
     | Primary Gold   | #FFD700 | Rankings, awards, accent highlights |
     | Accent Red     | #E53935 | Upsets, breaking news, dramatic moments |
     | Dark Navy      | #1A1A2E | Text overlay backgrounds |
     | White          | #FFFFFF | Body text on dark overlays |

     PARENTING EXAMPLE:
     | Primary Teal   | #0097A7 | Headlines, primary buttons, brand accent |
     | Warm Coral     | #FF6F61 | Call-to-action, highlights, urgent |
     | Soft Gold      | #F4C542 | Secondary accent, warmth |
     | Dark Slate     | #2C3E50 | Body text, overlays |
     | Light Cloud    | #F5F7FA | Backgrounds, breathing space |
     | White          | #FFFFFF | Text on dark backgrounds |
-->

| Name | Hex Code | Usage |
|------|----------|-------|
| {COLOR_1_NAME} | #{HEX_1} | {Where and when to use this color} |
| {COLOR_2_NAME} | #{HEX_2} | {Where and when to use this color} |
| {COLOR_3_NAME} | #{HEX_3} | {Where and when to use this color} |
| {COLOR_4_NAME} | #{HEX_4} | {Text overlay backgrounds (semi-transparent)} |
| White | #FFFFFF | Body text on dark overlays, secondary text |

<!-- TIP: Choose a dark color for overlay bars (navy, slate, charcoal).
     The compositor applies it at 40-50% opacity over images. -->


## Typography

<!-- Choose 2-3 fonts. The compositor script uses Poppins and Nunito by default
     (available in _engine/fonts/). If you pick different fonts, make sure the
     TTF files are available locally for the compositor.

     SPORTS: Bebas Neue (bold headlines), Montserrat (stats/subtitles), Open Sans (body)
     PARENTING: Poppins (bold headlines), Nunito (warm subtitles), Open Sans (body)
     GARDENING: Playfair Display (elegant headlines), Source Sans Pro (body), Roboto Mono (data)
-->

| Role | Font | Usage |
|------|------|-------|
| Headlines | **{HEADLINE_FONT}** | {Style notes — e.g., "Bold, modern, friendly"} |
| Subtitles | **{SUBTITLE_FONT}** | {Style notes — e.g., "Semi-bold, clean"} |
| Body Text | **{BODY_FONT}** | {Style notes — e.g., "Regular, readable"} |


## Image Dimensions

<!-- Standard dimensions for all social and article images.
     The engine uses these in Step 8 (image concepts) and Step 11 (production).

     Social images: 1080x1350 (4:5 vertical) — maximizes mobile feed real estate.
     Article heroes: 1200x630 (1.91:1 landscape) — for Open Graph and article headers.

     Some niches also define platform-specific sizes if they differ.
-->

| Platform | Width | Height | Aspect Ratio | Notes |
|----------|-------|--------|--------------|-------|
| Social (all platforms) | 1080 | 1350 | 4:5 vertical | Primary format for X, Facebook, Instagram |
| Article Hero / OG | 1200 | 630 | 1.91:1 landscape | Featured images and Open Graph |


## Composition Rules

<!-- Define how images are composed. These rules guide both the image concepts
     (Step 8) and the compositor script (Step 11).

     Be specific — vague rules lead to inconsistent output.
-->

1. Semi-transparent dark bar ({COLOR_4_NAME} at {40-50}% opacity) behind all text overlays
2. Text placement: {top-left / bottom-center / bottom-third} preferred
3. Keep {50-65}% of image clean for {photography / illustration}
4. Logo placement: {bottom-right corner / top-left / none}
5. {Action shots / Authentic candid / Illustrated scenes} preferred over {posed / stock-looking / clipart}
6. Headline: {HEADLINE_FONT} Bold, white, as large as possible in the overlay bar
7. Subtitle: {SUBTITLE_FONT}, {ACCENT_COLOR_NAME} ({ACCENT_HEX})
8. No website URL, no body text, no extra elements — headline + subtitle only
9. Minimal dead space — image and text fill the frame edge to edge

<!-- SPORTS ADDITIONS:
     - Horizontal/landscape orientation only (for action shots)
     - Player should be the focus — crop tight on action

     PARENTING ADDITIONS:
     - Diversity in family representation (race, family structure, abilities)
     - Seasonal accuracy — match current weather in photos
     - Kid-safe — all photos should feel warm and appropriate

     GARDENING ADDITIONS:
     - Close-up details preferred (petals, soil, tools in hand)
     - Natural lighting — avoid harsh flash or studio look
     - Show the work (hands in soil, watering, harvesting)
-->


## Photo Sourcing

<!-- This section depends on the photo_source setting in niche-config.yaml.
     Include ONLY the section that matches your photo source. Delete the others.
-->

### If photo_source is "imagn" (licensed sports photography)

- **Primary source:** Imagn (USA TODAY Sports Images)
- **URL format:** `https://www.imagn.com/search?q=SEARCH+TERMS`
- **Search term rules:** ONLY player/person name + team/organization. NO years, NO context, NO event names.
- **Credit required:** "(USA TODAY Sports Images)" or "(Imagn Images)"
- **Licensed through:** Reuters

### If photo_source is "stock" (free stock photos)

- **Primary source:** Unsplash (unsplash.com) — highest quality
- **Secondary source:** Pexels (pexels.com) — good variety
- **Search terms:** Descriptive (topic + mood + subjects), e.g., "family playground kids summer"
- **Selection guidelines:**
  1. Diversity matters — represent your audience's full range
  2. Authentic over posed — candid-feeling photos outperform studio shots
  3. Seasonal accuracy — match the current season in photos
  4. Horizontal orientation for social graphics
- **Credit:** No credit required for Unsplash or Pexels (appreciated but optional)

### If photo_source is "gemini" (AI-generated)

- **Requires:** `GEMINI_API_KEY` environment variable
- **Prompt style:** Detailed visual descriptions with scene, subjects, mood, lighting, color palette, art style
- **Mode:** {base_only / complete} (from niche-config.yaml gemini_config)
  - `base_only`: Clean backgrounds with open space for text overlay. NO text in generated image.
  - `complete`: Finished graphic with headline text, brand colors, and overlay baked in.
- **Consistency:** Use the same art style across all story images for visual cohesion
- **Brand colors:** Reference hex codes from the Colors section above in every prompt
- **Restrictions:** NEVER include celebrity likenesses, copyrighted characters, or brand logos


## Photo Credit Format

<!-- How credits appear in content.
     Different platforms may have different credit formats.
-->

- **Imagn:** "(USA TODAY Sports Images)" or "(Imagn Images)" — required on every image
- **Unsplash/Pexels:** "Photo by {photographer} on {platform}" — optional but appreciated
- **Gemini:** No credit needed (AI-generated)
- **Local/submitted photos:** Always credit: "Photo: {photographer/organization}"
- **Articles:** Credit in `<figcaption>` tag below the image


## Canva Workflow

<!-- Step-by-step for creating graphics in Canva.
     The compositor script handles most of this automatically now,
     but manual Canva work may still be needed for complex designs.
-->

1. Apply Brand Kit (ID: {CANVA_BRAND_KIT_ID}) for consistent fonts and colors
2. Use {HEADLINE_FONT} for headlines ({COLOR_1_NAME} or White)
3. Use {SUBTITLE_FONT} for subtitles ({COLOR_2_NAME} or {COLOR_3_NAME})
4. Add semi-transparent {COLOR_4_NAME} overlay bar for text readability
5. Include {BRAND_NAME} logo in {position}
6. Export as PNG

### Subtitle Colors by Story Type

<!-- Different story types may use different accent colors for the subtitle.
     The compositor script accepts a --subtitle-color flag.
-->

- **Default:** {COLOR_3_NAME} ({HEX_3}) — most stories
- **Urgent / Breaking:** {COLOR_2_NAME} ({HEX_2}) — recalls, crises, breaking news
- **Celebration / Achievement:** {COLOR_1_NAME} ({HEX_1}) — milestones, awards
