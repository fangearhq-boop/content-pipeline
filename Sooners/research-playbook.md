# Sooners Fan Recap — Research Playbook

The daily job is deterministic. It does not call a model and it does not browse past the allowlist.

## Pick a story

1. Fetch the SoonerSports teasers for football, both basketball teams, softball, and baseball, plus the On3 Oklahoma feed and the football schedule page.
2. Keep an item whose age is inside the sport window: football 4 days, basketball 10, softball and baseball 21. A missing or unparseable timestamp is stale. The recruiting slot does not quote feed headlines.
3. Skip a news URL that was already used in the last 21 days (`story-history.md`).
4. Build a tweet only from a verbatim span of that teaser. Every digit in the tweet has to occur as that same number in the span.
5. If nothing qualifies, publish the number-free fan line for that slot. Do not fill the digit in from memory.

## Do not upgrade a teaser

- "Making the case for a Jim Thorpe finalist" is not "he is a finalist."
- A preview that calls a team 21st-ranked does not license the ranking on the recap post unless that recap teaser repeats the ranking.
- "Dominant" is not a number and does not need a source. A score does.

## Fact-check log

One table. Columns are Claim, Source, Confidence, Slot, Status. Status is the exact word `VERIFIED`. A digit in a post has to appear on that slot's row. The source cell is the full URL. The log also contains the sentence `Acceptable for social`.

A day missing `06-fact-check-log.md`, a VERIFIED row on a banned or unknown host, or a tweet digit with no backing row must fail `verify_brief` before anything is written.
