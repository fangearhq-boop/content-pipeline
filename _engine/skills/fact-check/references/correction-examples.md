# Correction Examples — Good vs Bad

Real examples from production fact-checking runs. These illustrate the format rules
and common pitfalls.

---

## Good Corrections

### Simple field fix (single field, clear reason)
```python
{"index": 3, "field": "day", "old_value": 4, "new_value": 26,
 "reason": "Prince Fielder agreed to Detroit Tigers contract on January 26, 2012, not January 4"}
```
Why it's good: One field, old_value included for verification, reason is specific.

### Content wording fix
```python
{"index": 4, "field": "content", "old_value": "1.816 ERA", "new_value": "1.82 ERA",
 "reason": "Ed Walsh's career ERA is officially recorded as 1.82"}
```
Why it's good: Fixes a specific claim within the content field. old_value is the
substring being changed (though the full field value would also work).

### Clean removal with clear justification
```python
{"index": 8, "action": "remove",
 "reason": "Carlton Fisk never hit 500 home runs; he hit 376 in his career. Entry is fabricated."}
```
Why it's good: States what's wrong AND what the truth is. Future regeneration
can avoid the same mistake.

### Multiple corrections on same entry (done correctly)
```python
{"index": 11, "field": "month", "old_value": 3, "new_value": 9,
 "reason": "Carl Yastrzemski joined 3,000 Hits Club on September 12, 1979, not March"},
{"index": 11, "field": "day", "old_value": 10, "new_value": 12,
 "reason": "Correct day is September 12, not March 10"},
{"index": 11, "field": "year", "old_value": 1978, "new_value": 1979,
 "reason": "Yastrzemski reached 3,000 hits in 1979, not 1978"}
```
Why it's good: Each field gets its own correction. However — for date-anchored
content, this should actually be a REMOVAL since all three date components are wrong.
The entry was meant to fill the 3/10 slot and now it's on 9/12.

---

## Bad Corrections (DO NOT produce these)

### Compound field name
```python
{"index": 0, "field": "month, day, year",
 "old_value": "month: 1, day: 1, year: 1935",
 "new_value": "month: 2, day: 25, year: 1934",
 "reason": "John McGraw died on February 25, 1934, not January 1, 1935"}
```
Why it's bad: `"field": "month, day, year"` doesn't match any key in the entry dict.
The apply script looks for `entry["month, day, year"]` which doesn't exist, so the
correction silently fails. This was the single most common failure mode in production.

### "and" in field name
```python
{"index": 1, "field": "title and content",
 "old_value": "Clemens Wins MVP...",
 "new_value": "Clemens' 1999 Season...",
 "reason": "Clemens did not win 1999 MVP"}
```
Why it's bad: Same problem — no key called "title and content". Should be two
separate corrections, one for "title" and one for "content".

### Date correction on date-anchored content
```python
{"index": 25, "field": "month", "old_value": 6, "new_value": 9,
 "reason": "Cal Ripken Jr. broke Lou Gehrig's record on September 6, not June 29"}
```
Why it's bad: This entry was generated to fill the June 29 calendar slot. Moving it
to September 6 leaves June 29 empty and creates a duplicate on September 6. Should be:
```python
{"index": 25, "action": "remove",
 "reason": "Cal Ripken Jr. broke Lou Gehrig's record on September 6, 1995, not June 29. Entry generated for 6/29 slot — needs different event for that date."}
```

---

## Edge Cases

### Content field with partial fix
When only part of the content is wrong, you can either:

**Option A:** Replace the entire content field (simpler, always works)
```python
{"index": 15, "field": "content",
 "old_value": "Rivera achieved his 500th save, becoming the first pitcher ever to reach that plateau.",
 "new_value": "Rivera achieved his 500th save on June 28, 2009, becoming the second pitcher to reach that milestone after Trevor Hoffman.",
 "reason": "Rivera was second to 500 saves, not first. Hoffman reached 500 first."}
```

**Option B:** Write the correction as a targeted fix with context (also fine)
```python
{"index": 15, "field": "content",
 "old_value": "the first pitcher ever to reach that plateau",
 "new_value": "the second pitcher to reach that milestone after Trevor Hoffman",
 "reason": "Trevor Hoffman was the first to 500 saves, not Rivera"}
```

Option A is safer because old_value matching is exact. Option B can fail if the
text was slightly different than remembered.

### Unverifiable entry (not the same as fabricated)
```python
# DON'T remove entries just because you can't find a source.
# Flag them in the summary report instead:
#   "Index 47: Could not verify Timberwolves-Hornets trade on 9/9/2009.
#    No results found but not confirmed false. Recommend manual review."
```
Absence of search results doesn't prove an event didn't happen — it might just
mean it wasn't notable enough for online coverage. Only remove when you find
positive evidence of fabrication (e.g., the player never played for that team,
the stat is impossible, the timeline doesn't work).
