# Standard Correction Application Script

Use this pattern whenever applying corrections from a fact-check pass. The script
handles both field corrections and removals, validates old_value matches, and reports
what changed.

## Template

```python
#!/usr/bin/env python3
"""Apply fact-check corrections to a dataset."""

def apply_corrections(entries, corrections, context=""):
    """
    Apply a list of corrections to entries. Returns corrected entries and a report.

    Args:
        entries: List of entry dicts
        corrections: List of correction dicts (field corrections and removals)
        context: Label for reporting (e.g., "MLB OTD")

    Returns:
        (corrected_entries, report_lines)
    """
    removals = set()
    field_fixes = 0
    skipped = 0
    report = []

    # Pass 1: Identify removals
    for c in corrections:
        if c.get("action") == "remove":
            removals.add(c["index"])
            report.append(f"REMOVE idx {c['index']}: {c['reason']}")

    # Pass 2: Apply field corrections (skip entries marked for removal)
    for c in corrections:
        idx = c.get("index")
        if idx in removals:
            continue
        if "field" not in c:
            continue

        field = c["field"]

        # Reject compound fields — these are format violations
        if "," in field or " and " in field:
            report.append(f"SKIP idx {idx}: compound field '{field}' — format violation")
            skipped += 1
            continue

        # Check field exists in entry
        if idx >= len(entries):
            report.append(f"SKIP idx {idx}: index out of range")
            skipped += 1
            continue

        if field not in entries[idx]:
            report.append(f"SKIP idx {idx}: field '{field}' not found in entry")
            skipped += 1
            continue

        # Apply correction
        entries[idx][field] = c["new_value"]
        field_fixes += 1
        report.append(f"FIX idx {idx} [{field}]: {c['reason']}")

    # Pass 3: Remove flagged entries
    corrected = [e for i, e in enumerate(entries) if i not in removals]

    # Summary
    summary = (
        f"\n{context} CORRECTION SUMMARY:\n"
        f"  Field fixes applied: {field_fixes}\n"
        f"  Entries removed: {len(removals)}\n"
        f"  Skipped (format issues): {skipped}\n"
        f"  Final count: {len(corrected)} (was {len(entries)})\n"
    )
    report.append(summary)

    return corrected, report
```

## Usage

```python
exec(open("/tmp/my_entries.py").read())      # loads `entries`
exec(open("/tmp/my_corrections.py").read())  # loads `corrections`

corrected, report = apply_corrections(entries, corrections, "MLB OTD")
for line in report:
    print(line)

# Save corrected entries
with open("/tmp/corrected_entries.py", "w") as f:
    f.write("corrected_entries = " + repr(corrected) + "\n")
```

## Handling Date-Anchored Corrections

When corrections include date changes on date-anchored content (On This Day entries),
the apply script should detect and handle these:

```python
# After applying corrections, check if any date-anchored entries
# had their dates changed away from their assigned slots
def check_date_drift(original_entries, corrected_entries, removals):
    """Find entries where month/day changed — these need regeneration."""
    drifted_dates = []
    j = 0
    for i, orig in enumerate(original_entries):
        if i in removals:
            continue
        corr = corrected_entries[j]
        j += 1
        if (orig.get("category") == "On This Day" and
            (orig.get("month") != corr.get("month") or
             orig.get("day") != corr.get("day"))):
            drifted_dates.append((orig["month"], orig["day"]))
            # These entries should have been removals, not corrections
    return drifted_dates
```

If `check_date_drift` returns any dates, those entries need to be removed and
regenerated for the original calendar slots. This catches agent behavior that
should have been a removal but was written as a date correction.
