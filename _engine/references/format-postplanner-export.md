# FanGear HQ Content Engine: PostPlanner Export Format
**Reference for:** `_engine/scripts/generate-postplanner-export.py`

---

## PostPlanner Bulk Upload V3.1 — XLSX Format

PostPlanner requires a specific XLSX format for bulk importing posts. **CSV will not work.**

### Row Structure

| Row | Purpose |
|-----|---------|
| 1 | Comment row. Cell A1: `## {brand_name} -- PostPlanner Bulk Upload`. Cell B1: `BULK UPLOAD VERSION 3.1 – Please DO NOT EDIT this cell.` |
| 2 | Column header comment. A2: `## POSTING TIME`, B2: `CAPTION`, C2: `LINK`, D2: `MEDIA`, E2: `TITLE`, F2: `FIRST COMMENT`, G2: `FIRST COMMENT DELAY`, H2: `TOBI BACKGROUND`, I2: `REEL OR STORY` |
| 3+ | Data rows — one post per row |

### Column Definitions

| Column | Header | Description |
|--------|--------|-------------|
| A | POSTING TIME | `MM/DD/YYYY  HH:MM` in 24hr format. Empty = queued. |
| B | CAPTION | The post text. For X/Twitter, links go here too. |
| C | LINK | URL to link to. **Not used for X/Twitter** — links go in CAPTION. |
| D | MEDIA | Image or video URL. Empty for text-only posts. |
| E | TITLE | Pinterest/YouTube only. Not used for X/Twitter/Facebook. |
| F | FIRST COMMENT | Facebook/Instagram/LinkedIn only. Comment posted after the main post. |
| G | FIRST COMMENT DELAY | Delay in minutes before first comment posts: 5, 10, 15, 30, or 60. |
| H | TOBI BACKGROUND | Facebook TOBI (text-on-background-image). Background name, e.g. `true-black`, `shapes`. |
| I | REEL OR STORY | Facebook/Instagram: `reel` or `story`. |

### Post Type Auto-Detection

V3.1 auto-detects post type based on which columns are filled:
- **Text post:** Only B (caption)
- **Link post:** B + C (caption + link)
- **Image/Video:** B + D (caption + media URL)
- **TOBI:** B + H (caption + TOBI background name)
- **Reel/Story:** B + D + I (caption + media + reel/story)

### Critical Rules

- Cell B1 **must** contain `BULK UPLOAD VERSION 3.1` — PostPlanner uses this to detect the format
- Any row where cell A starts with `##` is treated as a comment and ignored
- Time format is **24-hour** (e.g., `13:00` not `1:00 PM`)
- Double space between date and time: `02/25/2026  13:00`
- File must be `.xlsx` (Excel), not `.csv`
- For X/Twitter: never put tweet text in the LINK column — it will be treated as a URL
- **TOBI background goes in Column H** — putting values in Column F/G will post them as first comments

### Usage

**Standard export (X/Twitter + Facebook):**
```bash
python _engine/scripts/generate-postplanner-export.py --niche {NICHE_FOLDER} YYYY-MM-DD
```

**TOBI export (Facebook Text On Background Image):**
```bash
python _engine/scripts/generate-postplanner-export.py --niche {NICHE_FOLDER} YYYY-MM-DD --tobi
```

The standard script:
1. Reads `niche-config.yaml` to get brand name, content prefix, and platforms
2. Parses `03-social-posts-x.md` for X/Twitter posts
3. Parses `04-social-posts-facebook.md` for Facebook posts (if platform is enabled)
4. Outputs `postplanner-imports/postplanner-upload-YYYY-MM-DD.xlsx` in the niche folder

The TOBI script:
1. Parses `03-social-posts-x.md` for X/Twitter text posts
2. Uses the EXACT same text as the tweet — no stripping, no truncation
3. Only change: `#NUMBER` rankings → `No. NUMBER` (avoids Facebook hashtag links)
4. Sets Column H = `true-black` for each post (TOBI background)
5. Outputs `postplanner-imports/postplanner-tobi-upload-YYYY-MM-DD.xlsx`

### Posting Time Detection

The script handles two time formats found in content markdown files:

1. **Heading format:** `#### Text Post -- 9:00 AM ET` (time in the section heading)
2. **Tag format:** `**[POSTING WINDOW: 7:00 AM CT]**` (time in a metadata tag below the post)

Both are converted to PostPlanner's `MM/DD/YYYY HH:MM` 24-hour format.
