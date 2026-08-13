# Image Manifest — COS Parenting
**Date:** 2026-08-13
**Pipeline Step:** 11 — Image Production

```yaml
pipeline_date: "2026-08-13"
brand_kit_id: "kAHCKfCZgk0"
photo_source: "gemini"
gemini_mode: "base_only"
gemini_model: "gemini-2.5-flash-image"

images:
  - story: 1
    type: social
    dimensions: "1200x675"
    gemini_mode: base_only
    prompt: "A cheerful Colorado summer collage scene showing three vignettes blended together: a family watching a rodeo from grandstands with cowboy hats, young children picking bright golden sunflowers in a farm field at dawn, and a family cheering at an outdoor soccer game. Warm golden-hour lighting. Vibrant sunflower yellows, sky blues, earthy browns. Families of diverse backgrounds, all smiling. Art style: editorial illustration, semi-realistic, saturated colors. Clean visual space in bottom third for text overlay. No logos, no text, no watermarks."
    output_file: "generated-images/story-1-weekend-roundup-social.png"
    status: not_started

  - story: 1
    type: article_hero
    dimensions: "1200x630"
    gemini_mode: base_only
    prompt: "A Colorado Springs mountain-backdrop summer scene with a family of four walking toward a festival entrance at golden hour. Rocky mountain peaks in background, cotton candy clouds. Warm orange and blue tones. Festive bunting overhead. Clean foreground with soft edges. Clean visual space in bottom third. No text, no logos."
    output_file: "generated-images/story-1-weekend-roundup-hero.png"
    status: not_started

  - story: 2
    type: social
    dimensions: "1200x675"
    gemini_mode: base_only
    prompt: "A soft, clinical-style product safety concept. Abstract silicone teething ring shape and a wooden learning tower stool in muted greens and grays against clean white background. Subtle red safety badge shape (no text) in upper corner. Soft studio lighting. No product logos or brand markings. Clean bottom third for text overlay."
    output_file: "generated-images/story-2-recalls-social.png"
    status: not_started

  - story: 2
    type: article_hero
    dimensions: "1200x630"
    gemini_mode: base_only
    prompt: "A parent's hands gently examining a small silicone teething toy on a clean white countertop. Soft focus baby nursery in neutral tones background. Natural window light. Calm, concerned mood. No logos, no text. Clean bottom third."
    output_file: "generated-images/story-2-recalls-hero.png"
    status: not_started

  - story: 3
    type: social
    dimensions: "1200x675"
    gemini_mode: base_only
    prompt: "A bright, cheerful back-to-school scene: an elementary-age child with a colorful backpack walking toward a school entrance on a sunny Colorado morning. Rocky Mountain foothills visible in background. Blue sky, green grass, red brick school facade. Warm morning light. Joyful, anticipatory mood. Clean bottom third for text overlay. No text, no logos."
    output_file: "generated-images/story-3-d20-school-social.png"
    status: not_started

  - story: 3
    type: article_hero
    dimensions: "1200x630"
    gemini_mode: base_only
    prompt: "A family of three (two parents and a school-age child) standing at a kitchen table with a backpack, school supply list, and a calendar visible. Morning light streaming through window. Warm, organized home setting. Teal and coral accent colors in kitchen decor. No logos, no text visible on calendar. Collaborative, prepared mood."
    output_file: "generated-images/story-3-d20-school-hero.png"
    status: not_started

  - story: 4
    type: social
    dimensions: "1200x675"
    gemini_mode: base_only
    prompt: "A soft-focus safety concept: a generic baby swing seat (no specific brand features) shown empty on a clean white background, with a soft amber safety overlay pattern suggesting caution. No infant present. Neutral beige, white, and muted orange tones. Clean studio lighting. No text, no logos. Clean bottom third."
    output_file: "generated-images/story-4-vevor-recall-social.png"
    status: not_started

  - story: 4
    type: article_hero
    dimensions: "1200x630"
    gemini_mode: base_only
    prompt: "A safe-sleep nursery scene: a simple wooden crib with a flat firm mattress and an infant sleeping on their back in a sleep sack. Clean, warm room free of clutter — no pillows, no bumpers, no inclined surfaces. Soft warm light from a nightlight. Peaceful, reassuring mood. No logos, no text."
    output_file: "generated-images/story-4-vevor-recall-hero.png"
    status: not_started

  - story: 5
    type: social
    dimensions: "1200x675"
    gemini_mode: base_only
    prompt: "A warm realistic living room scene at evening: a parent sitting with a school-age child at a kitchen table, both looking at a book rather than a screen. A tablet visible in background on a charging station on the counter — put away and off. Warm lamp light, cozy setting. Teal and warm amber tones. Calm, intentional mood. No text, no brand logos visible on devices. Clean bottom third."
    output_file: "generated-images/story-5-screen-time-social.png"
    status: not_started

  - story: 5
    type: article_hero
    dimensions: "1200x630"
    gemini_mode: base_only
    prompt: "A child's bedroom at night, curtains drawn, with a clear nightstand — no phone or tablet present, just a small lamp and a book. A middle-school-age child settled in bed, relaxed and ready for sleep. Soft warm light, peaceful atmosphere. The absence of devices is calm and natural. No text, no logos."
    output_file: "generated-images/story-5-screen-time-hero.png"
    status: not_started
```
