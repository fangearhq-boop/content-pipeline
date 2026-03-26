# FanGear HQ Content Engine: Image Concepts Format
**Universal Template** | Niche-specific values from: brand-guide.md, niche-config.yaml

---

## File Header

```
# {BRAND_NAME} - Image Concepts
**Date:** {CONCEPT_DATE}
**Prepared By:** FanGear HQ Content Engine
```

---

## Per-Story Format

Repeat this block for each story.

### STORY {N}: {STORY_TITLE}

**Photo:** {player name or team name}

| Platform | Headline | Subtitle |
|----------|----------|----------|
| X | {HEADLINE} | {SUBTITLE} |
| Facebook | {HEADLINE} | {SUBTITLE} |

---

## Rules (for content engine, not included in output)

- **Photo line** depends on CONFIG.photo_source:
  - Imagn: player name or team name ONLY (reviewer searches imagn manually)
  - Gemini: full AI image generation prompt (detailed scene description)
- If X and Facebook need different photos, add a second **Photo:** line labeled (FB)
- Overlay text: Bebas Neue headline (all caps), Montserrat subtitle — per brand-guide.md
- X image: 1200x675 | Facebook image: 1200x630 | Same photo OK (different crop)
