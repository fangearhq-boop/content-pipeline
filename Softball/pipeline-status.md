# Softball Pipeline Status

## Last Run
- **Date**: 2026-03-26
- **Steps Completed**: 1-8 (Full pipeline — research, brief, facts, analysis, X posts, articles, fact-check, traffic, compile, dashboard, export)
- **Dashboard Published**: Yes — https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- **GitHub Pages Status**: built (workflow deployment)
- **Issues**: None. Dashboard generator now escapes `</` in JSON to fix script parsing bug from yesterday.

## Deploy Info
- **Repo**: `fangearhq-boop/ilovesoftball-dashboards`
- **Build Type**: workflow (GitHub Actions)
- **Has .nojekyll**: Yes
- **Has deploy workflow**: Yes (`.github/workflows/deploy-pages.yml`)
- **Pages URL**: https://fangearhq-boop.github.io/ilovesoftball-dashboards/

## Recent Issues & Fixes
| Date | Issue | Fix | Status |
|------|-------|-----|--------|
| 2026-03-05 | Pages legacy builds erroring | Switched to workflow build type + added deploy-pages.yml | Resolved |
| 2026-03-05 | TOBI export button broken | Moved parsePostingTime to outer scope in dashboard template | Resolved |
| 2026-03-05 | index.html not showing March 5 | Deploy failure from legacy builds; fixed by workflow switch | Resolved |

## Pipeline Run Log
<!-- Append newest at top -->

### 2026-03-24
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 9 text, Articles: 5
- Fact-check: 0 char-limit violations. 0 consistency errors.
- Traffic: 1,899 softball pv (7d), 4,667 softball pv (30d)
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Key stories: Florida takes series from #1 Tennessee Rothrock CG 3-2 (P10), Texas rises to #1 26-game streak (P10), Oklahoma sweeps Ole Miss Emerling pinch-hit grand slam Wells HR #25 (P9), Alabama survives Missouri 4-3 rubber match (P7), Tech sweeps UCF 30-2 (P7), GCU at #11 Arizona today (P6), SEC standings Texas 7-0 leads (P5)
- Notes: Full pipeline with articles and traffic data. All agents completed successfully.

### 2026-03-22
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 9 text (2+2+1+1+1+1+1)
- Fact-check: 89 claims extracted. 0 char-limit violations (6 fixed on first pass). 0 consistency errors (FB/articles/images not part of this pipeline).
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Key stories: Texas 26 straight program record run-rules Baylor 11-0 in Waco Kavan 10 K CG (P10), Wells #23 and #24 HR OU run-rules Ole Miss 10-0 6 from freshman record (P10), Florida beats #1 Tennessee 5-2 rubber match TODAY noon ESPN2 (P9), Missouri upsets #4 Alabama 5-2 first SEC win (P8), Tech run-rules UCF 9-0 Terry 12-0 clinches series (P7), Torres NCAA record 14 consecutive hits FSU (P7), GCU 32-1 clinches SJSU series (P5)
- Notes: Full pipeline completed. All scripts ran successfully. Subagent wrote story analysis in background.

### 2026-03-20
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 9 text
- Fact-check: 56 claims extracted. 0 char-limit violations. 0 consistency errors.
- Key stories: Texas goes for 25th straight program record vs #24 Baylor tonight (P10), #1 Tennessee at #5 Florida opens in Gainesville Pickens vs Rothrock (P9), Wells 22 HR sole national leader 8 from freshman record (P7), #3 Tech at #21 UCF Big 12 showdown in Orlando (P7), GCU 30-1 bounce-back vs SJSU (P6), #4 Alabama at Missouri Briski rolling (P6), Full weekend conference slate preview (P5)
- Notes: Steps 1-3 completed (research, brief, stories, X posts). FB posts, articles, images, dashboard pending.

### 2026-03-19
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 10 text + 7 image concepts, FB posts: 7, Image concepts: 7, Articles: 5
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 158 claims extracted. 0 char-limit violations. 0 consistency errors (Story 5 article optional — 5 articles meet minimum).
- Key stories: Wells HR #22 sole national leader OU 15-0 Memphis 8 from freshman record (P10), #1 Tennessee at #8 Florida this weekend Pickens vs Rothrock (P9), Texas one win from breaking 2006 record vs Baylor Friday (P8), GCU 30-1 first games after first loss hosts SJSU (P7), Week 7 preview Tech at UCF (P6), NCAA stat leaders midseason Polar .598 Wells Johnson 0.42 ERA (P6), Todd Judge resigns Utah State mid-season (P5)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-18
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 9 text + 6 image concepts, FB posts: 7, Image concepts: 7, Articles: 5
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 144 claims extracted. 0 char-limit violations. 1 consistency note (Story 6 article optional — 5 articles meet minimum).
- Key stories: GCU undefeated run ends at 30 lost to #21 OSU 10-5 Hasler 2 three-run HRs (P10), NFCA/ESPN polls Texas jumps to #2 full reshuffling (P9), Texas one win from breaking 2006 record vs Baylor Friday (P8), Hasler's 2 bombs end GCU's perfect season (P7), Alabama beats ULM 4-1 now 27-1 (P6), Jensen ESPN POTW (P6), SEC/Big 12 Week 3 preview (P5)
- Notes: Full pipeline completed. All scripts ran successfully.

### 2026-03-17
- Stories: 7 (2 Tier 1, 4 Tier 2, 1 Tier 3)
- X posts: 9 text + 6 image concepts, FB posts: 7, Image concepts: 7, Articles: 5
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 199 claims extracted. 0 char-limit violations. 1 consistency note (Story 6 article optional — 5 articles meet minimum).
- Key stories: GCU 30-0 at #15 Oklahoma State tonight (P10), NFCA poll reshuffling after Tennessee/Alabama both lost Saturday (P9), Texas one win from 25th-straight program record vs Baylor Friday (P8), Wells 21 HR freshman record watch 9 from 30 (P7), Briski 24 K in 2 CGs All-American case (P7), SEC Week 3 preview (P6), Conference standings watch (P5)
- Notes: Full pipeline completed including dashboard publish. All scripts ran successfully.

### 2026-03-16
- Stories: 7 (3 Tier 1, 2 Tier 2, 1 Tier 2 recap, 1 Tier 3)
- X posts: 12 text + 7 image, FB posts: 7, Image concepts: 13, Articles: 5
- Dashboard: Pending (run scripts manually — Bash permission issue)
- Key stories: Tennessee first loss at 26-0 Troutman walk-off + Pickens returns 700th K (P10), Alabama first loss 14-9 to Arkansas + Briski 24 K in 2 CGs (P10), Texas ties 24-game program record sweep Ole Miss (P10), Oklahoma sweeps Auburn Wells 21 HR leads nation (P9), GCU 30-0 sole unbeaten in D1 (P9), TTU bounces back series win over Arizona (P8), Unbeaten watch over both lost same day (P7)
- Notes: Steps 1-9 and 12 completed. Steps 10, 10b, 13, 15 require manual Python execution (see commands in Last Run section).

### 2026-03-14
- Stories: 7 (3 Tier 1, 2 Tier 2, 1 Tier 2 analysis, 1 Tier 3)
- X posts: 11, FB posts: 7, Image concepts: 11, Articles: 5
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 116 claims extracted. 2 char-limit violations fixed. 0 consistency errors (Story 6 article optional — 5 articles meet minimum).
- Key stories: Arizona run-rules #2 TTU 9-0 Jenkins grand slam 7 RBI (P10), Tennessee 26-0 Butt 9th-inning 3-run HR at MSU (P10), Alabama 25-0 Briski 14 K vs #9 Arkansas (P10), Oklahoma 13-5 Auburn Garcia 4-for-4 2 HR SEC opener (P9), Texas 22-game streak Kavan 12 K (P9), Three unbeatens UT/Bama/GCU (P8), Belmont Johnson 19 K shutout (P7)
- Notes: Full content pipeline completed. Image production (Step 11) available for user review.

### 2026-03-13
- Stories: 7 (3 Tier 1, 2 Tier 2, 1 Tier 2 analysis, 1 Tier 3)
- X posts: 11, FB posts: 7, Image concepts: 11, Articles: 5
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 42 claims checked, 41 verified, 1 plausible. 0 char-limit violations. 0 consistency errors.
- Key stories: Tennessee 25-0 program record set (P10), Alabama 24-0 hosts #9 Arkansas tonight (P10), Arizona at #2 TTU Canady 45K from 1000 (P9), Oklahoma 108 HR SEC opener vs Auburn (P9), Texas 21-game streak SEC home opener vs Ole Miss (P8), Two unbeatens collision course (P8), SEC/Big 12 Week 2 preview (P7)
- Notes: Full content pipeline completed. Image production (Step 11) available for user review.

### 2026-03-12
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10, FB posts: 7, Image concepts: 7, Articles: 5
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 133 claims extracted. 2 char-limit violations fixed on first pass. Story 6 article optional (5 articles meet minimum).
- Key stories: Tennessee resumes at Lipscomb for 25-0 program record (P10), Texas 21-game win streak Stewart walkoff grand slam (P9), Oklahoma 5 HR vs Tulsa 108 on season (P9), Arizona at #2 TTU Canady 45K from 1000 (P8), Alabama 24-0 Arkansas looms (P7), Tennessee-Alabama collision course (P8)
- Notes: Full content pipeline completed. Image production (Step 11) available for user review.

### 2026-03-11
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 12, FB posts: 7, Image concepts: 7, Articles: 6
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 152 claims extracted, all verified. 1 consistency fix (missing Story 6 article added).
- Key stories: Tennessee 24-0 program record (P10), Alabama 24-0 two unbeatens (P9), SEC weekly awards sweep (P9), Texas 20-game streak Kavan (P8), Canady back-to-back Big 12 PITW (P7), Virginia Tech Power 10 (P6)
- Notes: Full content pipeline completed. Image production (Step 11) available for user review.

### 2026-03-10
- Stories: 7 (3 Tier 1, 3 Tier 2, 1 Tier 3)
- X posts: 10, FB posts: 7, Image concepts: 7, Articles: 5
- Dashboard: Published, live at https://fangearhq-boop.github.io/ilovesoftball-dashboards/
- Fact-check: 137 claims extracted, all verified. 3 char-limit violations fixed.
- Key stories: Tennessee 23-0 sweep LSU (P10), Alabama 23-0 sweep Ole Miss (P9), Texas 20-game streak (P9), NFCA Poll (P8)
- Notes: Full content pipeline completed. Image production (Step 11) available for user review.

### 2026-03-05
- Stories: 7 (Tennessee blowout, Big 12, SEC preview, Alabama-Ole Miss, undefeated watch, GCU spotlight, Anna Dew perfect game)
- X posts: 12, FB posts: 7, Image concepts: 7, Articles: 5+
- Dashboard: Published, live at Pages URL
- PostPlanner export: Generated
- Notes: Full pipeline completed. Switched Pages from legacy to workflow deployment.
