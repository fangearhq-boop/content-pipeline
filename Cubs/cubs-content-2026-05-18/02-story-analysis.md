# Story Analysis — 2026-05-18

---

### Insights applied

**API status:** Both `https://lucid-essence-production-97a5.up.railway.app/api/insights/cubs?days=21` and the series-context endpoint returned HTTP 403. This is the same recurring issue logged in every pipeline run since May 13. `tweet_count=0` fallback applied.

**Performance tuning:** No data available. Fell through entirely to `Cubs/brand-voice.md` defaults:
- 50/50 informative/bold split: Stories 1/3/5 informative-leaning; Stories 2/4/6 bold/hype-leaning.
- Blank line spacing between hook and body, blank line before hashtags (hard requirement).
- Opening style: Stat-backed hook or declarative statement per top performer patterns from prior sessions.
- ALL CAPS used on 1-2 words max: "TONIGHT," "FOURTEEN" style.
- No engagement questions. No filler slots.

No format changes possible without valid insights data. Would adjust by bucket (opening style, hashtag count, has_stat) if data returned.

---

### Series context

**API status:** `https://lucid-essence-production-97a5.up.railway.app/api/cubs/series-context` returned HTTP 403. Default fallback: `off_day=true`. **This fallback is INCORRECT** — confirmed via web research.

**Web research finding:** Cubs open a 3-game home series vs the Milwaukee Brewers on Monday May 18 at 6:40 PM CT at Wrigley Field. `is_series_start_today=TRUE`.

**Conflict flag:** The system prompt instructs "RESERVE the 7:00 AM CT slot for a 'Series Preview' story" when `is_series_start_today=true`. However, `research-playbook.md` (engine doc) under Posting Priority states: "Game recaps — always in the first available slot (7:00 AM for night games, 10:00 PM for just-ended games)." Engine docs win per the pipeline prompt: "If this prompt conflicts with _engine/SKILL.md or Cubs/SKILL.md, the niche+engine docs win." 

**Resolution:** The Crosstown Classic finale (White Sox 9-8, yesterday afternoon) recap goes to 7:00 AM per the research-playbook. The series preview moves to 8:15 AM — still excellent morning placement, nearly 11 hours before first pitch. Both stories get morning priority slots. No content is deprioritized.

---

### STORY 1: White Sox 9-8 Cubs — Crosstown Walkoff Recap

**Angle selection:** The game ending — Quero's walkoff HR after Conforto's heroic 9th-inning comeback — is the emotional core. Lead with the dramatic arc, not the box score. Cubs had the lead and blew it. The "since 2022" detail adds historical weight. Tone: gut-punch informative with a dry one-liner kicker. The Cubs fanbase remembers White Sox series losses differently than Cardinals ones — it stings more for being the city rival.

**Hook decision:** "Cubs had the lead in the 10th" — leads with narrative tension. Resists the temptation to lead with the final score, which is more impactful after the story lands.

**Format:** 3-paragraph structure. Para 1 sets the scene (comeback attempt). Para 2 delivers the blow (Quero HR). Para 3 gives the historical context + kicker.

---

### STORY 2: Brewers Series Preview — Imanaga vs Sproat

**Angle selection:** The matchup angle is strong on two levels: (1) Imanaga vs Sproat is a clear mismatch on paper (2.32 ERA vs 5.75 ERA), which gives Cubs fans confidence but also raises the "don't overlook" tension. (2) It's a division series with real standings stakes — Cardinals are 1.5 GB.

**Leading the tweet:** Per the DO NOT rule: "Do NOT lead a series-preview tweet with anything other than the matchup itself (opponent + length + location)." Opening with "3 games at Wrigley against the Brewers" satisfies: opponent (Brewers), length (3 games), location (Wrigley).

**Stakes:** Cubs lead the NL Central. Cardinals lurking at 1.5 GB. Brewers chasing. "Division separation" is the concrete stake.

**Pitcher angles:** Imanaga's ERA is the key data point. Sproat's ERA (5.75) sets up the "favorable matchup" narrative but should not be dwelt on — Cubs fans have seen that go wrong before.

---

### STORY 3: Roster Moves — Blach, Assad, Harvey

**Angle selection:** This is an informative transaction story, but the *why* is the real angle: the Cubs are patching depth holes created by the Boyd meniscus injury and Harvey's extended timeline. Ty Blach is a known commodity — 33-year-old southpaw, 5+ years of MLB experience, pitching depth. Assad going down shows the Cubs are comfortable with his service time and rotation depth at Iowa. Harvey to 60-day = he's not coming back until deep summer.

**Frame:** "Bullpen shuffle" + Boyd context = the story makes sense in one read. Don't need to over-explain Blach's track record in a tweet.

---

### STORY 4: Ben Brown vs Misiorowski

**Angle selection:** This is the most analytically interesting game of the series. Brown has been excellent (1.60 ERA, rotation revelation) and his career record vs the Brewers is genuinely good (2-0, 19 K, 2 ER in 18 IP). Misiorowski is the Brewers' legitimately elite arm — MLB leader in K/9. Framing this as a must-watch matchup serves the brand voice's "stat-backed bold take" persona.

**Stat selection:** Use Brown's ERA (1.60) + career Brewers record (2-0, 19 K/18 IP) — both HIGH confidence. For Misiorowski, use "MLB leader in K/9 (14.0)" — HIGH confidence. Avoid the 18.1 scoreless innings stat (MEDIUM, single source).

**FOLLOW-UP framing:** This directly follows the May 16 Brown story ("Next Start Tuesday, Pitch Count Expanding"). That story's follow-up note said "Tuesday's start line; pitch count escalation; Brewers matchup result." This tweet delivers on that setup.

---

### STORY 5: Peralta June 1 Clock

**Angle selection:** The calendar creates its own urgency — June 1 is 14 days away and counting. The Taillon + Boyd storylines since May 16 make this more urgent than when it was first covered May 15. The "triage not deadline" framing is strong and consistent with earlier coverage.

**Avoid:** Repeating "August 3 deadline" without context — the point is that the Cubs can't wait until August. Lead with the June 1 Mets date.

---

### STORY 6: Game Time Hype

**Angle selection:** Short, punchy pre-game energy tweet. Goes out 10 minutes before first pitch. Simple. No stats needed — Imanaga's name is enough.
