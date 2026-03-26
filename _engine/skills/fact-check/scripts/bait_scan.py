#!/usr/bin/env python3
"""
Engagement bait word scanner for FanGear HQ content.

Scans entry titles and content for engagement-bait words that violate
editorial policy. Can auto-fix common cases or report for manual review.

Usage:
    python bait_scan.py --entries /tmp/entries.py --var all_entries [--fix]

The --fix flag applies automatic replacements where safe:
    like → such as (in non-historical context)
    share → split/held (context-dependent)
    vote → selection (in non-election context)
"""

import sys
import re
import argparse

BAIT_WORDS = {"vote", "comment", "like", "share", "tag"}

# Safe automatic replacements (context-dependent)
AUTO_FIXES = {
    "like": "such as",
    "share": "split",
    "vote": "selection",
}


def scan_entry(entry, index):
    """Scan a single entry for bait words. Returns list of findings."""
    findings = []
    for field in ("title", "content"):
        text = entry.get(field, "")
        if not text:
            continue
        words = text.lower().split()
        for bait in BAIT_WORDS:
            if bait in words:
                findings.append({
                    "index": index,
                    "field": field,
                    "word": bait,
                    "context": text[:80],
                })
    return findings


def auto_fix_entry(entry, finding):
    """Attempt automatic replacement. Returns True if fixed."""
    field = finding["field"]
    word = finding["word"]
    text = entry.get(field, "")

    if word not in AUTO_FIXES:
        return False

    replacement = AUTO_FIXES[word]

    # Context-sensitive replacements
    if word == "share":
        # "share" in historical context (revenue sharing, etc.) → keep as is
        if any(w in text.lower() for w in ["revenue", "market", "profit"]):
            replacement = "share"  # keep it, it's not bait
            return False
        # "shared the lead" → "held the lead"
        if "shared" in text.lower():
            text = re.sub(r'\bshared\b', 'held', text, flags=re.IGNORECASE)
            entry[field] = text
            return True

    if word == "like":
        # "like" as a simile ("played like") is fine — only replace "like" as engagement bait
        # Simple heuristic: if preceded by a verb, it's a simile
        if re.search(r'\b\w+ed\s+like\b|\b\w+s\s+like\b', text.lower()):
            return False

    # Apply replacement
    pattern = rf'\b{re.escape(word)}\b'
    new_text = re.sub(pattern, replacement, text, count=1, flags=re.IGNORECASE)
    if new_text != text:
        entry[field] = new_text
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Scan for engagement bait words")
    parser.add_argument("--entries", required=True, help="Path to entries .py file")
    parser.add_argument("--var", required=True, help="Variable name")
    parser.add_argument("--fix", action="store_true", help="Auto-fix safe replacements")
    args = parser.parse_args()

    namespace = {}
    with open(args.entries, 'r', encoding='utf-8') as f:
        exec(f.read(), namespace)
    entries = namespace[args.var]

    all_findings = []
    for i, entry in enumerate(entries):
        all_findings.extend(scan_entry(entry, i))

    if not all_findings:
        print(f"Clean: 0 bait words found in {len(entries)} entries.")
        return

    print(f"Found {len(all_findings)} bait word instances in {len(entries)} entries:\n")

    fixed = 0
    for f_item in all_findings:
        status = ""
        if args.fix:
            if auto_fix_entry(entries[f_item["index"]], f_item):
                status = " → FIXED"
                fixed += 1
            else:
                status = " → MANUAL REVIEW"
        print(f"  [{f_item['index']}] {f_item['field']}: \"{f_item['word']}\"{status}")
        print(f"    Context: {f_item['context']}")

    if args.fix:
        print(f"\nAuto-fixed: {fixed}/{len(all_findings)}")
        # Save back
        with open(args.entries, 'w', encoding='utf-8') as f_out:
            f_out.write(f"{args.var} = {repr(entries)}\n")
        print(f"Saved to {args.entries}")


if __name__ == "__main__":
    main()
