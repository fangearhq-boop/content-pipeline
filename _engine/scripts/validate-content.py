#!/usr/bin/env python3
"""
FanGear HQ Content Format Validator

Validates that content files conform to the format contracts expected by
downstream pipeline scripts (PostPlanner export, review dashboard, etc.).

This is a FORMAT gate — it checks structure, not facts. Run this BEFORE
generate-review-dashboard.py and generate-postplanner-export.py.

Checks performed:
  1. X posts: code blocks exist, tweets ≤280 chars, no [CHARACTER COUNT] inside blocks
  2. Fact-check log: ## STORY N headings (H2 not H3), table format
  3. Facebook posts: code blocks exist, posting times extractable
  4. Daily brief: story count, tier assignments, posting windows
  5. Cross-file consistency: story counts match across all files

Usage:
    python validate-content.py --niche Softball 2026-03-06
    python validate-content.py --niche Cubs 2026-03-06
    python validate-content.py --niche Softball 2026-03-06 --fix  # auto-fix what it can
"""

import os
import re
import sys
import argparse
from pathlib import Path

# Fix Unicode output on Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def find_paths(niche_name, date_str):
    """Resolve niche folder and content folder paths."""
    engine_dir = Path(__file__).parent.parent  # _engine/
    niche_folder = engine_dir.parent / niche_name
    if not niche_folder.exists():
        # Case-insensitive fallback
        for entry in engine_dir.parent.iterdir():
            if entry.is_dir() and entry.name.lower() == niche_name.lower() and entry.name != '_engine':
                niche_folder = entry
                break

    if not niche_folder.exists():
        print(f"ERROR: Niche folder not found: {niche_name}")
        sys.exit(1)

    # Load content prefix from niche-config.yaml
    config_path = niche_folder / "niche-config.yaml"
    content_prefix = f"{niche_name.lower()}-content"
    platforms = []
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r'^content_prefix:\s*"?([^"#]+)"?\s*$', line.strip())
                if m:
                    content_prefix = m.group(1).strip()
                if line.strip().startswith("- ") and "x_twitter" in line:
                    platforms.append("x_twitter")
                if line.strip().startswith("- ") and "facebook" in line:
                    platforms.append("facebook")

    content_folder = niche_folder / f"{content_prefix}-{date_str}"
    return niche_folder, content_folder, platforms


def read_file(path):
    """Read file if it exists, return content or None."""
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

def validate_x_posts(content_folder, fix=False):
    """Validate X/Twitter posts format."""
    filepath = content_folder / "03-social-posts-x.md"
    issues = []
    warnings = []
    fixes_applied = []

    content = read_file(filepath)
    if content is None:
        return issues, warnings, fixes_applied  # File not present = not an error (platform may not be enabled)

    # Check 1: Story sections exist with ## STORY N: format
    story_headers = re.findall(r'^(#{2,4})\s+STORY\s+\d+:', content, re.MULTILINE)
    if not story_headers:
        issues.append("X POSTS: No ## STORY N: headers found")
    else:
        for h in story_headers:
            if h != "##":
                issues.append(f"X POSTS: Story header uses '{h}' (should be '##')")

    # Check 2: Code blocks exist around tweet content
    story_blocks = re.split(r'(?=## STORY\s+\d+:)', content)
    total_posts = 0
    posts_with_code_blocks = 0
    posts_without_code_blocks = 0

    for block in story_blocks:
        if not block.strip() or not re.match(r'## STORY', block.strip()):
            continue
        # Find post subsections
        post_sections = re.split(r'(?=#{3,4}\s+(?:Text|Image)\s+Post)', block)
        for section in post_sections:
            if not re.match(r'#{3,4}\s+(?:Text|Image)\s+Post', section.strip()):
                continue
            total_posts += 1
            if re.search(r'```\n.*?```', section, re.DOTALL):
                posts_with_code_blocks += 1
            else:
                posts_without_code_blocks += 1

    if posts_without_code_blocks > 0:
        issues.append(
            f"X POSTS: {posts_without_code_blocks}/{total_posts} posts missing code blocks (``` fences). "
            f"PostPlanner parser requires code blocks around tweet content."
        )

    # Check 3: Tweet character counts
    code_blocks = re.findall(r'```\n(.*?)```', content, re.DOTALL)
    for i, block_text in enumerate(code_blocks, 1):
        caption = block_text.strip()
        # Strip CHARACTER COUNT tags
        caption = re.sub(r'\n?\[(?:CHARACTER COUNT|CHAR(?:ACTER)? COUNT):.*?\]', '', caption, flags=re.IGNORECASE)
        caption = re.sub(r'\n?\[\d+/280\]', '', caption)
        caption = caption.strip()

        if not caption:
            continue

        char_count = len(caption)
        if char_count > 280:
            issues.append(
                f"X POSTS: Tweet #{i} is {char_count} chars (limit 280, over by {char_count - 280})"
            )

    # Check 4: [CHARACTER COUNT] tags inside code blocks (should not be there)
    for i, block_text in enumerate(code_blocks, 1):
        if re.search(r'\[CHARACTER COUNT:', block_text, re.IGNORECASE):
            if fix:
                fixes_applied.append(f"Removed [CHARACTER COUNT] tag from tweet #{i} code block")
            else:
                warnings.append(
                    f"X POSTS: Tweet #{i} has [CHARACTER COUNT] tag INSIDE code block — "
                    f"this inflates tweet length and will appear as tweet text. "
                    f"Run with --fix to auto-remove."
                )

    # Apply CHARACTER COUNT tag removal if fixing
    if fix and fixes_applied:
        content = re.sub(
            r'\n?\[CHARACTER COUNT:.*?\]',
            '',
            content,
            flags=re.IGNORECASE
        )

    # Check 5: Posting times extractable from headings
    time_pattern = re.compile(r'(\d{1,2}:\d{2}\s*[AP]M)\s+([A-Z]{2,3})')
    post_headings = re.findall(r'^#{3,4}\s+((?:Text|Image)\s+Post.*?)$', content, re.MULTILINE)
    posts_with_time = sum(1 for h in post_headings if time_pattern.search(h))
    posts_without_time = len(post_headings) - posts_with_time
    if posts_without_time > 0:
        issues.append(
            f"X POSTS: {posts_without_time}/{len(post_headings)} post headings missing posting time "
            f"(need format like '### Text Post — 9:00 AM ET')"
        )

    # Write fixes if any
    if fix and fixes_applied:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return issues, warnings, fixes_applied


def validate_fact_check_log(content_folder):
    """Validate fact-check log format."""
    filepath = content_folder / "06-fact-check-log.md"
    issues = []
    warnings = []

    content = read_file(filepath)
    if content is None:
        warnings.append("FACT-CHECK: 06-fact-check-log.md not found (Step 10 may not have run)")
        return issues, warnings

    # Check 1: Story headers use ## (H2), not ### (H3)
    h2_stories = re.findall(r'^##\s+STORY\s+\d+:', content, re.MULTILINE | re.IGNORECASE)
    h3_stories = re.findall(r'^###\s+STORY\s+\d+:', content, re.MULTILINE | re.IGNORECASE)

    if h3_stories and not h2_stories:
        issues.append(
            f"FACT-CHECK: All {len(h3_stories)} story headers use ### (H3) — "
            f"dashboard parser requires ## (H2). Change '### STORY' to '## STORY'."
        )
    elif h3_stories:
        issues.append(
            f"FACT-CHECK: {len(h3_stories)} story headers use ### (H3) mixed with {len(h2_stories)} using ## (H2). "
            f"All should use ## (H2)."
        )

    # Check 2: Table format exists with Status column
    tables = re.findall(r'^\|.*\|$', content, re.MULTILINE)
    if not tables:
        warnings.append("FACT-CHECK: No markdown tables found — expected claim verification tables")
    else:
        # Check for Status column
        has_status = any('Status' in row for row in tables)
        if not has_status:
            warnings.append("FACT-CHECK: No 'Status' column found in tables")

    return issues, warnings


def validate_facebook_posts(content_folder):
    """Validate Facebook posts format."""
    filepath = content_folder / "04-social-posts-facebook.md"
    issues = []
    warnings = []

    content = read_file(filepath)
    if content is None:
        return issues, warnings  # Not required for all niches

    # Check code blocks exist
    code_blocks = re.findall(r'```\n(.*?)```', content, re.DOTALL)
    post_headings = re.findall(r'^#{3,4}\s+(?:Long-Form|Image)\s+(?:Post|Caption)', content, re.MULTILINE)

    if post_headings and not code_blocks:
        issues.append(
            f"FACEBOOK: {len(post_headings)} posts found but 0 code blocks. "
            f"PostPlanner parser requires code blocks around post content."
        )
    elif len(code_blocks) < len(post_headings):
        warnings.append(
            f"FACEBOOK: {len(post_headings)} post headings but only {len(code_blocks)} code blocks"
        )

    return issues, warnings


def validate_daily_brief(content_folder):
    """Validate daily brief structure."""
    filepath = content_folder / "00-daily-brief.md"
    issues = []
    warnings = []

    content = read_file(filepath)
    if content is None:
        issues.append("DAILY BRIEF: 00-daily-brief.md not found")
        return issues, warnings, 0

    # Count stories
    story_headers = re.findall(r'^###\s+STORY\s+(\d+):', content, re.MULTILINE | re.IGNORECASE)
    story_count = len(story_headers)

    if story_count == 0:
        issues.append("DAILY BRIEF: No ### STORY N: headers found")

    # Check tier assignments
    tier_matches = re.findall(r'\*\*Tier:\*\*\s*(\d+)', content)
    if story_count > 0 and len(tier_matches) < story_count:
        warnings.append(
            f"DAILY BRIEF: Only {len(tier_matches)}/{story_count} stories have **Tier:** assignments"
        )

    # Check posting windows
    window_matches = re.findall(r'\*\*Posting Window:\*\*', content)
    if story_count > 0 and len(window_matches) < story_count:
        warnings.append(
            f"DAILY BRIEF: Only {len(window_matches)}/{story_count} stories have **Posting Window:**"
        )

    return issues, warnings, story_count


def validate_cross_consistency(content_folder, brief_story_count):
    """Check story counts match across files."""
    issues = []
    warnings = []

    files_to_check = {
        "X Posts (03)": "03-social-posts-x.md",
        "Facebook (04)": "04-social-posts-facebook.md",
        "Fact-Check (06)": "06-fact-check-log.md",
    }

    for label, filename in files_to_check.items():
        content = read_file(content_folder / filename)
        if content is None:
            continue

        # Count story sections
        story_headers = re.findall(r'^##\s+STORY\s+\d+:', content, re.MULTILINE | re.IGNORECASE)
        if not story_headers:
            # Try ### format too
            story_headers = re.findall(r'^###\s+STORY\s+\d+:', content, re.MULTILINE | re.IGNORECASE)

        if brief_story_count > 0 and len(story_headers) != brief_story_count:
            # Not necessarily an error — some files may have fewer stories by design
            # (e.g., fact-check may skip Story 7 "Weekend Preview")
            if len(story_headers) < brief_story_count - 1:
                warnings.append(
                    f"CONSISTENCY: {label} has {len(story_headers)} stories vs {brief_story_count} in daily brief"
                )

    return issues, warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Validate content file formats before export"
    )
    parser.add_argument(
        "--niche", required=True,
        help="Niche folder name (e.g., Cubs, Softball)"
    )
    parser.add_argument(
        "date", nargs="?", default=None,
        help="Date in YYYY-MM-DD format (defaults to today)"
    )
    parser.add_argument(
        "--fix", action="store_true",
        help="Auto-fix issues where possible (e.g., remove CHARACTER COUNT tags from code blocks)"
    )
    args = parser.parse_args()

    from datetime import datetime
    date_str = args.date or datetime.now().strftime("%Y-%m-%d")

    # Validate date format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"ERROR: Invalid date format '{date_str}'. Use YYYY-MM-DD")
        sys.exit(1)

    niche_folder, content_folder, platforms = find_paths(args.niche, date_str)

    if not content_folder.exists():
        print(f"ERROR: Content folder not found: {content_folder}")
        sys.exit(1)

    print(f"Validating content for: {args.niche}")
    print(f"  Date: {date_str}")
    print(f"  Folder: {content_folder.name}")
    if args.fix:
        print(f"  Mode: AUTO-FIX enabled")
    print()

    all_issues = []
    all_warnings = []
    all_fixes = []

    # 1. Daily brief
    issues, warnings, story_count = validate_daily_brief(content_folder)
    all_issues.extend(issues)
    all_warnings.extend(warnings)

    # 2. X/Twitter posts
    if not platforms or "x_twitter" in platforms:
        issues, warnings, fixes = validate_x_posts(content_folder, fix=args.fix)
        all_issues.extend(issues)
        all_warnings.extend(warnings)
        all_fixes.extend(fixes)

    # 3. Facebook posts
    if not platforms or "facebook" in platforms:
        issues, warnings = validate_facebook_posts(content_folder)
        all_issues.extend(issues)
        all_warnings.extend(warnings)

    # 4. Fact-check log
    issues, warnings = validate_fact_check_log(content_folder)
    all_issues.extend(issues)
    all_warnings.extend(warnings)

    # 5. Cross-file consistency
    issues, warnings = validate_cross_consistency(content_folder, story_count)
    all_issues.extend(issues)
    all_warnings.extend(warnings)

    # Report
    if all_fixes:
        print(f"🔧 Auto-fixed {len(all_fixes)} issue(s):")
        for fix in all_fixes:
            print(f"  ✓ {fix}")
        print()

    if all_issues:
        print(f"❌ {len(all_issues)} issue(s) found (will break downstream scripts):")
        for issue in all_issues:
            print(f"  • {issue}")
        print()

    if all_warnings:
        print(f"⚠ {len(all_warnings)} warning(s) (may indicate problems):")
        for warning in all_warnings:
            print(f"  • {warning}")
        print()

    if not all_issues and not all_warnings:
        print("✅ All format checks passed — content is ready for export.")
    elif not all_issues:
        print("✅ No blocking issues — safe to proceed with export (review warnings above).")
    else:
        print("❌ Fix the issues above before running PostPlanner export or dashboard generation.")
        sys.exit(1)


if __name__ == "__main__":
    main()
