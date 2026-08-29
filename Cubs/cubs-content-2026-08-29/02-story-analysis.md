# Cubs Story Analysis — August 29, 2026

## Insights Applied

### Performance Insights Read (from Cubs/_data/insights.json, generated 2026-08-29T08:30:00Z)

Two significant findings cleared all three gates (n≥8, Mann-Whitney p<0.05, |Cliff's delta|≥0.20):

**Finding 1 — has_stat=True wins** (strongest signal, effect size 0.308 "small")
- Winner: tweets WITH stats → median 109 impressions
- Loser: tweets WITHOUT stats → median 82 impressions
- Action: Fold specific stats into every tweet. Don't write a tweet that could run without at least one concrete number.

**Finding 2 — has_score=False wins** (effect size 0.256 "small")
- Winner: tweets WITHOUT scores → median 101 impressions
- Loser: tweets WITH scores → median 79 impressions
- Action: Do NOT lead with, or include, the raw game score. Lead with performance stats (ERA, K, IP, HR, SB, WAR) instead. The score can be inferred or omitted entirely.

**How these change today's drafts:**
- Story 1 (recap): Lead with Thornton's stat line, NOT the 10-8 final. Write "Thornton — 5 runs, 0.2 innings" before mentioning anything about the result.
- Story 3 (PCA): Already stat-heavy by design; double-check no scores slip in.
- Story 4 (Wild Card): W-L records are not "scores" — they're fine. Avoid writing "Cubs scored X" framing.
- Story 5 (game preview): Focus on ERA, recent performance, head-to-head stats rather than previewing a score.
- All tweets: Verify each has at least one stat (BA, ERA, IP, K, HR, SB, WAR, OPS, or record).

**Not in significant_findings (no action):**
- Raw bucket data for `by_hour_ct`, `by_weekday_ct`, `by_len_bucket`, etc. — not used for decisions (bypasses significance gates).
- `has_emoji_first_line` had no contrast (all 124 tweets are False) — not actionable.

---

### Series Context

**is_series_start_today:** False
**off_day:** False
**Series:** Cubs vs Cincinnati Reds (mid-series, Game 2 of 2)
- Game 1 played yesterday (Aug 28): Reds won 10-8 via Thornton bullpen collapse
- Game 2 today (Aug 29, 1:20 PM CT at Wrigley): Gausman vs Abbott
- Game 3 Sunday (Aug 30, 6:20 PM CT): TBD

**Application:** No dedicated series-preview slot reserved (not a series start). Day game means no post-game slots in today's schedule. Preview slot at 12:00 PM CT covers today's matchup.

---

## Story 1: Thornton Blowup — Cubs Fall 10-8

**Angle:** NEW STORY. Lead with the Thornton collapse, not the score (per has_score=False insight). Peterson pitched well (5 IP, 2 ER, 8 K — that's a quality start). Thornton's August ERA was 0.00 across 10 innings. Then in 0.2 innings: Trevino 2-run HR, Stephenson 3-run blast, 5 ER. Cubs scored 8 runs and still lost. The offense did their job.

**Hook:** "Trent Thornton. 10 scoreless August innings. Then 5 runs in two-thirds of one."

**Tone:** Frustrated but factual. Informed with edge. Not doom-posting.

**Insight application:** Lead with Thornton's 5-ER stat, NOT the 10-8 score. Note Peterson's 8 K. Per has_stat=True, include multiple concrete numbers.

**Tier:** 1

---

## Story 2: Bullpen Red Flag With October Approaching

**Angle:** FOLLOW UP on yesterday's loss. Sun-Times piece on bullpen regression is the hook. The fact that Thornton had a 0.00 August ERA before this and other relievers (Webb, Civale) are also concerning makes this a systemic story, not just one bad outing. Wiggins September callup is part of the answer.

**Hook:** "One bad Thornton outing isn't the story. The Sun-Times says key Cubs relievers are regressing to the mean. The timing is brutal."

**Tone:** Bold, analytical. Not panic — but honest acknowledgment of a real concern with a forward-looking kicker (September callups on Tuesday).

**Insight application:** Fold in Thornton's stat context (10 scoreless IP → 5 ER in 0.2 IP = ERA jump to 4.22). Has_stat=True: include the number.

**Tier:** 2

---

## Story 3: PCA MVP Watch

**Angle:** FOLLOW UP on ongoing season arc. Last covered Aug 27 (7.9 bWAR, 33 HR at that point). Today's angle: the full September case. Stats: .279/.932 OPS, 32 HR (may have dropped 1 from Aug 27 count — use conservative 32), 31 SB, 7.9 bWAR (leads all of baseball), 29/37 experts. Back-to-back 30-30 is confirmed franchise history.

**Hook:** "Pete Crow-Armstrong leads all of baseball in WAR — and he's already locked in back-to-back 30-30 seasons for the first time in Cubs history."

**Tone:** Celebratory, stat-backed, confident. This is our guy.

**Insight application:** has_stat=True — jam stats into every line. has_score=False — no scores needed here; this is a season-arc stat tweet.

**Tier:** 2

---

## Story 4: Wild Card Watch — Cubs 76-59

**Angle:** FOLLOW UP on standings. Cubs dropped yesterday but still hold WC1 at 76-59. Brewers (83-51) are running away with the division. Cardinals (67-68) are fading out of the picture. Sharp rival jab on Cardinals. September is the final sprint.

**Hook:** "The Cubs still hold the NL's top Wild Card spot at 76-59. The Cardinals are 67-68 in late August. Some things stay predictable."

**Tone:** Mix of informative (standings data) and rival jab (Cardinals). 50/50 split per brand voice.

**Insight application:** has_stat=True — include W-L records for multiple teams. has_score=False — standings records are not "game scores," fine to use.

**Tier:** 2

---

## Story 5: Game 2 Preview — Gausman vs Abbott, 1:20 PM CT

**Angle:** NEW STORY (game preview). Cubs looking for a bounce-back. Gausman fresh off his best Cubs start (7 IP, 0 ER vs D-backs Aug 25). Abbott has a 4.15 ERA but Cubs split two meetings this season — they knocked him out in the 4th in the second matchup (4 ER). The matchup favors Chicago on paper.

**Hook:** "Kevin Gausman takes the mound at Wrigley today — coming off a 7-inning shutout of the D-backs. Andrew Abbott (4.15 ERA) stands in the way."

**Tone:** Confident, game-day energy. Lead with Gausman's recent performance stat (7 IP, 0 ER). Preview structure: pitcher stats → head-to-head context → time/location.

**Insight application:** has_stat=True — Gausman ERA/recent performance + Abbott ERA. has_score=False — don't mention the Aug 25 final score, just the line.

**Tier:** 1

---

## Story 6: Matt Shaw Returns

**Angle:** NEW STORY. Shaw activated from IL ahead of yesterday's series opener. Two months away (since June 29). Returns with .246/.322/.415 and serious versatility. Alcántara optioned but returns Sept 1 with expansion. Shaw's presence gives Counsell more lineup flexibility for the stretch run.

**Hook:** "Matt Shaw is back. Two months on the IL, back on the active roster in time for the stretch run. The Cubs just got deeper."

**Tone:** Informative, positive. Depth story — not a lead, but a meaningful roster development.

**Insight application:** has_stat=True — .246/.322/.415, 4 HR, 4 SB in 56 games. has_score=False — no game scores needed.

**Tier:** 2
