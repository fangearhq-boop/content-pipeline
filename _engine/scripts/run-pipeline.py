#!/usr/bin/env python3
"""
FanGear HQ Pipeline Runner

Runs the post-content-generation pipeline steps in sequence:
  1. validate-content.py   — format gate (blocks on errors)
  2. generate-review-dashboard.py — HTML review dashboard
  3. generate-postplanner-export.py — PostPlanner XLSX
  4. publish-dashboard.py  — push dashboard to GitHub Pages

Uses the same Python interpreter for all steps (no "which python?" issues).
Stops on first failure so you don't publish broken content.

Usage:
    python run-pipeline.py --niche Softball 2026-03-06
    python run-pipeline.py --niche Cubs 2026-03-06
    python run-pipeline.py --niche Softball 2026-03-06 --fix        # auto-fix validation issues
    python run-pipeline.py --niche Softball 2026-03-06 --skip-publish  # skip GitHub push
    python run-pipeline.py --niche Cubs 2026-03-06 --tobi           # enable TOBI for PostPlanner
"""

import os
import sys
import argparse
import subprocess
import time
from datetime import datetime
from pathlib import Path

# Fix Unicode output on Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


SCRIPTS_DIR = Path(__file__).parent


def run_script(script_name, args_list):
    """Run a sibling script as a subprocess using the same Python interpreter."""
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        print(f"  ERROR: Script not found: {script_path}")
        return False

    cmd = [sys.executable, str(script_path)] + args_list
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    result = subprocess.run(cmd, env=env)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(
        description="Run the full post-content pipeline (validate -> dashboard -> export -> publish)"
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
        help="Pass --fix to validate-content.py (auto-fix what it can)"
    )
    parser.add_argument(
        "--skip-publish", action="store_true",
        help="Skip the publish-dashboard step (useful for local testing)"
    )
    parser.add_argument(
        "--tobi", action="store_true",
        help="Pass --tobi to generate-postplanner-export.py"
    )
    args = parser.parse_args()

    date_str = args.date or datetime.now().strftime("%Y-%m-%d")

    # Validate date format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"ERROR: Invalid date format '{date_str}'. Use YYYY-MM-DD")
        sys.exit(1)

    print("=" * 60)
    print(f"  FanGear HQ Pipeline -- {args.niche} {date_str}")
    print("=" * 60)
    print()

    steps = []

    # Step 1: Validate content format
    validate_args = ["--niche", args.niche, date_str]
    if args.fix:
        validate_args.append("--fix")
    steps.append(("validate-content.py", validate_args, "Format Validation"))

    # Step 2: Generate review dashboard
    steps.append(("generate-review-dashboard.py", ["--niche", args.niche, date_str], "Review Dashboard"))

    # Step 3: Generate PostPlanner export
    export_args = ["--niche", args.niche, date_str]
    if args.tobi:
        export_args.append("--tobi")
    steps.append(("generate-postplanner-export.py", export_args, "PostPlanner Export"))

    # Step 4: Publish dashboard (optional)
    if not args.skip_publish:
        steps.append(("publish-dashboard.py", ["--niche", args.niche, date_str], "Publish Dashboard"))

    total = len(steps)
    start_time = time.time()

    for i, (script, script_args, label) in enumerate(steps, 1):
        step_start = time.time()
        print(f"[{i}/{total}] {label}")
        print("-" * 40)

        success = run_script(script, script_args)
        elapsed = time.time() - step_start

        print()
        if not success:
            print(f"FAILED at step {i}/{total}: {label} ({elapsed:.1f}s)")
            print(f"Fix the issues above and re-run.")
            sys.exit(1)
        else:
            print(f"  OK ({elapsed:.1f}s)")
            print()

    total_elapsed = time.time() - start_time
    print("=" * 60)
    print(f"  Pipeline complete -- {total} steps in {total_elapsed:.1f}s")
    print("=" * 60)


if __name__ == "__main__":
    main()
