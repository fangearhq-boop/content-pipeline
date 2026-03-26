# Installation & Quick Start Guide

## File Location
Script saved to: `/sessions/hopeful-gifted-cori/mnt/Softball/generate-postplanner-csv.py`

## Prerequisites
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

The script is ready to use immediately. No installation required.

```bash
# Make it executable (optional)
chmod +x /sessions/hopeful-gifted-cori/mnt/Softball/generate-postplanner-csv.py
```

## Quick Start

### 1. Prepare Your Content

Place markdown files in the same directory as the script:

**`03-social-posts-x.md`** - X/Twitter content
**`04-social-posts-facebook.md`** - Facebook content

Optional: **`approvals.json`** - Approval tracking

### 2. Run the Script

```bash
# Today's date (auto-detected)
python generate-postplanner-csv.py

# Specific date
python generate-postplanner-csv.py 2026-02-14
```

### 3. Collect Output

CSV files are generated in `postplanner-imports/` subdirectory:
- `twitter-posts-YYYY-MM-DD.csv`
- `facebook-posts-YYYY-MM-DD.csv`

## File Specifications

### Input: 03-social-posts-x.md

```markdown
## STORY 1: Story Title

### Text Post
Tweet text (under 280 characters)

### Thread Concept
**Tweet 1:**
First tweet

**Tweet 2:**
Second tweet
```

### Input: 04-social-posts-facebook.md

```markdown
## STORY 1: Story Title

### Long-Form Post
Your long post here

### Engagement Prompt
Your engagement question?

### Image Post
Image caption here
```

### Input: approvals.json (Optional)

```json
{
  "x_story1_text": { "status": "approved" },
  "fb_story1": { "status": "approved" }
}
```

If this file exists, only "approved" posts are exported.

## Output Specifications

### twitter-posts-YYYY-MM-DD.csv
Columns: `content`, `type`, `hashtags`, `story`, `status`

### facebook-posts-YYYY-MM-DD.csv
Columns: `content`, `engagement_prompt`, `image_caption`, `story`, `status`

## Examples

```bash
# Generate for today
$ python generate-postplanner-csv.py
📅 Processing posts for: 2026-02-14
✓ Generated twitter-posts-2026-02-14.csv (6 posts)
✓ Generated facebook-posts-2026-02-14.csv (2 posts)
✅ Complete!

# Generate for specific date
$ python generate-postplanner-csv.py 2026-02-21
📅 Processing posts for: 2026-02-21
✓ Generated twitter-posts-2026-02-21.csv (6 posts)
✓ Generated facebook-posts-2026-02-21.csv (2 posts)
✅ Complete!
```

## Troubleshooting

**"No posts to export"**
- Verify markdown filenames: `03-social-posts-x.md`, `04-social-posts-facebook.md`
- Check formatting matches specification above

**"Invalid date format"**
- Use format: `YYYY-MM-DD` (e.g., `2026-02-14`)

**Posts show as "pending" but I approved them**
- Verify `approvals.json` post IDs match exactly
- Check JSON syntax is valid

## Script Features

✓ Automatic date handling (defaults to today)
✓ Approval filtering (when approvals.json exists)
✓ Hashtag extraction
✓ X/Twitter thread support (thread_start, thread_reply types)
✓ Facebook multi-section support
✓ Robust markdown parsing
✓ Standard library only (no external dependencies)
✓ Error handling with helpful messages
✓ PostPlanner-compatible CSV format

## Support Files Included

- `generate-postplanner-csv.py` - Main script (329 lines)
- `README_CSV_GENERATOR.md` - Detailed documentation
- `INSTALLATION.md` - This file
- `03-social-posts-x.md` - Example X posts
- `04-social-posts-facebook.md` - Example Facebook posts
- `approvals.json` - Example approvals file

## License

Use freely within your organization.
