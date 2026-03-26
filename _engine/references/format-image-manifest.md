# FanGear HQ Content Engine: Image Manifest Format
**Universal Template** | Niche-specific values from: brand-guide.md, brand-voice.md, niche-config.yaml

---

## Image Manifest Header

```yaml
pipeline_date: {YYYY-MM-DD}
last_updated: {YYYY-MM-DD HH:MM:SS}
brand_kit_id: {BRAND_KIT_ID_FROM_DESIGN_TOOL}
niche: {NICHE_NAME}
timezone: {CONFIG.timezone}
photo_source: {CONFIG.photo_source}
```

---

## Field Descriptions

| Field | Description | Required |
|-------|-------------|----------|
| **story_number** | Number from daily brief (1-8) | Yes |
| **story_title** | Story headline from daily brief | Yes |
| **tier** | Story tier: 1, 2, or 3 | Yes |
| **status** | not_started / photo_selected / imagn_selected / gemini_generated / canva_uploaded / design_created / exported | Yes |
| **x_image.dimensions** | Width x Height, should be 1200x675 | Yes |
| **x_image.photo_url** | URL to the photo selected (Unsplash, Getty, Imagn, etc.) | If photo_selected |
| **x_image.photo_source** | Source of photo: unsplash / getty / imagn / gemini / custom | If photo_selected or gemini_generated |
| **x_image.gemini_prompt** | The prompt used to generate the image via Gemini API | If gemini_generated |
| **x_image.gemini_image_path** | Local file path to the AI-generated image | If gemini_generated |
| **x_image.canva_asset_id** | Canva asset ID when uploaded | If canva_uploaded+ |
| **x_image.canva_design_id** | Canva design ID when design created | If design_created+ |
| **x_image.exported_url** | URL to exported final image | If exported |
| **x_image.text_overlay** | Array of text lines with formatting | Yes |
| **x_image.notes** | Any special notes about this image | Optional |
| **facebook_image.dimensions** | Width x Height, should be 1200x630 | Yes |
| **facebook_image.photo_url** | URL to the photo selected (Unsplash, Getty, Imagn, etc.) | If photo_selected |
| **facebook_image.photo_source** | Source of photo: unsplash / getty / imagn / gemini / custom | If photo_selected or gemini_generated |
| **facebook_image.gemini_prompt** | The prompt used to generate the image via Gemini API | If gemini_generated |
| **facebook_image.gemini_image_path** | Local file path to the AI-generated image | If gemini_generated |
| **facebook_image.canva_asset_id** | Canva asset ID when uploaded | If canva_uploaded+ |
| **facebook_image.canva_design_id** | Canva design ID when design created | If design_created+ |
| **facebook_image.exported_url** | URL to exported final image | If exported |
| **facebook_image.text_overlay** | Array of text lines with formatting | Yes |
| **facebook_image.notes** | Any special notes about this image | Optional |

---

## Image Manifest Template (YAML)

```yaml
pipeline_date: 2026-02-22
last_updated: 2026-02-22 09:00:00
brand_kit_id: {BRAND_KIT_ID}
niche: {NICHE_NAME}
timezone: {CONFIG.timezone}
photo_source: {CONFIG.photo_source}

stories:
  - story_number: 1
    story_title: {STORY_TITLE}
    tier: 1
    status: not_started

    x_image:
      dimensions: 1200x675
      photo_url: null
      photo_source: null
      canva_asset_id: null
      canva_design_id: null
      exported_url: null
      text_overlay:
        - text: "{Headline text from image-concepts}"
          font: "{CONFIG.headline_font}"
          size: {CONFIG.headline_font_size}
          color: "{CONFIG.primary_headline_color}"
          position: "top"
        - text: "{Subtitle text if applicable}"
          font: "{CONFIG.subtitle_font}"
          size: {CONFIG.subtitle_font_size}
          color: "{CONFIG.secondary_headline_color}"
          position: "top"
      notes: "{Any special composition or design notes}"

    facebook_image:
      dimensions: 1200x630
      photo_url: null
      photo_source: null
      canva_asset_id: null
      canva_design_id: null
      exported_url: null
      text_overlay:
        - text: "{Headline text from image-concepts}"
          font: "{CONFIG.headline_font}"
          size: {CONFIG.headline_font_size}
          color: "{CONFIG.primary_headline_color}"
          position: "top"
        - text: "{Subtitle text if applicable}"
          font: "{CONFIG.subtitle_font}"
          size: {CONFIG.subtitle_font_size}
          color: "{CONFIG.secondary_headline_color}"
          position: "top"
      notes: "{Any special composition or design notes}"

  - story_number: 2
    story_title: {STORY_TITLE}
    tier: 2
    status: not_started
    # ... (follow same structure as story 1)

  # Stories 3-N follow same pattern
```

---

## Status Lifecycle

### Status: `not_started`
- Initial state when image manifest is created
- Photo selection and design work haven't begun
- Next step: Move to `photo_selected` or `imagn_selected`

### Status: `photo_selected`
- Photo has been selected from search results
- `photo_url` and `photo_source` are populated
- Ready for Canva upload
- Next step: Move to `canva_uploaded`

### Status: `imagn_selected`
- Photo has been selected from Imagn API
- `photo_url` and `photo_source: imagn` populated
- Ready for Canva upload
- Next step: Move to `canva_uploaded`

### Status: `gemini_generated`
- Image has been generated by the Gemini API
- `photo_source: gemini`, `gemini_prompt`, and `gemini_image_path` populated
- **If gemini_config.mode = "base_only":** Image is a clean background with no text
  - Ready for Canva upload → text overlay → export
  - Next step: Move to `canva_uploaded`
- **If gemini_config.mode = "complete":** Image is a finished graphic with text baked in
  - Ready to use directly — no Canva step needed
  - Next step: Move to `exported` (save gemini_image_path as exported_url)

### Status: `canva_uploaded`
- Photo has been uploaded to Canva
- `canva_asset_id` is populated
- Canva design template created
- Next step: Move to `design_created` after text overlay applied

### Status: `design_created`
- Text overlay and design applied in Canva
- `canva_design_id` is populated
- Design ready for export
- Next step: Move to `exported` after final output

### Status: `exported`
- Final image exported from Canva
- `exported_url` populated with link to final file
- Image ready for posting
- Terminal state: Image complete

---

## How This File Is Used by Other Tools

### Dashboard & Progress Tracking
- Reads status field across all stories
- Displays progress percentage (X stories exported / total stories)
- Shows which images are blocking content publication
- Alerts when images fall behind schedule

### Image Creation Pipeline Tools
- Checks current status before next operation
- Advances status only after successful completion
- Validates required fields are populated before advancing
- Prevents out-of-order operations (e.g., export before design created)

### PostPlanner & Content Scheduler
- Reads `exported_url` to pull final image files
- Uses `story_number` to match images to posts
- Validates all required images are complete before posting
- Schedules posting based on story tier and platform

### Fact Verification Tools
- Cross-references story_number with research-notes.md
- Validates image content matches verified story facts
- Checks text overlay accuracy against source material
- Flags mismatches for correction

### Reporting & Analytics
- Tracks time from `not_started` to `exported` per story
- Measures bottlenecks in image creation pipeline
- Reports on photo source performance (unsplash vs. getty vs. imagn)
- Identifies optimization opportunities

---

## Text Overlay Formatting Rules

Each text overlay item includes:

```yaml
text_overlay:
  - text: "{The actual text displayed on image}"
    font: "{Font family from CONFIG}"
    size: {Numeric size in points}
    color: "{Hex color code from brand-guide}"
    position: "top" or "center" or "bottom"
    alignment: "left" or "center" or "right"
    overlay_bar_color: "{Hex code of overlay bar background}"
    overlay_opacity: 0.85  # 0-1 scale
```

**Validation:**
- `text`: Non-empty, max length appropriate for image size
- `font`: Must exist in {CONFIG.headline_font} or {CONFIG.subtitle_font}
- `size`: Readable when image displayed at 200x300px thumbnail
- `color`: Valid hex code, contrast ratio ≥ 4.5:1 against overlay bar
- `position`: Must be one of the three defined values
- `alignment`: Must match image composition notes from image-concepts.md

---

## Image Manifest Updates During Pipeline

### Phase 1: Image Concepts Created
```yaml
status: not_started
# All photo_url, canva_asset_id, canva_design_id, exported_url are null
# text_overlay structure is populated (ready for design)
```

### Phase 2a: Photos Selected (stock/imagn niches)
```yaml
status: photo_selected  # or imagn_selected
photo_url: https://unsplash.com/photos/ABC123
photo_source: unsplash  # or imagn
# canva_asset_id, canva_design_id, exported_url still null
```

### Phase 2b: Gemini Image Generated (gemini niches)
```yaml
status: gemini_generated
photo_source: gemini
gemini_prompt: "A photorealistic image of diverse families at a Colorado playground..."
gemini_image_path: ./parenting-content-2026-02-22/generated-images/story-1-x.png
# If base_only mode: proceed to Phase 3 (Canva upload)
# If complete mode: skip to Phase 5 (exported) — image is already finished
```

### Phase 3: Uploaded to Canva
```yaml
status: canva_uploaded
canva_asset_id: F1A2B3C4D5E6F7G8H9I0  # Asset ID from Canva
# canva_design_id, exported_url still null
```

### Phase 4: Design Created in Canva
```yaml
status: design_created
canva_design_id: D9K8L7M6N5O4P3Q2R1S0  # Design ID from Canva
# exported_url still null
```

### Phase 5: Final Export
```yaml
status: exported
exported_url: https://cdn.fangear.hq/exports/story-1-x-image.png
# All fields populated, image ready for posting
```

---

## Example: Complete Story Entry

```yaml
  - story_number: 1
    story_title: "League announces new playoff format changes"
    tier: 1
    status: exported

    x_image:
      dimensions: 1200x675
      photo_url: https://imagn.com/images/ABC123
      photo_source: imagn
      canva_asset_id: F1A2B3C4D5E6F7G8
      canva_design_id: D9K8L7M6N5O4P3Q2
      exported_url: https://cdn.fangear.hq/exports/story-1-x-image.png
      text_overlay:
        - text: "League Shakes Up Playoffs"
          font: "Montserrat"
          size: 48
          color: "#FFFFFF"
          position: "center"
          alignment: "center"
          overlay_bar_color: "#1A1A1A"
          overlay_opacity: 0.85
      notes: "High contrast for breaking news impact"

    facebook_image:
      dimensions: 1200x630
      photo_url: https://imagn.com/images/ABC123
      photo_source: imagn
      canva_asset_id: G7H8I9J0K1L2M3N4
      canva_design_id: E1F2G3H4I5J6K7L8
      exported_url: https://cdn.fangear.hq/exports/story-1-fb-image.png
      text_overlay:
        - text: "League Shakes Up Playoffs"
          font: "Montserrat"
          size: 48
          color: "#FFFFFF"
          position: "top"
          alignment: "center"
          overlay_bar_color: "#1A1A1A"
          overlay_opacity: 0.85
      notes: "Same asset, positioned for Facebook's taller ratio"
```

---

## Image Manifest Workflow Checklist

### Initial Creation:
- [ ] All story_number, story_title, tier fields populated
- [ ] All statuses set to `not_started`
- [ ] text_overlay structure populated from image-concepts.md
- [ ] Font and color references match brand-guide.md
- [ ] All dimensions correct (X: 1200x675, Facebook: 1200x630)

### During Photo Selection:
- [ ] photo_url and photo_source populated
- [ ] status updated to `photo_selected` or `imagn_selected`
- [ ] last_updated timestamp refreshed
- [ ] Imagn niches: Verify search term format (name + org only)

### During Canva Work:
- [ ] canva_asset_id populated after upload
- [ ] status updated to `canva_uploaded`
- [ ] canva_design_id populated after design created
- [ ] status updated to `design_created`

### After Export:
- [ ] exported_url populated with final image link
- [ ] status updated to `exported`
- [ ] last_updated timestamp refreshed
- [ ] All 5-8 stories have both X and Facebook images exported

### Final Validation:
- [ ] No null fields in exported entries
- [ ] All URLs are accessible
- [ ] Manifest ready for PostPlanner integration
- [ ] Ready for content publishing

---

## Manifest Maintenance & Rollback

**If an image needs revision:**
1. Update text_overlay as needed
2. Change status back to appropriate step (e.g., `design_created` to edit, then re-export)
3. Update canva_design_id if design was rebuilt
4. Update exported_url with new export
5. Update last_updated timestamp
6. Document change in notes field if needed

**Archiving completed manifests:**
- Keep current manifest in active directory
- Archive previous day's manifest in /archives/
- Reference archived manifests for historical data/analytics
