# Image Manifest — COS Parenting
**Date:** 2026-05-07
**Pipeline step:** 9 — Image Manifest

```yaml
pipeline_date: "2026-05-07"
brand_kit_id: "kAHCKfCZgk0"
photo_source: "gemini"
mode: "base_only"
model: "gemini-2.5-flash-image"
images:
  - id: story1-social
    story: 1
    type: social
    dimensions: "1200x675"
    prompt: "A diverse group of adults — teachers and parents of various ages and ethnicities — standing together outside a school building on a sunny Colorado morning. They hold simple handwritten signs in supportive, non-confrontational poses. Clean blue sky with Rocky Mountain hints in the background. Warm natural lighting. The bottom third is uncluttered to allow text overlay. Photorealistic style. No text, no logos, no branded signs visible. Base-only image."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story1-article
    story: 1
    type: article
    dimensions: "1200x630"
    prompt: "A wide exterior shot of a public school building in Colorado with a clear blue sky. The building has brick and glass architecture typical of Colorado Springs K-12 schools. Early morning light. No people, no signs, no text. Clean composition with open sky for text overlay. Photorealistic base image."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story2-social
    story: 2
    type: social
    dimensions: "1200x675"
    prompt: "A parent of mixed ethnicity sitting comfortably with a child (ages 7-9) on a couch, both looking at a tablet together with engaged expressions. Warm home lighting, cozy living room setting with soft Colorado mountain landscape visible through a window. The parent has a thoughtful, present expression. Bottom third clear for text overlay. No brand logos visible on the tablet. Photorealistic, warm-toned base image."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story2-article
    story: 2
    type: article
    dimensions: "1200x630"
    prompt: "A flatlay of a family tablet on a clean wooden table surrounded by children's items — a book, a small toy, a glass of water — soft Colorado sunlight coming through a window. No text or screen content visible on the tablet. Clean, editorial-style food/lifestyle photography aesthetic. Warm tones. Base image only."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story3-social
    story: 3
    type: social
    dimensions: "1200x675"
    prompt: "A joyful young child (age 3-4) wearing a red and blue outfit sitting in an audience seat at a theater, face lit up with excitement and wonder. Colorful stage lights in the background create a magical atmosphere. Bokeh effect on background. Clear space in the bottom third for text overlay. No trademarked characters or logos visible — only the child's expression and theater atmosphere. Photorealistic, vibrant colors."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story3-article
    story: 3
    type: article
    dimensions: "1200x630"
    prompt: "Wide interior shot of an empty performing arts theater from the audience perspective, looking toward a brightly lit stage with colorful stage lighting in blue, red, and yellow. Theater seats visible, no people. Clean composition with the stage centered. Photorealistic. No text, no logos. Base image only."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story4-social
    story: 4
    type: social
    dimensions: "1200x675"
    prompt: "A clean, minimal bathroom scene showing an empty bathtub from a slightly elevated angle. The bathtub is clean white with clear water. A yellow rubber duck sits on the edge. No bath seat or child visible. Soft natural bathroom lighting. Clean, bright, and simple. Clear bottom third for text overlay. Base image only, no text."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story4-article
    story: 4
    type: article
    dimensions: "1200x630"
    prompt: "An overhead view of a clean white bathtub partially filled with clear water, with gentle ripples. A few bath toys (rubber duck, foam shapes) float in the water. Bright, natural lighting. No child, no bath seat, no person. Clean editorial style. Photorealistic base image."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story5-social
    story: 5
    type: social
    dimensions: "1200x675"
    prompt: "A neatly folded children's matching pajama set (button-up top and pants) in pastel colors on a clean white surface. Soft studio lighting. The clothing is generic — no brand names, no logos, no specific licensed designs. Warm natural light from the side. Bottom third of the image is clear for text overlay. Photorealistic, lifestyle photo style."
    credit: "AI-generated (Gemini)"
    status: not_started

  - id: story5-article
    story: 5
    type: article
    dimensions: "1200x630"
    prompt: "A folded children's clothing set — a button-up long-sleeved top and matching pants in a soft pastel color — on a light wooden dresser surface. Clean natural light from a window. No text, no logos. Neutral background. Editorial flatlay style. Photorealistic base image."
    credit: "AI-generated (Gemini)"
    status: not_started
```

## Image Summary
- **Total images:** 10 (2 per story: 1 social 1200x675, 1 article hero 1200x630)
- **Photo source:** gemini (AI-generated via Google Gemini API)
- **Mode:** base_only — clean backgrounds, no text, no overlays
- **Model:** gemini-2.5-flash-image
- **Brand kit:** kAHCKfCZgk0
- **Bottom-third rule:** All social prompts specify clear bottom third for Canva text overlay
- **No trademark rule:** No celebrity likenesses, copyrighted characters, or brand logos in prompts
- **Status:** All not_started (Gemini generation happens post-dashboard)
