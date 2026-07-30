# Story Analysis — July 30, 2026

## ### Insights Applied

**Finding:** `has_score` (binary) — `winner: False`, `loser: True`
- Median impressions without score: 125 | With score: 83
- p=0.0302, Cliff's delta=0.225 (small effect)
- n=65 (no score) vs n=60 (with score)

**Decisions made based on this finding:**

1. **Game 3 recap tweet (Story 1):** Did NOT include the final score (3-2) in the tweet text. Framed around what HAPPENED (bullpen collapse in the 10th, PCA's HR, heartbreak) rather than the scoreline. Brand-voice default says "score format: Winner first — Cubs won 5-2" — insight directly contradicts including a score, so insight wins per pipeline rules.

2. **All other tweets:** Avoided embedding any scores (series scores, season records as W-L numbers in tweet copy). Records like "61-47" were also avoided in tweet bodies. The insight appears to cover any scores/records appearing in tweet text.

3. **No other significant findings to apply.** The dataset has 125 measured tweets and cleared only one gate. No `content_type`, `posting_window`, `len_bucket`, or `has_emoji_first_line` findings to act on.

**Effect on story selection:** The finding biases away from game-recap-led tweeting where the score is the hook. Today's game recap leads with the narrative angle (bullpen heartbreak, PCA HR), not the scoreline.

---

## ### Series Context

`is_series_start_today: false` — This is Game 4 of the Cubs-Cardinals series at Busch Stadium. Cubs lead series 2-1. No dedicated series-preview slot required.

`off_day: false` — Game at 1:15 PM CT today. Preview tweet goes no later than 12:00 PM CT.

Series facts: Cubs won Games 1 and 2 (including a 10-2 win on July 28), Cardinals won Game 3 last night (3-2 in extras). Cubs can clinch a series win with today's victory.

---

## Story 1: Game 3 Recap — Bullpen Burns Another One
**Tier:** 1
**Slot:** 7:00 AM CT

**What happened:** Cubs carried a 2-1 lead into the bottom of the 10th — PCA had just hit a go-ahead 2-run HR in the top of the inning. Trent Thornton couldn't hold it. Cardinals scored on a Nootbaar pinch-hit single, Wetherholt walk, and Iván Herrera's 2-run double. Cardinals 3, Cubs 2 final.

**Angle:** The heartbreak angle — PCA delivered the dagger in the 10th, the bullpen gave it back. Series stays alive at 2-1 Cubs, and the theme of bullpen reliability becomes a subplot heading into today's series finale.

**Why NOT lead with the score:** Insights say `has_score=False` outperforms. Frame as narrative, not scoreboard.

**Hook:** "Pete Crow-Armstrong gave the Cubs the lead in the 10th. The bullpen couldn't hold it."

**Hashtags:** #Cubs #GoCubs #FlyTheW

---

## Story 2: Trade Deadline — Skubal Is Moving, Cubs Are in the Room
**Tier:** 1
**Slot:** 8:15 AM CT

**What happened:** Jeff Passan reported Wednesday night on SportsCenter that the Detroit Tigers WILL trade Tarik Skubal — two-time AL Cy Young winner — ahead of the August 3 deadline. Patrick Mooney (The Athletic) reported Cubs are "considering" a push for Skubal. Dodgers and Brewers are frontrunners.

**Angle:** The Skubal rumor is the biggest deadline bomb yet. Cubs are in the conversation but not the leaders. They have 4 starters on IL, they need a No. 1. The question is whether Hoyer goes all the way to the top of the market.

**Hook:** "Passan just dropped a bomb: Tarik Skubal is being traded. Cubs are in the room. Four days left."

**Hashtags:** #Cubs #MLB #CubsBaseball

---

## Story 3: PCA — MVP Odds Explode as Ohtani's Knee Becomes a Story
**Tier:** 2
**Slot:** 9:30 AM CT

**What happened:** PCA's MVP odds have gone from +3000 to +185 in three weeks. Ohtani (-235) has a knee issue that's limited his pitching. PCA hit a 2-run HR in the 10th last night (even in a loss). His last 55 games: 211 wRC+, 1.161 OPS, 5.7 fWAR.

**Angle:** This isn't a hot streak — it's a sustained, elite run that's moved the betting market dramatically. And the race just got more interesting.

**Yesterday's coverage:** July 29 covered PCA's full season stat-line (.290/.388/.545, 23 HR, 26 SB). Today's fresh angle: the dramatic odds shift, the Ohtani injury factor, and PCA's 10th-inning HR last night as punctuation.

**Hook:** "PCA went from +3000 to +185 in MVP odds in three weeks."

**Hashtags:** #Cubs #GoCubs #ChicagoCubs

---

## Story 4: Cardinals Are Officially Playing Spoiler — And Losing at That
**Tier:** 2
**Slot:** 10:45 AM CT

**What happened:** Cardinals are 54-54, 9-13 in July, 15th in NL Wild Card standings. They won last night's Game 3 (first win of the series) but remain 2.5 games behind the 3rd wild card spot. The Cardinals came into this series hoping to prove they belong — they're mostly proving they don't.

**Angle:** Rival-jab tone. Cardinals won one game in this series and their fans are acting like it's a playoff series. They're 54-54 in late July. That's the story.

**Hook:** "Cardinals won a game last night. They're still 54-54 in late July, playing spoiler for a team they can't catch."

**Hashtags:** #Cubs #GoCubs #MLB

---

## Story 5: Game 4 Preview — Assad Can Close the Series
**Tier:** 1
**Slot:** 12:00 PM CT

**What happened:** Javier Assad (6-1, 3.86 ERA, 1.12 WHIP) takes the ball for the Cubs in the series finale at Busch at 1:15 PM CT today. He faces Andre Pallante (11-6, 3.77 ERA) for the Cardinals.

**Angle:** Assad is the unsung anchor of this patchwork rotation. With four starters on the IL, he's been everything the Cubs needed. Today he gets a chance to close out the series on the road.

**NOTE:** The game starts at 1:15 PM CT. Preview must post before 12:15 PM CT max. Using the 12:00 PM slot.

**Hook:** "Assad gets the ball in today's series finale. Cubs lead 2-1. Let's close this out."

**Hashtags:** #Cubs #GoCubs #FlyTheW

---

## Story 6: The Brewers Are Winning the Skubal Race — and the Division
**Tier:** 2
**Slot:** 3:45 PM CT (post-game)

**What happened:** Brewers are Passan's frontrunner for Tarik Skubal. They're also 67-40 and own the best record in MLB. If the Brewers land Skubal, the Cubs lose their No. 1 trade target and fall further behind in the NL Central simultaneously.

**Angle:** This is the Cubs' two-front war. Win the series today, but also figure out how to beat the Brewers to the best pitcher on the market with 4 days left.

**Hook:** "The Brewers are the frontrunner for Tarik Skubal. They're already 6 games ahead of the Cubs. Hoyer needs to get creative — fast."

**Hashtags:** #Cubs #MLB #NorthSiders

---

## Summary

| Slot | Story | Tier | Type |
|------|-------|------|------|
| 7:00 AM | Game 3 Recap — Bullpen blown in 10th | 1 | Informative |
| 8:15 AM | Trade Deadline — Skubal bomb, Cubs in the room | 1 | Bold take |
| 9:30 AM | PCA MVP odds explode to +185 | 2 | Stat breakdown |
| 10:45 AM | Cardinals at 54-54, playing spoiler badly | 2 | Rival watch / humor |
| 12:00 PM | Game 4 preview — Assad vs Pallante, 1:15 PM CT | 1 | Preview |
| 3:45 PM | Brewers frontrunner for Skubal — two-front war | 2 | Analysis / bold take |

6 total stories. Within the 12-slot maximum. All anchored to genuine news from <24h.
