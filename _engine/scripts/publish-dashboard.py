#!/usr/bin/env python3
"""
FanGear HQ Universal Dashboard Publisher

Works across all niches by loading niche-specific configuration dynamically.
Scans for all dated-content folders, regenerates index.html with discovered dates,
then git adds, commits, and pushes.

Usage:
    python publish-dashboard.py --niche Softball              # publish all dashboards for softball
    python publish-dashboard.py --niche Softball 2026-02-19   # publish only this date
    python publish-dashboard.py --niche Parenting             # publish all dashboards for parenting
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

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


# Day-of-week and month names for display
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


def discover_dashboards(niche_root, content_prefix, max_days=5):
    """Find all dated folders that contain a review-dashboard.html.

    Only returns the most recent `max_days` dashboards to keep the index
    page lightweight. Older dashboards remain on disk but are not linked.
    """
    dashboards = []
    for item in sorted(Path(niche_root).iterdir(), reverse=True):
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
                        })
                    except ValueError:
                        continue
    # Sort newest first, then limit to max_days
    dashboards.sort(key=lambda d: d['date'], reverse=True)
    if len(dashboards) > max_days:
        print(f"  Limiting index to {max_days} most recent dashboards ({len(dashboards)} found)")
    return dashboards[:max_days]


def generate_index(niche_root, dashboards, brand_name, content_prefix):
    """Generate index.html from discovered dashboards."""

    # Build the JS array entries
    js_entries = []
    for i, d in enumerate(dashboards):
        tag = 'latest' if i == 0 else ''
        js_entries.append(
            f"  {{ date: '{d['date']}', label: '{d['label']}', tag: '{tag}' }}"
        )
    js_array = ',\n'.join(js_entries)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{brand_name} — Content Review</title>
<style>
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
    font-size: 2.4rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
  }}
  .header p {{
    font-size: 0.95rem;
    opacity: 0.9;
  }}
  .container {{
    max-width: 700px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
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
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;600;700&display=swap');
</style>
</head>
<body>

<div class="header">
  <h1>{brand_name}</h1>
  <p>Daily Content Review Dashboards</p>
</div>

<div class="container" id="dashboard-list">
  <div class="empty">Loading dashboards...</div>
</div>

<script>
const dashboards = [
{js_array}
];

function render() {{
  const container = document.getElementById('dashboard-list');

  if (dashboards.length === 0) {{
    container.innerHTML = '<div class="empty">No dashboards yet. Run the content pipeline to generate one.</div>';
    return;
  }}

  container.innerHTML = dashboards.map(d => {{
    const folder = '{content_prefix}-' + d.date;
    const href = folder + '/review-dashboard.html';
    const badge = d.tag ? `<span class="badge">${{d.tag}}</span>` : '';
    return `
      <a class="date-card" href="${{href}}">
        <div class="date-info">
          <h2>${{d.label}}${{badge}}</h2>
          <span>${{d.date}}</span>
        </div>
        <div class="arrow">&rarr;</div>
      </a>
    `;
  }}).join('');
}}

render();
</script>

</body>
</html>"""

    index_path = Path(niche_root) / 'index.html'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ index.html updated with {len(dashboards)} dashboard(s)")
    return index_path


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


def ensure_deploy_infrastructure(niche_root):
    """Ensure .nojekyll and deploy workflow exist — prevents Jekyll build failures."""
    changed = False

    # .nojekyll
    nojekyll = Path(niche_root) / '.nojekyll'
    if not nojekyll.exists():
        nojekyll.touch()
        subprocess.run(['git', 'add', '.nojekyll'], capture_output=True, cwd=niche_root)
        print("  + Created .nojekyll (bypasses Jekyll)")
        changed = True

    # GitHub Actions deploy workflow
    workflow_dir = Path(niche_root) / '.github' / 'workflows'
    workflow_file = workflow_dir / 'deploy-pages.yml'
    if not workflow_file.exists():
        workflow_dir.mkdir(parents=True, exist_ok=True)
        workflow_file.write_text(DEPLOY_WORKFLOW_YAML)
        subprocess.run(
            ['git', 'add', '.github/workflows/deploy-pages.yml'],
            capture_output=True, cwd=niche_root
        )
        print("  + Created .github/workflows/deploy-pages.yml")
        changed = True

    return changed


def ensure_pages_workflow_mode(config):
    """Check if GitHub Pages is using workflow mode; switch if on legacy.

    Requires `gh` CLI to be installed and authenticated.
    """
    github_pages_url = config.get('github_pages_url', '')
    if not github_pages_url:
        return

    # Extract org/repo from URL like https://fangearhq-boop.github.io/ilovesoftball-dashboards/
    match = re.match(r'https://([^.]+)\.github\.io/([^/]+)', github_pages_url)
    if not match:
        return

    org, repo = match.group(1), match.group(2)
    full_repo = f"{org}/{repo}"

    try:
        result = subprocess.run(
            ['gh', 'api', f'repos/{full_repo}/pages', '--jq', '.build_type'],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            return  # gh not available or repo not found — non-fatal

        build_type = result.stdout.strip()
        if build_type == 'legacy':
            print(f"  ⚠ Pages using legacy Jekyll builder — switching to workflow mode...")
            subprocess.run(
                ['gh', 'api', '-X', 'PUT', f'repos/{full_repo}/pages',
                 '-f', 'build_type=workflow'],
                capture_output=True, text=True, timeout=10
            )
            print("  ✓ Switched to GitHub Actions deployment")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass  # gh CLI not available — non-fatal


def verify_deploy(config, expected_date=None, max_wait=90):
    """Wait for GitHub Pages to deploy and verify the site has the expected content.

    Returns True if verified, False if timed out or failed.
    """
    github_pages_url = config.get('github_pages_url', '')
    if not github_pages_url:
        return True  # No URL to verify

    match = re.match(r'https://([^.]+)\.github\.io/([^/]+)', github_pages_url)
    if not match:
        return True

    org, repo = match.group(1), match.group(2)
    full_repo = f"{org}/{repo}"

    print(f"\n⏳ Verifying deployment...")

    start = time.time()
    while time.time() - start < max_wait:
        try:
            result = subprocess.run(
                ['gh', 'api', f'repos/{full_repo}/pages/builds', '--jq', '.[0].status'],
                capture_output=True, text=True, timeout=10
            )
            status = result.stdout.strip()
            if status == 'built':
                # If we have an expected date, verify it appears in index.html
                if expected_date:
                    try:
                        curl_result = subprocess.run(
                            ['curl', '-sf', f'{github_pages_url}index.html'],
                            capture_output=True, text=True, timeout=10
                        )
                        if expected_date in curl_result.stdout:
                            print(f"✓ Deployed and verified — {expected_date} is live")
                            return True
                        else:
                            # Built but CDN cache may be stale — give it a moment
                            time.sleep(5)
                            continue
                    except (FileNotFoundError, subprocess.TimeoutExpired):
                        print(f"✓ Build succeeded (could not verify content via curl)")
                        return True
                else:
                    print(f"✓ Build succeeded")
                    return True
            elif status == 'errored':
                print(f"✗ Build errored — may need manual intervention")
                print(f"  Try: gh api -X POST repos/{full_repo}/pages/builds")
                return False
        except (FileNotFoundError, subprocess.TimeoutExpired):
            break  # gh not available

        time.sleep(10)

    elapsed = int(time.time() - start)
    print(f"⚠ Deploy verification timed out after {elapsed}s — check manually")
    print(f"  URL: {github_pages_url}")
    return False


def git_sync_remote():
    """Fetch and merge remote main before committing to avoid push rejections.

    Dashboard repos get pushed from multiple sessions/worktrees. Without
    syncing first, the local branch falls behind and git push fails.
    """
    # Fetch latest from remote
    result = subprocess.run(
        ['git', 'fetch', 'origin', 'main'],
        capture_output=True, text=True, timeout=15
    )
    if result.returncode != 0:
        print(f"⚠ git fetch failed: {result.stderr.strip()}")
        return  # Non-fatal — push may still work if already up-to-date

    # Check if local is behind remote
    behind = subprocess.run(
        ['git', 'rev-list', '--count', 'HEAD..origin/main'],
        capture_output=True, text=True
    )
    if behind.returncode != 0 or behind.stdout.strip() == '0':
        return  # Already up-to-date

    commits_behind = behind.stdout.strip()
    print(f"  ↓ Pulling {commits_behind} commit(s) from remote...")

    # Stash any uncommitted changes (story-history.md etc)
    stash_result = subprocess.run(
        ['git', 'stash', '--include-untracked', '--quiet'],
        capture_output=True, text=True
    )
    stashed = stash_result.returncode == 0

    # Merge remote (prefer theirs for index.html since we regenerate it)
    merge = subprocess.run(
        ['git', 'merge', 'origin/main', '--no-edit', '-X', 'theirs'],
        capture_output=True, text=True
    )
    if merge.returncode != 0:
        # If merge fails, reset to remote — dashboard files are regenerated anyway
        print("  ⚠ Merge conflict — resetting to remote (dashboards will be re-added)")
        subprocess.run(['git', 'merge', '--abort'], capture_output=True)
        subprocess.run(['git', 'reset', '--hard', 'origin/main'], capture_output=True)

    # Restore stashed changes
    if stashed:
        subprocess.run(
            ['git', 'stash', 'pop', '--quiet'],
            capture_output=True, text=True
        )

    print("  ✓ Synced with remote")


def git_publish(niche_root, content_prefix, config, specific_date=None):
    """Stage dashboard files, commit, and push."""
    os.chdir(niche_root)

    # Sync with remote first to prevent push rejections
    git_sync_remote()

    # Ensure deploy infrastructure exists (.nojekyll, workflow)
    ensure_deploy_infrastructure(niche_root)

    # Always stage index.html
    files_to_add = ['index.html']

    if specific_date:
        # Only add the specific date's dashboard
        dashboard_path = f'{content_prefix}-{specific_date}/review-dashboard.html'
        if os.path.exists(dashboard_path):
            files_to_add.append(dashboard_path)
        else:
            print(f"⚠ No dashboard found for {specific_date}")
    else:
        # Add all dashboards
        for item in Path(niche_root).iterdir():
            if item.is_dir() and item.name.startswith(content_prefix + '-'):
                dashboard = item / 'review-dashboard.html'
                if dashboard.exists():
                    files_to_add.append(str(dashboard.relative_to(niche_root)))

    # Git add
    for f in files_to_add:
        subprocess.run(['git', 'add', f], check=True, capture_output=True)

    # Check if there are changes to commit
    result = subprocess.run(['git', 'diff', '--cached', '--quiet'], capture_output=True)
    if result.returncode == 0:
        print("ℹ No changes to commit — dashboards are already up to date")
        return False

    # Commit
    if specific_date:
        msg = f"Publish {specific_date} review dashboard"
    else:
        msg = f"Publish review dashboards (updated {datetime.now().strftime('%Y-%m-%d %H:%M')})"

    subprocess.run(
        ['git', 'commit', '-m', msg],
        check=True, capture_output=True
    )
    print(f"✓ Committed: {msg}")

    # Push
    try:
        result = subprocess.run(
            ['git', 'push', 'origin', 'main'],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print("✓ Pushed to GitHub — site will update in ~60 seconds")
            return True
        else:
            print(f"⚠ Push failed: {result.stderr.strip()}")
            print("  Run 'git push origin main' manually to publish")
            return False
    except subprocess.TimeoutExpired:
        print("⚠ Push timed out — run 'git push origin main' manually")
        return False


def main():
    # Parse arguments
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
        print("Usage: python publish-dashboard.py --niche <name> [YYYY-MM-DD]")
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
    content_prefix = config.get('content_prefix', os.path.basename(niche_root).lower() + '-content')
    brand_name = config.get('brand_name', os.path.basename(niche_root))
    github_pages_url = config.get('github_pages_url', '')

    print(f"🔍 Scanning for dashboards...")
    print(f"  Niche: {brand_name}")
    print(f"  Prefix: {content_prefix}")
    print()

    dashboards = discover_dashboards(niche_root, content_prefix)

    if not dashboards:
        print("⚠ No dashboards found. Run the content pipeline first.")
        sys.exit(1)

    for d in dashboards:
        print(f"  • {d['date']} — {d['label']}")

    print()

    # Pre-flight: ensure Pages is on workflow mode (not legacy Jekyll)
    ensure_pages_workflow_mode(config)

    generate_index(niche_root, dashboards, brand_name, content_prefix)
    pushed = git_publish(niche_root, content_prefix, config, specific_date)

    # Print the URL
    if github_pages_url:
        print(f"\n🌐 Live at: {github_pages_url}")

    # Verify deployment if we pushed
    if pushed:
        verify_deploy(config, expected_date=specific_date)


if __name__ == '__main__':
    main()
