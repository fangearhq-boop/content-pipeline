# Story Analysis — June 12, 2026

---

### Insights Applied

**Significant findings read from Cubs/_data/insights.json (generated 2026-06-12T08:30:00Z, measured_tweet_count=54):**

Three findings cleared all gates (n≥8, Mann-Whitney U p<0.05, |Cliff's delta|≥0.20):

**Finding 1 — has_stat=True (effect: medium, Cliff's delta=0.435)**
- Winner: True (median 99.5 impressions) vs Loser: False (median 45.5 impressions)
- ~2.2x impression gap. Strongest signal in the dataset.
- **Applied:** Every tweet today contains at least one concrete, verifiable stat. Examples: "35-34", "28-41", "1.74 ERA", "0.88 WHIP", "58 K", "10th HR of the season", "9 runs since May 27", "41-23", "10-2". No tweet ships without a number.

**Finding 2 — posting_window=midday_12_18 (effect: small, Cliff's delta=0.32)**
- Winner: midday_12_18 (median 78.5 impressions) vs Loser: not_midday (median 43.5 impressions)
- **Applied:** 5 of 7 slots placed in the 12:00–5:00 PM CT window (12:00, 1:15, 2:30, 3:45, 5:00). The two morning slots (7:00 AM, 9:30 AM) are exceptions — the 7 AM is required by the series-start rule, and 9:30 AM is the first available slot for a Tier 1 game recap that must run before noon.

**Finding 3 — posting_window=morning_06_12 (effect: small, Cliff's delta=0.32)**
- Loser: morning_06_12 (median 43.5 impressions)
- **Applied:** Morning slots minimized to 2. Only the mandatory series-preview (7:00 AM) and the must-cover Tier 1 game recap (9:30 AM) break this rule. No optional morning slots added. The 8:15 AM "bold take" slot from the niche-config default schedule is skipped.

**No raw_buckets or per-bucket means were used to make decisions.** Only significant_findings were applied.

Note: `has_allcaps` was a winner in prior snapshots but is NOT in today's significant_findings. Per mandate: not applied.

---

### Series Context

**is_series_start_today=true**

Cubs (35-34) open a 3-game road series at Oracle Park tonight vs the San Francisco Giants (28-41). Game 1: 9:15 PM CT. Game 2: Sat 9:05 PM CT. Game 3: Sun 2:10 PM CT.

**Mandatory slot reserved:** 7:00 AM CT → Series Preview tweet. Lead: opponent + series length + location. Kicker: stakes (wild card, Cubs record, Assad starting).

**Series notes:**
- Giants are a true bottom-third team at 28-41 under first-year manager Tony Vitello
- This series is a buyer's audition for the Cubs' offense after weeks of under-performing
- Ben Brown starts Saturday — the series' marquee pitching matchup

---

### Story-by-Story Analysis

#### Story 1: Series Preview — Cubs at Oracle Park (7:00 AM)
- **Angle:** Matchup-led: opponent, series length, location. Kicker: Assad starting, Cubs' wild card context.
- **Tweet type:** Informative
- **Insight-adjusted:** Stats included (28-41, 35-34, 9:15 PM CT). No leading emoji. Morning slot is required per series-start rule.

#### Story 2: Game Recap — Cubs 9, Rockies 3 (9:30 AM)
- **Angle:** Score-led. Suzuki slam in the 4th is the hook. "Snapped a 3-game skid" is the narrative beat.
- **Tweet type:** Informative / game recap
- **Insight-adjusted:** Stats-dense (grand slam, 10th HR, 4th win, 9 runs, May 27 reference). Morning is a loser window but this is Tier 1 must-cover content — the first available slot after the mandatory 7 AM.

#### Story 3: Ben Brown — Saturday's Ace (12:00 PM)
- **Angle:** Anchor framing — Brown as the most reliable arm heading into this road trip. Saturday start is the timely hook.
- **Tweet type:** Bold/Informative
- **Insight-adjusted:** Strong stat density (1.74 ERA, 0.88 WHIP, 58 K, 0 HRs). Midday window (winner). No leading emoji.

#### Story 4: Rotation Crisis + Deadline (1:15 PM)
- **Angle:** Alarm bell. Four starters unavailable simultaneously. Names linked (Detmers, Ryan, Alcantara) add specificity. August 3 deadline = 52 days.
- **Tweet type:** Bold analysis
- **Insight-adjusted:** Stats included (4 starters out, August 3, 52 days). Midday window (winner). No leading emoji.
- **Differentiation from Story 3:** Story 3 is about who IS available (Brown as the answer). Story 4 is about the structural problem and future fix.

#### Story 5: Wild Card Reality (2:30 PM)
- **Angle:** After the win, honest accounting of where the Cubs stand. 35-34 feels better than 34-34 but doesn't change the math vs Brewers.
- **Tweet type:** Informative/standings
- **Insight-adjusted:** Stats-dense (35-34, 41-23, 28-41). Midday window (winner). No leading emoji.

#### Story 6: Iowa Cubs + Kelly (3:45 PM)
- **Angle:** Prospect pipeline as the quiet depth story — Iowa winning while the big club navigates injuries.
- **Tweet type:** Informative
- **Insight-adjusted:** Stats included (10-2 win). Midday window (winner). No leading emoji.

#### Story 7: Pre-Game Hype — Tonight at Oracle Park (5:00 PM)
- **Angle:** Accountability framing. Giants' Tony Vitello and 28-41 record = this is a team the Cubs should beat. Focus on the test, not just the schedule.
- **Tweet type:** Bold/hype
- **Insight-adjusted:** Stats included (28-41, 3 games). Still inside midday_12_18 window at 5:00 PM CT. No leading emoji.
- **Differentiation from Story 1 (7 AM preview):** Story 1 = informational setup (matchup, Assad, time). Story 7 = accountability challenge framing (Tony Vitello's inexperience, the test of beating bad teams consistently).

---

### 50/50 Mix Check

| Tweet | Type |
|-------|------|
| 1 — Series Preview | Informative |
| 2 — Game Recap | Informative |
| 3 — Ben Brown | Bold/Informative |
| 4 — Rotation Crisis | Bold |
| 5 — Wild Card | Informative |
| 6 — Iowa Prospects | Informative |
| 7 — Pre-Game Hype | Bold |

3 bold / 4 informative = roughly 43/57 split. Skewed slightly informative today, driven by two must-cover Tier 1 news posts (game recap + series preview) and one standings update. All slots have genuine news hooks — no filler.

---

### Slots Skipped and Why

- **8:15 AM** — morning window is a loser per insights; no standalone bold take compelling enough to override the signal
- **10:45 AM** — morning window continues; would create three morning slots total, overcrowding the loser window
- **6:30 PM** — too close to 5:00 PM pre-game hype (60-min rule); game also doesn't start until 9:15 PM CT
- **8:00 PM** — in-game reaction; game starts 9:15 PM CT, not available at pipeline time
- **9:30 PM** — post-game recap; game starts 9:15 PM CT, not available at pipeline time
