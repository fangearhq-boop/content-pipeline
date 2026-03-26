#!/usr/bin/env python3
"""
Universal correction application script.

Usage:
    python apply_corrections.py --entries /tmp/entries.py --var all_entries \
        --corrections /tmp/corrections.py --cor-var corrections \
        --output /tmp/corrected.py --out-var corrected_entries \
        [--date-anchored]

The --date-anchored flag enables detection of corrections that move entries
off their assigned calendar dates (for On This Day content). These get
converted to removals automatically.
"""

import sys
import argparse
from collections import Counter


def load_python_var(filepath, varname):
    """Load a Python variable from a .py file."""
    namespace = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        exec(f.read(), namespace)
    if varname not in namespace:
        print(f"ERROR: Variable '{varname}' not found in {filepath}")
        print(f"  Available: {[k for k in namespace if not k.startswith('_')]}")
        sys.exit(1)
    return namespace[varname]


def apply_corrections(entries, corrections, date_anchored=False):
    """
    Apply corrections to entries list. Returns (corrected_entries, report).

    If date_anchored=True, corrections that change month/day fields are
    converted to removals (since the entry exists for a specific calendar slot).
    """
    removals = set()
    field_fixes = 0
    date_drift_removals = 0
    skipped = 0
    report = []

    # Pre-scan: convert date-changing corrections to removals for anchored content
    if date_anchored:
        date_change_indices = set()
        for c in corrections:
            if c.get("action") == "remove":
                continue
            field = c.get("field", "")
            if field in ("month", "day"):
                date_change_indices.add(c["index"])

        for idx in date_change_indices:
            if idx < len(entries):
                e = entries[idx]
                removals.add(idx)
                date_drift_removals += 1
                report.append(
                    f"DATE-DRIFT REMOVE idx {idx} ({e.get('month')}/{e.get('day')}): "
                    f"Date correction would move entry off its calendar slot"
                )

    # Pass 1: Collect explicit removals
    for c in corrections:
        if c.get("action") == "remove":
            removals.add(c["index"])
            report.append(f"REMOVE idx {c['index']}: {c.get('reason', 'no reason given')}")

    # Pass 2: Apply field corrections
    for c in corrections:
        idx = c.get("index")
        if idx is None or idx in removals:
            continue
        if "field" not in c:
            continue

        field = c["field"]

        # Reject compound fields
        if "," in field or " and " in field:
            report.append(f"SKIP idx {idx}: compound field '{field}'")
            skipped += 1
            continue

        # Bounds check
        if idx >= len(entries):
            report.append(f"SKIP idx {idx}: out of range (max {len(entries) - 1})")
            skipped += 1
            continue

        # Field existence check
        if field not in entries[idx]:
            report.append(f"SKIP idx {idx}: field '{field}' not in entry")
            skipped += 1
            continue

        # Apply
        old = entries[idx][field]
        entries[idx][field] = c["new_value"]
        field_fixes += 1
        reason = c.get("reason", "")
        report.append(f"FIX idx {idx} [{field}]: {reason}")

    # Pass 3: Remove flagged entries
    corrected = [e for i, e in enumerate(entries) if i not in removals]

    # Summary
    report.append("")
    report.append("=" * 50)
    report.append(f"SUMMARY:")
    report.append(f"  Input entries: {len(entries)}")
    report.append(f"  Field fixes applied: {field_fixes}")
    report.append(f"  Explicit removals: {len(removals) - date_drift_removals}")
    if date_anchored:
        report.append(f"  Date-drift removals: {date_drift_removals}")
    report.append(f"  Skipped (format issues): {skipped}")
    report.append(f"  Output entries: {len(corrected)}")

    # Dates that need regeneration (for date-anchored content)
    if date_anchored:
        regen_dates = []
        for idx in removals:
            if idx < len(entries):
                e = entries[idx]
                m, d = e.get("month"), e.get("day")
                if m and d:
                    regen_dates.append(f"{m}/{d}")
        if regen_dates:
            report.append(f"  Dates needing regeneration: {regen_dates}")

    return corrected, report


def main():
    parser = argparse.ArgumentParser(description="Apply fact-check corrections")
    parser.add_argument("--entries", required=True, help="Path to entries .py file")
    parser.add_argument("--var", required=True, help="Variable name in entries file")
    parser.add_argument("--corrections", required=True, help="Path to corrections .py file")
    parser.add_argument("--cor-var", default="corrections", help="Variable name in corrections file")
    parser.add_argument("--output", required=True, help="Output path for corrected .py file")
    parser.add_argument("--out-var", default="corrected", help="Variable name in output file")
    parser.add_argument("--date-anchored", action="store_true",
                        help="Treat date corrections as removals (for OTD content)")
    args = parser.parse_args()

    entries = load_python_var(args.entries, args.var)
    corrections = load_python_var(args.corrections, args.cor_var)

    print(f"Loaded {len(entries)} entries, {len(corrections)} corrections")

    corrected, report = apply_corrections(
        entries, corrections, date_anchored=args.date_anchored
    )

    for line in report:
        print(line)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(f"{args.out_var} = {repr(corrected)}\n")

    print(f"\nSaved {len(corrected)} corrected entries to {args.output}")


if __name__ == "__main__":
    main()
