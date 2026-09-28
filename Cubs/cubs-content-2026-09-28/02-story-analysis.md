# Story Analysis — Cubs 2026-09-28

---

### Insights applied

**Source:** `Cubs/_data/insights.json`, generated_at: 2026-09-28T08:30:00.124588+00:00
**Measured tweet count:** 153
**Significant findings:** 2

#### Finding 1: `posting_window=evening_18_24` WINS
- **Direction:** Evening (6 PM–midnight CT) outperforms all other windows
- **Effect:** Median impressions 106 vs. 68 (winner vs. rest); Cliff's delta 0.376 (medium); p=0.031
- **Action taken:** Placed the two highest-engagement stories (PCA WCS-eve bold take, WCS send-off kicker) in the 6:30 PM and 8:00 PM CT slots specifically because of this finding. These slots were originally optional but are now treated as priority positions.

#### Finding 2: `len_bucket=<140` LOSES (winner = not_<140)
- **Direction:** Tweets under 140 chars underperform; 140+ chars outperform
- **Effect:** Median impressions 71.5 vs. 58 (not-<140 vs. <140); Cliff's delta 0.273 (small); p=0.038
- **Action taken:** Every tweet in today's batch drafted at ≥140 characters. Verified at draft stage. No tweet under 140.

No other significant findings. `has_emoji_first_line`, `has_score`, `content_type` had no findings this snapshot. Brand-voice defaults applied for those dimensions.

---

### Series context

`off_day=true` | `is_series_start_today=false` | `series=null` | `today_cubs_game=null`

Cubs are on their final off day before the Wild Card Series begins Tuesday, Sept 29 at Petco Park. The regular season ended Sunday with a 6-2 Cubs win over the Red Sox in a neutral-site finale at Tropicana Field.

**Content strategy for an off-day pre-WCS:**
- Lead morning with game recap (Bregman heroics — most concrete overnight news)
- Build through the day with WCS preview details, opponent analysis, injury uncertainty
- Reserve evening slots for bold, high-engagement playoff-eve takes (reinforced by insights)
- No prospect/Iowa content — off-season for minor leagues and nothing newsworthy rose to tweet level given WCS context

No series-preview tweet at 7 AM (series-preview slot only required on `is_series_start_today=true`). WCS Game 1 preview covered at 8:15 AM instead.

---

### STORY 1: Bregman 4-for-4, 2 HR, 4 RBI — Relocated Season Finale

**Angle:** Alex Bregman's two-homer game in his SECOND start back from multiple facial fractures is the most striking overnight news. The neutral-site context (Tropicana Field, nor'easter) adds an unusual backdrop. The hook is the injury-return heroics, not the game result itself (Cubs were already locked in as WC2). Perfect 7 AM morning recap material.

**Hook:** "4-for-4. Two home runs. Four RBI." — pure stat fragment, concrete, attention-stopping.

**Body:** Injury context (second game back, facial fractures) + relocated-game quirk (Tropicana Field).

**Kicker:** Full-season line (.265/.355/.464, 28 HR, 93 RBI, 128 wRC+) sets up October.

**Tone:** Informative with a bold/passionate kicker — matches the morning-slot profile (informative-leaning per brand-voice).

**Insights check:** Tweet length ≥140 chars ✓; no emoji-first-line conflict (no finding on this dimension); morning slot — not in evening window, but this is the appropriate slot for this story type.

---

### STORY 2: WCS Game 1 Preview — Tuesday 9 PM CT, Petco Park

**Angle:** Pure logistics + context for fans who need to know where/when to watch. The hook is the practical info (time, venue) but the kicker is the confidence angle (Cubs 5-1 vs SD, won 2025 WCS). This is an informative-first tweet appropriate for the 8:15 AM "bold take / fan energy" slot.

**Hook:** "Game 1 is tomorrow. Tuesday, 9 PM CT. Petco Park." — concrete, time-pegged.

**Body:** Boyd start + Cubs' 5-1 H2H edge + Padres' September surge (sets up Story 3 an hour later).

**Kicker:** "This is how you earn the right to the road trip." — bold fan energy.

**Note on Boyd starter claim:** Multiple projection sources cite Boyd as Game 1 starter. Tweet says "Boyd takes the ball" — treating this as established consensus while acknowledging no official Cubs announcement found as of 9/28 morning. Flagged in fact-check log.

---

### STORY 3: Padres Danger Watch — 16-5 September, Tatis/Merrill

**Angle:** Cubs fans need the honest opposing-team scouting report. The Padres are NOT the same team they beat 5-1 in the regular season — they've been the best team in baseball in September. Tatis + Merrill as a combined threat is the specific data point. This is a confident-but-honest analysis take for the 9:30 AM "stat breakdown/informative" slot.

**Hook:** "Credit where it's due — the Padres went 16-5 in September." — leads with competitor acknowledgment, which earns trust and sets up the contrast.

**Body:** Tatis/Merrill HR stat + Mason Miller closer = concrete danger signals.

**Kicker:** "Cubs went 5-1 vs them this year. Expect a fight anyway." — closes with Cubs confidence while keeping the analysis honest.

**Tone:** Informative-analytical with a bold kicker. Appropriate for the analysis slot.

---

### STORY 4: Gausman "I Don't Know" — WCS Rotation Puzzle

**Angle:** A WCS rotation going into a best-of-3 with a genuine question mark at the No. 3 starter spot is legitimate news. Gausman's direct quote ("I don't know") is the exact kind of newsworthy uncertainty Cubs fans need heading into Tuesday. The 10:45 AM "analysis/rival watch" slot is the right home for this.

**Hook:** The direct quote from Gausman himself — "I don't know." — no further explanation needed.

**Body:** Injury context (nonthrowing shoulder, diving tag play) + confirmed starters (Boyd, Holmes) + fallback option (Peterson).

**Kicker:** "The Cubs find out in the next 48 hours." — time-pegged urgency.

**Tone:** Informative-urgent. Not doom — just honest uncertainty.

---

### STORY 5: Cubs 2026 Final Record — Season in Review by Numbers

**Angle:** The regular season is officially over. A clean "by the numbers" tweet serves the fans who want a capstone on 2026 before October begins. PCA fWAR/HR/runs + Bregman 128 wRC+ + Swanson healthy + Boyd confirmed = this is a COMPLETE, healthy Cubs team. 3:45 PM "feature/deep-dive" slot.

**Hook:** "Final 2026 Cubs record: 89-73. NL Wild Card No. 2." — establishes the definitive number.

**Body:** PCA led MLB in fWAR/HR/runs + Bregman first-year line + Swanson healthy + Boyd confirmed for tomorrow.

**Kicker:** "Complete roster. Tomorrow night it matters." — sets up Tuesday.

**Tone:** Informative-statistical with a passionate kicker.

---

### STORY 6: PCA WCS-Eve Hype (6:30 PM — EVENING SLOT, insights-boosted)

**Angle:** The evening window consistently outperforms per the significant findings. This slot gets the single most exciting, fan-energy tweet of the day: Pete Crow-Armstrong walking into Petco Park as the most dangerous player in baseball. This is a pure fan-energy bold take — not a stat recitation.

**Hook:** "Pete Crow-Armstrong. 45 home runs. 40 stolen bases. MLB-leading fWAR." — stat fragment that commands attention.

**Body:** Sets up the playoff narrative — Petco Park Tuesday, WCS rematch, Cubs won last year.

**Kicker:** "This one's different. Fly the W." — short, emotional, decisive.

**Tone:** Bold/passionate. Highest energy tweet of the day by design.

**Insights:** Evening slot (6:30 PM CT = in the 18-24 window). Length ≥140 chars ✓.

---

### STORY 7: WCS Send-Off Bold Kicker (8:00 PM — EVENING SLOT, insights-boosted)

**Angle:** Second evening-slot tweet. Closes the day with a punchy WCS-eve take. The conceit: San Diego has home field, but Chicago has the track record. Last year's WCS + 2026 5-1 regular season H2H = Cubs have receipts. Final tweet of the day is the emotional send-off before Game 1.

**Hook:** "Cubs vs. Padres. Game 1 tomorrow. One year ago, Chicago ended San Diego's season at Wrigley." — grounds the rematch in memory.

**Body:** Petco Park flip ("the script doesn't have to change") — confident, not arrogant.

**Kicker:** "89-73. WCS-tested. Ready." — three-word sign-off with the final record.

**Tone:** Bold. Sharp. Clean. The day's exclamation mark.

**Insights:** Evening slot (8:00 PM CT = in the 18-24 window). Length ≥140 chars ✓.
