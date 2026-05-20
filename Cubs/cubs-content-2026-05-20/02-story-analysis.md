# Story Analysis — 2026-05-20
# Chicago Cubs Fan HQ

---

### Insights applied

**Findings read from Cubs/_data/insights.json (generated_at: 2026-05-20T08:30:00 UTC):**

6 significant findings cleared all three gates (n≥8, Mann-Whitney p<0.05, |Cliff's delta|≥0.20):

1. **content_type=rss_news (large, δ=0.479)** — Winner: not_rss_news (52.5 median impressions vs 27). All posts today are "brief" content_type. No RSS feed posts drafted. ✓

2. **len_bucket=140-200 (medium, δ=0.433)** — Winner: not_140-200 (42 vs 24.5 median). All 6 tweets intentionally drafted to land outside 140-200 chars. All are in the 200-260 range (232-267 chars). Character counts verified manually. ✓

3. **posting_window=overnight_00_06 (medium, δ=0.433)** — Winner: not_overnight (39 vs 25 median). No overnight slots used. Earliest post is 7:00 AM CT. ✓

4. **has_emoji_first_line (medium, δ=0.432)** — Winner: False (49 vs 26 median). No tweet leads with an emoji. This overrides brand-voice guide's allowance of leading emojis. ✓

5. **content_type=brief (medium, δ=0.430)** — Winner: brief (52 vs 27 median). All posts are brief type. ✓

6. **has_score=True (medium, δ=0.401)** — Winner: True (54 vs 31 median). Story 1 (game recap) leads with "Brewers 5, Cubs 2." — score is the very first line. ✓

**Net effect on today's drafts:** 
- Score embedded in first line of game recap (has_score compliance)
- No leading emojis on any tweet (strongest behavioral change vs brand-voice defaults)
- All tweets 200-267 chars (clear of 140-200 penalty bucket)
- No overnight slots
- All posts classified as "brief" type

---

### Series context

**Source:** Cubs/_data/series-context.json (generated_at: 2026-05-20T08:30:00 UTC)

- `is_series_start_today`: false — mid-series, no dedicated series-preview slot
- `off_day`: false — game today at 6:40 PM CT
- Opponent: Milwaukee Brewers (28-18, first in NL Central)
- Cubs: 29-20 (second, 0.5 GB)
- Venue: Wrigley Field
- Series: May 18-20, Cubs vs Brewers, 3 games. Cubs lost Game 1 (9-3) and Game 2 (5-2).
- Today is **Game 3 — series finale**. Cubs can be swept at home.

**Applied:** No series-preview tweet drafted (not Game 1). Series-sweep stakes embedded in Game 3 preview and game-time hype posts. Division implications (Brewers in first) woven into bold-take post.

---

### STORY 1: Brewers 5, Cubs 2 — Misiorowski Dominant Again

**Angle:** The headline is Misiorowski's continued dominance, not Brown's failure. 24.1 consecutive scoreless innings is a truly extraordinary run that deserves to be called out. Brown's loss is contextualized with his league-leading wild pitch stat — a sharp, specific detail. End on the streak (four straight losses) without melodrama.

**Engagement hook:** Misiorowski's scoreless streak is a statistic fans can rally around or argue about. The wild-pitch detail ("league-leading") is the kind of specific fact that prompts shares and replies.

**Tone:** Informative, clean, matter-of-fact. The loss speaks for itself; no need to editorialize.

**Tweet format:** Lead with score (has_score winner). Three paragraphs, no leading emoji. 254 chars (>200, in winning length range).

---

### STORY 2: Cubs Slide — Division Alarm

**Angle:** Four losses in a row, eight of last ten, dropped from first to half a game back. The hook is the combination of the losing streak AND the division context — this isn't random variance, it's a trend at a critical moment with the Brewers directly above them. The punchline is "Wrigley wants answers tonight" — setting up Game 3 as consequential.

**Engagement hook:** Divisional anxiety is peak fan-engagement territory. Stating the bad news directly (without doom-posting) respects fans' intelligence and prompts reactions.

**Tone:** Bold, concerned but not catastrophizing. Sharp and declarative.

**Tweet format:** Two paragraphs, declarative statements, no leading emoji. 238 chars.

---

### STORY 3: Matt Boyd Meniscus Surgery

**Angle:** The "playing with his kids" detail is compelling and humanizing, but the baseball consequence is the story — second IL stint, rotation in tatters. Threading to Peralta makes this tweet do double duty: injury update AND forward-looking narrative hook.

**Engagement hook:** The rotation health crisis is the season's biggest ongoing story. Tying Boyd's injury to the Peralta pursuit is the analytical take Cubs fans are already having.

**Tone:** Informative with a sharp take in the closer ("writing itself"). Not doom-posting — factual with a pointed observation.

**Tweet format:** Three stacked declarative paragraphs. No leading emoji. 247 chars.

---

### STORY 4: Game 3 Preview

**Angle:** The matchup is genuinely lopsided on paper: Harrison has been brilliant (2.09 ERA, ≤2 ER in all 8 starts), Cabrera has been vulnerable (HR in 5 straight). Stating this contrast plainly creates urgency. "No. 1 on today's task list: avoid a sweep" lands as both humor and truth.

**Engagement hook:** Game-day previews with concrete stats drive clicks and replies (fans either defend Cabrera or worry about Harrison). The sweep stakes are obvious but need saying.

**Tone:** Balanced informative with an edge of concern. Not panicked.

**Tweet format:** Three paragraphs. "No. 1" not "#1" per style guide. No leading emoji. 267 chars.

---

### STORY 5: Freddy Peralta Trade Clock

**Angle:** The Boyd surgery is the fresh hook that makes this a new post despite covering similar ground to yesterday's (May 19) Peralta story. The injury context is now worse: three rotation arms unavailable (Horton 16 months, Steele past the break, Boyd 6 weeks). The "12 days" is a specific, ticking countdown. Counsell connection is a differentiating factor.

**Engagement hook:** Trade speculation is perennial engagement bait for Cubs fans, but this has real teeth — three rotation injuries + June 1 deadline + Mets' known interest makes the story credible.

**Tone:** Bold, urgent, confident. "Counsell knows him cold" carries weight.

**Tweet format:** Two paragraphs. "No. 1" format used for roster ranking. No leading emoji. 257 chars.

**Note on prior coverage:** Yesterday's pipeline ran a Peralta story at 2:30 PM CT (13 days out). Today's fresh angle is Boyd's surgery as the new urgency hook (news broke post-pipeline). Counts as FOLLOW UP, not duplicate.

---

### STORY 6: Game Time Hype

**Angle:** Short, punchy pre-game energy post. Context-setting without being long-winded. "Game 3. Wrigley. 6:40 PM CT." is the three-fact lead. Division context given in one line. No question, just a statement of stakes.

**Tone:** Urgent, passionate. The "This one matters" closer is earned given the context.

**Tweet format:** Three short paragraphs. Direct. No leading emoji. 232 chars.
