#!/usr/bin/env python3
"""Decide whether the Sooners schedule job should write a day folder.

Hours 07 and 08 America/Denver proceed. Any other scheduled hour skips.
A manual run is not hour-gated. The generator itself no-ops when that
Chicago folder is already valid, so a second hit inside the window does
not write again.
"""

from __future__ import annotations

import sys

PROCEED_HOURS = frozenset({"07", "08"})


def scheduled_hour_action(hour: str, event_name: str = "schedule") -> str:
    if event_name != "schedule":
        return "proceed"
    if hour in PROCEED_HOURS:
        return "proceed"
    return "skip"


def main() -> int:
    hour = sys.argv[1] if len(sys.argv) > 1 else ""
    event_name = sys.argv[2] if len(sys.argv) > 2 else "schedule"
    print(scheduled_hour_action(hour, event_name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
