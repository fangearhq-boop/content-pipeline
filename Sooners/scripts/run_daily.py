#!/usr/bin/env python3
"""Generate a Sooners day, then publish it through a pull request.

`generate` resolves the Chicago date from the environment, skips work when
main or an open pull request already has a valid folder, and writes the
folder only when this run must create or refresh the branch.

`publish` squash-merges that pull request. It does not push to main.

Environment (never interpolated into a shell command):

- EVENT_NAME, INPUT_DATE, INPUT_COMMIT on generate
- FOLDER_DATE, PUBLISH_ACTION on publish
"""

from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path

NICHE = Path(__file__).resolve().parents[1]
ROOT = NICHE.parent
if str(NICHE) not in sys.path:
    sys.path.insert(0, str(NICHE))

import generate_daily  # noqa: E402
from sooners_brief.contract import chicago_today  # noqa: E402
from sooners_brief.publish import (  # noqa: E402
    PUBLISH_ACTIONS,
    CommandFailed,
    decide_action,
    publish,
    require_date,
)


def resolve_request() -> tuple[str, bool]:
    raw = os.environ.get("INPUT_DATE", "")
    if raw:
        folder_date = require_date(raw)
    else:
        folder_date = chicago_today().isoformat()
    event = os.environ.get("EVENT_NAME", "")
    commit = os.environ.get("INPUT_COMMIT", "")
    write = event == "schedule" or commit == "true"
    return folder_date, write


def generate_phase(repo: Path, folder_date: str, write: bool, loader=None) -> tuple[int, str]:
    on_date = datetime.strptime(require_date(folder_date), "%Y-%m-%d").date()
    niche = repo / "Sooners"
    if not write:
        return generate_daily.run(on_date, True, loader=loader, niche_root=niche), "dry-run"
    action = decide_action(repo, folder_date)
    if action in ("create", "reuse"):
        code = generate_daily.run(on_date, False, loader=loader, niche_root=niche)
        if code != 0:
            return code, action
    return 0, action


def _emit(folder_date: str, action: str, should_publish: bool) -> None:
    print(f"day_action={action}")
    print(f"folder_date={folder_date}")
    print(f"publish={'true' if should_publish else 'false'}")
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        handle.write(f"folder_date={folder_date}\n")
        handle.write(f"action={action}\n")
        handle.write(f"publish={'true' if should_publish else 'false'}\n")


def main(argv: list[str] | None = None) -> int:
    phase = (argv if argv is not None else sys.argv[1:])[:1]
    phase = phase[0] if phase else "generate"
    try:
        if phase == "generate":
            folder_date, write = resolve_request()
            code, action = generate_phase(ROOT, folder_date, write)
            should_publish = code == 0 and write and action in PUBLISH_ACTIONS and action != "noop"
            _emit(folder_date, action, should_publish)
            return code
        if phase == "publish":
            folder_date = require_date(os.environ.get("FOLDER_DATE", ""))
            action = os.environ.get("PUBLISH_ACTION", "")
            if action not in PUBLISH_ACTIONS or action == "noop":
                print(f"publish skipped for action {action or '(missing)'}")
                return 0 if action == "noop" else 1
            taken = publish(ROOT, folder_date, action)
            print(f"publish_action={taken}")
            print(f"branch=sooners-daily/{folder_date}")
            return 0
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except (CommandFailed, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print("phase must be generate or publish", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
