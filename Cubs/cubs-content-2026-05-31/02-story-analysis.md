# Story Analysis — 2026-05-31

---

## ### Insights Applied

**Snapshot loaded:** Cubs/_data/insights.json (generated_at: 2026-05-31T08:30:00.272842+00:00)  
**Significant findings:** 4 findings (all consumed below)

### Finding 1: content_type=brief — WINNER (medium effect, delta=0.444, p=0.011)
- brief tweets: median 56 impressions vs 27 for non-briefs
- **Action:** All 6 posts are brief format. No long-form threads or multi-part tweets.

### Finding 2: content_type=rss_news — LOSER (medium effect, delta=0.444, p=0.011)
- rss_news tweets: median 27 impressions vs 56 for non-rss
- **Action:** All posts are original editorial takes, not wire-style news dumps. No "Cubs beat Cardinals 6-1 last night. Here is a recap:" framing. Every tweet leads with a take or a sharp stat hook.

### Finding 3: has_stat=True — WINNER (medium effect, delta=0.337, p=0.006)
- tweets with stats: median 67 impressions vs 46 for no-stat tweets
- **Action:** Every tweet includes at least one specific statistic. Game recap: score + innings pitched. Bold take: ERA + IP. Preview: ERA, game time. Standings: records + GB. Boyd: ERA + estimated return date. Hype: score + record.

### Finding 4: posting_window=midday_12_18 — WINNER (small effect, delta=0.328, p=0.009)
- midday (12 PM–6 PM CT) tweets: median 77 impressions vs 45 for other windows
- **Action:** The two most compelling analysis stories (NL Central standings, Boyd update) are placed in the 1:15 PM and 2:30 PM midday slots. The Wicks preview is at 12:00 PM. Three of 6 slots are in the 12–6 PM window, which is the maximum practical given posting priority rules (recap must be 7 AM).

**No has_emoji_first_line finding in today's snapshot** — brand-voice.md defaults apply. Emojis may be used naturally (1-3 per post), positioned mid-post or end of post per voice guide. Not deliberately avoided today unlike some prior runs.

**No has_score finding in today's snapshot** — score is included in the recap tweet on story merit (PCA/Brown stats require the score context).

**No len_bucket finding in today's snapshot** — targeting 230-270 chars naturally; not specifically chasing 260+ bucket.

**No opening=allcaps_lead finding** — ALL CAPS may be used for 1-2 emphasis words per brand voice where it adds impact.

---

## ### Series Context

**Snapshot loaded:** Cubs/_data/series-context.json (generated_at: 2026-05-31T08:30:00.582626+00:00)

**Status:** `is_series_start_today=false` — mid-series (same Cardinals opponent as May 29-30). This is Game 3, the rubber game finale of a 3-game set at Busch Stadium.

**Case applied:** Mid-series (not series opener). NO dedicated series-preview slot at 7:00 AM. Game 2 recap takes the 7:00 AM slot per engine docs priority rule.

**Cardinals series arc:**
- Game 1 (May 29): Cardinals 6, Cubs 5 — Velázquez callup HR, Cardinals snapped 4-game skid
- Game 2 (May 30): Cubs 6, Cardinals 1 — Ben Brown 7 IP gem, PCA 4-for-5 444-ft HR, series even
- Game 3 (May 31): Wicks vs. Liberatore, 6:20 PM CT — rubber game, winner takes series

**Implications:** Winning tonight would give Cubs a series win vs their primary NL Central rival, pushing Cardinals to 30-27 and Cubs to 33-27. The Brewers (~34-21) are the division leader; taking division series from the Cardinals is how the Cubs close that gap.

---

## Story-by-Story Angle Analysis

### STORY 1: Game Recap — 7:00 AM CT

**Hook options considered:**
1. "Cubs 6, Cardinals 1" score-lead → CHOSEN (has_stat winner; score-led)
2. "Ben Brown masterclass" pitcher-lead → strong but buries the final score
3. "PCA 444-ft bomb" HR-lead → good but the story is the complete game performance

**Chosen angle:** Score in first line. Then Brown's 7-inning gem as the story. PCA's 444-ft HR + 4-hit night as the exclamation point. Jacob Webb's 8th consecutive scoreless outing as the kicker. "Series even" as the setup for tonight's rubber game.

**Insights adjustments:**
- has_stat: score + ERA + innings pitched included ✓
- brief: tight 3-paragraph structure ✓
- Not rss_news: editorial framing ("silenced Busch," "ace outing"), not wire copy ✓

---

### STORY 2: Ben Brown Bold Take — 9:30 AM CT

**Hook options considered:**
1. "The Cubs' rotation is broken — except for one guy" → strong
2. "Brown's ERA is now below 2.00" → stat-led, clean
3. "Best pitcher in the rotation nobody's talking about" → slightly clickbait

**Chosen angle:** Lead with Brown's sub-2.00 ERA stat, then call out the contrast — rotation has four key starters out, one guy is carrying it. The take: this is ace-level pitching hiding in plain sight.

**Insights adjustments:**
- has_stat: ~1.91 ERA after yesterday (MEDIUM — calculated), 7 IP vs Cardinals ✓
- Not rss_news: bold editorial claim ✓
- brief ✓

---

### STORY 3: Series Finale Preview — 12:00 PM CT (midday slot)

**Hook options considered:**
1. "Jordan Wicks has a 16.62 ERA, and the Cubs need him to win a division series game" → edgy, but leads with negative
2. "Cubs vs. Cardinals, rubber game, 6:20 PM CT tonight" → clean stakes-first lead
3. "Liberatore's inconsistency is the Cubs' best asset tonight" → creative angle

**Chosen angle:** Stakes-first lead. Rubber game, series on the line, 32-27 Cubs vs 30-26 Cardinals, first pitch 6:20 PM CT. Then the pitching matchup with context for both — Wicks' small sample, Liberatore's inconsistency. Frame it as competitive, not as "Wicks is going to collapse."

**Insights adjustments:**
- has_stat: both pitchers' ERAs, records, game time ✓
- midday slot (12:00 PM in midday_12_18 window) ✓
- Not rss_news: original analysis of the matchup ✓
- brief ✓

---

### STORY 4: NL Central Watch — 1:15 PM CT (midday slot)

**Hook options considered:**
1. "Brewers 34-21 and running — Cubs need to keep winning" → urgency-led
2. "Cubs are 2.5 back in the NL Central, this series is a statement opportunity" → rivalriness
3. Division table format → too RSS-news style

**Chosen angle:** The take is that this Cardinals series isn't just 3 games — it's a 6-point swing in the division race. Win tonight = Cubs 33-27, Cardinals 30-27. Brewers aren't going away but every series vs St. Louis matters. Mid-June is when the race gets real.

**Insights adjustments:**
- has_stat: records for all three teams + games back figure ✓
- midday slot (1:15 PM in midday_12_18 window) ✓
- brief ✓

---

### STORY 5: Boyd Iowa Rehab Start — 2:30 PM CT (midday slot)

**Hook options considered:**
1. "Boyd threw today — the rotation lifeline" → urgency-led
2. "Boyd + Brown = the path to June" → narrative
3. "Expected return June 19" → date-specific, clean

**Chosen angle:** Good news framing. Boyd made his first Iowa rehab start today, on schedule for two rehab outings then return. Pair with the rotation context (Horton out, Steele weeks away, Harvey/Thielbar unavailable). Brown is bridging; Boyd is the reinforcement.

**Insights adjustments:**
- has_stat: Boyd's 2-1, 6.00 ERA pre-injury + "2 rehab starts" + ~June 19 return ✓
- midday slot (2:30 PM in midday_12_18 window) ✓
- brief ✓

---

### STORY 6: Pre-Game Hype — 5:00 PM CT

**Hook options considered:**
1. "Momentum is real, Busch Stadium or not" → Cubs confidence
2. "Rubber game. 6:20 PM CT. Get ready." → punchy
3. Series context as setup

**Chosen angle:** Cubs have momentum from a dominant 6-1 win. The team that plays with confidence in a rival's house. Bold take: after Brown silenced Busch last night, the Cubs have every reason to win this series. Tonight, it ends with a series win.

**Insights adjustments:**
- has_stat: record (32-27) + series score (6-1) + game time ✓
- 5:00 PM CT is pre-midday window but post-2:30 PM — closest available slot for pre-game hype ✓
- bold/hype per brand voice ✓

---

## Cross-Story Consistency Check

- Score (Cubs 6, Cardinals 1) — used in Story 1 and referenced in Story 6. Consistent.
- Ben Brown ERA: Story 1 uses "7 IP, 3 H, 1 ER"; Story 2 uses "sub-2.00 ERA." Consistent.
- Series record: 1-1 going into Game 3. Story 1 sets up Game 3; Story 3 references it. Consistent.
- Cubs record: 32-27 used across Stories 1, 4, 6. Consistent.
- Boyd: "first Iowa rehab start" — Story 5 only. No conflict.
- Wicks ERA 16.62 (4.1 IP): Story 3 only. No conflict.

All story angles are distinct. No duplicate coverage of yesterday's May 30 topics.
