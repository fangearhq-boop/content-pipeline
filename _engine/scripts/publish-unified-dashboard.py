#!/usr/bin/env python3
"""
FanGear HQ Unified Dashboard Publisher

Publishes review dashboards from any niche into the unified content-dashboards repo.
Auto-generates niche-level and root-level index pages.

Usage:
    python publish-unified-dashboard.py --niche Softball 2026-03-19
    python publish-unified-dashboard.py --niche Cubs 2026-03-19
    python publish-unified-dashboard.py --niche Softball   # publish all recent dashboards
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

# Fix Unicode output on Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

UNIFIED_REPO = "fangearhq-boop/content-dashboards"
GITHUB_PAGES_URL = f"https://fangearhq-boop.github.io/content-dashboards/"
MAX_DASHBOARDS_PER_NICHE = 5

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

DEPLOY_WORKFLOW_YAML = """\
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deployment
        uses: actions/deploy-pages@v4
"""


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def find_engine_root():
    """Find the _engine directory (parent of scripts/)."""
    return Path(__file__).resolve().parent.parent


def find_niche_root(niche_name):
    """Find the niche project root."""
    niche_launches = find_engine_root().parent
    # Direct match
    niche_root = niche_launches / niche_name
    if niche_root.is_dir():
        return niche_root
    # Case-insensitive match
    for entry in niche_launches.iterdir():
        if entry.is_dir() and entry.name.lower() == niche_name.lower() and entry.name != '_engine':
            return entry
    print(f"ERROR: Niche folder not found: {niche_name}")
    print(f"  Looked in: {niche_launches}")
    sys.exit(1)


def load_niche_config(niche_root):
    """Load niche-config.yaml and return as dict (simple parser)."""
    config_path = niche_root / 'niche-config.yaml'
    if not config_path.is_file():
        print(f"WARNING: No niche-config.yaml found at {config_path}")
        return {}
    config = {}
    in_platforms = False
    platforms = []
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


# ---------------------------------------------------------------------------
# Dashboard discovery
# ---------------------------------------------------------------------------

def discover_dashboards(niche_root, content_prefix, max_days=MAX_DASHBOARDS_PER_NICHE):
    """Find dated folders containing review-dashboard.html. Returns newest first."""
    dashboards = []
    for item in sorted(niche_root.iterdir(), reverse=True):
        if item.is_dir() and item.name.startswith(content_prefix + '-'):
            dashboard_file = item / 'review-dashboard.html'
            if dashboard_file.exists():
                date_match = re.search(r'(\d{4}-\d{2}-\d{2})', item.name)
                if date_match:
                    date_str = date_match.group(1)
                    try:
                        dt = datetime.strptime(date_str, '%Y-%m-%d')
                        label = f"{DAYS[dt.weekday()]}, {MONTHS[dt.month - 1]} {dt.day}"
                        dashboards.append({
                            'date': date_str,
                            'label': label,
                            'folder': item.name,
                            'path': dashboard_file,
                        })
                    except ValueError:
                        continue
    dashboards.sort(key=lambda d: d['date'], reverse=True)
    return dashboards[:max_days]


# ---------------------------------------------------------------------------
# HTML generators
# ---------------------------------------------------------------------------

def generate_niche_index(niche_short, brand_name, dashboards):
    """Generate the niche-level index.html listing recent dashboards."""
    rows = []
    for i, d in enumerate(dashboards):
        badge = '<span class="badge">latest</span>' if i == 0 else ''
        rows.append(f'''      <a class="date-card" href="{d['date']}.html">
        <div class="date-info">
          <h2>{d['label']}{badge}</h2>
          <span>{d['date']}</span>
        </div>
        <div class="arrow">&rarr;</div>
      </a>''')

    rows_html = '\n'.join(rows)
    empty_msg = '<div class="empty">No dashboards yet.</div>' if not dashboards else ''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{brand_name} — Content Dashboards</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;600;700&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #1A1A2E;
    color: #fff;
    min-height: 100vh;
  }}
  .header {{
    background: linear-gradient(135deg, #FF8A00 0%, #E53935 100%);
    padding: 2rem 1.5rem;
    text-align: center;
  }}
  .header h1 {{
    font-family: 'Bebas Neue', Impact, sans-serif;
    font-size: 2.2rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
  }}
  .header p {{
    font-size: 0.95rem;
    opacity: 0.9;
  }}
  .back-link {{
    display: inline-block;
    margin: 1.5rem 0 0 1.5rem;
    color: #FF8A00;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 600;
  }}
  .back-link:hover {{ text-decoration: underline; }}
  .container {{
    max-width: 700px;
    margin: 0 auto;
    padding: 1rem 1.5rem 2rem;
  }}
  .date-card {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
    text-decoration: none;
    color: #fff;
    transition: all 0.2s ease;
  }}
  .date-card:hover {{
    background: rgba(255,138,0,0.15);
    border-color: #FF8A00;
    transform: translateY(-2px);
  }}
  .date-card .date-info h2 {{
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
  }}
  .date-card .date-info span {{
    font-size: 0.85rem;
    color: rgba(255,255,255,0.6);
  }}
  .date-card .arrow {{
    font-size: 1.5rem;
    color: #FF8A00;
  }}
  .badge {{
    display: inline-block;
    background: #FF8A00;
    color: #1A1A2E;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    margin-left: 0.6rem;
    vertical-align: middle;
    text-transform: uppercase;
  }}
  .empty {{
    text-align: center;
    padding: 3rem 1rem;
    color: rgba(255,255,255,0.4);
  }}
</style>
</head>
<body>

<div class="header">
  <h1>{brand_name}</h1>
  <p>Content Review Dashboards</p>
</div>

<a class="back-link" href="../index.html">&larr; All Niches</a>

<div class="container">
{rows_html}{empty_msg}
</div>

</body>
</html>'''


def generate_root_index(repo_root):
    """Generate the root index.html by auto-discovering niche subfolders."""
    # Load brand name manifest if it exists
    import json
    niche_manifest = {}
    manifest_path = repo_root / 'niches.json'
    if manifest_path.exists():
        try:
            niche_manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except Exception:
            pass

    niches = []
    for item in sorted(repo_root.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            # Check if it has at least one .html dashboard file
            html_files = sorted(
                [f for f in item.iterdir() if f.suffix == '.html' and f.name != 'index.html'],
                key=lambda f: f.name,
                reverse=True
            )
            if html_files:
                # Extract dates and find the latest
                latest_date = None
                dashboard_count = 0
                for hf in html_files:
                    date_match = re.match(r'(\d{4}-\d{2}-\d{2})\.html$', hf.name)
                    if date_match:
                        dashboard_count += 1
                        d = date_match.group(1)
                        if latest_date is None or d > latest_date:
                            latest_date = d

                # Look up full brand name from niches.json manifest
                niche_name = niche_manifest.get(item.name, item.name.upper() if len(item.name) <= 4 else item.name.capitalize())

                # Try to extract post count from the latest dashboard
                post_count = _extract_post_count(html_files[0]) if html_files else None

                niches.append({
                    'short': item.name,
                    'name': niche_name,
                    'latest_date': latest_date or 'N/A',
                    'dashboard_count': dashboard_count,
                    'post_count': post_count,
                })

    # Build niche cards
    cards = []
    for n in niches:
        date_display = n['latest_date']
        if date_display != 'N/A':
            try:
                dt = datetime.strptime(date_display, '%Y-%m-%d')
                date_display = f"{DAYS[dt.weekday()]}, {MONTHS[dt.month - 1]} {dt.day}"
            except ValueError:
                pass

        meta_line = f'<span class="meta-date">Last run: {date_display}</span>'
        if n['post_count']:
            meta_line += f'<span class="meta-posts">{n["post_count"]} posts</span>'
        meta_line += f'<span class="meta-count">{n["dashboard_count"]} dashboard{"s" if n["dashboard_count"] != 1 else ""}</span>'

        cards.append(f'''      <a class="niche-card" href="{n['short']}/index.html">
        <div class="card-content">
          <h2>{n['name']}</h2>
          <div class="card-meta">
            {meta_line}
          </div>
        </div>
        <div class="arrow">View Dashboards &rarr;</div>
      </a>''')

    cards_html = '\n'.join(cards)
    empty_msg = '<div class="empty">No niches found. Run the publish script for a niche first.</div>' if not cards else ''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FanGear HQ — Content Dashboards</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;600;700&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #1A1A2E;
    color: #fff;
    min-height: 100vh;
  }}
  .header {{
    background: linear-gradient(135deg, #FF8A00 0%, #E53935 100%);
    padding: 2.5rem 1.5rem;
    text-align: center;
  }}
  .header h1 {{
    font-family: 'Bebas Neue', Impact, sans-serif;
    font-size: 2.8rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
  }}
  .header p {{
    font-size: 1rem;
    opacity: 0.9;
  }}
  .container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
  }}
  .niche-card {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1.2rem;
    text-decoration: none;
    color: #fff;
    transition: all 0.2s ease;
  }}
  .niche-card:hover {{
    background: rgba(255,138,0,0.15);
    border-color: #FF8A00;
    transform: translateY(-2px);
  }}
  .card-content h2 {{
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
  }}
  .card-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem 1.2rem;
  }}
  .card-meta span {{
    font-size: 0.82rem;
    color: rgba(255,255,255,0.55);
  }}
  .meta-date::before {{ content: "\\1F4C5 "; }}
  .meta-posts::before {{ content: "\\1F4DD "; }}
  .meta-count::before {{ content: "\\1F4CA "; }}
  .arrow {{
    font-size: 0.95rem;
    font-weight: 600;
    color: #FF8A00;
    white-space: nowrap;
    margin-left: 1rem;
  }}
  .empty {{
    text-align: center;
    padding: 3rem 1rem;
    color: rgba(255,255,255,0.4);
  }}
  .footer {{
    text-align: center;
    padding: 2rem 1rem;
    font-size: 0.8rem;
    color: rgba(255,255,255,0.3);
  }}
  @media (max-width: 600px) {{
    .niche-card {{
      flex-direction: column;
      align-items: flex-start;
      gap: 0.8rem;
    }}
    .arrow {{
      margin-left: 0;
    }}
    .header h1 {{
      font-size: 2rem;
    }}
  }}
</style>
</head>
<body>

<div class="header">
  <h1>FanGear HQ</h1>
  <p>Content Review Dashboards</p>
</div>

<div class="container">
{cards_html}{empty_msg}
</div>

<div class="footer">
  Auto-generated by publish-unified-dashboard.py
</div>

</body>
</html>'''


def _extract_post_count(html_path):
    """Try to extract total post count from a dashboard HTML file."""
    try:
        content = html_path.read_text(encoding='utf-8', errors='replace')
        # Look for common patterns like "12 Posts" or "totalPosts: 12"
        match = re.search(r'(\d+)\s+(?:Total\s+)?Posts', content, re.IGNORECASE)
        if match:
            return int(match.group(1))
        # Try JSON data pattern
        match = re.search(r'"totalPosts"\s*:\s*(\d+)', content)
        if match:
            return int(match.group(1))
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# Git / deployment helpers
# ---------------------------------------------------------------------------

def _detect_github_pat():
    """Extract GitHub PAT from the current repo's git remote URL.

    Checks GITHUB_TOKEN env var first, then falls back to parsing the PAT
    embedded in the content-pipeline origin remote URL (format:
    https://<pat>@github.com/...). This means any environment that can push
    to content-pipeline can also push to content-dashboards — single source
    of truth, no extra env var needed.
    """
    pat = os.environ.get('GITHUB_TOKEN', '')
    if pat:
        return pat

    try:
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            capture_output=True, text=True, timeout=5,
            cwd=str(find_engine_root().parent)
        )
        if result.returncode == 0:
            url = result.stdout.strip()
            # Match https://<token>@github.com/...
            match = re.match(r'https://([^@]+)@github\.com/', url)
            if match:
                return match.group(1)
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    return ''


def clone_or_pull_repo(tmp_dir):
    """Clone the unified repo to tmp_dir. If it exists, pull latest."""
    repo_path = Path(tmp_dir) / 'content-dashboards'
    if repo_path.exists() and (repo_path / '.git').exists():
        print("  Pulling latest from remote...")
        subprocess.run(
            ['git', 'pull', 'origin', 'main', '--rebase'],
            cwd=str(repo_path), capture_output=True, text=True, timeout=30
        )
        return repo_path

    print(f"  Cloning {UNIFIED_REPO}...")
    pat = _detect_github_pat()
    clone_url = f'https://{pat}@github.com/{UNIFIED_REPO}.git' if pat else f'https://github.com/{UNIFIED_REPO}.git'
    result = subprocess.run(
        ['git', 'clone', clone_url, str(repo_path)],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        # Repo may be empty — init manually
        print("  Repo appears empty, initializing...")
        repo_path.mkdir(parents=True, exist_ok=True)
        subprocess.run(['git', 'init'], cwd=str(repo_path), capture_output=True)
        subprocess.run(['git', 'branch', '-M', 'main'], cwd=str(repo_path), capture_output=True)
        subprocess.run(
            ['git', 'remote', 'add', 'origin', clone_url],
            cwd=str(repo_path), capture_output=True
        )
    # Disable commit signing in this tmp clone — signing server only has context
    # for the content-pipeline source path, not tmp deployment clones.
    subprocess.run(['git', 'config', '--local', 'commit.gpgsign', 'false'],
                   cwd=str(repo_path), capture_output=True)
    subprocess.run(['git', 'config', '--local', 'user.email', 'fangearhq@gmail.com'],
                   cwd=str(repo_path), capture_output=True)
    subprocess.run(['git', 'config', '--local', 'user.name', 'Content Pipeline Bot'],
                   cwd=str(repo_path), capture_output=True)
    return repo_path


def ensure_deploy_infrastructure(repo_root):
    """Create .nojekyll and deploy workflow if they don't exist."""
    changed = False
    nojekyll = repo_root / '.nojekyll'
    if not nojekyll.exists():
        nojekyll.touch()
        subprocess.run(['git', 'add', '.nojekyll'], cwd=str(repo_root), capture_output=True)
        print("  + Created .nojekyll")
        changed = True

    workflow_dir = repo_root / '.github' / 'workflows'
    workflow_file = workflow_dir / 'deploy-pages.yml'
    if not workflow_file.exists():
        workflow_dir.mkdir(parents=True, exist_ok=True)
        workflow_file.write_text(DEPLOY_WORKFLOW_YAML)
        subprocess.run(
            ['git', 'add', '.github/workflows/deploy-pages.yml'],
            cwd=str(repo_root), capture_output=True
        )
        print("  + Created .github/workflows/deploy-pages.yml")
        changed = True

    return changed


def ensure_pages_workflow_mode():
    """Switch GitHub Pages to workflow mode if on legacy."""
    try:
        result = subprocess.run(
            ['gh', 'api', f'repos/{UNIFIED_REPO}/pages', '--jq', '.build_type'],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            # Pages not enabled yet — enable it
            print("  Enabling GitHub Pages (workflow mode)...")
            subprocess.run(
                ['gh', 'api', '-X', 'POST', f'repos/{UNIFIED_REPO}/pages',
                 '-f', 'build_type=workflow', '-f', 'source[branch]=main', '-f', 'source[path]=/'],
                capture_output=True, text=True, timeout=10
            )
            return

        build_type = result.stdout.strip()
        if build_type == 'legacy':
            print("  Switching Pages from legacy to workflow mode...")
            subprocess.run(
                ['gh', 'api', '-X', 'PUT', f'repos/{UNIFIED_REPO}/pages',
                 '-f', 'build_type=workflow'],
                capture_output=True, text=True, timeout=10
            )
            print("  Done")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass


def git_commit_and_push(repo_root, message):
    """Stage all changes, commit, and push."""
    subprocess.run(['git', 'add', '-A'], cwd=str(repo_root), capture_output=True)

    # Check for changes
    result = subprocess.run(
        ['git', 'diff', '--cached', '--quiet'],
        cwd=str(repo_root), capture_output=True
    )
    if result.returncode == 0:
        print("  No changes to commit — dashboards already up to date")
        return False

    subprocess.run(
        ['git', 'commit', '-m', message],
        cwd=str(repo_root), capture_output=True, text=True
    )
    print(f"  Committed: {message}")

    try:
        result = subprocess.run(
            ['git', 'push', '-u', 'origin', 'main'],
            cwd=str(repo_root), capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print("  Pushed to GitHub")
            return True
        else:
            print(f"  Push failed: {result.stderr.strip()}")
            return False
    except subprocess.TimeoutExpired:
        print("  Push timed out")
        return False


def verify_deploy(max_wait=90):
    """Wait for GitHub Pages to deploy."""
    print(f"\nVerifying deployment...")
    start = time.time()
    while time.time() - start < max_wait:
        try:
            result = subprocess.run(
                ['gh', 'api', f'repos/{UNIFIED_REPO}/pages/builds', '--jq', '.[0].status'],
                capture_output=True, text=True, timeout=10
            )
            status = result.stdout.strip()
            if status == 'built':
                print(f"  Deployed successfully")
                return True
            elif status == 'errored':
                print(f"  Build errored — check GitHub Actions")
                return False
        except (FileNotFoundError, subprocess.TimeoutExpired):
            break
        time.sleep(10)

    elapsed = int(time.time() - start)
    print(f"  Deploy verification timed out after {elapsed}s")
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    niche_name = None
    specific_date = None

    i = 0
    while i < len(args):
        if args[i] == '--niche' and i + 1 < len(args):
            niche_name = args[i + 1]
            i += 2
        elif re.match(r'\d{4}-\d{2}-\d{2}', args[i]):
            specific_date = args[i]
            i += 1
        else:
            i += 1

    if not niche_name:
        print("Usage: python publish-unified-dashboard.py --niche <name> [YYYY-MM-DD]")
        sys.exit(1)

    if specific_date:
        try:
            datetime.strptime(specific_date, '%Y-%m-%d')
        except ValueError:
            print(f"Error: Invalid date '{specific_date}'. Use YYYY-MM-DD")
            sys.exit(1)

    # Find niche and load config
    niche_root = find_niche_root(niche_name)
    config = load_niche_config(niche_root)
    content_prefix = config.get('content_prefix', niche_root.name.lower() + '-content')
    brand_name = config.get('brand_name', niche_root.name)
    brand_short = config.get('brand_short', niche_root.name).lower()

    print(f"Scanning for dashboards...")
    print(f"  Niche: {brand_name} ({brand_short})")
    print(f"  Prefix: {content_prefix}")
    print()

    # Discover dashboards
    dashboards = discover_dashboards(niche_root, content_prefix)
    if not dashboards:
        print("No dashboards found. Run the content pipeline first.")
        sys.exit(1)

    # Filter to specific date if provided
    if specific_date:
        matching = [d for d in dashboards if d['date'] == specific_date]
        if not matching:
            print(f"No dashboard found for {specific_date}")
            sys.exit(1)
        # Still keep all for the index, but only copy the specific one
        dashboards_to_copy = matching
    else:
        dashboards_to_copy = dashboards

    for d in dashboards:
        marker = " *" if d in dashboards_to_copy else ""
        print(f"  {d['date']} — {d['label']}{marker}")
    print()

    # Clone/pull the unified repo
    tmp_dir = tempfile.mkdtemp(prefix='content-dashboards-')
    print(f"Working in: {tmp_dir}")
    repo_root = clone_or_pull_repo(tmp_dir)

    # Create niche subfolder
    niche_dir = repo_root / brand_short
    niche_dir.mkdir(parents=True, exist_ok=True)

    # Copy dashboard files
    for d in dashboards_to_copy:
        src = d['path']
        dst = niche_dir / f"{d['date']}.html"
        shutil.copy2(str(src), str(dst))
        print(f"  Copied {d['date']}.html")

    # Generate niche index (uses all dashboards present in the folder)
    all_niche_htmls = sorted(
        [f for f in niche_dir.iterdir() if f.suffix == '.html' and f.name != 'index.html'],
        key=lambda f: f.name,
        reverse=True
    )
    # Build dashboard list from what's in the folder (limited to MAX)
    niche_dashboards = []
    for hf in all_niche_htmls[:MAX_DASHBOARDS_PER_NICHE]:
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})\.html$', hf.name)
        if date_match:
            date_str = date_match.group(1)
            try:
                dt = datetime.strptime(date_str, '%Y-%m-%d')
                label = f"{DAYS[dt.weekday()]}, {MONTHS[dt.month - 1]} {dt.day}"
                niche_dashboards.append({'date': date_str, 'label': label})
            except ValueError:
                continue

    # Remove excess dashboards (keep only most recent MAX)
    if len(all_niche_htmls) > MAX_DASHBOARDS_PER_NICHE:
        for old_file in all_niche_htmls[MAX_DASHBOARDS_PER_NICHE:]:
            if old_file.name != 'index.html':
                old_file.unlink()
                print(f"  Pruned old dashboard: {old_file.name}")

    niche_index_html = generate_niche_index(brand_short, brand_name, niche_dashboards)
    (niche_dir / 'index.html').write_text(niche_index_html, encoding='utf-8')
    print(f"  Generated {brand_short}/index.html")

    # Update niches.json manifest (maps folder short name → full brand name)
    import json
    manifest_path = repo_root / 'niches.json'
    niche_manifest = {}
    if manifest_path.exists():
        try:
            niche_manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except Exception:
            pass
    niche_manifest[brand_short] = brand_name
    manifest_path.write_text(json.dumps(niche_manifest, indent=2, ensure_ascii=False), encoding='utf-8')

    # Generate root index
    root_index_html = generate_root_index(repo_root)
    (repo_root / 'index.html').write_text(root_index_html, encoding='utf-8')
    print("  Generated root index.html")

    # Ensure deploy infra
    ensure_deploy_infrastructure(repo_root)

    # Commit and push
    if specific_date:
        msg = f"Publish {brand_short} dashboard for {specific_date}"
    else:
        msg = f"Publish {brand_short} dashboards ({len(dashboards_to_copy)} files)"

    pushed = git_commit_and_push(repo_root, msg)

    # Setup Pages if needed
    if pushed:
        ensure_pages_workflow_mode()

    print(f"\nLive at: {GITHUB_PAGES_URL}")
    print(f"  Niche: {GITHUB_PAGES_URL}{brand_short}/")

    if pushed:
        verify_deploy()

    # Cleanup
    try:
        shutil.rmtree(tmp_dir, ignore_errors=True)
    except Exception:
        pass


if __name__ == '__main__':
    main()
