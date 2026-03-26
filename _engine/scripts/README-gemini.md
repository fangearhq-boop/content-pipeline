# Gemini Image Generation — Technical Reference
**Script:** `generate-gemini-image.py`
**Added:** 2026-02-23
**Status:** Fully implemented and tested

---

## Overview

AI-powered image generation for the FanGear HQ content pipeline using Google's Gemini API. Replaces stock photo searches (Unsplash/Pexels) for non-sport niches where custom AI imagery produces better results than generic stock.

### Two Modes

| Mode | How It Works | When to Use |
|------|-------------|-------------|
| **`base_only`** | Gemini generates a clean background image with no text. Upload to Canva, add branded text overlays, export. | When brand consistency matters (uses Canva brand kit fonts/colors) |
| **`complete`** | Gemini generates a finished graphic with text baked in. Bypasses Canva entirely. | When speed matters and brand precision is less critical |

### Models

| Model | Speed | Cost | Max Resolution | Best For |
|-------|-------|------|----------------|----------|
| `gemini-2.5-flash-image` | Fast | ~$0.04/image | 1K (1344x768) | Daily production |
| `gemini-3-pro-image-preview` | Slower | ~$0.20/image | 2K/4K | Hero images, high-visibility content |

---

## Prerequisites

### Python Packages
```bash
pip install google-genai Pillow
```

### Environment Variable
```bash
export GEMINI_API_KEY="your-key-here"
```
The API key requires a Google Cloud project with **billing enabled** (free tier has extremely low limits). Get a key at https://aistudio.google.com/apikey

---

## Usage

### Single Image
```bash
python generate-gemini-image.py \
    --prompt "A photorealistic playground scene in Colorado Springs..." \
    --dimensions 1200x675 \
    --mode base_only \
    --output ./generated-images/story-1-x.png
```

### Both Platforms for a Story
```bash
python generate-gemini-image.py \
    --prompt "A photorealistic playground scene in Colorado Springs..." \
    --story-number 1 \
    --content-folder ./parenting-content-2026-02-22 \
    --mode base_only
```
This generates two images:
- `generated-images/story-1-x.png` (1200x675)
- `generated-images/story-1-facebook.png` (1200x630)

### Dry Run (Preview Without API Call)
```bash
python generate-gemini-image.py \
    --prompt "..." \
    --dimensions 1200x675 \
    --dry-run
```

### Budget Report
```bash
python generate-gemini-image.py --budget
```

### Higher Quality Model
```bash
python generate-gemini-image.py \
    --prompt "..." \
    --model gemini-3-pro-image-preview \
    --dimensions 1200x675
```

---

## Cost Guardrails

Every API call is logged and tracked. Multiple layers prevent accidental overspending:

### Limits

| Guardrail | Default | Override |
|-----------|---------|----------|
| **Daily cap** | 50 images/day | `GEMINI_DAILY_CAP` env var or `--daily-cap N` |
| **Per-run cap** | 20 images/execution | `--per-run-cap N` |
| **Monthly warning** | $25.00/month | `GEMINI_MONTHLY_WARN` env var |

### How They Work

- **Daily cap (50)** — Hard block. Normal day = ~16 images (8 stories x 2 platforms). Cap leaves room for regenerations but catches any runaway loop.
- **Per-run cap (20)** — Hard block per script execution. Prevents a single invocation from going wild. Resets each time the script starts.
- **Monthly warning ($25)** — Soft warning printed to console when threshold is exceeded. Does not block, just alerts.

### Cost Math

| Scenario | Images | Cost (flash) | Cost (pro) |
|----------|--------|-------------|------------|
| 1 story (X + FB) | 2 | $0.08 | $0.40 |
| Full day (8 stories) | 16 | $0.64 | $3.20 |
| Full month (30 days) | 480 | $19.20 | $96.00 |
| Daily cap maxed | 50 | $2.00 | $10.00 |

### Generation Log

All API calls are recorded in `gemini-generation-log.json` (same directory as the script). Each entry includes:
- Timestamp (UTC)
- Model used
- Mode (base_only/complete)
- Dimensions
- Estimated cost
- Success/failure
- Output path

---

## How It Fits in the Content Pipeline

### Step 8: Image Concepts
When `photo_source: "gemini"` in niche-config.yaml, Step 8 writes **Gemini Image Prompts** instead of stock photo search terms. These are detailed visual descriptions including:
- Scene and subjects
- Mood and lighting
- Color palette guidance
- Art style (e.g., "photorealistic, editorial photography")
- For `base_only`: instruction to leave clean space for text overlays, no text in image
- For `complete`: includes headline text, colors, and placement

### Step 11: Image Production
The Gemini workflow in Step 11b:
1. Read the image prompt from image-concepts.md
2. Run `generate-gemini-image.py` with the prompt
3. Show generated image to user for approval
4. **If `base_only` mode:** Upload to Canva -> apply text overlay -> export (same as stock photo flow)
5. **If `complete` mode:** Image is done -> save path to manifest, mark as exported
6. If user rejects: regenerate with adjusted prompt
7. Update image-manifest.md with all tracking fields

### Image Manifest Status Flow

For Gemini-generated images, the manifest status lifecycle is:

```
not_started -> gemini_generated -> canva_uploaded -> design_created -> exported
                                   (base_only mode only)

not_started -> gemini_generated -> exported
                                   (complete mode — skips Canva)
```

Manifest fields specific to Gemini:
- `photo_source: gemini`
- `gemini_prompt:` — the exact prompt used (for regeneration)
- `gemini_image_path:` — local file path to the generated image

---

## Niche Configuration

In any niche's `niche-config.yaml`:

```yaml
photo_source: "gemini"

gemini_config:
  mode: "base_only"                    # "base_only" or "complete"
  model: "gemini-2.5-flash-image"      # or "gemini-3-pro-image-preview"
```

### Currently Using Gemini
- **COS Parenting** — `base_only` mode with `gemini-2.5-flash-image`

### Not Using Gemini (Uses Other Sources)
- Sports niches typically use `photo_source: "imagn"` for licensed athlete/team photos

---

## Technical Details

### Dimension Handling
Gemini API only supports aspect ratios (16:9, 1:1, etc.) and resolution tiers (1K/2K/4K) — not exact pixel dimensions. The script:
1. Maps target dimensions to the closest aspect ratio (e.g., 1200x675 -> 16:9)
2. Generates at native resolution (e.g., 1344x768 for 16:9 at 1K)
3. Resizes with PIL LANCZOS to exact target dimensions (e.g., 1200x675)

### Retry Logic
- 3 retries max
- Rate limit errors (HTTP 429): exponential backoff (5s, 10s, 15s)
- Other errors: 5s delay between retries
- All failures logged

### Module Import
The script can also be imported as a Python module:
```python
from generate_gemini_image import generate_image, generate_story_images

path = generate_image(
    prompt="A warm playground scene...",
    width=1200, height=675,
    mode="base_only"
)
```

---

## Prompt Writing Tips (for Step 8 Image Concepts)

### For `base_only` Mode
- Describe the scene vividly: subjects, setting, mood, lighting, time of day
- Specify "photorealistic" or your preferred art style
- Mention "leave the upper/lower third as open sky/space for text overlay"
- Do NOT mention any text, words, or logos — the script automatically appends a "no text" instruction
- Include brand color guidance if relevant to the scene

### For `complete` Mode
- Include everything above PLUS:
- The exact headline text to render
- Font style description (e.g., "bold white sans-serif text")
- Color values (e.g., "on a semi-transparent #2C3E50 overlay bar")
- Text placement (e.g., "centered across the bottom third")

### Example Prompt (base_only)
```
A warm photorealistic image of diverse families enjoying a sunny day at a
Colorado Springs playground, with Pikes Peak visible in the background,
golden afternoon light, children playing on colorful equipment while parents
chat nearby, autumn leaves on the ground, shot from a slight low angle to
convey energy and joy. Leave the upper third of the image as open sky for
text overlay space.
```

### Style Keywords That Work Well
`photorealistic`, `editorial photography`, `lifestyle photography`, `warm and inviting`, `authentic candid style`, `modern clean aesthetic`, `golden hour lighting`

### Avoid in Prompts
Celebrity likenesses, copyrighted characters, specific brand logos, violent/inappropriate content

---

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `GEMINI_API_KEY environment variable not set` | Key not exported in shell | `export GEMINI_API_KEY="your-key"` |
| `429 RESOURCE_EXHAUSTED` | Rate limit or quota exceeded | Wait and retry. If persistent, check billing is enabled on Google Cloud project |
| `GUARDRAIL BLOCKED: Daily limit reached` | Hit the 50 images/day cap | Wait until tomorrow, or override with `--daily-cap N` |
| `GUARDRAIL BLOCKED: Per-run limit reached` | Generated 20+ images in one execution | Start a new execution, or override with `--per-run-cap N` |
| `Response contained no image data` | API returned text instead of image | Retry (usually transient). Check prompt isn't triggering content filters |
| Image has unwanted text artifacts | Gemini sometimes adds text despite instructions | Regenerate with emphasis on "absolutely no text" in prompt |
