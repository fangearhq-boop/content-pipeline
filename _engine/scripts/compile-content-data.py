#!/usr/bin/env python3
"""
FanGear HQ Content Data Compiler

Reads markdown content files (daily brief, X posts, Facebook posts, image concepts,
fact-check log) and produces a structured 07-content-data.json file.

This JSON file is the single source of truth for downstream consumers:
- generate-review-dashboard.py (review dashboard)
- generate-postplanner-export.py (PostPlanner XLSX export)

Usage:
    python compile-content-data.py --niche Softball 2026-03-13
    python compile-content-data.py --niche Cubs 2026-03-13
    # or auto-detect niche from cwd:
    python compile-content-data.py 2026-03-13
"""

import sys
import os
import json
import re
from datetime import datetime, timezone
from pathlib import Path

# Fix Unicode output on Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Path helpers (shared with other engine scripts)
# ---------------------------------------------------------------------------

def find_engine_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_niche_root(niche_name=None):
    engine_root = find_engine_root()
    niche_launches = os.path.dirname(engine_root)
    if niche_name:
        niche_root = os.path.join(niche_launches, niche_name)
        if os.path.isdir(niche_root):
            return niche_root
        for entry in os.listdir(niche_launches):
            if entry.lower() == niche_name.lower() and entry != '_engine':
                return os.path.join(niche_launches, entry)
        print(f"ERROR: Niche folder not found: {niche_name}")
        sys.exit(1)
    else:
        cwd = os.getcwd()
        check = cwd
        while check != os.path.dirname(check):
            if os.path.isfile(os.path.join(check, 'niche-config.yaml')):
                return check
            check = os.path.dirname(check)
        print("ERROR: Could not auto-detect niche. Use --niche <name>")
        sys.exit(1)


def load_niche_config(niche_root):
    config_path = os.path.join(niche_root, 'niche-config.yaml')
    if not os.path.isfile(config_path):
        return {}
    config = {}
    platforms = []
    in_platforms = False
    with open(config_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
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


def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Warning: Error reading {path}: {e}")
        return ""


# ---------------------------------------------------------------------------
# Character counting (URL = 23 chars for Twitter)
# ---------------------------------------------------------------------------

def count_tweet_chars(text):
    clean = text.strip()
    clean = re.sub(r'https?://\S+', 'x' * 23, clean)
    return len(clean)


# ---------------------------------------------------------------------------
# Daily Brief parser
# ---------------------------------------------------------------------------

def parse_daily_brief(content):
    """Parse daily brief into story metadata and publishing schedule."""
    stories = {}
    schedule = []

    # Parse story sections
    story_pattern = r'^### STORY\s+(\d+):\s*(.+?)(?=^### STORY|\n## |\Z)'
    for m in re.finditer(story_pattern, content, re.MULTILINE | re.DOTALL):
        num = int(m.group(1))
        body = m.group(2).strip()
        lines = body.split('\n')
        title = lines[0].strip() if lines else f"Story {num}"

        story = {
            'story_num': num,
            'title': title,
            'tier': 0,
            'status': '',
            'angle': '',
            'tweet_type': '',
            'posting_window': '',
        }

        for line in lines[1:]:
            stripped = line.strip()
            if stripped.startswith('- **Tier:**'):
                tier_m = re.search(r'(\d)', stripped)
                if tier_m:
                    story['tier'] = int(tier_m.group(1))
            elif stripped.startswith('- **Status:**'):
                val = stripped.split('**Status:**', 1)[1].strip()
                if 'NEW STORY' in val.upper():
                    story['status'] = 'NEW STORY'
                elif 'FOLLOW UP' in val.upper():
                    story['status'] = 'FOLLOW UP'
                elif 'SKIP' in val.upper():
                    story['status'] = 'SKIP'
            elif stripped.startswith('- **Angle:**'):
                story['angle'] = stripped.split('**Angle:**', 1)[1].strip()
            elif stripped.startswith('- **Type:**'):
                story['tweet_type'] = stripped.split('**Type:**', 1)[1].strip()
            elif stripped.startswith('- **Posting window:**'):
                story['posting_window'] = stripped.split('**Posting window:**', 1)[1].strip()

        stories[num] = story

    # Parse publishing schedule table
    table_m = re.search(r'## Publishing Schedule\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if table_m:
        for row in table_m.group(1).strip().split('\n'):
            row = row.strip()
            if not row.startswith('|') or '---' in row:
                continue
            cells = [c.strip() for c in row.split('|')[1:-1]]
            if len(cells) >= 3 and cells[0] and not cells[0].startswith('Time'):
                schedule.append({
                    'time': cells[0],
                    'description': cells[1],
                    'type': cells[2] if len(cells) > 2 else '',
                })

    return stories, schedule


# ---------------------------------------------------------------------------
# X Posts parser
# ---------------------------------------------------------------------------

def parse_x_posts(content, brief_stories):
    """
    Parse X/Twitter posts file into structured tweet data.
    Returns dict: story_num -> list of tweet dicts.
    """
    result = {}

    # Split by story headers — supports alphanumeric IDs like 2A, 1B, 4B
    story_pattern = r'^### STORY\s+(\d+\w*):\s*(.+?)(?=^### STORY|^## Post Summary|\Z)'
    for m in re.finditer(story_pattern, content, re.MULTILINE | re.DOTALL):
        story_id = m.group(1).strip()
        story_body = m.group(2).strip()

        # Map compound IDs (2A, 1B) to parent story number
        num_match = re.match(r'(\d+)', story_id)
        parent_num = int(num_match.group(1)) if num_match else 0

        # Extract title (first line)
        lines = story_body.split('\n')
        title = lines[0].strip() if lines else ''

        # Try extracting tweets by **Post XY** labels
        tweets = _extract_by_post_labels(story_body, story_id)

        # Fallback: try code blocks
        if not tweets:
            tweets = _extract_by_code_blocks(story_body, story_id)

        # Final fallback: treat entire content as one tweet
        if not tweets:
            tweets = _extract_single_tweet(story_body, story_id, title)

        # Enrich with daily brief metadata
        brief = brief_stories.get(parent_num, {})
        for tweet in tweets:
            if not tweet.get('posting_time') and brief.get('posting_window'):
                tweet['posting_time'] = brief['posting_window']
            if not tweet.get('tweet_type') and brief.get('tweet_type'):
                tweet['tweet_type'] = brief['tweet_type']

        if parent_num not in result:
            result[parent_num] = []
        result[parent_num].extend(tweets)

    return result


def _extract_by_post_labels(body, story_id):
    """Extract tweets split by **Post XY** labels."""
    post_pattern = re.compile(r'^\*\*Post\s+(\w+)\*\*\s*$', re.MULTILINE)
    matches = list(post_pattern.finditer(body))
    if not matches:
        return []

    tweets = []
    for i, m in enumerate(matches):
        label = f"Post {m.group(1)}"
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        text = body[start:end].strip()
        # Stop at --- or ## Post Summary
        text = re.split(r'^---$|^## Post Summary', text, flags=re.MULTILINE)[0].strip()
        if not text:
            continue
        tweets.append(_make_tweet(label, text))

    return tweets


def _extract_by_code_blocks(body, story_id):
    """Extract tweets from ``` code blocks."""
    blocks = re.findall(r'```\s*\n(.*?)```', body, re.DOTALL)
    if not blocks:
        return []

    tweets = []
    for i, block in enumerate(blocks):
        text = block.strip()
        if not text:
            continue
        label = f"Post {story_id}" if len(blocks) == 1 else f"Post {story_id}-{i+1}"
        tweets.append(_make_tweet(label, text))

    return tweets


def _extract_single_tweet(body, story_id, title):
    """Treat entire body as a single tweet (minus title and separators)."""
    lines = body.split('\n')
    content_lines = []
    skipped_title = False
    for line in lines:
        stripped = line.strip()
        if not skipped_title:
            if stripped:
                skipped_title = True  # Skip title line
            continue
        if stripped == '---' or stripped.startswith('## Post Summary'):
            break
        content_lines.append(line)

    text = '\n'.join(content_lines).strip()
    if not text:
        return []
    return [_make_tweet(f"Post {story_id}", text)]


def _make_tweet(label, text):
    """Create a tweet dict from label and raw text."""
    # Clean metadata tags from text
    clean = text
    clean = re.sub(r'\[CHARACTER COUNT:.*?\]', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'\[CHAR COUNT:.*?\]', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'\[\d+/280\]', '', clean)
    clean = re.sub(r'\*?\*?\[POSTING WINDOW:.*?\]\*?\*?', '', clean)
    clean = re.sub(r'\*?\*?\[TYPE:.*?\]\*?\*?', '', clean)
    clean = re.sub(r'\n{3,}', '\n\n', clean)
    clean = clean.strip()

    # Extract hashtags
    hashtags = re.findall(r'#\w+', clean)

    # Extract posting time from text if present (e.g., embedded [POSTING WINDOW: X])
    time_m = re.search(r'\[POSTING WINDOW:\s*([^\]]+)\]', text)
    posting_time = time_m.group(1).strip() if time_m else ''

    # Extract type from text if present
    type_m = re.search(r'\[TYPE:\s*([^\]]+)\]', text)
    tweet_type = type_m.group(1).strip() if type_m else ''

    return {
        'label': label,
        'text': clean,
        'posting_time': posting_time,
        'tweet_type': tweet_type,
        'hashtags': hashtags,
        'char_count': count_tweet_chars(clean),
    }


# ---------------------------------------------------------------------------
# Facebook Posts parser
# ---------------------------------------------------------------------------

def parse_facebook_posts(content, brief_stories):
    """Parse Facebook posts file. Returns dict: story_num -> fb dict."""
    result = {}

    story_pattern = r'^### STORY\s+(\d+):\s*(.+?)(?=^### STORY|^## Post Summary|\Z)'
    for m in re.finditer(story_pattern, content, re.MULTILINE | re.DOTALL):
        story_num = int(m.group(1))
        body = m.group(2).strip()

        fb = {'long_form': '', 'image_caption': '', 'posting_time': ''}

        # Split by Long-Form Post and Image Caption labels
        lf_match = re.search(
            r'\*\*Long-Form Post(?:\s*\(([^)]+)\))?\*\*\s*\n(.*?)(?=\*\*Image Caption|\Z)',
            body, re.DOTALL
        )
        if lf_match:
            if lf_match.group(1):
                fb['posting_time'] = lf_match.group(1).strip()
            fb['long_form'] = lf_match.group(2).strip()

        ic_match = re.search(
            r'\*\*Image Caption(?:\s*\(([^)]+)\))?\*\*\s*\n(.*?)(?=^---$|\Z)',
            body, re.DOTALL | re.MULTILINE
        )
        if ic_match:
            fb['image_caption'] = ic_match.group(2).strip()

        # Fallback posting time from daily brief
        brief = brief_stories.get(story_num, {})
        if not fb['posting_time'] and brief.get('posting_window'):
            fb['posting_time'] = brief['posting_window']

        result[story_num] = fb

    return result


# ---------------------------------------------------------------------------
# Image Concepts parser
# ---------------------------------------------------------------------------

def parse_image_concepts(content):
    """Parse image concepts file. Returns dict: story_num -> list of image dicts."""
    result = {}

    story_pattern = r'^### STORY\s+(\d+):\s*(.+?)(?=^### STORY|^## Image Summary|\Z)'
    for m in re.finditer(story_pattern, content, re.MULTILINE | re.DOTALL):
        story_num = int(m.group(1))
        body = m.group(2).strip()

        images = []
        # Split by **Image XY** labels
        img_pattern = re.compile(
            r'\*\*Image\s+(\w+)\s*(?:—|--|-)\s*(.+?)\*\*\s*\n(.*?)(?=\*\*Image\s+\w|$)',
            re.DOTALL
        )
        for im in img_pattern.finditer(body):
            label = f"Image {im.group(1)}"
            size_desc = im.group(2).strip()
            img_body = im.group(3).strip()

            image = {
                'label': label,
                'size_desc': size_desc,
                'search_terms': [],
                'text_overlay': [],
                'composition': '',
                'usage': '',
            }

            for line in img_body.split('\n'):
                stripped = line.strip()
                if stripped.startswith('- **Photo search:**') or stripped.startswith('- **Imagn search:**'):
                    val = stripped.split(':**', 1)[1].strip().strip('"')
                    image['search_terms'].append(val)
                elif stripped.startswith('- **Text overlay:**'):
                    val = stripped.split(':**', 1)[1].strip().strip('"')
                    image['text_overlay'].append(val)
                elif stripped.startswith('- **Composition:**'):
                    image['composition'] = stripped.split(':**', 1)[1].strip()
                elif stripped.startswith('- **Usage:**'):
                    image['usage'] = stripped.split(':**', 1)[1].strip()

            images.append(image)

        if images:
            result[story_num] = images
        elif 'no image' not in body.lower():
            # Fallback: story has image content but not in expected format
            result[story_num] = [{'label': 'Image', 'raw': body}]

    return result


# ---------------------------------------------------------------------------
# Research Notes parser
# ---------------------------------------------------------------------------

def parse_research_notes(content_folder):
    """Parse 01-research-notes.md into per-story verified facts.

    Extracts the confidence-tagged facts ([HIGH], [MEDIUM], [LOW]) and source
    attributions for each story. This research is the foundation for accurate
    article generation and angle exploration in downstream tools.

    Returns dict: story_num -> {facts: str, sources: str}
    """
    result = {}
    path = os.path.join(content_folder, "01-research-notes.md")
    content = read_file(path)
    if not content:
        return result

    story_pattern = r'^### STORY\s+(\d+):\s*(.+?)(?=^### STORY|\Z)'
    for m in re.finditer(story_pattern, content, re.MULTILINE | re.DOTALL):
        story_num = int(m.group(1))
        body = m.group(2).strip()

        # Split body into facts and sources
        lines = body.split('\n')
        fact_lines = []
        source_lines = []
        in_sources = False

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped == '---':
                continue
            if stripped.lower().startswith('source') or stripped.lower().startswith('- source'):
                in_sources = True
                source_lines.append(stripped)
            elif in_sources and not stripped.startswith('- **['):
                source_lines.append(stripped)
            else:
                in_sources = False
                fact_lines.append(stripped)

        result[story_num] = {
            'facts': '\n'.join(fact_lines),
            'sources': '\n'.join(source_lines),
        }

    return result


# ---------------------------------------------------------------------------
# Fact-Check Log parser
# ---------------------------------------------------------------------------

def parse_fact_check_log(content_folder):
    """Parse fact-check log. Returns dict: story_num -> status dict."""
    result = {}
    path = os.path.join(content_folder, "06-fact-check-log.md")
    content = read_file(path)
    if not content:
        return result

    # Count claims per story
    story_pattern = r'^### STORY\s+(\d+):\s*(.+?)(?=^### STORY|\Z)'
    for m in re.finditer(story_pattern, content, re.MULTILINE | re.DOTALL):
        story_num = int(m.group(1))
        body = m.group(2)

        claims = len(re.findall(r'^\s*[-*]\s+\*?\*?Claim', body, re.MULTILINE | re.IGNORECASE))
        if claims == 0:
            claims = len(re.findall(r'^\s*[-*]\s+', body, re.MULTILINE))

        verified = len(re.findall(r'✅|VERIFIED|verified', body))
        flagged = len(re.findall(r'⚠|WARNING|PLAUSIBLE|UNVERIFIED|❌', body, re.IGNORECASE))
        corrected = len(re.findall(r'CORRECTED|FIXED|corrected', body, re.IGNORECASE))

        status = 'verified'
        if flagged > 0 or corrected > 0:
            status = 'warning'
        elif verified == 0 and claims > 0:
            status = 'unverified'

        result[story_num] = {
            'status': status,
            'claims_checked': claims,
            'claims_flagged': flagged,
            'errors_corrected': corrected,
        }

    return result


# ---------------------------------------------------------------------------
# Articles scanner
# ---------------------------------------------------------------------------

def scan_articles(content_folder):
    """Scan for article HTML files. Returns dict: story_num -> article dict."""
    result = {}

    for folder in [os.path.join(content_folder, 'articles'), content_folder]:
        if not os.path.isdir(folder):
            continue
        for fname in sorted(os.listdir(folder)):
            if not fname.startswith('article-') or not fname.endswith('.html'):
                continue
            filepath = os.path.join(folder, fname)
            content = read_file(filepath)
            if not content:
                continue

            # Extract story number from filename: article-01-slug.html
            num_m = re.search(r'article-(\d+)', fname)
            story_num = int(num_m.group(1)) if num_m else 0

            # Extract headline
            h1_m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
            headline = h1_m.group(1).strip() if h1_m else fname

            # Word count (strip HTML tags)
            text_only = re.sub(r'<[^>]+>', ' ', content)
            word_count = len(text_only.split())

            result[story_num] = {
                'filename': fname,
                'headline': headline,
                'word_count': word_count,
            }

    return result


# ---------------------------------------------------------------------------
# Assemble and validate
# ---------------------------------------------------------------------------

def assemble_json(config, date_str, brief_stories, schedule, x_posts,
                  fb_posts, image_concepts, fact_checks, articles,
                  research_notes=None):
    """Assemble all parsed data into the final JSON structure."""
    if research_notes is None:
        research_notes = {}

    platforms = config.get('platforms', ['x'])
    has_facebook = 'facebook' in platforms
    has_articles = config.get('article_word_count_min') is not None or any(articles.values())

    stories = []
    errors = []
    warnings = []

    # Build story list from daily brief (the canonical story list)
    for num in sorted(brief_stories.keys()):
        brief = brief_stories[num]
        story = {
            'story_num': num,
            'title': brief['title'],
            'tier': brief['tier'],
            'status': brief['status'],
            'angle': brief.get('angle', ''),
            'posting_window': brief.get('posting_window', ''),
            'x_posts': x_posts.get(num, []),
            'facebook': fb_posts.get(num) if has_facebook else None,
            'article': articles.get(num),
            'image_concepts': image_concepts.get(num),
            'fact_check': fact_checks.get(num),
            'research': research_notes.get(num),
        }
        stories.append(story)

        # Validation
        if not story['x_posts']:
            warnings.append(f"Story {num}: No X/Twitter posts found")
        if has_facebook and not story['facebook']:
            warnings.append(f"Story {num}: No Facebook posts found")
        if not story['posting_window']:
            warnings.append(f"Story {num}: No posting window specified")
        for tweet in story['x_posts']:
            if tweet['char_count'] > 280:
                errors.append(f"Story {num}, {tweet['label']}: {tweet['char_count']} chars (over 280 limit)")

    # Check for X posts that don't match any daily brief story
    all_brief_nums = set(brief_stories.keys())
    for num in x_posts:
        if num not in all_brief_nums and num != 0:
            warnings.append(f"X posts for story {num} exist but story not in daily brief")

    # Stats
    total_x = sum(len(s['x_posts']) for s in stories)
    total_fb = sum(1 for s in stories if s.get('facebook') and s['facebook'].get('long_form'))
    total_articles = sum(1 for s in stories if s.get('article'))
    total_images = sum(len(s['image_concepts']) for s in stories if s.get('image_concepts'))

    # Check for missing files
    missing_files = []

    return {
        'schema_version': '2.0',
        'date': date_str,
        'compiled_at': datetime.now(timezone.utc).isoformat(),
        'niche': {
            'brand_name': config.get('brand_name', ''),
            'brand_short': config.get('brand_short', ''),
            'content_prefix': config.get('content_prefix', ''),
            'platforms': platforms,
            'timezone': config.get('timezone', ''),
            'photo_source': config.get('photo_source', 'none'),
        },
        'schedule': schedule,
        'stories': stories,
        'pipeline_stats': {
            'total_stories': len(stories),
            'x_posts_count': total_x,
            'facebook_posts_count': total_fb,
            'articles_count': total_articles,
            'image_concepts_count': total_images,
        },
        'validation': {
            'errors': errors,
            'warnings': warnings,
            'missing_files': missing_files,
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    niche_name = None
    date_str = None

    i = 0
    while i < len(args):
        if args[i] == '--niche' and i + 1 < len(args):
            niche_name = args[i + 1]
            i += 2
        elif re.match(r'^\d{4}-\d{2}-\d{2}$', args[i]):
            date_str = args[i]
            i += 1
        else:
            i += 1

    if not date_str:
        print("Usage: python compile-content-data.py [--niche <name>] YYYY-MM-DD")
        sys.exit(1)

    niche_root = find_niche_root(niche_name)
    config = load_niche_config(niche_root)

    brand_name = config.get('brand_name', os.path.basename(niche_root))
    content_prefix = config.get('content_prefix', 'content')
    print(f"Niche: {brand_name}")
    print(f"Date: {date_str}")

    content_folder = os.path.join(niche_root, f"{content_prefix}-{date_str}")
    if not os.path.isdir(content_folder):
        print(f"ERROR: Content folder not found: {content_folder}")
        sys.exit(1)

    # 1. Parse daily brief (canonical story list + schedule)
    brief_content = read_file(os.path.join(content_folder, "00-daily-brief.md"))
    if not brief_content:
        print("ERROR: 00-daily-brief.md not found or empty")
        sys.exit(1)
    brief_stories, schedule = parse_daily_brief(brief_content)
    print(f"  ✓ Daily Brief: {len(brief_stories)} stories, {len(schedule)} schedule slots")

    # 2. Parse X/Twitter posts
    x_content = read_file(os.path.join(content_folder, "03-social-posts-x.md"))
    x_posts = parse_x_posts(x_content, brief_stories) if x_content else {}
    total_tweets = sum(len(v) for v in x_posts.values())
    print(f"  ✓ X/Twitter Posts: {total_tweets} tweets across {len(x_posts)} stories")

    # 3. Parse Facebook posts (if platform supported)
    fb_posts = {}
    platforms = config.get('platforms', ['x'])
    if 'facebook' in platforms:
        fb_content = read_file(os.path.join(content_folder, "04-social-posts-facebook.md"))
        fb_posts = parse_facebook_posts(fb_content, brief_stories) if fb_content else {}
        print(f"  ✓ Facebook Posts: {len(fb_posts)} stories")
    else:
        print(f"  - Facebook: skipped (not in platforms)")

    # 4. Parse image concepts
    img_content = read_file(os.path.join(content_folder, "05-image-concepts.md"))
    image_concepts = parse_image_concepts(img_content) if img_content else {}
    if image_concepts:
        total_imgs = sum(len(v) for v in image_concepts.values())
        print(f"  ✓ Image Concepts: {total_imgs} concepts across {len(image_concepts)} stories")
    else:
        print(f"  - Image Concepts: none found")

    # 5. Parse research notes (verified facts per story)
    research_notes = parse_research_notes(content_folder)
    if research_notes:
        print(f"  ✓ Research Notes: {len(research_notes)} stories with verified facts")
    else:
        print(f"  - Research Notes: none found")

    # 6. Parse fact-check log
    fact_checks = parse_fact_check_log(content_folder)
    if fact_checks:
        print(f"  ✓ Fact-Check: {len(fact_checks)} stories checked")
    else:
        print(f"  - Fact-Check: no log found")

    # 7. Scan articles
    articles = scan_articles(content_folder)
    if articles:
        print(f"  ✓ Articles: {len(articles)} found")
    else:
        print(f"  - Articles: none found")

    # 8. Assemble JSON
    data = assemble_json(config, date_str, brief_stories, schedule, x_posts,
                         fb_posts, image_concepts, fact_checks, articles,
                         research_notes)

    # 8. Write output
    output_path = os.path.join(content_folder, "07-content-data.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Compiled: {output_path}")
    print(f"  Stories: {data['pipeline_stats']['total_stories']}")
    print(f"  X posts: {data['pipeline_stats']['x_posts_count']}")
    print(f"  FB posts: {data['pipeline_stats']['facebook_posts_count']}")
    print(f"  Articles: {data['pipeline_stats']['articles_count']}")
    print(f"  Images: {data['pipeline_stats']['image_concepts_count']}")

    # Report validation issues
    v = data['validation']
    if v['errors']:
        print(f"\n❌ ERRORS ({len(v['errors'])}):")
        for e in v['errors']:
            print(f"  - {e}")
    if v['warnings']:
        print(f"\n⚠ WARNINGS ({len(v['warnings'])}):")
        for w in v['warnings']:
            print(f"  - {w}")
    if not v['errors'] and not v['warnings']:
        print(f"\n✓ Validation: all clear")

    return 0 if not v['errors'] else 1


if __name__ == '__main__':
    sys.exit(main())
