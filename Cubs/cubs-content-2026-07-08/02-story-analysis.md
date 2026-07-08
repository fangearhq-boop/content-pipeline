# 02-story-analysis.md — Story Analysis
# Date: 2026-07-08

---

## ### Insights Applied

**Snapshot generated:** 2026-07-08T08:30:00.277471+00:00
**Measured tweet count:** 74
**Significant findings:** 3 findings cleared all gates (n≥8, Mann-Whitney U p<0.05, |Cliff's delta|≥0.20)

### Finding 1 — has_stat=True (MEDIUM effect, p=0.0072, delta=0.388)
**Winner:** tweets WITH a concrete stat → 106.5 median impressions
**Loser:** tweets WITHOUT a stat → 60.0 median impressions
**Action taken:** Every tweet today includes at least one specific, cited statistic. For the game recap, this means leading with the score. For the standings post, it means citing exact records. For the trade deadline post, it means Joe Ryan's ERA and FIP. This is the strongest signal in the dataset and drives the most consequential drafting change.

### Finding 2 — len_bucket=200-260 (SMALL effect, p=0.0377, delta=0.292)
**Winner:** tweets NOT in 200-260 char range → 90 median impressions
**Loser:** tweets IN 200-260 char range → 62 median impressions
**Action taken:** Each tweet is drafted to land either under 200 chars OR over 260 chars (up to 280 max), actively avoiding the 200-260 middle zone. The brand-voice spacing rules (blank lines between hook/detail/hashtags) naturally push tweets toward 260+, which is the ideal zone.

### Finding 3 — len_bucket=260+ (SMALL effect, p=0.0377, delta=0.292)
**Winner:** tweets 260+ chars → 90 median impressions
**Loser:** tweets in other buckets → 62 median impressions
**Action taken:** Longer tweets (260-280) are the target length when there's enough content. The blank-line spacing format from brand-voice.md helps reach this naturally without padding.

**Net drafting rule applied:** Lead every tweet with a stat. Use the blank-line spacing format. Aim for 260-280 chars; if content runs short, trim to well under 200 rather than parking in the 200-260 zone.

---

## ### Series Context

**is_series_start_today:** false
**off_day:** false
**Series:** Cubs at Baltimore Orioles (mid-series — Game 2 of 3-game series)
**Cubs record:** 51-40 | **Orioles record:** 42-50
**Venue:** Oriole Park at Camden Yards
**Today's game:** Wed 5:35 PM CT | Colin Rea vs Dean Kremer

No mandatory 7:00 AM series preview tweet (series started yesterday). Game 2 preview is covered at 12:00 PM CT. The 7:00 AM slot is correctly reserved for the Game 1 recap.

---

### STORY 1: Cubs 5, Orioles 2 — Game Recap (July 7)

**Freshness tags:** game-recap, road-win, Boyd-strong

**Summary:** The Cubs won 5-2 at Camden Yards on Tuesday night with Matthew Boyd delivering a quality start (game score 61). Dansby Swanson continued his hot stretch. The Cubs improved to 51-40 and are 7-3 over their last 10 games.

**Relevance:** The game recap is always the first tweet. Fans wake up wanting to know what happened. A win fuels morning momentum content.

**Key angles:**
1. Boyd's quality start — game score 61, strong enough to keep Cubs in the win
2. Swanson's hot bat — 9-for-22 over last 6 games as a stat hook
3. Cubs 7-3 in last 10 — momentum angle for the win streak
4. Orioles 42-50 — context on the opponent's fall
5. Score-first format (Cubs won 5-2) with stat layering

**Headline options:**
- "Cubs Beat Orioles 5-2 in Baltimore" (news-style)
- "Boyd Delivers. Cubs Cruise to 5-2 Win." (voice-style)
- "Four Straight Wins — Boyd and Swanson Lead Cubs Past Baltimore" (momentum)

**Tone:** Informative → Passionate. Win energy with stat grounding.

---

### STORY 2: Cubs Rolling — 16-6 Since June 10

**Freshness tags:** hot-streak, best-in-MLB, momentum

**Summary:** Since June 10, the Cubs have posted a 16-6 record — the best mark in MLB over that span. At 51-40, this isn't a fluke team finding its footing; it's a team that's been playing championship-caliber baseball for the past four weeks.

**Relevance:** Bold takes drive engagement. Cubs fans want to feel vindicated about this team.

**Key angles:**
1. 16-6 since June 10 as the stat anchor
2. "Best in MLB" framing — but this is a superlative from AI summaries. Will hedge slightly: "near the top of baseball" unless verified. Flag for fact-check.
3. Context: This stretch includes a rotation missing 5 starters — makes it even more impressive
4. Rival comparison: Cardinals have been fading, Brewers dominating — Cubs are the wild card standout
5. Forward-looking: If this team is this good injured, what happens when the rotation comes back?

**Headline options:**
- "16-6 Since June 10 — The Cubs Are the Hottest Team in Baseball" (bold)
- "Nobody Is Hotter Than the Cubs Right Now" (engagement)
- "51 Wins. 5 Rotation Arms on the IL. This Cubs Team Is Built Different." (voice)

**Tone:** Bold / Passionate. Peak enthusiasm.

---

### STORY 3: Wild Card Watch — Cardinals Losing Ground

**Freshness tags:** standings, wild-card, Cardinals-falling

**Summary:** The Cubs (51-40) hold the No. 2 NL Wild Card spot. The Cardinals dropped their July 7 game to the Brewers 4-3 and continue to fade — now approximately 4 games back in the wild card race. The Brewers are running away with the NL Central, which means Cubs fans should want that No. 2 WC spot to be secure.

**Relevance:** Rival jabs + standings context = dual-purpose tweet. Cardinals shade is always on-brand.

**Key angles:**
1. Cubs record (51-40) as the anchor stat
2. Cardinals lost to Brewers — continuing to fade
3. Cardinals record as the contrast (approximately 4 games back)
4. Three wild card spots — Cubs position is comfortable but not secure
5. Phillies and Marlins also in the race — context needed

**Headline options:**
- "Cubs 51-40. Cardinals? Falling Fast." (jab)
- "Wild Card Update: Cubs Hold. Cards Fold." (rhythmic bold take)
- "While the Cubs Are Rolling, the Cardinals Are Stumbling" (comparative)

**Tone:** Informative with a rival jab edge.

---

### STORY 4: Trade Deadline — Joe Ryan Is the Target

**Freshness tags:** trade-deadline, Joe-Ryan, rotation-need

**Summary:** The 2026 MLB Trade Deadline is August 3 — 26 days away. With five starters on the IL, the Cubs need rotation reinforcement badly. Joe Ryan (Twins, 3.36 ERA, 2.82 FIP, 104.1 IP) is emerging as the leading target — he's a legitimate top-of-rotation arm with one more year of team control after 2026.

**Relevance:** Trade deadline content is Tier 2 on the seasonal calendar. Cubs fans are hungry for any real trade reporting. Joe Ryan is a specific, exciting name.

**Key angles:**
1. August 3 deadline date — 26 days of urgency
2. Joe Ryan stats as the hook (ERA + FIP together = elite framing)
3. Cubs' rotation situation: 5 starters on IL = most in baseball context
4. Ryan's 2027 control year makes this more than a rental
5. Compare to the rentals-only approach: why Ryan is different

**Headline options:**
- "Joe Ryan. 3.36 ERA. 2.82 FIP. Cubs, Get This Done." (bold/stat-heavy)
- "26 Days to the Deadline — The Cubs Need Joe Ryan" (urgency)
- "Cubs' Trade Target Is Clear: Joe Ryan Is the Missing Piece" (clear statement)

**Tone:** Bold / Analytical. Stats + strong take.

---

### STORY 5: Game 2 Preview — Rea vs Kremer

**Freshness tags:** game-preview, Colin-Rea, Camden-Yards

**Summary:** Game 2 of the Baltimore series tips off at 5:35 PM CT. Colin Rea (6-5, 4.74 ERA) takes the mound for the Cubs against Dean Kremer (1-1, 3.18 ERA), who has been sharp since returning from a quad strain. Cubs are rolling at 51-40; Orioles are 11.5 games back and searching for answers.

**Relevance:** Standard pre-game content. Fans planning to watch need the matchup and time.

**Key angles:**
1. Rea vs Kremer matchup with specific stats
2. Orioles context (42-50, 11.5 games back) — they're down
3. Cubs' hot stretch as the opener
4. 5:35 PM CT on Marquee
5. Cubs chance to take 2-of-3 in the series

**Headline options:**
- "Cubs-Orioles Game 2: Rea vs Kremer, 5:35 PM CT — Let's Finish This" (fan energy)
- "Game 2 in Baltimore. Cubs Roll Out Colin Rea vs a Kremer Comeback." (informative)
- "Rea Takes the Ball Tonight. Cubs Look to Go Up 2-0 in the Series." (clean)

**Tone:** Informative + Pre-game hype.

---

### STORY 6: Injury Roundup — Taillon Confirmed Post-ASB; Roberts on IL

**Freshness tags:** Taillon-timeline, Roberts-IL, injury-roundup

**Summary:** The Cubs' injury situation evolved overnight: Jameson Taillon (hamstring) is now confirmed to return AFTER the All-Star break — not before, despite earlier hope. His rehab start (3.1 IP, 1 ER) went well enough to set up a second outing before returning. Wyatt Roberts hit the 15-day IL with forearm inflammation, and Jordan Milner is out 4-6 weeks post-appendectomy.

**Relevance:** Fans tracking rotation health want the latest. The Taillon update is a meaningful shift (was pre-ASB hope, now confirmed post-ASB).

**Key angles:**
1. Taillon update: rehab start stats (3.1 IP, 1 ER) + post-ASB return = the FOLLOW-UP hook
2. Roberts on 15-day IL (forearm) = roster opening that could bring up Antoine Kelly
3. Milner timeline (appendectomy = 4-6 weeks)
4. Cumulative injury context: 5 starters, multiple bullpen arms down
5. Silver lining: even without them, Cubs are 51-40

**Headline options:**
- "Taillon Update: One More Rehab Start, Then Post-All-Star Return" (news-style)
- "More Cubs Injury News: Roberts on IL, Taillon Timeline Shifts" (roster roundup)
- "Cubs Are 51-40 With 5 Rotation Arms Out. Let That Sink In." (bold/passionate)

**Tone:** Informative (primary) with some bold framing on the silver lining.

---

### STORY 7: Antoine Kelly — Iowa Cubs Lefty Worth Watching

**Freshness tags:** Antoine-Kelly, prospect-callup, Iowa-Cubs

**Summary:** Acquired from the Dodgers in June, lefty reliever Antoine Kelly has been one of the most dominant arms at Triple-A Iowa — posting a sub-1.00 ERA in 13+ innings with a fastball touching triple digits and a strikeout rate above 27%. With Wyatt Roberts on the 15-day IL, there's now a roster opening, and Kelly is the most logical bullpen callup.

**Relevance:** Prospect content + roster move speculation. Owen Ayers is also thriving at Double-A (21 HRs) as supporting color.

**Key angles:**
1. Kelly's ERA as the stat anchor (sub-1.00 is eye-catching)
2. The acquisition context: Dodgers trade = Cubs identified him as hidden gem
3. Roberts' IL = roster opening
4. Fastball velocity as the scouting hook
5. Mention Ayers as bonus color (raking at Double-A)

**Headline options:**
- "Antoine Kelly's Iowa ERA Is Under 1.00. It's Time." (bold callup take)
- "Cubs Prospect Watch: The Lefty From Dodgers May Be Ready for the Bigs" (news)
- "With Roberts on the IL, Antoine Kelly's Callup Window Just Opened" (news + hook)

**Tone:** Feature/Prospect. Enthusiastic but grounded in stats.
