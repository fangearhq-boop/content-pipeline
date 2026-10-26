#!/usr/bin/env python3
"""Write Sooners/sooners-content-YYYY-MM-DD for the Chicago local date.

The folder name uses America/Chicago because sooners-x-bot does. The scheduled
workflow calls this at 7:05 AM America/Denver, which is 8:05 AM Chicago, before
the 9:00 AM CT slot.

    python Sooners/generate_daily.py --dry-run
    python Sooners/generate_daily.py --date 2026-10-26
"""

from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

NICHE = Path(__file__).resolve().parent
if str(NICHE) not in sys.path:
    sys.path.insert(0, str(NICHE))

from sooners_brief.contract import chicago_today, verify_brief, verify_day, x_length  # noqa: E402
from sooners_brief.generate import (  # noqa: E402
    build_drafts,
    day_paths,
    history_row,
    load_history,
    render_day,
)
from sooners_brief.sources import SourceFetchError, load_bundle  # noqa: E402


def parse_args():
    parser = argparse.ArgumentParser(description="Generate the Sooners daily X brief.")
    parser.add_argument("--date", help="America/Chicago date YYYY-MM-DD. Default: today in Chicago.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the brief and verdict. Do not write the niche folder or story history.",
    )
    return parser.parse_args()


def run(on_date, dry_run: bool, loader=None, niche_root: Path | None = None) -> int:
    loader = loader or load_bundle
    root = niche_root or NICHE
    folder, posts_path, fact_path = day_paths(root, on_date)
    if not dry_run and posts_path.is_file() and fact_path.is_file():
        existing = verify_day(folder)
        if existing.ok:
            print(f"already valid: {folder}")
            print(existing.summary())
            return 0

    history_path = root / "story-history.md"
    history = load_history(history_path.read_text(encoding="utf-8")) if history_path.is_file() else []
    try:
        bundle = loader(on_date)
    except SourceFetchError as exc:
        print(f"source fetch failed: {exc}", file=sys.stderr)
        return 1
    drafts = build_drafts(bundle, on_date, history)
    posts, facts = render_day(on_date, drafts)
    hold = verify_brief(posts, facts)

    print(f"date_chicago={on_date.isoformat()} folder={folder.name}")
    for draft in drafts:
        print(f"slot={draft.slot_ct} chars={x_length(draft.text)} url={draft.url} title={draft.title}")
    print(hold.summary())
    if not hold.ok:
        return 1

    if dry_run:
        print("\n----- 03-social-posts-x.md -----\n")
        print(posts)
        print("----- 06-fact-check-log.md -----\n")
        print(facts)
        print("dry-run: nothing written")
        return 0

    folder.mkdir(parents=True, exist_ok=True)
    posts_path.write_text(posts, encoding="utf-8")
    fact_path.write_text(facts, encoding="utf-8")
    written = verify_day(folder)
    if not written.ok:
        print(written.summary(), file=sys.stderr)
        return 1

    _append_history(history_path, on_date, drafts)
    _write_status(root, on_date, drafts)
    print(f"wrote {folder}")
    return 0


def main() -> int:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(name)s: %(message)s")
    args = parse_args()
    on_date = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else chicago_today()
    return run(on_date, args.dry_run)


def _append_history(path: Path, on_date, drafts) -> None:
    if not path.is_file():
        path.write_text(
            "# Sooners Story History\n\n"
            "| Date | Slot | URL | Title |\n"
            "|------|------|-----|-------|\n",
            encoding="utf-8",
        )
    rows = "".join(history_row(on_date, draft) + "\n" for draft in drafts if draft.url)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(rows)


def _write_status(root: Path, on_date, drafts) -> None:
    lines = [
        "# Sooners Pipeline Status",
        "",
        f"Last run: {on_date.isoformat()} (America/Chicago folder date)",
        "Steps: fetch allowlisted sources, write 03-social-posts-x.md and 06-fact-check-log.md, verify.",
        "Verdict: Acceptable for social",
        "",
        "| Slot | Title | URL |",
        "|------|-------|-----|",
    ]
    for draft in drafts:
        lines.append(f"| {draft.slot_ct} | {draft.title.replace('|', '/')} | {draft.url} |")
    lines.append("")
    (root / "pipeline-status.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
