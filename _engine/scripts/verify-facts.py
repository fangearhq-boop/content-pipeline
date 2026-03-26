#!/usr/bin/env python3
"""
FanGear HQ Universal Fact-Check & Consistency Checker

Works across all niches by loading niche-specific claim patterns dynamically.
Universal checks (consistency, character counts, dates/times) are built in.
Niche-specific claim extraction (scores, prices, stats, etc.) comes from each
niche's claim-patterns.py module.

Usage:
    python verify-facts.py --niche Softball 2026-02-22           # Both checks
    python verify-facts.py --niche Softball 2026-02-22 --facts   # Fact-check only
    python verify-facts.py --niche Softball 2026-02-22 --consistency  # Consistency only
    python verify-facts.py --niche Softball 2026-02-22 --images  # Image manifest only

    # Auto-detect niche from current directory:
    python verify-facts.py 2026-02-22
"""

import os
import re
import sys
import importlib.util
from datetime import datetime
from collections import OrderedDict, Counter

# Fix Unicode output on Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Path helpers
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


def find_content_folder(niche_root, content_prefix, date_str):
    """Locate the dated content folder."""
    content_folder = os.path.join(niche_root, f"{content_prefix}-{date_str}")
    if not os.path.isdir(content_folder):
        print(f"ERROR: Content folder not found: {content_folder}")
        sys.exit(1)
    return content_folder


def read_file_if_exists(path):
    """Read file contents or return empty string."""
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


# ---------------------------------------------------------------------------
# Niche claim pattern loading
# ---------------------------------------------------------------------------

def load_niche_claim_patterns(niche_root):
    """
    Dynamically load the niche's claim-patterns.py module.
    Returns the extract_niche_claims function, or None if not found.
    """
    patterns_path = os.path.join(niche_root, 'claim-patterns.py')
    if not os.path.isfile(patterns_path):
        print(f"WARNING: No claim-patterns.py found at {patterns_path}")
        print("  Only universal claim extraction will run.")
        return None

    spec = importlib.util.spec_from_file_location("niche_claims", patterns_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, 'extract_niche_claims'):
        return module.extract_niche_claims
    else:
        print(f"WARNING: claim-patterns.py missing extract_niche_claims() function")
        return None


def load_niche_priority_labels(niche_root):
    """Load niche-specific priority labels, with universal defaults."""
    labels = {1: 'HIGH', 2: 'MEDIUM', 3: 'LOW'}
    # Could parse from niche-config.yaml if needed
    return labels


# ---------------------------------------------------------------------------
# Story extraction from daily brief
# ---------------------------------------------------------------------------

def extract_stories_from_brief(brief_text):
    """
    Parse the daily brief to extract story numbers, titles, and tiers.
    Returns OrderedDict: {story_num: {'title': str, 'tier': int, 'text': str}}
    """
    stories = OrderedDict()
    pattern = r'^#{2,3}\s+STORY\s+(\d+):\s*(.+?)(?=^#{2,3}\s+STORY|\Z)'
    for match in re.finditer(pattern, brief_text, re.MULTILINE | re.DOTALL):
        num = match.group(1)
        full_block = match.group(2).strip()
        title_line = full_block.split('\n')[0].strip()

        # Extract tier
        tier = 3  # default
        tier_match = re.search(r'\*\*Tier:\*\*\s*(\d)', full_block)
        if tier_match:
            tier = int(tier_match.group(1))

        # Also check Priority field for tier inference
        if not tier_match:
            priority_match = re.search(r'\*\*Priority:\*\*\s*(\w+)', full_block)
            if priority_match:
                priority = priority_match.group(1).upper()
                if priority == 'CRITICAL':
                    tier = 1
                elif priority == 'HIGH':
                    tier = 2

        stories[num] = {
            'title': title_line,
            'tier': tier,
            'text': full_block
        }
    return stories


def extract_story_sections(content):
    """
    Split any content file into story-numbered sections.
    Returns dict: {story_num: section_text}
    Handles both "STORY N:" and "STORIES N+M:" headers.
    For combined headers like "STORIES 1+5:", section is keyed by the first number.
    """
    sections = {}
    # Match STORY or STORIES headers — the lookahead also matches STORIES
    pattern = r'^#{2,3}\s+STOR(?:Y|IES)\s+[\d+]*?(\d+)[\d+]*:\s*(.+?)(?=^#{2,3}\s+STOR(?:Y|IES)|\Z)'
    for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
        story_num = match.group(1)
        section_text = match.group(2).strip()
        if story_num in sections:
            # Append to existing section (e.g., Story 2 informative + Story 2 bold take)
            sections[story_num] += "\n\n" + section_text
        else:
            sections[story_num] = section_text
    return sections


# ---------------------------------------------------------------------------
# Universal claim extraction (applies to ALL niches)
# ---------------------------------------------------------------------------

def extract_universal_claims(text, claim_list, story_num):
    """
    Extract claims that are universal across all niches:
    - Times (HIGH)
    - Day-of-week claims (HIGH)
    - Date claims (HIGH)
    These are the most error-prone categories regardless of niche.
    """

    def get_context(match, radius=50):
        ctx = text[max(0, match.start() - radius):match.end() + radius].strip()
        return re.sub(r'\s+', ' ', ctx)

    # 1. TIMES: "N:NN PM ET" etc — HIGH PRIORITY (universal)
    for match in re.finditer(
        r'\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)\s*(?:ET|CT|MT|PT|EST|CST|MST|PST|MDT|EDT)?',
        text
    ):
        claim_list.append({
            'type': 'Time',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })

    # 2. DAY-OF-WEEK CLAIMS: "Monday", "Friday" etc — HIGH PRIORITY (universal)
    for match in re.finditer(
        r'(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)',
        text, re.IGNORECASE
    ):
        after = text[match.end():match.end() + 60]
        if re.search(r'(?:game|match|plays|faces|hosts|opens|starts|at\s+\d|event|,)',
                     after, re.IGNORECASE):
            claim_list.append({
                'type': 'Date',
                'value': match.group().strip(),
                'context': get_context(match, 40),
                'story': story_num,
                'priority': 1
            })

    # 3. "Month Day" patterns — HIGH PRIORITY (universal)
    for match in re.finditer(
        r'(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|'
        r'Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)'
        r'\.?\s+\d{1,2}(?:st|nd|rd|th)?',
        text, re.IGNORECASE
    ):
        claim_list.append({
            'type': 'Date',
            'value': match.group().strip(),
            'context': get_context(match, 40),
            'story': story_num,
            'priority': 1
        })


# ---------------------------------------------------------------------------
# Consistency check (universal)
# ---------------------------------------------------------------------------

def check_consistency(content_folder, brief_stories, config=None):
    """
    Verify every story in the daily brief has entries in downstream files.
    Respects niche config: skips Facebook/image/article checks when not applicable.
    Returns list of issue strings.
    """
    issues = []
    config = config or {}

    # Determine which platforms and features are active
    platforms = config.get('platforms', ['x_twitter', 'facebook'])
    if isinstance(platforms, str):
        platforms = [platforms]
    photo_source = config.get('photo_source', '')
    article_max = int(config.get('article_word_count_max', '9999'))

    files_to_check = {
        'Story Analysis (02)': '02-story-analysis.md',
        'X Posts (03)': '03-social-posts-x.md',
    }

    # Only check Facebook file if facebook is an active platform
    if 'facebook' in platforms:
        files_to_check['Facebook Posts (04)'] = '04-social-posts-facebook.md'

    # Only check image concepts if photo_source is not "none"
    if photo_source != 'none':
        files_to_check['Image Concepts (05)'] = '05-image-concepts.md'

    for label, filename in files_to_check.items():
        path = os.path.join(content_folder, filename)
        content = read_file_if_exists(path)
        if not content:
            issues.append(f"MISSING FILE: {filename} does not exist")
            continue

        file_stories = extract_story_sections(content)

        for story_num, story_info in brief_stories.items():
            if story_num not in file_stories:
                issues.append(
                    f"MISSING STORY: Story {story_num} ({story_info['title'][:40]}...) "
                    f"not found in {filename}"
                )

    # Check articles folder — only if articles are expected (word count > 0)
    if article_max > 0:
        articles_dir = os.path.join(content_folder, 'articles')
        article_files = []
        if os.path.isdir(articles_dir):
            article_files = [f for f in os.listdir(articles_dir) if f.endswith('.html')]

        for story_num, story_info in brief_stories.items():
            if story_info['tier'] <= 2:
                has_article = any(f'article-{story_num.zfill(2)}' in f for f in article_files)
                if not has_article:
                    issues.append(
                        f"MISSING ARTICLE: Tier {story_info['tier']} Story {story_num} "
                        f"({story_info['title'][:40]}...) has no article in articles/"
                    )

    # Check X posts for character count issues — check EVERY code block tweet
    x_content = read_file_if_exists(os.path.join(content_folder, '03-social-posts-x.md'))
    if x_content:
        # Find all code blocks in the entire X posts file
        tweet_pattern = re.compile(
            r'(?:^#{2,4}\s+.*?Post.*?$)(.*?)```\n?(.*?)\n?```',
            re.MULTILINE | re.DOTALL
        )
        # Simpler approach: split by story headers, then find ALL code blocks in each
        x_stories = extract_story_sections(x_content)
        tweet_num = 0
        for story_num, section in x_stories.items():
            # Find ALL code blocks in this story section (not just the first)
            code_blocks = re.findall(r'```\n?(.*?)\n?```', section, re.DOTALL)
            for block_idx, post_text in enumerate(code_blocks, 1):
                tweet_num += 1
                post_text = post_text.strip()
                if not post_text:
                    continue

                # Remove markdown formatting for count
                clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', post_text)
                clean = re.sub(r'https?://\S+', '                       ', clean)  # URLs = 23 chars
                # Remove annotations (various formats)
                clean = re.sub(r'_Character count:.*?_', '', clean)
                clean = re.sub(r'\[CHARACTER COUNT:.*?\]', '', clean, flags=re.IGNORECASE)
                clean = re.sub(r'\[CHAR COUNT:.*?\]', '', clean, flags=re.IGNORECASE)
                clean = re.sub(r'\[\d+/280\]', '', clean)
                clean = re.sub(r'\[POSTING WINDOW:.*?\]', '', clean)
                char_count = len(clean.strip())

                if char_count > 280:
                    issues.append(
                        f"CHAR LIMIT: Story {story_num} tweet #{block_idx} is {char_count} chars "
                        f"(limit 280)"
                    )

                # Check if the embedded [CHARACTER COUNT] tag matches reality
                tag_match = re.search(r'\[CHARACTER COUNT:\s*(\d+)/280\]', post_text, re.IGNORECASE)
                if tag_match:
                    tagged_count = int(tag_match.group(1))
                    if abs(tagged_count - char_count) > 2:  # Allow 2-char tolerance
                        issues.append(
                            f"CHAR MISMATCH: Story {story_num} tweet #{block_idx} tag says "
                            f"{tagged_count}/280 but actual count is {char_count}/280"
                        )

    return issues


# ---------------------------------------------------------------------------
# Image manifest check (universal)
# ---------------------------------------------------------------------------

def check_image_manifest(content_folder, brief_stories):
    """
    Check if 07-image-manifest.md exists and report image production status.
    """
    manifest_path = os.path.join(content_folder, '07-image-manifest.md')
    issues = []
    summary = {'exported': 0, 'in_progress': 0, 'not_started': 0, 'total': 0}

    if not os.path.isfile(manifest_path):
        issues.append("IMAGE MANIFEST: 07-image-manifest.md not found")
        return issues, summary

    content = read_file_if_exists(manifest_path)
    if not content:
        issues.append("IMAGE MANIFEST: 07-image-manifest.md is empty")
        return issues, summary

    current_story = None
    current_platform = None
    statuses = {}

    for line in content.split('\n'):
        story_match = re.match(r'^\s+"(\d+)":\s*$', line)
        if story_match:
            current_story = story_match.group(1)
            current_platform = None
            if current_story not in statuses:
                statuses[current_story] = {}
            continue

        if current_story:
            platform_match = re.match(r'^\s+(x_image|facebook_image):\s*$', line)
            if platform_match:
                current_platform = platform_match.group(1)
                continue

            if current_platform:
                status_match = re.match(r'^\s+status:\s+(\S+)', line)
                if status_match:
                    statuses[current_story][current_platform] = status_match.group(1)
                    continue

    for story_num, story_info in brief_stories.items():
        tier = story_info['tier']
        story_statuses = statuses.get(story_num, {})

        if not story_statuses and tier <= 2:
            issues.append(
                f"IMAGE MISSING: Tier {tier} Story {story_num} "
                f"({story_info['title'][:40]}...) has no image entries in manifest"
            )
            summary['not_started'] += 2
            summary['total'] += 2
            continue

        for platform in ['x_image', 'facebook_image']:
            status = story_statuses.get(platform, 'not_started')
            summary['total'] += 1

            if status == 'exported':
                summary['exported'] += 1
            elif status == 'not_started':
                summary['not_started'] += 1
                if tier <= 2:
                    issues.append(
                        f"IMAGE NOT STARTED: Tier {tier} Story {story_num} "
                        f"{platform} still not_started"
                    )
            else:
                summary['in_progress'] += 1

    return issues, summary


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def generate_fact_check_log(display_date, brand_name, brief_stories, all_claims,
                            consistency_issues, priority_labels):
    """Generate the fact-check log markdown, grouped by story."""

    # Deduplicate claims within each story
    deduped = []
    seen = set()
    for claim in all_claims:
        key = (claim['story'], claim['type'], claim['value'])
        if key not in seen:
            seen.add(key)
            deduped.append(claim)

    deduped.sort(key=lambda c: (c['story'], c['priority'], c['type']))

    lines = [
        f"# Fact-Check Log — {brand_name} — {display_date}",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Claims extracted:** {len(deduped)}",
        "",
        "## Verification Priority Guide",
        "",
    ]

    for pri in sorted(priority_labels):
        lines.append(f"- **{priority_labels[pri]} (Priority {pri}):** {priority_labels.get(f'{pri}_desc', '')}")

    lines.extend(["", "---", ""])

    if consistency_issues:
        lines.append("## Consistency Issues")
        lines.append("")
        for issue in consistency_issues:
            lines.append(f"- {issue}")
        lines.extend(["", "---", ""])

    for story_num, story_info in brief_stories.items():
        story_claims = [c for c in deduped if c['story'] == story_num]
        if not story_claims:
            continue

        title = story_info['title'][:60]
        tier = story_info['tier']
        high_count = sum(1 for c in story_claims if c['priority'] == 1)

        lines.append(f"## Story {story_num}: {title}")
        lines.append(f"**Tier {tier}** | **{len(story_claims)} claims** | "
                      f"**{high_count} high-priority**")
        lines.append("")
        lines.append("| Priority | Type | Claim | Context | Source | Result | Notes |")
        lines.append("|----------|------|-------|---------|--------|--------|-------|")

        for claim in story_claims:
            pri = priority_labels.get(claim['priority'], '?')
            ctx = claim['context'][:55].replace('|', '\\|').replace('\n', ' ')
            val = claim['value'][:40].replace('|', '\\|')
            lines.append(f"| {pri} | {claim['type']} | {val} | {ctx} | | | |")

        lines.extend(["", "### Corrections Applied", "- (none yet)", "", "---", ""])

    return "\n".join(lines), len(deduped)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Parse arguments
    args = sys.argv[1:]
    niche_name = None
    date_str = None
    mode = 'both'

    i = 0
    while i < len(args):
        if args[i] == '--niche' and i + 1 < len(args):
            niche_name = args[i + 1]
            i += 2
        elif args[i] == '--facts':
            mode = 'facts'
            i += 1
        elif args[i] == '--consistency':
            mode = 'consistency'
            i += 1
        elif args[i] == '--images':
            mode = 'images'
            i += 1
        elif not date_str and re.match(r'\d{4}-\d{2}-\d{2}', args[i]):
            date_str = args[i]
            i += 1
        else:
            i += 1

    if not date_str:
        print("Usage: python verify-facts.py --niche <name> YYYY-MM-DD [--facts|--consistency|--images]")
        sys.exit(1)

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print(f"ERROR: Invalid date format '{date_str}'. Use YYYY-MM-DD.")
        sys.exit(1)

    # Find niche and load config
    niche_root = find_niche_root(niche_name)
    config = load_niche_config(niche_root)
    content_prefix = config.get('content_prefix', os.path.basename(niche_root).lower() + '-content')
    brand_name = config.get('brand_name', os.path.basename(niche_root))

    print(f"Niche: {brand_name}")
    print(f"Content prefix: {content_prefix}")
    print(f"Date: {date_str}")

    content_folder = find_content_folder(niche_root, content_prefix, date_str)
    display_date = date_obj.strftime('%B %d, %Y')

    # Load niche claim patterns
    niche_claim_fn = load_niche_claim_patterns(niche_root)
    priority_labels = load_niche_priority_labels(niche_root)

    # Always parse the daily brief for story structure
    brief = read_file_if_exists(os.path.join(content_folder, '00-daily-brief.md'))
    if not brief:
        print("ERROR: 00-daily-brief.md not found")
        sys.exit(1)

    brief_stories = extract_stories_from_brief(brief)
    print(f"Found {len(brief_stories)} stories in daily brief")

    # --- Consistency check ---
    consistency_issues = []
    if mode in ('both', 'consistency'):
        consistency_issues = check_consistency(content_folder, brief_stories, config)
        if consistency_issues:
            print(f"\n⚠ CONSISTENCY ISSUES ({len(consistency_issues)}):")
            for issue in consistency_issues:
                print(f"  - {issue}")
        else:
            print("✓ All stories present in all content files")

    # --- Fact extraction ---
    all_claims = []
    if mode in ('both', 'facts'):
        content_files = {
            '00-daily-brief.md': brief,
            '01-research-notes.md': read_file_if_exists(
                os.path.join(content_folder, '01-research-notes.md')),
            '02-story-analysis.md': read_file_if_exists(
                os.path.join(content_folder, '02-story-analysis.md')),
            '03-social-posts-x.md': read_file_if_exists(
                os.path.join(content_folder, '03-social-posts-x.md')),
            '04-social-posts-facebook.md': read_file_if_exists(
                os.path.join(content_folder, '04-social-posts-facebook.md')),
        }

        articles_dir = os.path.join(content_folder, 'articles')
        if os.path.isdir(articles_dir):
            for fname in sorted(os.listdir(articles_dir)):
                if fname.endswith('.html'):
                    content_files[f'articles/{fname}'] = read_file_if_exists(
                        os.path.join(articles_dir, fname))

        for filename, content in content_files.items():
            if not content:
                continue
            story_sections = extract_story_sections(content)
            for story_num, section_text in story_sections.items():
                if story_num in brief_stories:
                    # Universal claims (dates, times)
                    extract_universal_claims(section_text, all_claims, story_num)
                    # Niche-specific claims
                    if niche_claim_fn:
                        niche_claim_fn(section_text, all_claims, story_num)

            # Also extract from header area
            header = content.split('## STORY')[0] if '## STORY' in content else ''
            if header:
                extract_universal_claims(header, all_claims, '0')
                if niche_claim_fn:
                    niche_claim_fn(header, all_claims, '0')

        # Generate the log
        log_content, claim_count = generate_fact_check_log(
            display_date, brand_name, brief_stories, all_claims,
            consistency_issues, priority_labels
        )

        output_path = os.path.join(content_folder, '06-fact-check-log.md')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(log_content)

        print(f"\n✓ Fact-check log written to: {output_path}")
        print(f"  Total claims: {claim_count}")

        pri_counts = Counter(c['priority'] for c in all_claims)
        for pri in sorted(pri_counts):
            print(f"  {priority_labels.get(pri, '?')}: {pri_counts[pri]}")

    # --- Image manifest check ---
    if mode in ('both', 'images'):
        image_issues, image_summary = check_image_manifest(content_folder, brief_stories)
        if image_issues:
            print(f"\n⚠ IMAGE ISSUES ({len(image_issues)}):")
            for issue in image_issues:
                print(f"  - {issue}")
        else:
            print("✓ All image entries look good")

        total = image_summary['total']
        if total > 0:
            print(f"\n  Image production summary:")
            print(f"    Exported:    {image_summary['exported']}/{total}")
            print(f"    In progress: {image_summary['in_progress']}/{total}")
            print(f"    Not started: {image_summary['not_started']}/{total}")
        elif mode == 'images':
            print("  No image manifest found — run Step 11 to create one")

    # Write consistency-only report if needed
    if mode == 'consistency' and consistency_issues:
        output_path = os.path.join(content_folder, '06-fact-check-log.md')
        existing = read_file_if_exists(output_path)
        if not existing:
            lines = [
                f"# Fact-Check Log — {brand_name} — {display_date}",
                "",
                "## Consistency Issues",
                "",
            ]
            for issue in consistency_issues:
                lines.append(f"- {issue}")
            lines.append("")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(lines))
            print(f"\n✓ Consistency report written to: {output_path}")


if __name__ == "__main__":
    main()
