#!/usr/bin/env python3
"""
FanGear HQ WordPress Publisher

Publishes articles from 07-content-data.json to WordPress via REST API.
Works across all niches by loading niche-specific config dynamically.
Skips niches with no articles (e.g., Cubs with article_word_count_min=0).
Optionally generates AI featured images via Gemini and uploads them.

Usage:
    python publish-to-wordpress.py --niche Softball 2026-03-06
    python publish-to-wordpress.py --niche Softball 2026-03-06 --dry-run
    python publish-to-wordpress.py --niche Softball 2026-03-06 --status publish
    python publish-to-wordpress.py --niche Softball 2026-03-06 --images     # generate featured images
    python publish-to-wordpress.py --niche Softball 2026-03-06 --images --dry-run
"""

import base64
import json
import mimetypes
import os
import re
import sys
import argparse
import tempfile
import time
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin

# Fix Unicode output on Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Path helpers (same pattern as publish-dashboard.py)
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
                if in_platforms and not stripped.startswith('- '):
                    in_platforms = False
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


# ---------------------------------------------------------------------------
# WordPress API client
# ---------------------------------------------------------------------------

# Niche brand name -> WordPress category name mapping
NICHE_CATEGORIES = {
    "I Love Softball": "Softball",
    "Chicago Cubs Fan HQ": "Cubs",
    "Ballpark Banter": "MLB",
    "Hoop Heroes": "NBA",
    "F1 Fanrecap": "F1",
    "Golf Fanrecap": "Golf",
    "Tennis Fanrecap": "Tennis",
}


class WordPressClient:
    """Minimal WordPress REST API client using urllib (no requests dependency)."""

    def __init__(self, site_url, username, app_password):
        self.api_url = site_url.rstrip('/') + '/wp-json/wp/v2'
        # WordPress Application Passwords use Basic Auth
        credentials = f"{username}:{app_password}"
        self.auth_header = 'Basic ' + base64.b64encode(credentials.encode()).decode()
        self._category_cache = {}

    def _request(self, method, endpoint, data=None):
        """Make an authenticated request to the WP REST API."""
        url = f"{self.api_url}/{endpoint}"
        headers = {
            'Authorization': self.auth_header,
            'Content-Type': 'application/json',
            'User-Agent': 'FanGearHQ-ContentPipeline/1.0',
        }

        body = json.dumps(data).encode('utf-8') if data else None
        req = Request(url, data=body, headers=headers, method=method)

        try:
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except HTTPError as e:
            error_body = e.read().decode('utf-8', errors='replace')
            print(f"  ERROR: WordPress API {method} {endpoint} returned {e.code}")
            try:
                error_json = json.loads(error_body)
                print(f"    Message: {error_json.get('message', error_body[:200])}")
            except json.JSONDecodeError:
                print(f"    Response: {error_body[:200]}")
            return None
        except URLError as e:
            print(f"  ERROR: Could not reach WordPress API: {e.reason}")
            return None

    def get_or_create_category(self, category_name):
        """Get existing category ID or create it. Caches results."""
        if category_name in self._category_cache:
            return self._category_cache[category_name]

        # Search for existing category
        url = f"categories?search={category_name}&per_page=100"
        result = self._request('GET', url)
        if result:
            for cat in result:
                if cat['name'].lower() == category_name.lower():
                    self._category_cache[category_name] = cat['id']
                    return cat['id']

        # Create new category
        result = self._request('POST', 'categories', {'name': category_name})
        if result and 'id' in result:
            self._category_cache[category_name] = result['id']
            print(f"  Created WordPress category: {category_name} (ID: {result['id']})")
            return result['id']

        return None

    def upload_media(self, image_path, title=None, alt_text=None):
        """Upload an image to the WP media library. Returns media data or None."""
        filename = os.path.basename(image_path)
        content_type = mimetypes.guess_type(filename)[0] or 'image/png'

        with open(image_path, 'rb') as f:
            image_data = f.read()

        url = f"{self.api_url}/media"
        headers = {
            'Authorization': self.auth_header,
            'Content-Type': content_type,
            'Content-Disposition': f'attachment; filename="{filename}"',
            'User-Agent': 'FanGearHQ-ContentPipeline/1.0',
        }

        req = Request(url, data=image_data, headers=headers, method='POST')

        try:
            with urlopen(req, timeout=60) as resp:
                media = json.loads(resp.read().decode('utf-8'))

            media_id = media.get('id')

            # Set alt text if provided
            if media_id and alt_text:
                self._request('POST', f'media/{media_id}', {'alt_text': alt_text})

            return media
        except HTTPError as e:
            error_body = e.read().decode('utf-8', errors='replace')
            print(f"    ERROR: Media upload failed ({e.code})")
            try:
                error_json = json.loads(error_body)
                print(f"      Message: {error_json.get('message', error_body[:200])}")
            except json.JSONDecodeError:
                print(f"      Response: {error_body[:200]}")
            return None
        except URLError as e:
            print(f"    ERROR: Could not reach WordPress for media upload: {e.reason}")
            return None

    def create_post(self, title, content, status='draft', categories=None,
                    excerpt=None, slug=None, featured_media=None):
        """Create a WordPress post. Returns post data or None on failure."""
        post_data = {
            'title': title,
            'content': content,
            'status': status,
        }
        if categories:
            post_data['categories'] = categories
        if excerpt:
            post_data['excerpt'] = excerpt
        if slug:
            post_data['slug'] = slug
        if featured_media:
            post_data['featured_media'] = featured_media

        return self._request('POST', 'posts', post_data)

    def test_connection(self):
        """Verify API credentials work. Returns True/False."""
        result = self._request('GET', 'users/me')
        if result and 'id' in result:
            print(f"  WordPress auth OK (user: {result.get('name', 'unknown')})")
            return True
        print("  ERROR: WordPress authentication failed")
        return False


# ---------------------------------------------------------------------------
# Featured image generation via Gemini
# ---------------------------------------------------------------------------

def generate_featured_image(title, category, content_folder, story_num, dry_run=False):
    """Generate a featured image for an article using Gemini.

    Returns the path to the generated image, or None on failure.
    """
    # Import the existing Gemini generator
    scripts_dir = Path(__file__).parent
    sys.path.insert(0, str(scripts_dir))
    try:
        from generate_gemini_image import generate_image
    except ImportError:
        # Try with hyphenated filename (Python import workaround)
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "generate_gemini_image",
            str(scripts_dir / "generate-gemini-image.py")
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        generate_image = mod.generate_image

    # Build a prompt for an editorial hero image — NO human figures
    # Use team logos, mascots, stadiums, equipment, and symbolic imagery
    prompt = (
        f"A professional editorial hero image for a sports news article titled: "
        f'"{title}". '
        f"Sport: {category}. "
        f"DO NOT include any human figures, players, coaches, or people. "
        f"Instead use: team logos, mascots, realistic stadium scenes, sports equipment "
        f"(softballs, gloves, bats, helmets), dramatic field/diamond shots, "
        f"scoreboards, trophies, or symbolic editorial compositions. "
        f"Use real team branding and colors when teams are mentioned in the title. "
        f"Cinematic lighting, rich colors, wide banner composition. "
        f"No watermarks. Suitable for a news website featured image."
    )

    # Save to content folder's generated-images dir
    gen_dir = Path(content_folder) / "generated-images"
    gen_dir.mkdir(parents=True, exist_ok=True)
    output_path = str(gen_dir / f"wp-hero-story-{story_num}.png")

    if dry_run:
        print(f"    [DRY RUN] Would generate image: {output_path}")
        print(f"    [DRY RUN] Prompt: {prompt[:100]}...")
        return "DRY_RUN"

    result = generate_image(
        prompt=prompt,
        width=1200,
        height=630,
        mode="base_only",
        output_path=output_path,
        dry_run=False,
    )

    return result


# ---------------------------------------------------------------------------
# Article processing
# ---------------------------------------------------------------------------

def extract_article_body(html_content):
    """Extract the inner content of <article> tag, stripping the HTML wrapper.

    WordPress adds its own <html>/<head>/<body>, so we only want the
    content inside <article>...</article>.
    """
    # Extract content between <article> and </article>
    match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fallback: extract content between <body> and </body>
    match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Last resort: return as-is
    return html_content


def extract_excerpt(html_content, max_length=300):
    """Extract first paragraph text as excerpt."""
    match = re.search(r'<p>(.*?)</p>', html_content, re.DOTALL)
    if match:
        # Strip HTML tags from the paragraph
        text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if len(text) > max_length:
            text = text[:max_length].rsplit(' ', 1)[0] + '...'
        return text
    return None


def article_to_slug(filename):
    """Convert article filename to a URL slug.

    article-01-ncaa-softball-rankings.html -> ncaa-softball-rankings
    """
    slug = filename.replace('.html', '')
    # Remove the article-NN- prefix
    slug = re.sub(r'^article-\d+-', '', slug)
    return slug


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Publish pipeline articles to WordPress via REST API"
    )
    parser.add_argument("--niche", required=True, help="Niche folder name (e.g., Softball, MLB)")
    parser.add_argument("date", nargs="?", default=None, help="YYYY-MM-DD (defaults to today)")
    parser.add_argument("--dry-run", action="store_true", help="Preview what would be published without making API calls")
    parser.add_argument("--status", default="draft", choices=["draft", "publish"], help="WordPress post status (default: draft)")
    parser.add_argument("--images", action="store_true", help="Generate AI featured images via Gemini and attach to posts")
    args = parser.parse_args()

    date_str = args.date or datetime.now().strftime("%Y-%m-%d")

    # Validate date format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"ERROR: Invalid date format '{date_str}'. Use YYYY-MM-DD")
        sys.exit(1)

    # Load niche config
    niche_root = find_niche_root(args.niche)
    config = load_niche_config(niche_root)
    content_prefix = config.get('content_prefix', 'content')
    brand_name = config.get('brand_name', args.niche)

    # Check if niche produces articles
    article_min = int(config.get('article_word_count_min', '0'))
    if article_min == 0:
        print(f"Skipping {brand_name} -- articles disabled (word_count_min=0)")
        sys.exit(0)

    # Load content data
    content_folder = os.path.join(niche_root, f"{content_prefix}-{date_str}")
    data_path = os.path.join(content_folder, "07-content-data.json")
    if not os.path.isfile(data_path):
        print(f"ERROR: {data_path} not found")
        print("  Run compile-content-data.py first")
        sys.exit(1)

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Collect stories that have articles
    articles_to_publish = []
    articles_dir = os.path.join(content_folder, "articles")

    for story in data.get('stories', []):
        article_info = story.get('article')
        if not article_info or not article_info.get('filename'):
            continue

        article_path = os.path.join(articles_dir, article_info['filename'])
        if not os.path.isfile(article_path):
            print(f"  WARNING: Article file not found: {article_info['filename']}")
            continue

        with open(article_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        articles_to_publish.append({
            'story_num': story.get('story_num', 0),
            'title': article_info.get('headline', story.get('title', 'Untitled')),
            'filename': article_info['filename'],
            'html': html_content,
            'word_count': article_info.get('word_count', 0),
        })

    if not articles_to_publish:
        print(f"No articles to publish for {brand_name} on {date_str}")
        sys.exit(0)

    # Determine WordPress category for this niche
    category_name = NICHE_CATEGORIES.get(brand_name, args.niche)

    print(f"WordPress Publisher")
    print(f"  Niche: {brand_name}")
    print(f"  Date: {date_str}")
    print(f"  Articles: {len(articles_to_publish)}")
    print(f"  Category: {category_name}")
    print(f"  Status: {args.status}")
    print(f"  Images: {'Gemini AI' if args.images else 'none'}")
    print()

    if args.dry_run:
        print("[DRY RUN] Would publish:")
        for art in articles_to_publish:
            slug = article_to_slug(art['filename'])
            print(f"  - {art['title']}")
            print(f"    Slug: {slug}")
            print(f"    Words: {art['word_count']}")
            if args.images:
                generate_featured_image(
                    art['title'], category_name, content_folder,
                    art['story_num'], dry_run=True
                )
        print(f"\n[DRY RUN] {len(articles_to_publish)} articles would be published as {args.status}")
        sys.exit(0)

    # Load WordPress credentials from environment
    wp_url = os.environ.get('WP_FANRUMOR_URL', 'https://fanrumor.com')
    wp_user = os.environ.get('WP_FANRUMOR_USERNAME')
    wp_pass = os.environ.get('WP_FANRUMOR_APP_PASSWORD')

    if not wp_user or not wp_pass:
        print("WARNING: WordPress credentials not configured -- skipping publish")
        print("  Set WP_FANRUMOR_USERNAME and WP_FANRUMOR_APP_PASSWORD environment variables")
        sys.exit(0)

    # Strip spaces from Application Password (WP displays them with spaces)
    wp_pass = wp_pass.replace(' ', '')

    # Connect and verify
    wp = WordPressClient(wp_url, wp_user, wp_pass)
    if not wp.test_connection():
        sys.exit(1)

    # Get or create the category
    category_id = wp.get_or_create_category(category_name)
    categories = [category_id] if category_id else []

    # Publish each article
    published = 0
    failed = 0

    for art in articles_to_publish:
        title = art['title']
        slug = article_to_slug(art['filename'])
        body = extract_article_body(art['html'])
        excerpt = extract_excerpt(art['html'])
        featured_media_id = None

        print(f"  Publishing: {title}")

        # Generate and upload featured image if --images flag is set
        if args.images:
            print(f"    Generating featured image...")
            image_path = generate_featured_image(
                title, category_name, content_folder, art['story_num']
            )
            if image_path and image_path != "DRY_RUN":
                print(f"    Uploading to WordPress media library...")
                media = wp.upload_media(
                    image_path,
                    title=title,
                    alt_text=title,
                )
                if media and 'id' in media:
                    featured_media_id = media['id']
                    print(f"    Image uploaded (media ID: {featured_media_id})")
                else:
                    print(f"    Image upload failed, publishing without featured image")
            else:
                print(f"    Image generation failed, publishing without featured image")

        result = wp.create_post(
            title=title,
            content=body,
            status=args.status,
            categories=categories,
            excerpt=excerpt,
            slug=slug,
            featured_media=featured_media_id,
        )

        if result and 'id' in result:
            post_url = result.get('link', f"{wp_url}/?p={result['id']}")
            print(f"    OK (ID: {result['id']}, status: {args.status})")
            print(f"    URL: {post_url}")
            published += 1

            # ─── Affiliate Auto-Linking (MLB, NBA only) ──────────
            affiliate_niches = {'mlb', 'nba'}
            if args.niche.lower() in affiliate_niches:
                autolink_url = os.environ.get('COMMAND_CENTER_URL', '').rstrip('/')
                autolink_key = os.environ.get('COMMAND_CENTER_API_KEY', '')
                if autolink_url and autolink_key:
                    try:
                        autolink_data = json.dumps({
                            "wp_post_id": result['id'],
                            "channel": "article",
                            "content_id": slug,
                        }).encode('utf-8')
                        autolink_req = Request(
                            f"{autolink_url}/api/affiliates/link-article",
                            data=autolink_data,
                            headers={
                                'Content-Type': 'application/json',
                                'x-api-key': autolink_key,
                            },
                            method='POST',
                        )
                        with urlopen(autolink_req, timeout=30) as resp:
                            link_result = json.loads(resp.read().decode('utf-8'))
                            injected = link_result.get('links_injected', 0)
                            if injected > 0:
                                entities = [l['entity'] for l in link_result.get('links', [])]
                                print(f"    Affiliate links: {injected} injected ({', '.join(entities)})")
                            else:
                                print(f"    Affiliate links: none matched")
                    except Exception as e:
                        print(f"    Affiliate linking skipped: {e}")
        else:
            print(f"    FAILED")
            failed += 1

        # Small delay between posts to be polite to the API
        time.sleep(0.5)

    print()
    print(f"Results: {published} published, {failed} failed out of {len(articles_to_publish)} articles")

    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
