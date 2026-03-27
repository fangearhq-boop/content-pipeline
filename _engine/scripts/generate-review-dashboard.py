#!/usr/bin/env python3
"""
FanGear HQ Universal Review Dashboard Generator

This script generates an interactive HTML review dashboard for reviewing
content including daily briefs, social posts, articles, and image concepts.
Works across all niches by loading niche-specific config dynamically.

Usage:
    python generate-review-dashboard.py --niche Softball 2026-02-22
    python generate-review-dashboard.py --niche Parenting 2026-02-22
    # or auto-detect niche from cwd:
    python generate-review-dashboard.py 2026-02-22
"""

import sys
import os
import json
import re
import html
from datetime import datetime
from pathlib import Path
import importlib.util

# Fix Unicode output on Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Path helpers (copied from verify-facts.py)
# ---------------------------------------------------------------------------

def find_engine_root():
    """Find the _engine directory (parent of scripts/)."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_niche_root(niche_name=None):
    """Find the niche project root from --niche arg or current directory."""
    engine_root = find_engine_root()
    niche_launches = os.path.dirname(engine_root)

    if niche_name:
        niche_root = os.path.join(niche_launches, niche_name)
        if os.path.isdir(niche_root):
            return niche_root
        # Try case-insensitive match
        for entry in os.listdir(niche_launches):
            if entry.lower() == niche_name.lower() and entry != '_engine':
                return os.path.join(niche_launches, entry)
        print(f"ERROR: Niche folder not found: {niche_name}")
        print(f"  Looked in: {niche_launches}")
        sys.exit(1)
    else:
        # Auto-detect: walk up from cwd looking for niche-config.yaml
        cwd = os.getcwd()
        check = cwd
        while check != os.path.dirname(check):
            if os.path.isfile(os.path.join(check, 'niche-config.yaml')):
                return check
            check = os.path.dirname(check)
        print("ERROR: Could not auto-detect niche. Use --niche <name>")
        sys.exit(1)


def load_niche_config(niche_root):
    """Load niche-config.yaml and return as dict."""
    config_path = os.path.join(niche_root, 'niche-config.yaml')
    if not os.path.isfile(config_path):
        print(f"WARNING: No niche-config.yaml found at {config_path}")
        return {}

    config = {}
    platforms = []
    in_platforms = False
    with open(config_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            # Detect platforms list items
            if in_platforms:
                if stripped.startswith('- '):
                    platforms.append(stripped[2:].strip().strip('"').strip("'"))
                    continue
                else:
                    in_platforms = False
            if ':' in stripped:
                key, _, value = stripped.partition(':')
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key == 'platforms' and not value:
                    in_platforms = True
                    continue
                if value:
                    config[key] = value
    if platforms:
        config['platforms'] = platforms
    return config


# ---------------------------------------------------------------------------
# Data loading functions
# ---------------------------------------------------------------------------

def load_json_data(folder_path):
    """
    Load structured JSON data from 07-content-data.json if it exists.
    Returns the parsed JSON dict or None if not available.
    """
    json_path = os.path.join(folder_path, "07-content-data.json")
    if not os.path.isfile(json_path):
        return None
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Warning: Error reading JSON data file: {e}")
        return None


def read_file(path):
    """Safely read a file, return empty string if not found."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Warning: Error reading {path}: {e}")
        return ""


def build_stories_from_json_v2(json_data, folder_path):
    """
    Build the all_stories list from schema v2.0 JSON (produced by compile-content-data.py).
    Each x_post tweet gets its own card with tweet_label and posting metadata.
    Returns (all_stories, fact_check_results) tuple.
    """
    all_stories = []
    fact_check_results = {}

    for story in json_data.get('stories', []):
        story_num = story.get('story_num', 0)
        title = story.get('title', f'Story {story_num}')
        tier = story.get('tier', 0)
        posting_window = story.get('posting_window', '')

        # Daily brief card — reconstruct summary from structured fields
        brief_lines = [title]
        if tier:
            brief_lines.append(f"- **Tier:** {tier}")
        if story.get('status'):
            brief_lines.append(f"- **Status:** {story['status']}")
        if story.get('angle'):
            brief_lines.append(f"- **Angle:** {story['angle']}")
        if posting_window:
            brief_lines.append(f"- **Posting window:** {posting_window}")
        all_stories.append({
            'id': f'story-{story_num}-daily_brief',
            'story_num': str(story_num),
            'title': title,
            'content': '\n'.join(brief_lines),
            'type': 'daily_brief',
            'subsections': {},
            'posting_window': posting_window,
        })

        # X/Twitter posts — one card per tweet
        for i, tweet in enumerate(story.get('x_posts', [])):
            all_stories.append({
                'id': f'story-{story_num}-x_post-{i+1}',
                'story_num': str(story_num),
                'title': title,
                'tweet_label': tweet.get('label', f'Tweet {i+1}'),
                'content': tweet.get('text', ''),
                'type': 'x_post',
                'subsections': {},
                'posting_window': tweet.get('posting_time', posting_window),
                'tweet_type': tweet.get('tweet_type', ''),
                'hashtags': ' '.join(tweet.get('hashtags', [])),
                'char_count': tweet.get('char_count', 0),
                'tier': str(tier),
            })

        # Facebook posts
        fb = story.get('facebook')
        if fb and (fb.get('long_form') or fb.get('image_caption')):
            fb_parts = []
            if fb.get('long_form'):
                fb_parts.append(f"### Long-Form Post\n{fb['long_form']}")
            if fb.get('image_caption'):
                fb_parts.append(f"### Image Post Caption\n{fb['image_caption']}")
            all_stories.append({
                'id': f'story-{story_num}-facebook',
                'story_num': str(story_num),
                'title': title,
                'content': '\n\n'.join(fb_parts),
                'type': 'facebook',
                'subsections': {},
                'posting_window': fb.get('posting_time', posting_window),
            })

        # Image concepts
        img_list = story.get('image_concepts')
        if img_list and isinstance(img_list, list):
            img_parts = []
            for img in img_list:
                label = img.get('label', 'Image')
                size = img.get('size_desc', '')
                img_parts.append(f"**{label} — {size}**")
                for term in img.get('search_terms', []):
                    img_parts.append(f"- **Photo search:** {term}")
                for overlay in img.get('text_overlay', []):
                    img_parts.append(f"- **Text overlay:** {overlay}")
                if img.get('composition'):
                    img_parts.append(f"- **Composition:** {img['composition']}")
                if img.get('usage'):
                    img_parts.append(f"- **Usage:** {img['usage']}")
                img_parts.append('')
            all_stories.append({
                'id': f'story-{story_num}-image_concept',
                'story_num': str(story_num),
                'title': f"{title} — Image Concept",
                'content': '\n'.join(img_parts),
                'type': 'image_concept',
                'subsections': {},
            })

        # Fact-check
        fc = story.get('fact_check')
        if fc:
            status = fc.get('status', 'unverified')
            fact_check_results[str(story_num)] = status

    # Also load articles from folder (HTML files aren't in JSON content)
    articles = read_articles_from_folder(folder_path)
    all_stories.extend(articles)

    return all_stories, fact_check_results


def build_stories_from_json(json_data, folder_path):
    """
    Build the all_stories list from legacy JSON data (pre-v2.0).
    This is more reliable than markdown but less structured than v2.0.
    Returns (all_stories, fact_check_results) tuple.
    """
    all_stories = []
    fact_check_results = {}

    for story in json_data.get('stories', []):
        story_num = story.get('story_num', 0)
        title = story.get('title', f'Story {story_num}')
        content = story.get('content', {})

        # Daily brief
        if content.get('daily_brief'):
            all_stories.append({
                'id': f'story-{story_num}-daily_brief',
                'story_num': str(story_num),
                'title': title,
                'content': content['daily_brief'],
                'type': 'daily_brief',
                'subsections': {}
            })

        # X posts
        x_data = content.get('x_post', {})
        if x_data.get('text_post') or x_data.get('thread'):
            x_content_parts = []
            posting_window = x_data.get('posting_window', '')
            if posting_window:
                x_content_parts.append(f"**[POSTING WINDOW: {posting_window}]**\n")
            if x_data.get('text_post'):
                x_content_parts.append(f"### Text Post\n{x_data['text_post']}")
            if x_data.get('thread'):
                x_content_parts.append("### Thread Concept")
                for i, tweet in enumerate(x_data['thread'], 1):
                    x_content_parts.append(f"**Tweet {i}:**\n{tweet}")
            if x_data.get('image_concept'):
                x_content_parts.append(f"### Image Post Concept\n{x_data['image_concept']}")

            all_stories.append({
                'id': f'story-{story_num}-x_post',
                'story_num': str(story_num),
                'title': title,
                'content': '\n\n'.join(x_content_parts),
                'type': 'x_post',
                'subsections': {},
                'posting_window': posting_window
            })

        # Facebook posts
        fb_data = content.get('facebook', {})
        if fb_data.get('long_form'):
            fb_content_parts = []
            posting_window = fb_data.get('posting_window', '')
            if posting_window:
                fb_content_parts.append(f"**[POSTING WINDOW: {posting_window}]**\n")
            fb_content_parts.append(f"### Long-Form Post\n{fb_data['long_form']}")
            if fb_data.get('image_caption'):
                fb_content_parts.append(f"### Image Post Caption\n{fb_data['image_caption']}")

            all_stories.append({
                'id': f'story-{story_num}-facebook',
                'story_num': str(story_num),
                'title': title,
                'content': '\n\n'.join(fb_content_parts),
                'type': 'facebook',
                'subsections': {},
                'posting_window': posting_window
            })

        # Image concepts
        img_data = content.get('image_concept', {})
        if img_data.get('description'):
            img_content_parts = [img_data['description']]
            if img_data.get('photo_search_terms') or img_data.get('imagn_search_terms'):
                # Support both keys for backwards compatibility
                search_terms_key = 'photo_search_terms' if 'photo_search_terms' in img_data else 'imagn_search_terms'
                img_content_parts.append("### Photo Search Terms")
                for term in img_data[search_terms_key]:
                    img_content_parts.append(f"- {term}")
            if img_data.get('text_overlay'):
                img_content_parts.append("### Text Overlay Copy")
                for line in img_data['text_overlay']:
                    img_content_parts.append(f'"{line}"')

            all_stories.append({
                'id': f'story-{story_num}-image_concept',
                'story_num': str(story_num),
                'title': f"{title} — Image Concept",
                'content': '\n'.join(img_content_parts),
                'type': 'image_concept',
                'subsections': {}
            })

        # Fact-check results from JSON
        fc_data = story.get('fact_check', {})
        if fc_data:
            status = fc_data.get('status', 'unverified')
            if fc_data.get('claims_flagged', 0) > 0 or fc_data.get('errors_corrected', 0) > 0:
                fact_check_results[str(story_num)] = 'warning'
            elif status == 'verified' and fc_data.get('claims_checked', 0) > 0:
                fact_check_results[str(story_num)] = 'verified'
            else:
                fact_check_results[str(story_num)] = 'unverified'

    # Also load articles from the articles/ folder (HTML files aren't in JSON)
    articles = read_articles_from_folder(folder_path)
    all_stories.extend(articles)

    return all_stories, fact_check_results


def read_articles_from_folder(folder_path):
    """Read all HTML article files from articles/ subfolder AND content root."""
    articles = []
    seen_filenames = set()

    # Check articles/ subfolder first
    articles_folder = os.path.join(folder_path, "articles")
    if os.path.isdir(articles_folder):
        try:
            for filename in sorted(os.listdir(articles_folder)):
                if filename.endswith('.html'):
                    file_path = os.path.join(articles_folder, filename)
                    content = read_file(file_path)
                    if content:
                        title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
                        title = title_match.group(1) if title_match else filename
                        slug = filename.replace('.html', '')
                        articles.append({
                            'id': f'article-{slug}',
                            'filename': filename,
                            'title': title,
                            'content': content,
                            'type': 'article'
                        })
                        seen_filenames.add(filename)
        except Exception as e:
            print(f"Warning: Error reading articles subfolder: {e}")

    # Also check content root for article-*.html files
    try:
        for filename in sorted(os.listdir(folder_path)):
            if filename.startswith('article-') and filename.endswith('.html') and filename not in seen_filenames:
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    content = read_file(file_path)
                    if content:
                        title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
                        title = title_match.group(1) if title_match else filename
                        slug = filename.replace('.html', '')
                        articles.append({
                            'id': f'article-{slug}',
                            'filename': filename,
                            'title': title,
                            'content': content,
                            'type': 'article'
                        })
    except Exception as e:
        print(f"Warning: Error reading articles from content root: {e}")

    return articles


def parse_markdown_stories(content, content_type):
    """
    Parse markdown content into individual stories.
    Looks for '## STORY N:' headers as delimiters.
    For x_post type, splits each story into individual tweet cards.
    """
    stories = []
    # Reset per-story tweet counter for this parse run
    parse_markdown_stories._story_tweet_counts = {}

    if not content.strip():
        return stories

    # Split by story headers
    story_pattern = r'^#{2,3}\s+STORY\s+(\d+\w*):\s*(.+?)(?=^#{2,3}\s+STORY|\Z)'
    matches = re.finditer(story_pattern, content, re.MULTILINE | re.DOTALL)

    for match in matches:
        story_num = match.group(1)
        story_content = match.group(2).strip()

        # Extract title from first line or from subsections
        lines = story_content.split('\n')
        title = lines[0].strip() if lines else f"Story {story_num}"

        if content_type == 'x_post':
            # Split into individual tweet cards for better review
            # Track per-story tweet count to avoid duplicate IDs when same story appears multiple times
            if not hasattr(parse_markdown_stories, '_story_tweet_counts'):
                parse_markdown_stories._story_tweet_counts = {}
            start_idx = parse_markdown_stories._story_tweet_counts.get(story_num, 0)
            tweet_cards = extract_individual_tweets(story_num, title, story_content, start_index=start_idx)
            if tweet_cards:
                parse_markdown_stories._story_tweet_counts[story_num] = start_idx + len(tweet_cards)
                stories.extend(tweet_cards)
            else:
                # Fallback: treat as single card if parsing fails
                stories.append({
                    'id': f'story-{story_num}-{content_type}',
                    'story_num': story_num,
                    'title': title,
                    'content': story_content,
                    'type': content_type,
                    'subsections': parse_subsections(story_content)
                })
        else:
            stories.append({
                'id': f'story-{story_num}-{content_type}',
                'story_num': story_num,
                'title': title,
                'content': story_content,
                'type': content_type,
                'subsections': parse_subsections(story_content)
            })

    return stories


def extract_individual_tweets(story_num, story_title, story_content, start_index=0):
    """
    Extract individual tweets from a story's X post content.
    Each code block (``` ... ```) is treated as one tweet.
    Returns a list of card dicts, one per tweet.
    start_index: offset for tweet numbering to avoid duplicate IDs when
                 the same story_num appears in multiple sections.
    """
    cards = []
    lines = story_content.split('\n')

    in_code_block = False
    current_tweet_lines = []
    current_label = ""        # e.g., "Text Post", "Thread Tweet 1"
    current_type = ""         # Informative, Bold, Humor, etc.
    current_window = ""       # Posting window time
    tweet_index = start_index  # Counter for unique IDs within this story
    thread_tweet_num = 0      # Track thread tweet numbering
    in_thread = False

    # Pre-scan to extract tier info
    tier_match = re.search(r'\*\*Tier:\*\*\s*(.+)', story_content)
    tier = tier_match.group(1).strip() if tier_match else ""

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect section headers for labeling AND extract posting time
        if stripped.startswith('### Text Post') or stripped.startswith('#### Text Post'):
            current_label = re.sub(r'^#{3,4}\s*', '', stripped).strip()
            in_thread = False
            thread_tweet_num = 0
            # Extract time from heading like "Text Post 1 — 7:00 AM CT (Informative)"
            time_match = re.search(r'(\d{1,2}:\d{2}\s*[AP]M)\s+([A-Z]{2,3})', stripped)
            if time_match:
                current_window = time_match.group(1).strip() + ' ' + time_match.group(2).strip()
            continue
        if re.match(r'^#{3,4}\s+Thread', stripped, re.IGNORECASE):
            in_thread = True
            thread_tweet_num = 0
            current_label = re.sub(r'^#{3,4}\s*', '', stripped).strip()
            # Extract time from thread heading too
            time_match = re.search(r'(\d{1,2}:\d{2}\s*[AP]M)\s+([A-Z]{2,3})', stripped)
            if time_match:
                current_window = time_match.group(1).strip() + ' ' + time_match.group(2).strip()
            continue
        if stripped.startswith('### Image Post') or stripped.startswith('#### Image Post'):
            current_label = "Image Post Concept"
            in_thread = False
            # Extract time from image post heading too
            time_match = re.search(r'(\d{1,2}:\d{2}\s*[AP]M)\s+([A-Z]{2,3})', stripped)
            if time_match:
                current_window = time_match.group(1).strip() + ' ' + time_match.group(2).strip()
            continue

        # Detect thread tweet headers like **Tweet 1 (Hook):**
        tweet_header_match = re.match(r'^\*\*Tweet\s+(\d+)\s*\(([^)]+)\)\s*:\*\*', stripped)
        if tweet_header_match:
            thread_tweet_num = int(tweet_header_match.group(1))
            tweet_role = tweet_header_match.group(2).strip()
            current_label = f"Thread {thread_tweet_num}/{tweet_role}"
            continue

        # Code block boundaries
        if stripped.startswith('```'):
            if in_code_block:
                # End of code block — we have a complete tweet
                in_code_block = False
                tweet_text = '\n'.join(current_tweet_lines).strip()
                if tweet_text:
                    # Look ahead for metadata after the code block
                    post_window, post_type, post_charcount = _extract_tweet_metadata(lines, i + 1)
                    current_window = post_window or current_window
                    current_type = post_type or current_type

                    tweet_index += 1

                    # Build label for this tweet
                    if in_thread and thread_tweet_num > 0:
                        label = f"Thread {thread_tweet_num}"
                    elif current_label:
                        label = current_label
                    else:
                        label = f"Tweet {tweet_index}"

                    # Extract hashtags from tweet text
                    hashtag_matches = re.findall(r'#\w+', tweet_text)
                    hashtags = ' '.join(hashtag_matches) if hashtag_matches else ''

                    # Character count
                    char_count = count_tweet_chars(tweet_text)

                    cards.append({
                        'id': f'story-{story_num}-x_post-{tweet_index}',
                        'story_num': story_num,
                        'title': f"{story_title}",
                        'tweet_label': label,
                        'content': tweet_text,
                        'type': 'x_post',
                        'subsections': {},
                        'posting_window': current_window,
                        'tweet_type': current_type,
                        'hashtags': hashtags,
                        'char_count': char_count,
                        'tier': tier,
                    })

                current_tweet_lines = []
            else:
                # Start of code block
                in_code_block = True
                current_tweet_lines = []
            continue

        if in_code_block:
            current_tweet_lines.append(line)

    # If no code blocks found, try parsing plain text format
    # Handles two formats:
    #   1. **Post XY** labels (Softball style: multiple tweets per story)
    #   2. Plain text with --- separators (Cubs style: one tweet per story header)
    if not cards:
        cards = _extract_tweets_plain_text(story_num, story_title, story_content, start_index, tier)

    return cards


def _extract_tweets_plain_text(story_num, story_title, story_content, start_index, tier):
    """
    Fallback tweet extractor for plain text formats (no code blocks).
    Handles:
      - **Post XY** labels: splits by label, each label = one tweet
      - Plain text: treats entire content (minus title/summary lines) as one tweet
    """
    cards = []
    lines = story_content.split('\n')

    # Try splitting by **Post XY** labels first
    post_label_pattern = re.compile(r'^\*\*Post\s+(\w+)\*\*\s*$')
    post_sections = []
    current_label = None
    current_lines = []

    for line in lines:
        stripped = line.strip()
        m = post_label_pattern.match(stripped)
        if m:
            if current_label is not None and current_lines:
                post_sections.append((current_label, '\n'.join(current_lines).strip()))
            current_label = f"Post {m.group(1)}"
            current_lines = []
        elif current_label is not None:
            # Skip --- separators and ## Post Summary sections
            if stripped == '---' or stripped.startswith('## Post Summary'):
                if current_lines:
                    post_sections.append((current_label, '\n'.join(current_lines).strip()))
                    current_label = None
                    current_lines = []
                if stripped.startswith('## Post Summary'):
                    break
            else:
                current_lines.append(line)

    # Flush last section
    if current_label is not None and current_lines:
        post_sections.append((current_label, '\n'.join(current_lines).strip()))

    if post_sections:
        tweet_index = start_index
        for label, text in post_sections:
            text = text.strip()
            if not text:
                continue
            tweet_index += 1
            hashtag_matches = re.findall(r'#\w+', text)
            hashtags = ' '.join(hashtag_matches) if hashtag_matches else ''
            char_count = count_tweet_chars(text)
            cards.append({
                'id': f'story-{story_num}-x_post-{tweet_index}',
                'story_num': story_num,
                'title': story_title,
                'tweet_label': label,
                'content': text,
                'type': 'x_post',
                'subsections': {},
                'posting_window': '',
                'tweet_type': '',
                'hashtags': hashtags,
                'char_count': char_count,
                'tier': tier,
            })
        return cards

    # No **Post** labels found — treat entire content as a single tweet
    # Skip the title line (first non-empty line) and any trailing --- or summary
    content_lines = []
    skipped_title = False
    for line in lines:
        stripped = line.strip()
        if not skipped_title:
            if stripped:
                skipped_title = True  # Skip the title line
            continue
        if stripped == '---' or stripped.startswith('## Post Summary'):
            break
        content_lines.append(line)

    tweet_text = '\n'.join(content_lines).strip()
    if tweet_text:
        hashtag_matches = re.findall(r'#\w+', tweet_text)
        hashtags = ' '.join(hashtag_matches) if hashtag_matches else ''
        char_count = count_tweet_chars(tweet_text)
        cards.append({
            'id': f'story-{story_num}-x_post-{start_index + 1}',
            'story_num': story_num,
            'title': story_title,
            'tweet_label': f"Tweet {start_index + 1}",
            'content': tweet_text,
            'type': 'x_post',
            'subsections': {},
            'posting_window': '',
            'tweet_type': '',
            'hashtags': hashtags,
            'char_count': char_count,
            'tier': tier,
        })

    return cards


def _extract_tweet_metadata(lines, start_idx):
    """Look ahead from start_idx to extract posting window, type, and char count."""
    window = ""
    tweet_type = ""
    char_count = ""

    # Only scan the next 8 lines for metadata
    for j in range(start_idx, min(start_idx + 8, len(lines))):
        stripped = lines[j].strip()
        if not stripped:
            continue
        # Stop if we hit a new section header or code block
        if stripped.startswith('###') or stripped.startswith('```') or stripped.startswith('## STORY'):
            break

        window_match = re.search(r'\[POSTING WINDOW:\s*([^\]]+)\]', stripped)
        if window_match:
            window = window_match.group(1).strip()

        type_match = re.search(r'\[TYPE:\s*([^\]]+)\]', stripped)
        if type_match:
            tweet_type = type_match.group(1).strip()

        count_match = re.search(r'\[CHARACTER COUNT:\s*([^\]]+)\]', stripped)
        if count_match:
            char_count = count_match.group(1).strip()

    return window, tweet_type, char_count


def count_tweet_chars(text):
    """Count characters for a tweet, treating URLs as 23 chars each."""
    # Strip metadata tags that aren't part of the actual tweet
    text = re.sub(r'\[CHARACTER COUNT:.*?\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[CHAR COUNT:.*?\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[\d+/280\]', '', text)
    url_pattern = re.compile(r'https?://\S+')
    urls = url_pattern.findall(text)
    clean = url_pattern.sub('', text)
    return len(clean.strip()) + (23 * len(urls))


def parse_subsections(content):
    """Extract subsections from story content (### headers)."""
    subsections = {}
    pattern = r'^###\s+(.+?)(?=^###|\Z)'
    matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)

    for match in matches:
        section_title = match.group(1).strip().split('\n')[0]
        section_content = match.group(1).strip()
        subsections[section_title] = section_content

    return subsections


def count_chars_no_urls(text):
    """Count characters excluding URLs for Twitter character limit."""
    # Strip metadata tags that aren't part of the actual tweet
    text = re.sub(r'\[CHARACTER COUNT:.*?\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[CHAR COUNT:.*?\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[\d+/280\]', '', text)
    # Remove URLs (they count as 23 chars on Twitter)
    text_no_urls = re.sub(r'https?://\S+', '', text)
    return len(text_no_urls.strip())


def extract_photo_search_terms(content):
    """Extract photo search terms from image concept content."""
    terms = []
    in_search_section = False
    for line in content.split('\n'):
        stripped = line.strip()
        if 'Photo Search Terms' in stripped or 'Imagn Search Terms' in stripped or 'Stock Photo Search Terms' in stripped:
            in_search_section = True
            continue
        if in_search_section:
            if stripped.startswith('- '):
                terms.append(stripped[2:].strip())
            elif stripped.startswith('**') or stripped.startswith('###') or (stripped and not stripped.startswith('-')):
                in_search_section = False
    return terms


def extract_text_overlay(content):
    """Extract text overlay copy from image concept content."""
    lines = []
    in_overlay_section = False
    for line in content.split('\n'):
        stripped = line.strip()
        if 'Text Overlay Copy' in stripped:
            in_overlay_section = True
            continue
        if in_overlay_section:
            if stripped.startswith('"') or stripped.startswith('"'):
                lines.append(stripped.strip('""\u201c\u201d'))
            elif stripped.startswith('**') or stripped.startswith('###'):
                in_overlay_section = False
    return lines


def build_photo_search_url(term, photo_source):
    """Build a clickable photo search URL from a search term."""
    import urllib.parse
    encoded = urllib.parse.quote_plus(term)
    if photo_source == 'imagn':
        return f"https://www.imagn.com/search?q={encoded}"
    else:  # 'stock' or default
        return f"https://unsplash.com/s/photos/{encoded}"


def parse_image_manifest(folder_path):
    """
    Parse the image manifest YAML file and return a dict mapping
    story numbers to their image URLs and statuses.

    Returns: {
        '1': {
            'x_image': {'status': 'exported', 'exported_url': '...', 'imagn_url': '...'},
            'facebook_image': {'status': 'not_started', ...}
        }, ...
    }
    """
    manifest_path = os.path.join(folder_path, "07-image-manifest.md")
    content = read_file(manifest_path)

    if not content.strip():
        return {}

    # Simple YAML-like parsing — extract per-story image data
    # We do a lightweight parse rather than requiring pyyaml
    results = {}
    current_story = None
    current_platform = None

    for line in content.split('\n'):
        stripped = line.strip()

        # Match story number: '  "1":'
        story_match = re.match(r'^"(\d+)":', stripped)
        if story_match:
            current_story = story_match.group(1)
            results[current_story] = {'x_image': {}, 'facebook_image': {}}
            current_platform = None
            continue

        # Match platform: '    x_image:' or '    facebook_image:'
        if current_story:
            if stripped == 'x_image:':
                current_platform = 'x_image'
                continue
            elif stripped == 'facebook_image:':
                current_platform = 'facebook_image'
                continue

        # Match key-value pairs within a platform
        if current_story and current_platform:
            kv_match = re.match(r'^(\w+):\s*"?(.+?)"?\s*$', stripped)
            if kv_match:
                key = kv_match.group(1)
                value = kv_match.group(2).strip('"')
                results[current_story][current_platform][key] = value

    return results


def get_image_status_badge(story_id, image_manifest):
    """Generate image production status badge HTML for an image concept card."""
    story_num_match = re.search(r'story-(\d+)', story_id)
    if not story_num_match:
        return ''

    story_num = story_num_match.group(1)
    if not image_manifest:
        return '<span class="image-badge image-not-started" title="No image manifest found">NO IMAGES</span>'

    story_data = image_manifest.get(story_num, {})
    if not story_data:
        return '<span class="image-badge image-not-started" title="No image production started">NOT STARTED</span>'

    # Check both platforms
    x_status = story_data.get('x_image', {}).get('status', 'not_started')
    fb_status = story_data.get('facebook_image', {}).get('status', 'not_started')

    if x_status == 'exported' and fb_status == 'exported':
        return '<span class="image-badge image-exported" title="All images exported">IMAGES READY</span>'
    elif x_status in ('exported', 'design_created', 'canva_uploaded', 'imagn_selected') or \
         fb_status in ('exported', 'design_created', 'canva_uploaded', 'imagn_selected'):
        return '<span class="image-badge image-in-progress" title="Image production in progress">IN PROGRESS</span>'
    else:
        return '<span class="image-badge image-not-started" title="No image production started">NOT STARTED</span>'


def parse_fact_check_log(folder_path):
    """
    Parse the fact-check log file and return a dict mapping story numbers
    to their fact-check status: 'verified', 'warning', or 'unverified'.

    The log uses this format:
    ## Story N: Title
    - CLAIM: ... → VERIFIED (source)
    - CLAIM: ... → REMOVED — not in sources
    - CLAIM: ... → UNVERIFIED — flagged for manual review
    """
    log_path = os.path.join(folder_path, "06-fact-check-log.md")
    content = read_file(log_path)

    if not content.strip():
        # No fact-check log exists — everything is unverified
        return {}

    results = {}
    current_story = None
    has_warning = False
    has_unverified = False
    claim_count = 0

    for line in content.split('\n'):
        stripped = line.strip()

        # Detect story headers
        story_match = re.match(r'^##\s+Story\s+(\d+)', stripped, re.IGNORECASE)
        if story_match:
            # Save previous story status
            if current_story is not None:
                if has_unverified:
                    results[current_story] = 'warning'
                elif has_warning:
                    results[current_story] = 'warning'
                elif claim_count > 0:
                    results[current_story] = 'verified'
                else:
                    results[current_story] = 'unverified'

            current_story = story_match.group(1)
            has_warning = False
            has_unverified = False
            claim_count = 0
            continue

        # Check claim results — supports both table rows and bullet-point format
        if current_story and (stripped.startswith('- ') or stripped.startswith('| ')):
            # Skip table headers and separator rows
            if stripped.startswith('| Priority') or stripped.startswith('|---'):
                continue
            claim_count += 1
            lower = stripped.lower()
            if 'removed' in lower or 'unverified' in lower or 'flagged' in lower:
                has_warning = True
            elif 'corrected' in lower:
                has_warning = True
            elif 'verified' in lower or 'confirmed' in lower:
                pass  # Good
            elif 'warning' in lower:
                has_warning = True

    # Save last story
    if current_story is not None:
        if has_unverified:
            results[current_story] = 'warning'
        elif has_warning:
            results[current_story] = 'warning'
        elif claim_count > 0:
            results[current_story] = 'verified'
        else:
            results[current_story] = 'unverified'

    return results


def get_fact_check_badge_html(story_id, fact_check_results):
    """Generate fact-check badge HTML for a story card."""
    # Extract story number from ID
    story_num_match = re.search(r'story-(\d+)', story_id)
    if not story_num_match:
        return ''

    story_num = story_num_match.group(1)

    if not fact_check_results:
        # No fact-check log exists at all
        return '<span class="fact-check-badge fact-check-unverified" title="No fact-check log found — content not verified">NOT VERIFIED</span>'

    status = fact_check_results.get(story_num, 'unverified')

    if status == 'verified':
        return '<span class="fact-check-badge fact-check-verified" title="All factual claims verified against sources">FACT-CHECKED</span>'
    elif status == 'warning':
        return '<span class="fact-check-badge fact-check-warning" title="Some claims were removed or flagged for review">REVIEW FLAGS</span>'
    else:
        return '<span class="fact-check-badge fact-check-unverified" title="Content not yet fact-checked">NOT VERIFIED</span>'


def create_html_dashboard(date, all_stories, brand_name, content_prefix, photo_source,
                         fact_check_results=None, image_manifest=None, traffic_data=None):
    """Generate the complete HTML dashboard with full content view and inline editing."""

    total_items = len(all_stories)

    # Build stories JSON with FULL content for JS
    stories_json = json.dumps([{
        'id': story['id'],
        'title': story['title'],
        'content': story['content'],
        'type': story['type'],
        'posting_window': story.get('posting_window', ''),
        'tweet_type': story.get('tweet_type', ''),
        'hashtags': story.get('hashtags', ''),
        'tweet_label': story.get('tweet_label', ''),
    } for story in all_stories])
    # Escape </ sequences to prevent HTML parser from prematurely closing <script> tags
    # when article HTML content contains </title>, </section>, etc. inside JSON strings
    stories_json = stories_json.replace('</', '<\\/')

    # Build image manifest JSON for JS — maps story numbers to exported URLs
    manifest_for_js = {}
    if image_manifest:
        for story_num, story_data in image_manifest.items():
            manifest_for_js[story_num] = {}
            for platform in ('x_image', 'facebook_image'):
                pdata = story_data.get(platform, {})
                manifest_for_js[story_num][platform] = {
                    'status': pdata.get('status', 'not_started'),
                    'exported_url': pdata.get('exported_url', ''),
                    'imagn_url': pdata.get('imagn_url', '')
                }
    image_manifest_json = json.dumps(manifest_for_js)

    # Brand colors (defaults from Softball if not in config)
    header_color_1 = "#FF8A00"
    header_color_2 = "#E53935"

    # Store localStorage key prefix
    review_storage_key = content_prefix + '-review'
    schedule_storage_key = content_prefix + '-schedule-config'

    # Determine photo source label
    photo_source_label = "Search Imagn for Photos" if photo_source == "imagn" else "Search for Stock Photos"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(brand_name)} — Content Review Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #f5f5f5;
            display: flex;
            min-height: 100vh;
            color: #333;
        }}

        .sidebar {{
            width: 280px;
            background: #1a1a2e;
            color: white;
            padding: 30px 20px;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            z-index: 10;
        }}

        .sidebar h1 {{ font-size: 18px; margin-bottom: 10px; color: {header_color_1}; font-weight: 700; }}
        .sidebar-date {{ font-size: 12px; color: #aaa; margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid #333; }}
        .sidebar-section {{ margin-bottom: 25px; }}
        .sidebar-section-title {{ font-size: 12px; text-transform: uppercase; color: #999; margin-bottom: 12px; font-weight: 600; letter-spacing: 1px; }}

        .nav-item {{
            display: block; padding: 12px 15px; margin-bottom: 8px; border-radius: 6px;
            cursor: pointer; transition: all 0.3s ease; font-size: 14px; color: #ddd; user-select: none;
        }}
        .nav-item:hover {{ background: #2d2d44; color: {header_color_1}; }}
        .nav-item.active {{ background: {header_color_1}; color: white; }}
        .nav-item-count {{ float: right; background: rgba(255, 107, 53, 0.3); padding: 2px 8px; border-radius: 3px; font-size: 12px; }}
        .nav-item.active .nav-item-count {{ background: rgba(0, 0, 0, 0.2); }}

        .main-content {{ margin-left: 280px; flex: 1; display: flex; flex-direction: column; }}

        .header {{
            background: white; padding: 25px 40px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-bottom: 3px solid {header_color_1};
        }}
        .header h1 {{ font-size: 28px; color: #1a1a2e; margin-bottom: 10px; }}
        .header-meta {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; }}
        .progress-bar {{ flex: 1; min-width: 200px; }}
        .progress-label {{ font-size: 13px; color: #666; margin-bottom: 8px; font-weight: 500; }}
        .progress-container {{ width: 100%; height: 8px; background: #ddd; border-radius: 4px; overflow: hidden; }}
        .progress-fill {{ height: 100%; background: linear-gradient(90deg, {header_color_1}, {header_color_2}); transition: width 0.3s ease; }}
        .header-actions {{ display: flex; gap: 10px; }}

        .btn {{
            padding: 10px 16px; border: none; border-radius: 6px; font-size: 14px;
            font-weight: 600; cursor: pointer; transition: all 0.3s ease; white-space: nowrap;
        }}
        .btn-primary {{ background: {header_color_1}; color: white; }}
        .btn-primary:hover {{ background: {header_color_2}; }}
        .btn-secondary {{ background: #f0f0f0; color: #333; }}
        .btn-secondary:hover {{ background: #e0e0e0; }}

        .filter-bar {{
            background: white; padding: 20px 40px; display: flex;
            gap: 10px; flex-wrap: wrap; border-bottom: 1px solid #eee;
        }}
        .filter-btn {{
            padding: 8px 14px; border: 1px solid #ddd; background: white;
            border-radius: 5px; cursor: pointer; font-size: 13px; transition: all 0.3s ease;
        }}
        .filter-btn:hover {{ border-color: {header_color_1}; color: {header_color_1}; }}
        .filter-btn.active {{ background: {header_color_1}; color: white; border-color: {header_color_1}; }}

        .content {{ flex: 1; padding: 30px 40px; overflow-y: auto; }}

        .cards-container {{ display: flex; flex-direction: column; gap: 20px; max-width: 900px; }}

        .card {{
            background: white; border-radius: 8px; padding: 24px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: all 0.3s ease;
            border-left: 5px solid #ccc; display: none;
        }}
        .card.show {{ display: block; }}
        .card.approved {{ border-left-color: #22c55e; }}
        .card.needs-edit {{ border-left-color: #eab308; }}
        .card.rejected {{ border-left-color: #ef4444; }}
        .card:hover {{ box-shadow: 0 4px 16px rgba(0,0,0,0.12); }}

        .card-header {{ display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px; }}
        .card-title {{ font-size: 16px; font-weight: 600; color: #1a1a2e; flex: 1; margin-right: 10px; }}

        .card-badge {{
            display: inline-block; padding: 4px 10px; border-radius: 4px;
            font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;
        }}
        .badge-x-post {{ background: #1da1f2; color: white; }}
        .badge-facebook {{ background: #4267b2; color: white; }}
        .badge-article {{ background: #9333ea; color: white; }}
        .badge-image {{ background: #06b6d4; color: white; }}
        .badge-brief {{ background: #10b981; color: white; }}

        .fact-check-badge {{
            display: inline-block; padding: 3px 8px; border-radius: 4px;
            font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;
            margin-left: 6px;
        }}
        .fact-check-verified {{ background: #dcfce7; color: #166534; border: 1px solid #86efac; }}
        .fact-check-warning {{ background: #fef9c3; color: #854d0e; border: 1px solid #fde047; }}
        .fact-check-unverified {{ background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }}

        /* Content area — preview (collapsed) and full (expanded) */
        .card-content {{
            background: #f9f9f9; padding: 15px; border-radius: 6px;
            margin-bottom: 15px; font-size: 13px; line-height: 1.6; color: #555;
            position: relative;
        }}
        .card-content-text {{
            white-space: pre-wrap; word-break: break-word;
        }}

        /* Collapsed state: limit height with fade */
        .card-content.collapsed {{
            max-height: 200px; overflow: hidden;
        }}
        .card-content.collapsed::after {{
            content: '';
            position: absolute; bottom: 0; left: 0; right: 0; height: 60px;
            background: linear-gradient(transparent, #f9f9f9);
            pointer-events: none;
        }}

        /* Expanded state: no limit */
        .card-content.expanded {{
            max-height: none; overflow: visible;
        }}
        .card-content.expanded::after {{ display: none; }}

        .expand-toggle {{
            display: inline-block; margin-bottom: 12px; padding: 6px 14px;
            background: #eee; border: 1px solid #ddd; border-radius: 4px;
            cursor: pointer; font-size: 12px; font-weight: 600; color: #555;
            transition: all 0.2s ease;
        }}
        .expand-toggle:hover {{ background: #ddd; color: #333; }}

        /* Inline editing */
        .edit-textarea {{
            width: 100%; padding: 15px; border: 2px solid {header_color_1};
            border-radius: 6px; font-size: 13px; font-family: inherit;
            line-height: 1.6; resize: vertical; min-height: 200px;
            background: #fffef5; color: #333; display: none;
        }}
        .edit-textarea:focus {{
            outline: none; box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.15);
        }}
        .card.editing .card-content {{ display: none; }}
        .card.editing .edit-textarea {{ display: block; }}
        .card.editing .expand-toggle {{ display: none; }}

        .edit-bar {{
            display: none; gap: 8px; margin-bottom: 12px; padding: 10px;
            background: #fff8f0; border: 1px solid #ffcc99; border-radius: 6px;
            align-items: center;
        }}
        .card.editing .edit-bar {{ display: flex; }}
        .edit-bar-label {{ font-size: 12px; font-weight: 600; color: #cc6600; flex: 1; }}
        .edit-bar .btn {{ padding: 7px 14px; font-size: 12px; }}

        .tweet-meta-bar {{
            display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; padding: 0;
        }}
        .tweet-meta-badge {{
            display: inline-block; padding: 4px 10px; border-radius: 4px;
            font-size: 11px; font-weight: 600; letter-spacing: 0.3px;
        }}
        .tweet-meta-label {{ background: #e0e7ff; color: #3730a3; }}
        .tweet-meta-time {{ background: #fef3c7; color: #92400e; }}
        .tweet-meta-type {{ background: #d1fae5; color: #065f46; }}
        .tweet-meta-tier {{ background: #f3e8ff; color: #6b21a8; }}
        .tweet-meta-hashtags {{ background: #dbeafe; color: #1e40af; font-family: monospace; }}

        .char-count {{
            font-size: 12px; margin: 0 0 10px 0; padding: 8px;
            background: #f0f0f0; border-radius: 4px;
        }}
        .char-count.warning {{ background: #fee2e2; color: #991b1b; }}

        .card-actions {{ display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }}
        .action-btn {{
            flex: 1; padding: 10px; border: none; border-radius: 5px;
            cursor: pointer; font-size: 13px; font-weight: 600;
            transition: all 0.3s ease; white-space: nowrap; min-width: 100px;
        }}
        .btn-approve {{ background: #e8f5e9; color: #22c55e; border: 1px solid #22c55e; }}
        .btn-approve:hover {{ background: #22c55e; color: white; }}
        .btn-edit {{ background: #fff3e0; color: #e65100; border: 1px solid #ff9800; }}
        .btn-edit:hover {{ background: #ff9800; color: white; }}
        .btn-reject {{ background: #fee2e2; color: #ef4444; border: 1px solid #ef4444; }}
        .btn-reject:hover {{ background: #ef4444; color: white; }}
        .btn-copy {{ background: #f0f0f0; color: #333; border: 1px solid #ddd; }}
        .btn-copy:hover {{ background: #e0e0e0; }}

        .notes-section {{ display: none; margin-bottom: 12px; }}
        .notes-section.show {{ display: block; }}
        .notes-label {{ font-size: 12px; font-weight: 600; color: #666; margin-bottom: 6px; }}
        .notes-textarea {{
            width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px;
            font-size: 13px; font-family: inherit; resize: vertical; min-height: 60px;
        }}
        .notes-textarea:focus {{ outline: none; border-color: {header_color_1}; box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1); }}

        .status-label {{
            font-size: 11px; font-weight: 600; text-transform: uppercase;
            padding: 4px 8px; border-radius: 3px; margin-top: 10px; display: inline-block;
        }}
        .status-approved {{ background: #e8f5e9; color: #22c55e; }}
        .status-needs-edit {{ background: #fffbeb; color: #f59e0b; }}
        .status-rejected {{ background: #fee2e2; color: #ef4444; }}
        .status-edited {{ background: #e3f2fd; color: #1565c0; }}

        .empty-state {{ text-align: center; padding: 60px 20px; color: #999; }}
        .empty-state-icon {{ font-size: 48px; margin-bottom: 15px; }}

        /* Approval stats bar */
        .approval-stats {{
            display: flex; gap: 16px; margin-top: 12px; flex-wrap: wrap;
        }}
        .stat-chip {{
            display: inline-flex; align-items: center; gap: 6px;
            padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 600;
        }}
        .stat-approved {{ background: #dcfce7; color: #16a34a; }}
        .stat-rejected {{ background: #fee2e2; color: #dc2626; }}
        .stat-unreviewed {{ background: #f3f4f6; color: #6b7280; }}
        .stat-dot {{ width: 8px; height: 8px; border-radius: 50%; }}
        .stat-approved .stat-dot {{ background: #22c55e; }}
        .stat-rejected .stat-dot {{ background: #ef4444; }}
        .stat-unreviewed .stat-dot {{ background: #9ca3af; }}

        /* PostPlanner XLSX button */
        .btn-csv {{ background: #7c3aed; color: white; }}
        .btn-csv:hover {{ background: #6d28d9; }}
        .btn-csv:disabled {{ background: #c4b5fd; cursor: not-allowed; }}

        /* Schedule settings panel */
        .schedule-panel {{
            display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: white; border-radius: 12px; padding: 30px; z-index: 1000;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3); width: 500px; max-width: 90vw; max-height: 80vh; overflow-y: auto;
        }}
        .schedule-panel.show {{ display: block; }}
        .schedule-overlay {{ display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 999; }}
        .schedule-overlay.show {{ display: block; }}
        .schedule-panel h3 {{ color: #1a1a2e; margin-bottom: 20px; font-size: 18px; }}
        .schedule-section {{ margin-bottom: 20px; }}
        .schedule-section label {{ display: block; font-size: 13px; font-weight: 600; color: #555; margin-bottom: 6px; }}
        .schedule-section input {{ width: 100%; padding: 8px 12px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; }}
        .schedule-section input:focus {{ outline: none; border-color: #7c3aed; }}
        .time-slots {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }}
        .time-slot {{
            display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px;
            background: #f3f0ff; border: 1px solid #c4b5fd; border-radius: 20px; font-size: 13px;
        }}
        .time-slot .remove-slot {{ cursor: pointer; color: #999; font-weight: bold; }}
        .time-slot .remove-slot:hover {{ color: #ef4444; }}
        .add-slot-btn {{
            padding: 6px 14px; background: #f3f0ff; border: 1px dashed #7c3aed; border-radius: 20px;
            cursor: pointer; font-size: 13px; color: #7c3aed;
        }}
        .add-slot-btn:hover {{ background: #ede9fe; }}
        .schedule-actions {{ display: flex; gap: 10px; justify-content: flex-end; margin-top: 20px; }}

        /* Photo search links for image concepts */
        .photo-section {{
            margin-bottom: 15px; padding: 12px; background: #f0f9ff;
            border: 1px solid #bae6fd; border-radius: 6px;
        }}
        .photo-section-title {{
            font-size: 12px; font-weight: 700; color: #0369a1; text-transform: uppercase;
            letter-spacing: 0.5px; margin-bottom: 8px;
        }}
        .photo-links {{ display: flex; flex-wrap: wrap; gap: 6px; }}
        .photo-link {{
            display: inline-block; padding: 6px 12px; background: #0ea5e9;
            color: white; border-radius: 4px; font-size: 12px; font-weight: 500;
            text-decoration: none; transition: all 0.2s ease; cursor: pointer;
        }}
        .photo-link:hover {{ background: #0284c7; }}

        /* Image URL input and preview for image concepts */
        .image-url-section {{
            margin-bottom: 15px; padding: 12px; background: #f0fdf4;
            border: 1px solid #bbf7d0; border-radius: 6px;
        }}
        .image-url-section label {{
            display: block; font-size: 12px; font-weight: 700; color: #166534;
            text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px;
        }}
        .image-url-input {{
            width: 100%; padding: 8px 10px; border: 1px solid #86efac;
            border-radius: 4px; font-size: 13px; font-family: monospace;
            background: white; box-sizing: border-box;
        }}
        .image-url-input:focus {{ outline: none; border-color: #22c55e; box-shadow: 0 0 0 2px rgba(34,197,94,0.2); }}
        .image-url-hint {{
            font-size: 11px; color: #6b7280; margin-top: 4px;
        }}
        .image-preview {{
            margin-top: 8px; text-align: center;
        }}
        .image-preview img {{
            max-width: 100%; max-height: 200px; border-radius: 4px;
            border: 1px solid #d1d5db; display: none;
        }}
        .image-preview img.loaded {{ display: inline-block; }}

        /* Image production status badges */
        .image-badge {{
            display: inline-block; padding: 2px 8px; border-radius: 3px;
            font-size: 10px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.5px; margin-left: 6px;
        }}
        .image-exported {{ background: #dcfce7; color: #166534; }}
        .image-in-progress {{ background: #fef3c7; color: #92400e; }}
        .image-not-started {{ background: #f3f4f6; color: #6b7280; }}

        /* Text overlay preview for image concepts */
        .overlay-section {{
            margin-bottom: 15px; padding: 15px; background: #1a1a2e;
            border-radius: 6px; text-align: center;
        }}
        .overlay-line {{
            font-family: 'Bebas Neue', Impact, 'Arial Black', sans-serif;
            color: #ffd700; font-size: 18px; font-weight: 700; line-height: 1.4;
            text-transform: uppercase; letter-spacing: 1px;
        }}
        .overlay-line.sub {{ color: #ffffff; font-size: 14px; font-weight: 400; letter-spacing: 0; text-transform: none; }}

        /* Article content rendered as HTML */
        .article-frame {{
            width: 100%; border: 1px solid #ddd; border-radius: 6px;
            background: white; min-height: 300px;
        }}

        @media (max-width: 768px) {{
            .sidebar {{ width: 100%; height: auto; position: relative; padding: 20px; }}
            .main-content {{ margin-left: 0; }}
            .content {{ padding: 20px; }}
            .header {{ padding: 15px 20px; }}
            .header h1 {{ font-size: 20px; }}
            .filter-bar {{ padding: 15px 20px; }}
            .header-meta {{ flex-direction: column; align-items: stretch; }}
            .progress-bar {{ min-width: auto; }}
        }}

        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: #f1f1f1; }}
        ::-webkit-scrollbar-thumb {{ background: #888; border-radius: 4px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #555; }}
"""

    # Only include traffic panel CSS if we have traffic data
    if traffic_data and traffic_data.get('summary'):
        html_content += f"""
        /* ─── Traffic Performance Panel ─── */
        .traffic-panel {{
            background: white; margin: 20px 30px 0; border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow: hidden;
        }}
        .traffic-panel-header {{
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: white; padding: 20px 25px; display: flex; justify-content: space-between; align-items: center;
        }}
        .traffic-panel-header h2 {{ font-size: 18px; font-weight: 700; }}
        .traffic-panel-header .tp-subtitle {{ font-size: 12px; color: #aaa; margin-top: 4px; }}
        .traffic-panel-toggle {{
            background: rgba(255,255,255,0.15); border: none; color: white; padding: 6px 14px;
            border-radius: 6px; cursor: pointer; font-size: 13px;
        }}
        .traffic-panel-toggle:hover {{ background: rgba(255,255,255,0.25); }}
        .traffic-panel-body {{ padding: 25px; }}
        .traffic-panel-body.collapsed {{ display: none; }}

        .tp-kpis {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 16px; margin-bottom: 25px;
        }}
        .tp-kpi {{
            background: #f8f9fa; border-radius: 10px; padding: 18px; text-align: center;
            border: 1px solid #e9ecef;
        }}
        .tp-kpi-value {{ font-size: 28px; font-weight: 700; color: #1a1a2e; }}
        .tp-kpi-label {{ font-size: 12px; color: #666; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .tp-kpi-trend {{ font-size: 13px; margin-top: 6px; font-weight: 600; }}
        .tp-kpi-trend.up {{ color: #22c55e; }}
        .tp-kpi-trend.down {{ color: #ef4444; }}

        .tp-sections {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
        @media (max-width: 1200px) {{ .tp-sections {{ grid-template-columns: 1fr; }} }}

        .tp-section {{ background: #f8f9fa; border-radius: 10px; padding: 20px; border: 1px solid #e9ecef; }}
        .tp-section h3 {{ font-size: 14px; font-weight: 600; color: #333; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px; }}

        .tp-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
        .tp-table th {{ text-align: left; padding: 8px 10px; border-bottom: 2px solid #dee2e6; color: #666; font-weight: 600; font-size: 11px; text-transform: uppercase; }}
        .tp-table td {{ padding: 8px 10px; border-bottom: 1px solid #eee; }}
        .tp-table tr:hover {{ background: #e9ecef; }}
        .tp-table .tp-title {{ max-width: 320px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
        .tp-table .tp-num {{ text-align: right; font-variant-numeric: tabular-nums; font-weight: 500; }}

        .tp-chart-container {{ position: relative; height: 120px; margin-bottom: 10px; }}
        .tp-bar-chart {{ display: flex; align-items: flex-end; gap: 3px; height: 100px; }}
        .tp-bar {{
            flex: 1; background: {header_color_1}; border-radius: 3px 3px 0 0; min-width: 6px;
            position: relative; transition: opacity 0.2s;
        }}
        .tp-bar:hover {{ opacity: 0.8; }}
        .tp-bar-label {{
            position: absolute; bottom: -18px; left: 50%; transform: translateX(-50%);
            font-size: 9px; color: #999; white-space: nowrap;
        }}
        .tp-chart-dates {{ display: flex; justify-content: space-between; font-size: 10px; color: #999; margin-top: 4px; }}

        .tp-period-btns {{ display: flex; gap: 4px; }}
        .tp-period-btn {{
            background: #e9ecef; border: none; padding: 4px 10px; border-radius: 4px;
            font-size: 12px; cursor: pointer; color: #666; font-weight: 600;
        }}
        .tp-period-btn:hover {{ background: #dee2e6; }}
        .tp-period-btn.active {{ background: {header_color_1}; color: white; }}
"""

    html_content += f"""    </style>
</head>
<body>
    <div class="sidebar">
        <h1>{html.escape(brand_name)}</h1>
        <div class="sidebar-date">Review Dashboard<br>{date}</div>

        <div class="sidebar-section">
            <div class="sidebar-section-title">Content Types</div>
"""

    # Count items by type
    type_counts = {}
    for story in all_stories:
        story_type = story['type']
        type_counts[story_type] = type_counts.get(story_type, 0) + 1

    # Build sidebar navigation
    type_labels = {
        'daily_brief': 'Daily Brief',
        'x_post': 'X / Twitter Posts',
        'facebook': 'Facebook Posts',
        'article': 'Articles',
        'image_concept': 'Image Concepts'
    }

    for content_type, label in type_labels.items():
        count = type_counts.get(content_type, 0)
        if count > 0:
            html_content += f'''            <div class="nav-item" onclick="filterByType('{content_type}')">
                {label}
                <span class="nav-item-count">{count}</span>
            </div>
'''

    html_content += f"""
            <div class="nav-item" onclick="filterByType('all')">
                All Items
                <span class="nav-item-count">{total_items}</span>
            </div>
        </div>

        <div class="sidebar-section">
            <div class="sidebar-section-title">Status Filter</div>
            <div class="nav-item" onclick="filterByStatus('all')">All</div>
            <div class="nav-item" onclick="filterByStatus('unreviewed')">Unreviewed</div>
            <div class="nav-item" onclick="filterByStatus('approved')">Approved</div>
            <div class="nav-item" onclick="filterByStatus('needs-edit')">Needs Edit</div>
            <div class="nav-item" onclick="filterByStatus('rejected')">Rejected</div>
        </div>

        <div class="sidebar-section">
            <div class="sidebar-section-title">Actions</div>
            <div class="nav-item" onclick="approveAll()" style="color: #22c55e;">
                Approve All
            </div>
            <div class="nav-item" onclick="exportApprovals()" style="color: {header_color_1};">
                Export Results JSON
            </div>
            <div class="nav-item" onclick="downloadPostPlannerCSV()" style="color: #a78bfa;">
                PostPlanner Upload
            </div>
            <div class="nav-item" onclick="downloadTOBIExport()" style="color: #f472b6;">
                TOBI Upload
            </div>
        </div>
    </div>

    <div class="main-content">
        <div class="header">
            <h1>{html.escape(brand_name)} — Content Review Dashboard</h1>
            <div class="header-meta">
                <div class="progress-bar">
                    <div class="progress-label">
                        <span id="reviewed-count">0</span> of <span id="total-count">{total_items}</span> items reviewed
                    </div>
                    <div class="progress-container">
                        <div class="progress-fill" id="progress-fill" style="width: 0%"></div>
                    </div>
                    <div class="approval-stats" id="approval-stats">
                        <span class="stat-chip stat-approved"><span class="stat-dot"></span> <span id="stat-approved-count">0</span> approved</span>
                        <span class="stat-chip stat-rejected"><span class="stat-dot"></span> <span id="stat-rejected-count">0</span> rejected</span>
                        <span class="stat-chip stat-unreviewed"><span class="stat-dot"></span> <span id="stat-unreviewed-count">0</span> unreviewed</span>
                    </div>
                </div>
                <div class="header-actions">
                    <button class="btn btn-secondary" onclick="resetAll()">Reset All</button>
                    <button class="btn btn-csv" id="btn-csv" onclick="downloadPostPlannerCSV()" disabled>PostPlanner Upload (0 approved)</button>
                    <button class="btn btn-csv" id="btn-tobi" onclick="downloadTOBIExport()" disabled style="background: #831843; border-color: #f472b6;">TOBI Upload (0 approved)</button>
                    <button class="btn btn-primary" onclick="exportApprovals()">Export JSON</button>
                </div>
            </div>
        </div>

        <div class="filter-bar">
            <button class="filter-btn active" onclick="filterByStatus('all')">All</button>
            <button class="filter-btn" onclick="filterByStatus('unreviewed')">Unreviewed</button>
            <button class="filter-btn" onclick="filterByStatus('approved')">Approved</button>
            <button class="filter-btn" onclick="filterByStatus('needs-edit')">Needs Edit</button>
            <button class="filter-btn" onclick="filterByStatus('rejected')">Rejected</button>
        </div>

"""

    # ─── Traffic Performance Panel ───
    if traffic_data and traffic_data.get('summary'):
        s = traffic_data['summary']
        s7 = s.get('7d', {})
        s30 = s.get('30d', {})
        prev7 = s.get('prev_7d', {})
        sb_pv_7d = s.get('softball_pageviews_7d', 0)
        sb_pv_30d = s.get('softball_pageviews_30d', 0)

        # Week-over-week change
        prev_pv = prev7.get('pageviews', 0)
        wow_pct = round((s7['pageviews'] - prev_pv) / prev_pv * 100) if prev_pv > 0 else 0
        wow_class = 'up' if wow_pct >= 0 else 'down'
        wow_arrow = '&#9650;' if wow_pct >= 0 else '&#9660;'
        wow_text = f'{wow_arrow} {abs(wow_pct)}% vs prev week'

        prev_users = prev7.get('users', 0)
        wow_users_pct = round((s7['users'] - prev_users) / prev_users * 100) if prev_users > 0 else 0
        wow_users_class = 'up' if wow_users_pct >= 0 else 'down'
        wow_users_arrow = '&#9650;' if wow_users_pct >= 0 else '&#9660;'

        # Daily chart bars
        daily = traffic_data.get('daily', [])[-14:]  # Last 14 days
        max_pv = max((d['pageviews'] for d in daily), default=1)
        bars_html = ''
        for d in daily:
            h = max(4, int(d['pageviews'] / max_pv * 100))
            day_label = d['date'][-5:]  # MM-DD
            bars_html += f'<div class="tp-bar" style="height:{h}px" title="{d["date"]}: {d["pageviews"]:,} pageviews"></div>\n'

        chart_start = daily[0]['date'][-5:] if daily else ''
        chart_end = daily[-1]['date'][-5:] if daily else ''

        # Top articles table (build for both 7d and 30d)
        def build_articles_rows(pages_list, limit=10):
            rows = ''
            for i, p in enumerate(pages_list[:limit]):
                title = html.escape(p['title'][:70])
                rows += f'<tr><td style="color:#999;width:30px">{i+1}</td><td class="tp-title" title="{html.escape(p["title"])}">{title}</td><td class="tp-num">{p["pageviews"]:,}</td><td class="tp-num">{p["users"]:,}</td></tr>'
            return rows

        articles_rows_7d = build_articles_rows(traffic_data.get('top_pages_7d', []))
        articles_rows_30d = build_articles_rows(traffic_data.get('top_pages_30d', []), 15)

        # Sources table
        sources = traffic_data.get('sources_7d', [])[:6]
        sources_rows = ''
        total_src_sessions = sum(src['sessions'] for src in sources) or 1
        for src in sources:
            pct = round(src['sessions'] / total_src_sessions * 100)
            source_name = html.escape(src['source'])
            sources_rows += f'<tr><td>{source_name}</td><td class="tp-num">{src["sessions"]:,}</td><td class="tp-num" style="width:60px">{pct}%</td></tr>'

        # Monthly softball breakdown
        monthly = traffic_data.get('monthly_softball', [])
        monthly_rows = ''
        for m in monthly:
            monthly_rows += f'<tr><td style="font-weight:600">{html.escape(m.get("label", m["yearMonth"]))}</td><td class="tp-num">{m["pageviews"]:,}</td><td class="tp-num">{m["users"]:,}</td><td class="tp-num">{m["articles"]:,}</td></tr>'

        gen_time = traffic_data.get('generated_at', '')[:16].replace('T', ' ')

        # Embed daily data as JSON for interactive chart
        daily_json = json.dumps(daily)

        html_content += f"""
        <div class="traffic-panel" id="traffic-panel">
            <div class="traffic-panel-header">
                <div>
                    <h2>Content Performance &mdash; fanrumor.com</h2>
                    <div class="tp-subtitle">Updated {gen_time} &bull; GA4 data</div>
                </div>
                <button class="traffic-panel-toggle" onclick="document.getElementById('tp-body').classList.toggle('collapsed'); this.textContent = this.textContent === 'Hide' ? 'Show' : 'Hide'">Hide</button>
            </div>
            <div class="traffic-panel-body" id="tp-body">
                <div class="tp-kpis">
                    <div class="tp-kpi">
                        <div class="tp-kpi-value" id="tp-kpi-pv">{s7['pageviews']:,}</div>
                        <div class="tp-kpi-label" id="tp-kpi-pv-label">Total Pageviews (7d)</div>
                        <div class="tp-kpi-trend {wow_class}" id="tp-kpi-pv-trend">{wow_text}</div>
                    </div>
                    <div class="tp-kpi">
                        <div class="tp-kpi-value" id="tp-kpi-users">{s7['users']:,}</div>
                        <div class="tp-kpi-label" id="tp-kpi-users-label">Unique Visitors (7d)</div>
                        <div class="tp-kpi-trend {wow_users_class}" id="tp-kpi-users-trend">{wow_users_arrow} {abs(wow_users_pct)}% vs prev week</div>
                    </div>
                    <div class="tp-kpi">
                        <div class="tp-kpi-value" id="tp-kpi-sessions">{s7['sessions']:,}</div>
                        <div class="tp-kpi-label" id="tp-kpi-sessions-label">Sessions (7d)</div>
                    </div>
                    <div class="tp-kpi">
                        <div class="tp-kpi-value" id="tp-kpi-avg">{round(s7['pageviews'] / 7):,}</div>
                        <div class="tp-kpi-label" id="tp-kpi-avg-label">Avg Daily Views (7d)</div>
                    </div>
                </div>

                <div class="tp-sections">
                    <div class="tp-section">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
                            <h3 style="margin:0">Daily Pageviews</h3>
                            <div class="tp-period-btns">
                                <button class="tp-period-btn" onclick="tpSetPeriod(7)" id="tp-btn-7">7d</button>
                                <button class="tp-period-btn active" onclick="tpSetPeriod(14)" id="tp-btn-14">14d</button>
                                <button class="tp-period-btn" onclick="tpSetPeriod(30)" id="tp-btn-30">30d</button>
                            </div>
                        </div>
                        <div id="tp-chart-area">
                            <div class="tp-chart-container">
                                <div class="tp-bar-chart" id="tp-bar-chart"></div>
                            </div>
                            <div class="tp-chart-dates" id="tp-chart-dates"></div>
                        </div>
                        <div id="tp-chart-tooltip" style="display:none;position:fixed;background:#1a1a2e;color:white;padding:8px 12px;border-radius:6px;font-size:12px;pointer-events:none;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,0.3)"></div>
                    </div>
                    <div class="tp-section">
                        <h3>Traffic Sources (7d)</h3>
                        <table class="tp-table">
                            <thead><tr><th>Source</th><th style="text-align:right">Sessions</th><th style="text-align:right">%</th></tr></thead>
                            <tbody>{sources_rows}</tbody>
                        </table>
                    </div>
                </div>

                <div class="tp-sections" style="margin-top:20px">
                    <div class="tp-section">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
                            <h3 style="margin:0">Top Performing Articles</h3>
                            <div class="tp-period-btns">
                                <button class="tp-period-btn active" onclick="tpSetArticles('7d')" id="tp-art-7d">7d</button>
                                <button class="tp-period-btn" onclick="tpSetArticles('30d')" id="tp-art-30d">30d</button>
                            </div>
                        </div>
                        <table class="tp-table" id="tp-articles-7d">
                            <thead><tr><th style="width:30px">#</th><th>Article</th><th style="text-align:right">Views</th><th style="text-align:right">Users</th></tr></thead>
                            <tbody>{articles_rows_7d}</tbody>
                        </table>
                        <table class="tp-table" id="tp-articles-30d" style="display:none">
                            <thead><tr><th style="width:30px">#</th><th>Article</th><th style="text-align:right">Views</th><th style="text-align:right">Users</th></tr></thead>
                            <tbody>{articles_rows_30d}</tbody>
                        </table>
                    </div>
                    <div class="tp-section">
                        <h3>Softball Visitors by Month</h3>
                        <table class="tp-table">
                            <thead><tr><th>Month</th><th style="text-align:right">Views</th><th style="text-align:right">Visitors</th><th style="text-align:right">Articles</th></tr></thead>
                            <tbody>{monthly_rows}</tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <script>
        (function() {{
            var dailyData = {daily_json};
            var chartEl = document.getElementById('tp-bar-chart');
            var datesEl = document.getElementById('tp-chart-dates');
            var tooltip = document.getElementById('tp-chart-tooltip');

            function fmt(n) {{ return n.toString().replace(/\\B(?=(\\d{{3}})+(?!\\d))/g, ','); }}

            function renderChart(days) {{
                var data = dailyData.slice(-days);
                var max = Math.max.apply(null, data.map(function(d) {{ return d.pageviews; }}));
                if (max === 0) max = 1;
                var html = '';
                var totalPv = 0, totalUsers = 0, totalSessions = 0;
                data.forEach(function(d) {{
                    var h = Math.max(4, Math.round(d.pageviews / max * 100));
                    html += '<div class="tp-bar" style="height:' + h + 'px" data-date="' + d.date + '" data-pv="' + d.pageviews + '" data-users="' + d.users + '" data-sessions="' + d.sessions + '"></div>';
                    totalPv += d.pageviews;
                    totalUsers += d.users;
                    totalSessions += d.sessions;
                }});
                chartEl.innerHTML = html;
                datesEl.innerHTML = '<span>' + data[0].date.slice(5) + '</span><span>' + data[data.length-1].date.slice(5) + '</span>';

                // Update KPI cards
                var label = days + 'd';
                document.getElementById('tp-kpi-pv').textContent = fmt(totalPv);
                document.getElementById('tp-kpi-pv-label').textContent = 'Total Pageviews (' + label + ')';
                document.getElementById('tp-kpi-users').textContent = fmt(totalUsers);
                document.getElementById('tp-kpi-users-label').textContent = 'Unique Visitors (' + label + ')';
                document.getElementById('tp-kpi-sessions').textContent = fmt(totalSessions);
                document.getElementById('tp-kpi-sessions-label').textContent = 'Sessions (' + label + ')';
                var avg = Math.round(totalPv / data.length);
                document.getElementById('tp-kpi-avg').textContent = fmt(avg);
                document.getElementById('tp-kpi-avg-label').textContent = 'Avg Daily Views (' + label + ')';

                // Update trend for 7d (compare to previous 7d)
                if (days === 7) {{
                    var prev = dailyData.slice(-14, -7);
                    var prevPv = 0, prevUsers = 0;
                    prev.forEach(function(d) {{ prevPv += d.pageviews; prevUsers += d.users; }});
                    var pvPct = prevPv > 0 ? Math.round((totalPv - prevPv) / prevPv * 100) : 0;
                    var uPct = prevUsers > 0 ? Math.round((totalUsers - prevUsers) / prevUsers * 100) : 0;
                    var pvArrow = pvPct >= 0 ? '&#9650;' : '&#9660;';
                    var uArrow = uPct >= 0 ? '&#9650;' : '&#9660;';
                    document.getElementById('tp-kpi-pv-trend').innerHTML = pvArrow + ' ' + Math.abs(pvPct) + '% vs prev week';
                    document.getElementById('tp-kpi-pv-trend').className = 'tp-kpi-trend ' + (pvPct >= 0 ? 'up' : 'down');
                    document.getElementById('tp-kpi-users-trend').innerHTML = uArrow + ' ' + Math.abs(uPct) + '% vs prev week';
                    document.getElementById('tp-kpi-users-trend').className = 'tp-kpi-trend ' + (uPct >= 0 ? 'up' : 'down');
                }} else {{
                    document.getElementById('tp-kpi-pv-trend').textContent = '';
                    document.getElementById('tp-kpi-users-trend').textContent = '';
                }}

                chartEl.querySelectorAll('.tp-bar').forEach(function(bar) {{
                    bar.addEventListener('mouseenter', function(e) {{
                        tooltip.innerHTML = '<strong>' + bar.dataset.date + '</strong><br>' +
                            bar.dataset.pv + ' pageviews<br>' +
                            bar.dataset.users + ' users<br>' +
                            bar.dataset.sessions + ' sessions';
                        tooltip.style.display = 'block';
                    }});
                    bar.addEventListener('mousemove', function(e) {{
                        tooltip.style.left = (e.clientX + 12) + 'px';
                        tooltip.style.top = (e.clientY - 10) + 'px';
                    }});
                    bar.addEventListener('mouseleave', function() {{
                        tooltip.style.display = 'none';
                    }});
                }});
            }}

            window.tpSetPeriod = function(days) {{
                renderChart(days);
                document.querySelectorAll('.tp-period-btns .tp-period-btn').forEach(function(b) {{ b.classList.remove('active'); }});
                var btn = document.getElementById('tp-btn-' + days);
                if (btn) btn.classList.add('active');
            }};

            window.tpSetArticles = function(period) {{
                document.getElementById('tp-articles-7d').style.display = period === '7d' ? '' : 'none';
                document.getElementById('tp-articles-30d').style.display = period === '30d' ? '' : 'none';
                document.getElementById('tp-art-7d').classList.toggle('active', period === '7d');
                document.getElementById('tp-art-30d').classList.toggle('active', period === '30d');
            }};

            renderChart(14);
        }})();
        </script>
"""

    html_content += """
        <div class="content">
            <div class="cards-container" id="cards-container">
"""

    # Generate cards for each story
    for idx, story in enumerate(all_stories):
        # Full content for display (escaped for HTML)
        is_article = story['type'] == 'article'
        full_content_escaped = html.escape(story['content'])
        is_long = len(story['content']) > 400

        # Check if this is an individual tweet card (has tweet-level metadata)
        is_individual_tweet = story.get('tweet_label') is not None

        # Determine badge type
        if story['type'] == 'x_post':
            badge_text = 'X POST'
            badge_class = 'badge-x-post'
        elif story['type'] == 'facebook':
            badge_text = 'FACEBOOK'
            badge_class = 'badge-facebook'
        elif story['type'] == 'article':
            badge_text = 'ARTICLE'
            badge_class = 'badge-article'
        elif story['type'] == 'image_concept':
            badge_text = 'IMAGE'
            badge_class = 'badge-image'
        else:
            badge_text = 'BRIEF'
            badge_class = 'badge-brief'

        # Character count for X posts
        char_count_html = ""
        if story['type'] == 'x_post':
            if is_individual_tweet:
                char_count = story.get('char_count', count_tweet_chars(story['content']))
            else:
                char_count = count_chars_no_urls(story['content'])
            warning = " warning" if char_count > 280 else ""
            char_count_html = f'<div class="char-count{warning}" id="charcount-{story["id"]}">Characters: {char_count}/280{"  OVER LIMIT" if char_count > 280 else ""}</div>'

        # Tweet metadata bar (posting window, type, hashtags) for individual tweet cards
        tweet_meta_html = ""
        if is_individual_tweet:
            meta_parts = []
            if story.get('tweet_label'):
                meta_parts.append(f'<span class="tweet-meta-badge tweet-meta-label">{html.escape(story["tweet_label"])}</span>')
            if story.get('posting_window'):
                meta_parts.append(f'<span class="tweet-meta-badge tweet-meta-time">{html.escape(story["posting_window"])}</span>')
            if story.get('tweet_type'):
                meta_parts.append(f'<span class="tweet-meta-badge tweet-meta-type">{html.escape(story["tweet_type"])}</span>')
            if story.get('tier'):
                meta_parts.append(f'<span class="tweet-meta-badge tweet-meta-tier">Tier {html.escape(story["tier"])}</span>')
            if story.get('hashtags'):
                meta_parts.append(f'<span class="tweet-meta-badge tweet-meta-hashtags">{html.escape(story["hashtags"])}</span>')
            if meta_parts:
                tweet_meta_html = f'<div class="tweet-meta-bar">{"".join(meta_parts)}</div>'

        # Photo search links and text overlay for image concepts
        photo_html = ""
        if story['type'] == 'image_concept':
            search_terms = extract_photo_search_terms(story['content'])
            overlay_lines = extract_text_overlay(story['content'])

            if search_terms:
                links_html = ""
                for term in search_terms:
                    url = build_photo_search_url(term, photo_source)
                    escaped_term = html.escape(term)
                    links_html += f'<a class="photo-link" href="{url}" target="_blank" rel="noopener">{escaped_term}</a>\n'
                photo_html += f'''<div class="photo-section">
                        <div class="photo-section-title">{photo_source_label}</div>
                        <div class="photo-links">{links_html}</div>
                    </div>'''

            if overlay_lines:
                overlay_html = ""
                for i, line in enumerate(overlay_lines):
                    css_class = "overlay-line" if i == 0 else "overlay-line sub"
                    overlay_html += f'<div class="{css_class}">{html.escape(line)}</div>\n'
                photo_html += f'''<div class="overlay-section">
                        {overlay_html}
                    </div>'''

            # Image URL input field and preview
            story_num_match = re.search(r'story-(\d+)', story['id'])
            story_num = story_num_match.group(1) if story_num_match else '0'
            # Determine platform from title (X Image vs Facebook Image)
            platform_key = 'x_image' if 'X Image' in story.get('title', '') or 'x-image' in story['id'] else 'facebook_image'
            # Check manifest for pre-existing URL
            pre_url = ''
            if image_manifest:
                sdata = image_manifest.get(story_num, {})
                pdata = sdata.get(platform_key, {})
                pre_url = pdata.get('exported_url', '') or pdata.get('imagn_url', '')
            pre_loaded = 'loaded' if pre_url else ''
            pre_value = html.escape(pre_url) if pre_url else ''

            # Image status badge
            img_badge = get_image_status_badge(story['id'], image_manifest)

            photo_hint = "Paste Imagn or exported image URL here" if photo_source == "imagn" else "Paste Unsplash or stock photo URL here"

            photo_html += f'''<div class="image-url-section">
                        <label>Selected Image URL {img_badge}</label>
                        <input type="text" class="image-url-input"
                               data-story="{story_num}" data-platform="{platform_key}"
                               placeholder="{photo_hint}"
                               value="{pre_value}"
                               onchange="updateImageURL(this)"
                               onpaste="setTimeout(function(){{ updateImageURL(event.target) }}, 100)">
                        <div class="image-url-hint">Copy the direct image URL from your photo source after selecting</div>
                        <div class="image-preview">
                            <img src="{pre_url}" alt="Image preview" class="{pre_loaded}"
                                 id="img-preview-{story_num}-{platform_key}"
                                 onerror="this.classList.remove('loaded')">
                        </div>
                    </div>'''

        # Content display: collapsed by default for long content
        collapsed_class = "collapsed" if is_long else "expanded"

        # For articles, render as iframe with srcdoc; for others, plain text
        if is_article:
            # Escape for srcdoc attribute (double-escape quotes)
            srcdoc_content = story['content'].replace('&', '&amp;').replace('"', '&quot;')
            content_html = f'<iframe class="article-frame" srcdoc="{srcdoc_content}" style="width:100%;min-height:400px;border:1px solid #ddd;border-radius:6px;"></iframe>'
            content_display = f"""
                    <div class="card-content expanded" id="content-{story['id']}">
                        {content_html}
                    </div>"""
        else:
            content_display = f"""
                    <div class="card-content {collapsed_class}" id="content-{story['id']}">
                        <div class="card-content-text">{full_content_escaped}</div>
                    </div>"""

        # Expand/collapse toggle for long non-article content
        toggle_html = ""
        if is_long and not is_article:
            toggle_html = f'<span class="expand-toggle" id="toggle-{story["id"]}" onclick="toggleExpand(\'{story["id"]}\')">Show Full Content</span>'

        # Edit textarea (hidden by default, shown when editing)
        edit_textarea = f'<textarea class="edit-textarea" id="editor-{story["id"]}" placeholder="Edit content here...">{html.escape(story["content"])}</textarea>'

        # Edit bar (shown when in edit mode)
        edit_bar = f"""
                    <div class="edit-bar" id="editbar-{story['id']}">
                        <span class="edit-bar-label">Editing mode — make your changes above</span>
                        <button class="btn btn-primary" onclick="saveAndApprove('{story['id']}')">Save &amp; Approve</button>
                        <button class="btn btn-secondary" onclick="cancelEdit('{story['id']}')">Cancel</button>
                    </div>"""

        # Fact-check badge
        fc_badge = get_fact_check_badge_html(story['id'], fact_check_results)

        # Create card HTML
        html_content += f"""                <div class="card" data-id="{story['id']}" data-type="{story['type']}" data-status="unreviewed">
                    <div class="card-header">
                        <div class="card-title">{html.escape(story['title'])}</div>
                        <div>{fc_badge}<span class="card-badge {badge_class}">{badge_text}</span></div>
                    </div>
                    {tweet_meta_html}
{content_display}
                    {edit_textarea}
                    {toggle_html}
                    {edit_bar}
                    {char_count_html}
                    {photo_html}

                    <div class="card-actions" id="actions-{story['id']}">
                        <button class="action-btn btn-approve" onclick="approveCard('{story['id']}')">Approve</button>
                        <button class="action-btn btn-edit" onclick="startEdit('{story['id']}')">Edit</button>
                        <button class="action-btn btn-reject" onclick="rejectCard('{story['id']}')">Reject</button>
                        <button class="action-btn btn-copy" onclick="copyContent('{story['id']}')">Copy</button>
                    </div>

                    <div class="notes-section" id="notes-{story['id']}">
                        <div class="notes-label">Reviewer Notes:</div>
                        <textarea class="notes-textarea" id="textarea-{story['id']}" placeholder="Add reviewer notes..."></textarea>
                    </div>

                    <div class="status-label" id="status-{story['id']}"></div>
                </div>
"""

    html_content += """            </div>

            <div class="empty-state" id="empty-state" style="display: none;">
                <div class="empty-state-icon">No items match your filter</div>
            </div>
        </div>
    </div>

    <!-- Schedule settings modal -->
    <div class="schedule-overlay" id="schedule-overlay" onclick="closeSchedulePanel()"></div>
    <div class="schedule-panel" id="schedule-panel">
        <h3>Posting Schedule Settings</h3>
        <div class="schedule-section">
            <label>Post Date (defaults to content date)</label>
            <input type="date" id="schedule-date" />
        </div>
        <div class="schedule-section">
            <label>X / Twitter Time Slots</label>
            <div class="time-slots" id="x-time-slots"></div>
            <div style="margin-top:8px;">
                <input type="time" id="new-x-time" style="width:auto;display:inline-block;margin-right:8px;" />
                <span class="add-slot-btn" onclick="addTimeSlot('x')">+ Add Slot</span>
            </div>
        </div>
        <div class="schedule-section">
            <label>Facebook Time Slots</label>
            <div class="time-slots" id="fb-time-slots"></div>
            <div style="margin-top:8px;">
                <input type="time" id="new-fb-time" style="width:auto;display:inline-block;margin-right:8px;" />
                <span class="add-slot-btn" onclick="addTimeSlot('fb')">+ Add Slot</span>
            </div>
        </div>
        <div class="schedule-section" style="background:#f9f9f9;padding:12px;border-radius:6px;font-size:12px;color:#666;">
            Posts will be assigned to time slots in order. If you have more posts than slots, they wrap around. After downloading, upload the file directly to PostPlanner via Bulk Upload.
        </div>
        <div class="schedule-actions">
            <button class="btn btn-secondary" onclick="closeSchedulePanel()">Cancel</button>
            <button class="btn btn-csv" onclick="generateAndDownload()">Generate &amp; Download XLSX</button>
        </div>
    </div>

    <!-- SheetJS for XLSX generation (loaded async so it doesn't block) -->
    <script async src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
    <script>
"""

    # Build JS as a proper string with direct substitution
    js_code = f"""
        const DATE = '{date}';
        const BRAND_NAME = '{brand_name}';
        const REVIEW_STORAGE_KEY = '{review_storage_key}';
        const SCHEDULE_STORAGE_KEY = '{schedule_storage_key}';
        const PHOTO_SOURCE = '{photo_source}';
        let reviewData = {{}};
        const allStories = {stories_json};
        const imageManifest = {image_manifest_json};
        let imageURLs = {{}}; // Runtime store: {{'1_x_image': 'url', '1_facebook_image': 'url', ...}}

        // Image URL management
        function updateImageURL(inputEl) {{
            var story = inputEl.dataset.story;
            var platform = inputEl.dataset.platform;
            var url = inputEl.value.trim();
            var key = story + '_' + platform;
            imageURLs[key] = url;

            // Update preview thumbnail
            var preview = document.getElementById('img-preview-' + story + '-' + platform);
            if (preview) {{
                if (url) {{
                    preview.src = url;
                    preview.classList.add('loaded');
                    preview.onerror = function() {{ this.classList.remove('loaded'); }};
                }} else {{
                    preview.src = '';
                    preview.classList.remove('loaded');
                }}
            }}
        }}

        function getImageURLForStory(storyTitle, platform) {{
            // Try runtime imageURLs first (user-pasted)
            // Extract story number from title
            for (var key in imageURLs) {{
                if (imageURLs[key] && key.endsWith('_' + platform)) {{
                    var storyNum = key.split('_')[0];
                    // Check if this story matches by looking at allStories
                    for (var i = 0; i < allStories.length; i++) {{
                        if (allStories[i].title === storyTitle &&
                            allStories[i].id.indexOf('story-' + storyNum) !== -1) {{
                            return imageURLs[key];
                        }}
                    }}
                }}
            }}

            // Try manifest data
            for (var num in imageManifest) {{
                var mdata = imageManifest[num];
                if (mdata && mdata[platform] && mdata[platform].exported_url) {{
                    // Check if this story number matches
                    for (var j = 0; j < allStories.length; j++) {{
                        if (allStories[j].title === storyTitle &&
                            allStories[j].id.indexOf('story-' + num) !== -1) {{
                            return mdata[platform].exported_url;
                        }}
                    }}
                }}
            }}

            return '';
        }}

        function initializeApp() {{
            const saved = localStorage.getItem(REVIEW_STORAGE_KEY + '-' + DATE);
            if (saved) {{
                try {{
                    reviewData = JSON.parse(saved);
                }} catch (e) {{
                    reviewData = {{}};
                }}
            }}

            allStories.forEach(function(story) {{
                if (!reviewData[story.id]) {{
                    reviewData[story.id] = {{
                        id: story.id,
                        type: story.type,
                        status: 'unreviewed',
                        notes: '',
                        content: story.content,
                        editedContent: null
                    }};
                }}
                // Migrate old data: ensure editedContent field exists
                if (reviewData[story.id].editedContent === undefined) {{
                    reviewData[story.id].editedContent = null;
                }}
            }});

            // Restore UI state
            Object.keys(reviewData).forEach(function(storyId) {{
                var data = reviewData[storyId];
                var card = document.querySelector('[data-id="' + storyId + '"]');
                if (card) {{
                    card.setAttribute('data-status', data.status);
                    var textarea = document.getElementById('textarea-' + storyId);
                    if (textarea) textarea.value = data.notes || '';
                    // If content was edited, update the display and editor
                    if (data.editedContent) {{
                        var contentText = card.querySelector('.card-content-text');
                        if (contentText) contentText.textContent = data.editedContent;
                        var editor = document.getElementById('editor-' + storyId);
                        if (editor) editor.value = data.editedContent;
                    }}
                    updateCardVisuals(storyId, data.status, !!data.editedContent);
                }}
            }});

            updateProgress();
            filterByStatus('all');
        }}

        function toggleExpand(storyId) {{
            var content = document.getElementById('content-' + storyId);
            var toggle = document.getElementById('toggle-' + storyId);
            if (content.classList.contains('collapsed')) {{
                content.classList.remove('collapsed');
                content.classList.add('expanded');
                toggle.textContent = 'Collapse';
            }} else {{
                content.classList.remove('expanded');
                content.classList.add('collapsed');
                toggle.textContent = 'Show Full Content';
            }}
        }}

        function startEdit(storyId) {{
            var card = document.querySelector('[data-id="' + storyId + '"]');
            if (!card) return;
            card.classList.add('editing');
            var editor = document.getElementById('editor-' + storyId);
            if (editor) {{
                // If previously edited, load edited content; otherwise load original
                var data = reviewData[storyId];
                if (data && data.editedContent) {{
                    editor.value = data.editedContent;
                }}
                editor.focus();
                // Auto-resize for articles
                editor.style.minHeight = Math.max(300, editor.scrollHeight) + 'px';
            }}
        }}

        function saveAndApprove(storyId) {{
            var editor = document.getElementById('editor-' + storyId);
            if (!editor) return;
            var newContent = editor.value;

            // Save the edited content
            if (!reviewData[storyId]) {{
                reviewData[storyId] = {{ id: storyId, status: 'approved', notes: '', content: '', editedContent: null }};
            }}
            reviewData[storyId].editedContent = newContent;

            // Update the display text
            var card = document.querySelector('[data-id="' + storyId + '"]');
            var contentText = card ? card.querySelector('.card-content-text') : null;
            if (contentText) contentText.textContent = newContent;

            // Exit edit mode
            if (card) card.classList.remove('editing');

            // Approve
            setStatus(storyId, 'approved');
            updateCardVisuals(storyId, 'approved', true);

            // Update char count for X posts
            updateCharCount(storyId, newContent);
        }}

        function cancelEdit(storyId) {{
            var card = document.querySelector('[data-id="' + storyId + '"]');
            if (card) card.classList.remove('editing');
        }}

        function updateCharCount(storyId, text) {{
            var el = document.getElementById('charcount-' + storyId);
            if (!el) return;
            // Strip metadata tags before counting
            var clean = text.replace(/\\[CHARACTER COUNT:.*?\\]/gi, '');
            clean = clean.replace(/\\[CHAR COUNT:.*?\\]/gi, '');
            clean = clean.replace(/\\[\\d+\\/280\\]/g, '');
            // Remove URLs for Twitter count
            var textNoUrls = clean.replace(/https?:\\/\\/\\S+/g, '');
            var count = textNoUrls.trim().length;
            el.textContent = 'Characters: ' + count + '/280' + (count > 280 ? '  OVER LIMIT' : '');
            el.className = count > 280 ? 'char-count warning' : 'char-count';
        }}

        function approveCard(storyId) {{
            setStatus(storyId, 'approved');
            document.getElementById('notes-' + storyId).classList.remove('show');
        }}

        function rejectCard(storyId) {{
            setStatus(storyId, 'rejected');
            document.getElementById('notes-' + storyId).classList.add('show');
        }}

        function setStatus(storyId, status) {{
            if (!reviewData[storyId]) {{
                var story = allStories.find(function(s) {{ return s.id === storyId; }});
                reviewData[storyId] = {{
                    id: storyId,
                    type: story ? story.type : '',
                    status: status,
                    notes: '',
                    content: story ? story.content : '',
                    editedContent: null
                }};
            }}

            reviewData[storyId].status = status;

            var textarea = document.getElementById('textarea-' + storyId);
            if (textarea) reviewData[storyId].notes = textarea.value;

            localStorage.setItem(REVIEW_STORAGE_KEY + '-' + DATE, JSON.stringify(reviewData));

            var card = document.querySelector('[data-id="' + storyId + '"]');
            if (card) card.setAttribute('data-status', status);
            updateCardVisuals(storyId, status, !!(reviewData[storyId] && reviewData[storyId].editedContent));
            updateProgress();
        }}

        function updateCardVisuals(storyId, status, wasEdited) {{
            var card = document.querySelector('[data-id="' + storyId + '"]');
            if (!card) return;

            card.classList.remove('approved', 'needs-edit', 'rejected');
            if (status !== 'unreviewed') card.classList.add(status);

            var statusLabel = document.getElementById('status-' + storyId);
            if (statusLabel) {{
                statusLabel.className = 'status-label';
                if (status === 'approved' && wasEdited) {{
                    statusLabel.textContent = 'APPROVED (EDITED)';
                    statusLabel.classList.add('status-edited');
                }} else if (status === 'approved') {{
                    statusLabel.textContent = 'APPROVED';
                    statusLabel.classList.add('status-approved');
                }} else if (status === 'needs-edit') {{
                    statusLabel.textContent = 'NEEDS EDIT';
                    statusLabel.classList.add('status-needs-edit');
                }} else if (status === 'rejected') {{
                    statusLabel.textContent = 'REJECTED';
                    statusLabel.classList.add('status-rejected');
                }} else {{
                    statusLabel.textContent = '';
                }}
            }}
        }}

        function updateProgress() {{
            var approved = 0, rejected = 0, unreviewed = 0;
            allStories.forEach(function(story) {{
                var data = reviewData[story.id];
                if (!data || data.status === 'unreviewed') unreviewed++;
                else if (data.status === 'approved') approved++;
                else if (data.status === 'rejected') rejected++;
                else unreviewed++;
            }});
            var reviewed = approved + rejected;
            var total = allStories.length;
            var percentage = total > 0 ? (reviewed / total * 100) : 0;
            document.getElementById('reviewed-count').textContent = reviewed;
            document.getElementById('total-count').textContent = total;
            document.getElementById('progress-fill').style.width = percentage + '%';
            // Update stat chips
            document.getElementById('stat-approved-count').textContent = approved;
            document.getElementById('stat-rejected-count').textContent = rejected;
            document.getElementById('stat-unreviewed-count').textContent = unreviewed;
            // Update CSV button
            var csvBtn = document.getElementById('btn-csv');
            var tobiBtn = document.getElementById('btn-tobi');
            var socialApproved = countApprovedSocialPosts();
            if (csvBtn) {{
                if (socialApproved > 0) {{
                    csvBtn.disabled = false;
                    csvBtn.textContent = 'PostPlanner Upload (' + socialApproved + ' posts)';
                }} else {{
                    csvBtn.disabled = true;
                    csvBtn.textContent = 'PostPlanner Upload (0 approved)';
                }}
            }}
            // Update TOBI button (counts only X/Twitter text posts)
            if (tobiBtn) {{
                var xApproved = countApprovedXPosts();
                if (xApproved > 0) {{
                    tobiBtn.disabled = false;
                    tobiBtn.textContent = 'TOBI Upload (' + xApproved + ' posts)';
                }} else {{
                    tobiBtn.disabled = true;
                    tobiBtn.textContent = 'TOBI Upload (0 approved)';
                }}
            }}
        }}

        function countApprovedSocialPosts() {{
            var count = 0;
            allStories.forEach(function(story) {{
                var data = reviewData[story.id];
                if (data && data.status === 'approved' && (story.type === 'x_post' || story.type === 'facebook')) {{
                    count++;
                }}
            }});
            return count;
        }}

        function countApprovedXPosts() {{
            var count = 0;
            allStories.forEach(function(story) {{
                var data = reviewData[story.id];
                if (data && data.status === 'approved' && story.type === 'x_post') {{
                    count++;
                }}
            }});
            return count;
        }}

        function escapeCSVField(text) {{
            if (!text) return '';
            // If field contains comma, quote, or newline, wrap in quotes and escape inner quotes
            if (text.indexOf(',') !== -1 || text.indexOf('"') !== -1 || text.indexOf('\\n') !== -1) {{
                return '"' + text.replace(/"/g, '""') + '"';
            }}
            return text;
        }}

        function extractHashtags(text) {{
            if (!text) return '';
            var matches = text.match(/#\\w+/g);
            return matches ? matches.join(' ') : '';
        }}

        // ========== POSTING SCHEDULE SYSTEM ==========
        var defaultXSlots = ['09:00', '12:00', '15:00', '18:00', '21:00'];
        var defaultFBSlots = ['10:00', '13:00', '17:00'];

        function getScheduleConfig() {{
            var saved = localStorage.getItem(SCHEDULE_STORAGE_KEY);
            if (saved) {{
                try {{ return JSON.parse(saved); }} catch(e) {{}}
            }}
            return {{ xSlots: defaultXSlots.slice(), fbSlots: defaultFBSlots.slice() }};
        }}

        function saveScheduleConfig(config) {{
            localStorage.setItem(SCHEDULE_STORAGE_KEY, JSON.stringify(config));
        }}

        function renderTimeSlots() {{
            var config = getScheduleConfig();
            var xContainer = document.getElementById('x-time-slots');
            var fbContainer = document.getElementById('fb-time-slots');

            xContainer.innerHTML = config.xSlots.map(function(t, i) {{
                return '<span class="time-slot">' + t + ' <span class="remove-slot" onclick="removeTimeSlot(\\x27x\\x27,' + i + ')">&times;</span></span>';
            }}).join('');

            fbContainer.innerHTML = config.fbSlots.map(function(t, i) {{
                return '<span class="time-slot">' + t + ' <span class="remove-slot" onclick="removeTimeSlot(\\x27fb\\x27,' + i + ')">&times;</span></span>';
            }}).join('');
        }}

        function addTimeSlot(platform) {{
            var inputId = platform === 'x' ? 'new-x-time' : 'new-fb-time';
            var val = document.getElementById(inputId).value;
            if (!val) return;
            var config = getScheduleConfig();
            var arr = platform === 'x' ? config.xSlots : config.fbSlots;
            if (arr.indexOf(val) === -1) {{
                arr.push(val);
                arr.sort();
            }}
            saveScheduleConfig(config);
            renderTimeSlots();
            document.getElementById(inputId).value = '';
        }}

        function removeTimeSlot(platform, index) {{
            var config = getScheduleConfig();
            var arr = platform === 'x' ? config.xSlots : config.fbSlots;
            arr.splice(index, 1);
            saveScheduleConfig(config);
            renderTimeSlots();
        }}

        function downloadPostPlannerCSV() {{
            // Open schedule panel instead of direct download
            openSchedulePanel();
        }}

        function openSchedulePanel() {{
            document.getElementById('schedule-date').value = DATE;
            renderTimeSlots();
            document.getElementById('schedule-panel').classList.add('show');
            document.getElementById('schedule-overlay').classList.add('show');
        }}

        function closeSchedulePanel() {{
            document.getElementById('schedule-panel').classList.remove('show');
            document.getElementById('schedule-overlay').classList.remove('show');
        }}

        function formatTimeForPostPlanner(time24, dateStr) {{
            // Output PostPlanner V2 format: MM/DD/YYYY  HH:MM (24hr)
            var parts = dateStr.split('-');
            return parts[1] + '/' + parts[2] + '/' + parts[0] + '  ' + time24;
        }}

        function redistributeTimes(rows) {{
            // Ensure all post times are at least 30 min from now,
            // evenly spaced through the rest of the day.
            if (rows.length === 0) return rows;

            var now = new Date();
            var nowMinutes = now.getHours() * 60 + now.getMinutes();
            var floorMinutes = nowMinutes + 30;
            var endMinutes = 22 * 60; // 10:00 PM cutoff

            // Check if ANY post times have already passed
            var anyPast = rows.some(function(row) {{
                var parts = row.time.split(':');
                var rowMin = parseInt(parts[0], 10) * 60 + parseInt(parts[1], 10);
                return rowMin < floorMinutes;
            }});

            if (!anyPast) return rows; // all times are in the future, keep them

            if (floorMinutes >= endMinutes) {{
                alert('It is past 9:30 PM — not enough time remaining to schedule all posts today. Posts will use original times.');
                return rows;
            }}

            var availableMinutes = endMinutes - floorMinutes;
            var spacing = Math.floor(availableMinutes / rows.length);
            if (spacing < 15) spacing = 15; // minimum 15 min gap
            if (spacing > 90) spacing = 90; // maximum 90 min gap

            rows.forEach(function(row, i) {{
                var postMinutes = floorMinutes + (i * spacing);
                if (postMinutes >= 24 * 60) postMinutes = 23 * 60 + 45;
                var h = Math.floor(postMinutes / 60);
                var m = postMinutes % 60;
                row.time = (h < 10 ? '0' : '') + h + ':' + (m < 10 ? '0' : '') + m;
            }});

            var firstTime = rows[0].time;
            var lastTime = rows[rows.length - 1].time;
            console.log('PostPlanner export: redistributed ' + rows.length + ' posts from ' + firstTime + ' to ' + lastTime + ' (' + spacing + ' min apart)');
            return rows;
        }}

        // Parse actual time from posting_window string like "7:00 AM CT" -> "07:00"
        function parsePostingTime(timeStr) {{
            if (!timeStr) return null;
            var m = timeStr.match(/(\\d{{1,2}}):(\\d{{2}})\\s*(AM|PM)/i);
            if (!m) return null;
            var h = parseInt(m[1], 10);
            var min = m[2];
            var ampm = m[3].toUpperCase();
            if (ampm === 'PM' && h !== 12) h += 12;
            if (ampm === 'AM' && h === 12) h = 0;
            return (h < 10 ? '0' : '') + h + ':' + min;
        }}

        // Generic window name fallback
        var windowToTime = {{
            'Morning': '09:00',
            'Midday': '12:00',
            'Afternoon': '15:00',
            'Evening': '18:00',
            'Late Night': '21:00'
        }};

        function generateAndDownload() {{
            var config = getScheduleConfig();
            var postDate = document.getElementById('schedule-date').value || DATE;

            var xRows = [];
            var fbRows = [];

            allStories.forEach(function(story) {{
                var data = reviewData[story.id];
                if (!data || data.status !== 'approved') return;
                var finalContent = data.editedContent || story.content;

                if (story.type === 'x_post') {{
                    // If this is an individual tweet card (has tweet_label), use directly
                    if (story.tweet_label) {{
                        xRows.push({{
                            content: finalContent,
                            type: story.tweet_type || 'text',
                            hashtags: story.hashtags || extractHashtags(finalContent),
                            story: story.title,
                            posting_window: story.posting_window || ''
                        }});
                    }} else {{
                        // Legacy: parse full story markdown for individual tweets
                        var sections = parseXPostContent(finalContent, story.title);
                        sections.forEach(function(post) {{
                            xRows.push({{
                                content: post.text,
                                type: post.type,
                                hashtags: extractHashtags(post.text),
                                story: story.title
                            }});
                        }});
                    }}
                }} else if (story.type === 'facebook') {{
                    var fbPost = parseFacebookContent(finalContent, story.title);
                    if (fbPost) {{
                        fbRows.push(fbPost);
                    }}
                }}
            }});

            if (xRows.length === 0 && fbRows.length === 0) {{
                alert('No approved social posts to export.');
                return;
            }}

            // Assign times: use posting_window property first, then content tag, then round-robin
            function assignTimes(rows, slots, label) {{
                if (slots.length === 0) slots = ['12:00'];
                var timeFallbacks = [];
                return rows.map(function(row, i) {{
                    row.date = postDate;
                    // 1. Try posting_window property (e.g., "7:00 AM CT")
                    var parsed = parsePostingTime(row.posting_window);
                    if (parsed) {{
                        row.time = parsed;
                        return row;
                    }}
                    // 2. Try [POSTING WINDOW: ...] tag in content
                    var windowMatch = row.content ? row.content.match(/\\[POSTING WINDOW:\\s*([^\\]]+)\\]/) : null;
                    if (windowMatch) {{
                        parsed = parsePostingTime(windowMatch[1]);
                        if (parsed) {{
                            row.time = parsed;
                            return row;
                        }}
                        if (windowToTime[windowMatch[1].trim()]) {{
                            row.time = windowToTime[windowMatch[1].trim()];
                            return row;
                        }}
                    }}
                    // 3. Fall back to round-robin
                    row.time = slots[i % slots.length];
                    timeFallbacks.push('Post ' + (i + 1) + ': no parsed time, using ' + row.time);
                    return row;
                }});
                // Warn if any posts had to use fallback times
                if (timeFallbacks.length > 0) {{
                    console.warn('TIME WARNING (' + label + '): ' + timeFallbacks.length + ' post(s) had no parsed posting time:\\n' + timeFallbacks.join('\\n'));
                }}
            }}

            xRows = assignTimes(xRows, config.xSlots, 'X/Twitter');
            fbRows = assignTimes(fbRows, config.fbSlots, 'Facebook');

            // Generate XLSX in PostPlanner Bulk Upload V2 format
            if (typeof XLSX === 'undefined') {{
                alert('SheetJS library not loaded. Falling back to CSV download.');
                fallbackCSVDownload(xRows, fbRows, postDate);
                return;
            }}

            // Combine all rows and sort by original time
            var allRows = xRows.concat(fbRows);
            allRows.sort(function(a, b) {{
                return a.time.localeCompare(b.time);
            }});

            // Smart time redistribution
            allRows = redistributeTimes(allRows);

            var wb = XLSX.utils.book_new();

            // PostPlanner V3.1 format: Row 1 = version marker, Row 2 = headers, Row 3+ = data
            var data = [
                ['## ' + BRAND_NAME + ' -- PostPlanner Bulk Upload', 'BULK UPLOAD VERSION 3.1 \u2013 Please DO NOT EDIT this cell.', '', '', '', '', '', '', ''],
                ['## POSTING TIME', 'CAPTION', 'LINK', 'MEDIA', 'TITLE', 'FIRST COMMENT', 'FIRST COMMENT DELAY', 'TOBI BACKGROUND', 'REEL OR STORY']
            ];

            allRows.forEach(function(row) {{
                var caption = cleanMarkdownForPost(row.content);
                var mediaUrl = '';
                if (row.type === 'image' || row.type === 'IMAGE') {{
                    mediaUrl = getImageURLForStory(row.story, row.platform === 'facebook' ? 'facebook_image' : 'x_image') || '';
                }}
                data.push([
                    formatTimeForPostPlanner(row.time, postDate),
                    caption,
                    '',
                    mediaUrl,
                    '', '', '', '', ''
                ]);
            }});

            var sheet = XLSX.utils.aoa_to_sheet(data);
            sheet['!cols'] = [
                {{wch: 20}}, {{wch: 80}}, {{wch: 30}}, {{wch: 30}}, {{wch: 10}}, {{wch: 20}}, {{wch: 18}}, {{wch: 18}}, {{wch: 14}}
            ];
            XLSX.utils.book_append_sheet(wb, sheet, 'Sheet1');

            // Download
            XLSX.writeFile(wb, 'postplanner-upload-' + postDate + '.xlsx');
            closeSchedulePanel();

            var msg = 'Downloaded postplanner-upload-' + postDate + '.xlsx with ';
            var parts = [];
            if (xRows.length > 0) parts.push(xRows.length + ' X posts');
            if (fbRows.length > 0) parts.push(fbRows.length + ' Facebook posts');
            alert(msg + parts.join(' and ') + '.\\n\\nUpload this file to PostPlanner via Bulk Upload.');
        }}

        function cleanMarkdownForPost(text) {{
            // Strip markdown formatting and metadata that shouldn't appear in social posts
            if (!text) return '';
            return text
                .replace(/\\[CHARACTER COUNT:.*?\\]/gi, '')
                .replace(/\\[CHAR COUNT:.*?\\]/gi, '')
                .replace(/\\[\\d+\\/280\\]/g, '')
                .replace(/\\*\\*\\[POSTING WINDOW:.*?\\]\\*\\*/g, '')
                .replace(/\\[POSTING WINDOW:.*?\\]/g, '')
                .replace(/\\*\\*([^*]+)\\*\\*/g, '$1')
                .replace(/\\*([^*]+)\\*/g, '$1')
                .replace(/^#+\\s+/gm, '')
                .replace(/^[-*]\\s+/gm, '')
                .replace(/```[\\s\\S]*?```/g, '')
                .replace(/\\n{{3,}}/g, '\\n\\n')
                .trim();
        }}

        function fallbackCSVDownload(xRows, fbRows, postDate) {{
            // Fallback if SheetJS fails to load — generates CSV in V2-like format
            var allRows = xRows.concat(fbRows);
            allRows.sort(function(a, b) {{ return a.time.localeCompare(b.time); }});
            if (allRows.length === 0) {{
                alert('No approved posts to export.');
                closeSchedulePanel();
                return;
            }}
            // Smart time redistribution (same as XLSX path)
            allRows = redistributeTimes(allRows);
            var csv = '## ' + BRAND_NAME + ' -- PostPlanner Bulk Upload,' + escapeCSVField('BULK UPLOAD VERSION 3.1 \u2013 Please DO NOT EDIT this cell.') + ',,,,,,,\\n';
            csv += '## POSTING TIME,CAPTION,LINK,MEDIA,TITLE,FIRST COMMENT,FIRST COMMENT DELAY,TOBI BACKGROUND,REEL OR STORY\\n';
            allRows.forEach(function(row) {{
                csv += escapeCSVField(formatTimeForPostPlanner(row.time, postDate)) + ',' +
                       escapeCSVField(cleanMarkdownForPost(row.content)) + ',' +
                       ',,,,,,\\n';
            }});
            downloadFile(csv, 'postplanner-upload-' + postDate + '.csv', 'text/csv');
            closeSchedulePanel();
        }}

        function downloadTOBIExport() {{
            // Generate TOBI XLSX directly (no schedule panel needed — uses same times)
            generateAndDownloadTOBI();
        }}

        function stripHashtags(text) {{
            // Remove lines that are entirely hashtags, and trailing blank lines
            var lines = text.split('\\n');
            var cleaned = [];
            for (var i = 0; i < lines.length; i++) {{
                var stripped = lines[i].trim();
                if (stripped && stripped.split(/\\s+/).every(function(w) {{ return w.charAt(0) === '#'; }})) {{
                    continue;
                }}
                cleaned.push(lines[i]);
            }}
            while (cleaned.length > 0 && !cleaned[cleaned.length - 1].trim()) {{
                cleaned.pop();
            }}
            return cleaned.join('\\n');
        }}

        function generateAndDownloadTOBI() {{
            var postDate = document.getElementById('schedule-date') ?
                document.getElementById('schedule-date').value || DATE : DATE;

            // Collect approved X/Twitter text posts only
            var xRows = [];
            allStories.forEach(function(story) {{
                var data = reviewData[story.id];
                if (!data || data.status !== 'approved') return;
                if (story.type !== 'x_post') return;

                var finalContent = data.editedContent || story.content;
                if (story.tweet_label) {{
                    xRows.push({{
                        content: finalContent,
                        posting_window: story.posting_window || '',
                        story: story.title
                    }});
                }}
            }});

            if (xRows.length === 0) {{
                alert('No approved X/Twitter posts for TOBI export.');
                return;
            }}

            // Assign times — use same logic as regular export (posting_window → content tag → round-robin)
            var tobiSlots = defaultXSlots.slice();
            if (tobiSlots.length === 0) tobiSlots = ['12:00'];
            var tobiTimeFallbacks = [];
            xRows = xRows.map(function(row, i) {{
                row.date = postDate;
                // 1. Try posting_window property (e.g., "7:00 AM CT")
                var parsed = parsePostingTime(row.posting_window);
                if (parsed) {{
                    row.time = parsed;
                    return row;
                }}
                // 2. Try [POSTING WINDOW: ...] tag in content
                var windowMatch = row.content ? row.content.match(/\\[POSTING WINDOW:\\s*([^\\]]+)\\]/) : null;
                if (windowMatch) {{
                    parsed = parsePostingTime(windowMatch[1]);
                    if (parsed) {{
                        row.time = parsed;
                        return row;
                    }}
                }}
                // 3. Fall back to round-robin through time slots (NOT 12:00)
                row.time = tobiSlots[i % tobiSlots.length];
                tobiTimeFallbacks.push('Post ' + (i + 1) + ': no parsed time, using ' + row.time);
                return row;
            }});
            // Warn if any posts had to use fallback times
            if (tobiTimeFallbacks.length > 0) {{
                console.warn('TOBI TIME WARNING: ' + tobiTimeFallbacks.length + ' post(s) had no parsed posting time:\\n' + tobiTimeFallbacks.join('\\n'));
            }}

            // Sort by time
            xRows.sort(function(a, b) {{ return a.time.localeCompare(b.time); }});

            // Smart time redistribution
            xRows = redistributeTimes(xRows);

            // TOBI processing: preserve hashtags + emojis as much as possible
            var TOBI_LIMIT = 130;

            function extractHashtags(text) {{
                var matches = text.match(/#\\w+/g);
                return matches || [];
            }}

            function extractTrailingEmoji(text) {{
                var m = text.match(/\\s*([\\u{{1F300}}-\\u{{1FAFF}}\\u2600-\\u27BF\\u2B50\\u26A0-\\u26FF]+)\\s*$/u);
                if (m) {{
                    return {{ emoji: m[1], text: text.substring(0, m.index).trimEnd() }};
                }}
                return {{ emoji: null, text: text }};
            }}

            function truncateAtSentence(text, limit) {{
                var sentences = text.split(/(?<=[.!?])\\s+/);
                // Merge standalone emoji fragments into preceding sentence
                var merged = [];
                for (var s = 0; s < sentences.length; s++) {{
                    var trimmed = sentences[s].trim();
                    if (!trimmed) continue;
                    if (merged.length > 0 && !/[A-Za-z0-9]/.test(trimmed)) {{
                        merged[merged.length - 1] = merged[merged.length - 1] + ' ' + trimmed;
                    }} else {{
                        merged.push(trimmed);
                    }}
                }}
                var truncated = '';
                for (var s = 0; s < merged.length; s++) {{
                    var candidate = truncated ? truncated + ' ' + merged[s] : merged[s];
                    if (candidate.length <= limit) {{
                        truncated = candidate;
                    }} else {{
                        break;
                    }}
                }}
                // Clean up trailing abbreviation fragments (Dr., Mr., vs.)
                if (truncated) {{
                    var parts = truncated.split(' ');
                    var last = parts[parts.length - 1];
                    if (parts.length > 1 && last.length <= 4 && /^[A-Za-z]+\\.$/.test(last)) {{
                        parts.pop();
                        truncated = parts.join(' ');
                    }}
                }}
                return truncated || text.substring(0, limit - 3) + '...';
            }}

            function fitHashtagsWithinLimit(text, hashtags, limit) {{
                if (!hashtags.length) return text;
                // Try all hashtags, then progressively fewer
                for (var n = hashtags.length; n > 0; n--) {{
                    var tagBlock = '\\n\\n' + hashtags.slice(0, n).join(' ');
                    if ((text + tagBlock).length <= limit) {{
                        return text + tagBlock;
                    }}
                }}
                return text;
            }}

            if (typeof XLSX === 'undefined') {{
                alert('SheetJS library not loaded. Cannot generate TOBI XLSX.');
                return;
            }}

            var wb = XLSX.utils.book_new();
            var data = [
                ['## ' + BRAND_NAME + ' -- PostPlanner TOBI Bulk Upload', 'BULK UPLOAD VERSION 3.1 \u2013 Please DO NOT EDIT this cell.', '', '', '', '', '', '', ''],
                ['## POSTING TIME', 'CAPTION', 'LINK', 'MEDIA', 'TITLE', 'FIRST COMMENT', 'FIRST COMMENT DELAY', 'TOBI BACKGROUND', 'REEL OR STORY']
            ];

            var keptHashtags = 0;
            var strippedHashtags = 0;

            xRows.forEach(function(row, i) {{
                var caption = cleanMarkdownForPost(row.content);

                // If full caption fits under limit, use as-is — ALL hashtags + emojis preserved
                if (caption.length <= TOBI_LIMIT) {{
                    if (extractHashtags(caption).length > 0) keptHashtags++;
                    data.push([
                        formatTimeForPostPlanner(row.time, postDate),
                        caption, '', '', '', '', '', 'true-black', ''
                    ]);
                    return;
                }}

                // Over limit — decompose and rebuild intelligently
                var hashtags = extractHashtags(caption);
                var coreText = stripHashtags(caption).trimEnd();
                var emojiResult = extractTrailingEmoji(coreText);
                var trailing_emoji = emojiResult.emoji;
                var coreNoEmoji = emojiResult.text.trimEnd();

                // Step 1: Get core text under limit
                var result;
                if (coreNoEmoji.length <= TOBI_LIMIT) {{
                    result = coreNoEmoji;
                }} else {{
                    result = truncateAtSentence(coreNoEmoji, TOBI_LIMIT);
                }}

                // Step 2: Try to add back trailing emoji
                if (trailing_emoji) {{
                    var withEmoji = result + ' ' + trailing_emoji;
                    if (withEmoji.length <= TOBI_LIMIT) {{
                        result = withEmoji;
                    }}
                }}

                // Step 3: Try to add back as many hashtags as possible
                if (hashtags.length > 0) {{
                    var before = result;
                    result = fitHashtagsWithinLimit(result, hashtags, TOBI_LIMIT);
                    if (result !== before) keptHashtags++;
                    else strippedHashtags++;
                }}

                data.push([
                    formatTimeForPostPlanner(row.time, postDate),
                    result, '', '', '', '', '', 'true-black', ''
                ]);
            }});

            var sheet = XLSX.utils.aoa_to_sheet(data);
            sheet['!cols'] = [
                {{wch: 20}}, {{wch: 80}}, {{wch: 10}}, {{wch: 10}}, {{wch: 10}}, {{wch: 20}}, {{wch: 18}}, {{wch: 18}}, {{wch: 14}}
            ];
            XLSX.utils.book_append_sheet(wb, sheet, 'Sheet1');

            XLSX.writeFile(wb, 'postplanner-tobi-upload-' + postDate + '.xlsx');

            alert('Downloaded TOBI export with ' + xRows.length + ' posts.\\n\\n' +
                  keptHashtags + ' posts kept hashtags, ' + strippedHashtags + ' had hashtags removed for length.\\n\\n' +
                  'Background: true-black (Column H).\\nUpload to PostPlanner for Facebook TOBI posts.');
        }}

        function parseXPostContent(content, storyTitle) {{
            var posts = [];
            var lines = content.split('\\n');

            var inTextPost = false;
            var inThread = false;
            var currentTweetNum = 0;
            var currentText = [];

            for (var i = 0; i < lines.length; i++) {{
                var line = lines[i];
                var trimmed = line.trim();

                if (trimmed.match(/^###\\s+Text Post/i)) {{
                    flushPost();
                    inTextPost = true;
                    inThread = false;
                    currentText = [];
                    continue;
                }}
                if (trimmed.match(/^###\\s+Thread Concept/i)) {{
                    flushPost();
                    inTextPost = false;
                    inThread = true;
                    currentText = [];
                    currentTweetNum = 0;
                    continue;
                }}
                if (trimmed.match(/^###\\s+Image Post/i)) {{
                    flushPost();
                    inTextPost = false;
                    inThread = false;
                    continue;
                }}
                if (trimmed.match(/^###\\s/)) {{
                    flushPost();
                    inTextPost = false;
                    inThread = false;
                    continue;
                }}

                if (inThread && trimmed.match(/^\\*\\*Tweet\\s+\\d+/i)) {{
                    flushPost();
                    currentTweetNum++;
                    currentText = [];
                    continue;
                }}

                if (inTextPost || (inThread && currentTweetNum > 0)) {{
                    if (trimmed !== '') {{
                        currentText.push(line);
                    }}
                }}
            }}
            flushPost();

            function flushPost() {{
                if (currentText.length === 0) return;
                var text = currentText.join('\\n').trim();
                if (!text) return;

                if (inTextPost) {{
                    posts.push({{ text: text, type: 'text' }});
                }} else if (inThread && currentTweetNum > 0) {{
                    posts.push({{
                        text: text,
                        type: currentTweetNum === 1 ? 'thread_start' : 'thread_reply'
                    }});
                }}
                currentText = [];
            }}

            return posts;
        }}

        function parseFacebookContent(content, storyTitle) {{
            var lines = content.split('\\n');
            var inLongForm = false;
            var inImagePost = false;
            var longFormLines = [];
            var imageCaption = '';

            for (var i = 0; i < lines.length; i++) {{
                var trimmed = lines[i].trim();

                if (trimmed.match(/^###\\s+Long-Form Post/i)) {{
                    inLongForm = true;
                    inImagePost = false;
                    longFormLines = [];
                    continue;
                }}
                if (trimmed.match(/^###\\s+Image Post Caption/i) || trimmed.match(/^###\\s+Image Post/i)) {{
                    inLongForm = false;
                    inImagePost = true;
                    continue;
                }}
                if (trimmed.match(/^###\\s/) || trimmed.match(/^---/)) {{
                    inLongForm = false;
                    inImagePost = false;
                    continue;
                }}

                if (inLongForm) {{
                    longFormLines.push(lines[i]);
                }}
                if (inImagePost && trimmed !== '') {{
                    imageCaption = trimmed;
                    inImagePost = false;
                }}
            }}

            var longForm = longFormLines.join('\\n').trim();
            if (!longForm) return null;

            return {{
                content: longForm,
                image_caption: imageCaption,
                story: storyTitle
            }};
        }}

        function downloadFile(content, filename, mimeType) {{
            var blob = new Blob([content], {{ type: mimeType }});
            var url = URL.createObjectURL(blob);
            var link = document.createElement('a');
            link.href = url;
            link.download = filename;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        }}

        var currentStatusFilter = 'all';
        var currentTypeFilter = 'all';

        function filterByStatus(status) {{
            currentStatusFilter = status;
            applyFilters();
            document.querySelectorAll('.filter-btn').forEach(function(btn) {{
                btn.classList.remove('active');
                if (btn.textContent.trim().toLowerCase().replace(/\\s+/g, '') === status.replace('-', '').toLowerCase() ||
                    (status === 'all' && btn.textContent.trim() === 'All') ||
                    (status === 'needs-edit' && btn.textContent.trim() === 'Needs Edit')) {{
                    btn.classList.add('active');
                }}
            }});
            document.querySelectorAll('.sidebar .nav-item').forEach(function(item) {{ item.classList.remove('active'); }});
        }}

        function filterByType(type) {{
            currentTypeFilter = type;
            currentStatusFilter = 'all';
            applyFilters();
            document.querySelectorAll('.sidebar .nav-item').forEach(function(item) {{ item.classList.remove('active'); }});
            document.querySelectorAll('.filter-btn').forEach(function(btn) {{
                btn.classList.remove('active');
                if (btn.textContent.trim() === 'All') btn.classList.add('active');
            }});
        }}

        function applyFilters() {{
            var cards = document.querySelectorAll('.card');
            var visibleCount = 0;
            cards.forEach(function(card) {{
                var cardStatus = card.getAttribute('data-status');
                var cardType = card.getAttribute('data-type');
                var matchesStatus = (currentStatusFilter === 'all') || (cardStatus === currentStatusFilter);
                var matchesType = (currentTypeFilter === 'all') || (cardType === currentTypeFilter);
                if (matchesStatus && matchesType) {{
                    card.classList.add('show');
                    visibleCount++;
                }} else {{
                    card.classList.remove('show');
                }}
            }});
            document.getElementById('empty-state').style.display = visibleCount === 0 ? 'block' : 'none';
        }}

        function approveAll() {{
            if (!confirm('Approve all ' + allStories.length + ' items?')) return;
            allStories.forEach(function(story) {{ setStatus(story.id, 'approved'); }});
        }}

        function resetAll() {{
            if (confirm('Reset all reviews? This cannot be undone.')) {{
                localStorage.removeItem(REVIEW_STORAGE_KEY + '-' + DATE);
                location.reload();
            }}
        }}

        function copyContent(storyId) {{
            var data = reviewData[storyId];
            var story = allStories.find(function(s) {{ return s.id === storyId; }});
            var text = (data && data.editedContent) ? data.editedContent : (story ? story.content : '');
            navigator.clipboard.writeText(text).then(function() {{
                var btn = document.querySelector('[data-id="' + storyId + '"] .btn-copy');
                if (btn) {{ var orig = btn.textContent; btn.textContent = 'Copied!'; setTimeout(function() {{ btn.textContent = orig; }}, 1500); }}
            }});
        }}

        function exportApprovals() {{
            var items = [];
            allStories.forEach(function(story) {{
                var data = reviewData[story.id] || {{}};
                items.push({{
                    id: story.id,
                    type: story.type,
                    title: story.title,
                    status: data.status || 'unreviewed',
                    notes: data.notes || '',
                    content: story.content,
                    editedContent: data.editedContent || null,
                    finalContent: data.editedContent || story.content
                }});
            }});

            var exportData = {{
                date: DATE,
                reviewed_by: '',
                reviewed_at: new Date().toISOString(),
                items: items
            }};

            var dataStr = JSON.stringify(exportData, null, 2);
            var dataBlob = new Blob([dataStr], {{ type: 'application/json' }});
            var url = URL.createObjectURL(dataBlob);
            var link = document.createElement('a');
            link.href = url;
            link.download = 'approvals-' + DATE + '.json';
            link.click();
            URL.revokeObjectURL(url);
        }}

        // Auto-save notes as you type
        document.addEventListener('input', function(e) {{
            if (e.target.classList.contains('notes-textarea')) {{
                var storyId = e.target.id.replace('textarea-', '');
                if (reviewData[storyId]) {{
                    reviewData[storyId].notes = e.target.value;
                    localStorage.setItem(REVIEW_STORAGE_KEY + '-' + DATE, JSON.stringify(reviewData));
                }}
            }}
        }});

        initializeApp();
"""

    html_content += js_code
    html_content += """
    </script>
</body>
</html>
"""

    return html_content


def main():
    """Main function."""
    # Parse arguments
    args = sys.argv[1:]
    niche_name = None
    date_str = None

    i = 0
    while i < len(args):
        if args[i] == '--niche' and i + 1 < len(args):
            niche_name = args[i + 1]
            i += 2
        elif re.match(r'\d{4}-\d{2}-\d{2}', args[i]):
            date_str = args[i]
            i += 1
        else:
            i += 1

    if not date_str:
        print("Usage: python generate-review-dashboard.py --niche <name> YYYY-MM-DD")
        print("   or: python generate-review-dashboard.py YYYY-MM-DD (auto-detect niche)")
        sys.exit(1)

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print(f"ERROR: Invalid date format '{date_str}'. Use YYYY-MM-DD.")
        sys.exit(1)

    # Find niche and load config
    niche_root = find_niche_root(niche_name)
    config = load_niche_config(niche_root)
    brand_name = config.get('brand_name', os.path.basename(niche_root))
    content_prefix = config.get('content_prefix', os.path.basename(niche_root).lower() + '-content')
    photo_source = config.get('photo_source', 'imagn')  # Default to 'imagn' or 'stock'

    print(f"Niche: {brand_name}")
    print(f"Content prefix: {content_prefix}")
    print(f"Photo source: {photo_source}")
    print(f"Date: {date_str}")

    # Find content folder
    content_folder = os.path.join(niche_root, f"{content_prefix}-{date_str}")
    if not os.path.isdir(content_folder):
        print(f"Error: Content folder not found: {content_folder}")
        sys.exit(1)

    print(f"Reading content for {date_str}...")

    # Try JSON data source first (more reliable than markdown parsing)
    json_data = load_json_data(content_folder)

    if json_data and json_data.get('schema_version') == '2.0':
        print("✓ Found 07-content-data.json v2.0 (compiled)")
        all_stories, fact_check_results = build_stories_from_json_v2(json_data, content_folder)
        stats = json_data.get('pipeline_stats', {})
        print(f"  ✓ Stories from JSON: {len(all_stories)} items")
        if stats:
            print(f"  ✓ Pipeline stats: {stats.get('total_stories', '?')} stories, "
                  f"{stats.get('x_posts_count', '?')} tweets, "
                  f"{stats.get('facebook_posts_count', '?')} FB posts, "
                  f"{stats.get('articles_count', '?')} articles")
    elif json_data:
        print("✓ Found 07-content-data.json (legacy format)")
        all_stories, fact_check_results = build_stories_from_json(json_data, content_folder)
        stats = json_data.get('pipeline_stats', {})
        print(f"  ✓ Stories from JSON: {len(all_stories)} items")
        if stats:
            print(f"  ✓ Pipeline stats: {stats.get('total_stories', '?')} stories, "
                  f"{stats.get('articles_produced', '?')} articles, "
                  f"{stats.get('fact_check_claims_total', '?')} claims checked")
    else:
        print("⚠ No JSON data file found — falling back to markdown parsing")
        all_stories = []

        # Read daily brief
        daily_brief_path = os.path.join(content_folder, "00-daily-brief.md")
        daily_brief = read_file(daily_brief_path)
        if daily_brief:
            stories = parse_markdown_stories(daily_brief, 'daily_brief')
            all_stories.extend(stories)
            print(f"  ✓ Daily Brief: {len(stories)} items")

        # Read X posts
        x_posts_path = os.path.join(content_folder, "03-social-posts-x.md")
        x_posts = read_file(x_posts_path)
        if x_posts:
            stories = parse_markdown_stories(x_posts, 'x_post')
            all_stories.extend(stories)
            print(f"  ✓ X/Twitter Posts: {len(stories)} items")

        # Read Facebook posts
        facebook_path = os.path.join(content_folder, "04-social-posts-facebook.md")
        facebook = read_file(facebook_path)
        if facebook:
            stories = parse_markdown_stories(facebook, 'facebook')
            all_stories.extend(stories)
            print(f"  ✓ Facebook Posts: {len(stories)} items")

        # Read image concepts
        image_concepts_path = os.path.join(content_folder, "05-image-concepts.md")
        image_concepts = read_file(image_concepts_path)
        if image_concepts:
            stories = parse_markdown_stories(image_concepts, 'image_concept')
            all_stories.extend(stories)
            print(f"  ✓ Image Concepts: {len(stories)} items")

        # Read articles
        articles = read_articles_from_folder(content_folder)
        all_stories.extend(articles)
        print(f"  ✓ Articles: {len(articles)} items")

        # Parse fact-check log from markdown
        fact_check_results = parse_fact_check_log(content_folder)
        if fact_check_results:
            print(f"✓ Fact-check log found: {len(fact_check_results)} stories checked")
        else:
            print(f"⚠ No fact-check log found — cards will show 'NOT VERIFIED'")

    # Check if we found any content
    if not all_stories:
        print(f"Warning: No content found in {content_folder}")

    # Parse image manifest if it exists (used by both JSON and markdown paths)
    image_manifest = parse_image_manifest(content_folder)
    if image_manifest:
        exported_count = sum(
            1 for s in image_manifest.values()
            for p in ('x_image', 'facebook_image')
            if s.get(p, {}).get('status') == 'exported'
        )
        print(f"✓ Image manifest found: {len(image_manifest)} stories, {exported_count} images exported")
    else:
        print(f"⚠ No image manifest found — image URL fields will be empty")

    # Load traffic data if available
    traffic_data = None
    traffic_path = os.path.join(niche_root, "fanrumor-traffic.json")
    if os.path.isfile(traffic_path):
        try:
            with open(traffic_path, 'r', encoding='utf-8') as f:
                traffic_data = json.load(f)
            sb_pv = traffic_data.get('summary', {}).get('softball_pageviews_7d', 0)
            print(f"  \u2713 Traffic data loaded: {sb_pv:,} softball pageviews (7d)")
        except Exception as e:
            print(f"  \u26a0 Failed to load traffic data: {e}")

    # Generate HTML
    print(f"\nGenerating review dashboard...")
    html_content = create_html_dashboard(
        date_str, all_stories, brand_name, content_prefix, photo_source,
        fact_check_results, image_manifest, traffic_data
    )

    # Write to file
    output_path = os.path.join(content_folder, "review-dashboard.html")
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ Dashboard created: {output_path}")
        print(f"✓ Total items: {len(all_stories)}")
    except Exception as e:
        print(f"Error writing dashboard: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
