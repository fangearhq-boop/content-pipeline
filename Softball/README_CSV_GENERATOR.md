# PostPlanner CSV Generator

A Python script that generates PostPlanner-compatible CSV files from approved social media content in markdown format.

## Features

- Parses X/Twitter posts from `03-social-posts-x.md`
- Parses Facebook posts from `04-social-posts-facebook.md`
- Supports approval filtering via `approvals.json`
- Generates timestamped CSV files ready for PostPlanner import
- Extracts hashtags automatically
- Handles thread posts for X/Twitter
- Only uses Python standard library (csv, re, json, os, sys, datetime)

## Usage

### Basic Usage (Today's Date)

```bash
python generate-postplanner-csv.py
```

### Specific Date

```bash
python generate-postplanner-csv.py 2026-02-14
```

### Output

Creates two CSV files in `postplanner-imports/` subdirectory:
- `twitter-posts-YYYY-MM-DD.csv`
- `facebook-posts-YYYY-MM-DD.csv`

## File Structure

### Input Files

Place markdown files in the same directory as the script:

#### `03-social-posts-x.md` Format

```markdown
## STORY 1: Story Name

### Text Post
Your tweet text here (max 280 chars)

### Thread Concept
**Tweet 1:**
First tweet text

**Tweet 2:**
Second tweet text
```

#### `04-social-posts-facebook.md` Format

```markdown
## STORY 1: Story Name

### Long-Form Post
Your long-form post content here

### Engagement Prompt
Question to encourage comments

### Image Post
Image caption text
```

### `approvals.json` (Optional)

If this file exists, only posts with `"status": "approved"` are exported.

```json
{
  "x_story1_text": {
    "status": "approved",
    "approved_by": "manager",
    "approved_date": "2026-02-12"
  },
  "x_story1_thread_start": {
    "status": "pending"
  },
  "fb_story1": {
    "status": "approved"
  }
}
```

**Post ID Format:**
- X text posts: `x_storyN_text`
- X thread starts: `x_storyN_thread_start`
- X thread replies: `x_storyN_thread_M` (where M is the tweet number)
- Facebook posts: `fb_storyN`

## Output CSV Formats

### twitter-posts-YYYY-MM-DD.csv

| Column | Description |
|--------|-------------|
| `content` | Tweet text (≤280 characters) |
| `type` | `text`, `thread_start`, or `thread_reply` |
| `hashtags` | Space-separated hashtags extracted from content |
| `story` | Story reference name |
| `status` | `approved` or `pending` |

### facebook-posts-YYYY-MM-DD.csv

| Column | Description |
|--------|-------------|
| `content` | Long-form post text |
| `engagement_prompt` | Question to encourage engagement |
| `image_caption` | Caption for image post (if available) |
| `story` | Story reference name |
| `status` | `approved` or `pending` |

## Examples

### Example: With Approvals File

If `approvals.json` exists and contains approval status for posts:

```bash
$ python generate-postplanner-csv.py 2026-02-14
📅 Processing posts for: 2026-02-14
📁 Content folder: /path/to/folder
💾 Output folder: /path/to/folder/postplanner-imports

✓ Approvals file found: 10 entries
  → Filtered to 6 X posts and 2 Facebook posts

✓ Generated twitter-posts-2026-02-14.csv (6 posts)
✓ Generated facebook-posts-2026-02-14.csv (2 posts)

✅ Complete! CSV files ready in: postplanner-imports/
```

### Example: Without Approvals File

If no `approvals.json` exists, all posts are exported:

```bash
$ python generate-postplanner-csv.py
📅 Processing posts for: 2026-02-14
📁 Content folder: /path/to/folder
💾 Output folder: /path/to/folder/postplanner-imports

ℹ No approvals file found: exporting all posts

✓ Generated twitter-posts-2026-02-14.csv (12 posts)
✓ Generated facebook-posts-2026-02-14.csv (2 posts)

✅ Complete! CSV files ready in: postplanner-imports/
```

## Parsing Rules

### X/Twitter Posts
- Posts are extracted from sections under `## STORY N:` headers
- Text posts are under `### Text Post` sections
- Thread posts are under `### Thread Concept` sections
- Tweets are identified by `**Tweet M:**` markers
- All posts must be ≤280 characters
- Hashtags are automatically extracted from post text

### Facebook Posts
- Stories are sections under `## STORY N:` headers
- Long-form posts are under `### Long-Form Post` sections
- Engagement prompts are under `### Engagement Prompt` sections
- Image captions are under `### Image Post` sections
- At least a long-form post is required to create an entry

## Error Handling

- **Invalid date format:** Script exits with error message
- **Missing markdown files:** Warning logged, continues with empty posts
- **Invalid approvals.json:** Warning logged, treats as no approvals
- **No posts found:** Warning logged for each missing post type

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Troubleshooting

### No posts are being exported
1. Verify markdown files are named correctly:
   - `03-social-posts-x.md`
   - `04-social-posts-facebook.md`
2. Check file structure follows the format documented above
3. If using approvals, verify post IDs match the format (e.g., `x_story1_text`)

### Posts appear as "pending" but I approved them
1. Check `approvals.json` for correct post IDs
2. Ensure status field is exactly: `"status": "approved"`
3. Verify JSON syntax is valid

### Character limit warnings not appearing
The script silently skips posts over 280 characters for Twitter. Check your markdown source if expected posts are missing.

## Development

The script consists of three main classes:

- **SocialPostParser:** Reads and parses markdown files, manages approvals
- **CSVExporter:** Writes CSV files in PostPlanner format
- **main():** Orchestrates the workflow

All parsing uses standard regex patterns matching the markdown format.
