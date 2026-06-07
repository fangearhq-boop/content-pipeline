# Image Manifest — COS Parenting
**Date:** 2026-06-07
**Pipeline Step:** 10 — Image Manifest
**Photo Source:** gemini (AI-generated)
**Mode:** base_only
**Model:** gemini-2.5-flash-image

## Status Legend
- `not_started` — image not yet generated
- `generating` — Gemini API call in progress
- `generated` — image created, not yet uploaded
- `uploaded` — image uploaded to WordPress media library
- `published` — image assigned to post/article

---

## Story 1: Vevor Baby Swing Recall

| Image | Type | Dimensions | Status |
|-------|------|------------|--------|
| Social | X format | 1200x675 | not_started |
| Article Hero | Landscape | 1200x630 | not_started |

**Prompts:** Neutral nursery product backdrop (social); soft infant care/safety concept — white fabrics, crib elements (article)
**Notes:** No baby likenesses; no brand logos; clean bottom third

---

## Story 2: COS Parks Budget Cuts

| Image | Type | Dimensions | Status |
|-------|------|------------|--------|
| Social | X format | 1200x675 | not_started |
| Article Hero | Landscape | 1200x630 | not_started |

**Prompts:** Sunny city park with playground equipment (social); landscape view with Pikes Peak, neighborhood park setting (article)
**Notes:** No people; clean bottom third; Colorado sky

---

## Story 3: PPYMCA Summer Camp

| Image | Type | Dimensions | Status |
|-------|------|------------|--------|
| Social | X format | 1200x675 | not_started |
| Article Hero | Landscape | 1200x630 | not_started |

**Prompts:** Colorful art supplies on bright table (social); activity table with paints and paper, summer light (article)
**Notes:** No children; no brand logos; cheerful palette

---

## Story 4: COS Childcare Desert

| Image | Type | Dimensions | Status |
|-------|------|------------|--------|
| Social | X format | 1200x675 | not_started |
| Article Hero | Landscape | 1200x630 | not_started |

**Prompts:** Warm, empty daycare/classroom room (social); eastern COS residential landscape view (article)
**Notes:** No children or faces; no brand logos

---

## Story 5: D11 Labor Dispute

| Image | Type | Dimensions | Status |
|-------|------|------------|--------|
| Social | X format | 1200x675 | not_started |
| Article Hero | Landscape | 1200x630 | not_started |

**Prompts:** Elementary school exterior — brick, flag, lawn (social); empty school hallway (article)
**Notes:** No people; no identifying school signage

---

## Gemini Generation Notes
- API key: configured in environment (GEMINI_API_KEY)
- All images: mode = base_only (Canva adds text overlays)
- Cost estimate: 10 images × ~$0.04 = ~$0.40
- Generation command: python _engine/scripts/generate-article-images.py --niche COS 2026-06-07
