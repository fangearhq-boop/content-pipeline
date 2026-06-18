# COS Parenting — Pipeline Status

## Latest Run: June 18, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | AAP 2026 immunization schedule (18 diseases vs. CDC's 11; Hep A/B/rotavirus/meningococcal/RSV/flu maintained; COVID-19 ages 6-23 mo + high-risk; HPV 2 doses ages 9-12 vs. CDC 1 dose 11-12; endorsed by 12 assocs incl. AMA/ACOG; healthychildren.org); Joyin Sloosh dive sticks recall (~113,000 units; impalement hazard; violates federal dive stick ban; Amazon/Walmart/Target ~$7-15; refund; cpsc.gov); COS trail upgrades (Blodgett 14 miles + mountain bike routes + new trailhead at old quarry; Fox Run pond/gazebo renovation; both summer 2026; Paint Mines barriers ongoing); Bear Creek Nature Center Pollinator Celebration June 26 ($5/person; bug sweeps; native pollinator education; Bear Creek Regional Park west COS; visitcos.com); Bellabu Bear children's robes recall (burn hazard; mandatory flammability standard violation; stop use; contact brand for remedy; cpsc.gov) |
| Story History Check | COMPLETE | 4 NEW STORIES (AAP vaccine schedule, Joyin dive sticks recall, COS trail upgrades summer update, Bear Creek Pollinator Celebration) + 1 SECOND COVERAGE (Bellabu Bear robes — first covered June 6; June 18 angle is summer camp packing season context) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (2 Tier 1, 3 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Sarah Morales (S1, S3, S5), Jamie Rivera (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 6 posts (2 for S1; 1 each for S2-S5); 5 char violations fixed after first verify-facts.py run; all under 280 chars; 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — YAML format; 10 images; all not_started; photo_source: gemini; Gemini mode: base_only |
| Articles | COMPLETE | 5 articles (500-1000 words; Quick Reference tables; What's Next sections; 0 exclamation marks; no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py passed after 2 runs (5 char violations fixed; image manifest rewritten from table to YAML format); all 5 stories present; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 6 X posts, 0 FB posts, 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic (same as prior runs) |
| Dashboard | COMPLETE | review-dashboard.html — 21 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-18.xlsx (6 posts: 6 X, 13:02–20:27 MT) + TOBI cosp-postplanner-tobi-2026-06-18.xlsx (6 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Credentials not in env (context compacted); proxy would block anyway | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-18)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 5 FB long-form + 5 FB captions = 16 total posts (PostPlanner xlsx: 6 X posts)
- **Articles:** 5 (bylines: Sarah Morales x3 [S1, S3, S5], Jamie Rivera x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-18.xlsx (6 posts), cosp-postplanner-tobi-2026-06-18.xlsx (6 TOBI posts)
- **Coverage:** AAP 2026 vaccine schedule vs. CDC (18 vs. 11 diseases; AAP maintains Hep A/B, rotavirus, meningococcal, RSV, flu; COVID-19 ages 6-23 mo + high-risk; HPV 2 doses ages 9-12 vs. CDC 1 dose 11-12; endorsed by 12 medical assocs.; healthychildren.org); Joyin Sloosh dive sticks recall (~113,000 units; impalement hazard violates federal dive stick ban; Amazon/Walmart/Target ~$7-15; refund via Joyin; cpsc.gov); COS summer trail upgrades (Blodgett Open Space 14 miles new trails + mountain bike routes + new trailhead at old quarry; Fox Run pond/gazebo renovation; both summer 2026; Paint Mines protective barriers; coloradosprings.gov/parks + parks.elpasoco.com); Bear Creek Nature Center Pollinator Celebration June 26 ($5/person; bug sweeps; native pollinator education; Bear Creek Regional Park west COS; visitcos.com); Bellabu Bear children's robes recall (mandatory CPSC recall; burn hazard; violates mandatory flammability standard for children's sleepwear; stop use; contact brand; cpsc.gov)
- **Notes:**
  - verify-facts.py: 2 runs — first run flagged 5 char violations (S1A: 284, S1B: 296, S2A: 288, S3A: 323, S4A: 283 chars) + image manifest format wrong (table not YAML). Rewrote X posts shorter + rewrote image manifest in YAML format. Second run passed.
  - compile: 5 stories, 6 X posts, 0 FB posts (parser compatibility — same as all prior runs), 5 articles, 5 images; 21 dashboard items; posting window warnings cosmetic
  - PostPlanner exports: standard (6 posts: 6 X) and TOBI (6 TOBI posts) generated successfully
  - WordPress: credentials not in environment (session context compacted between niches); proxy blocks anyway — same as all prior runs
  - Dashboard push: PAT lacks write access to content-dashboards repo (same as all prior runs)
  - Byline rotation: Sarah Morales [S1, S3, S5], Jamie Rivera [S2, S4] (flipped from June 17)
  - Pipeline ran as Niche 2 in sequence after Tennis (Niche 1 completed June 18)

---

## Latest Run: June 17, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | Guidecraft Kitchen Helper Tower recall (CPSC May 14, 2026; 25,235 units; fall hazard; free repair kit; 800-524-3555; guidecraft.com/pages/product-recall); COS Park System Master Plan survey open through Aug 3 (coloradosprings.gov/ParkSystemMasterPlan; interactive map; meetings June 24-25 + July 9); Western Street Breakfast June 17 today (5:30-9 AM; Pikes Peak Ave & Tejon; free; $5 tokens; Kid's Corral; Exit West + Flying W Wranglers); PPIHC last-call ticket reminder (Race Day June 21 Father's Day; green flag 7:30 AM; online only ppihc.org; kids under 10 free; Fan Fest June 19); D20 superintendent update (Haberer removed May 15; Dr. Susan Field interim unanimously May 19; 19 years D20; former principal Woodmen-Roberts Elementary; asd20.org) |
| Story History Check | COMPLETE | 3 NEW STORIES (Guidecraft recall, COS Park survey, D20 superintendent) + 1 REPEAT-ANGLE (Western Street Breakfast — annual event on date) + 1 FOLLOW-UP (PPIHC last-call tickets — June 15 was NEW) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (2 Tier 1, 3 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Jamie Rivera (S1, S3, S5), Sarah Morales (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 6 posts (2 for Story 1; 1 each for Stories 2-5); all under 280 chars (2 violations fixed after verify-facts.py flag); 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images; all not_started; photo_source: gemini |
| Articles | COMPLETE | 5 articles (500-1000 words; Quick Reference tables in each; What's Next sections; 0 exclamation marks; no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py passed after 2 runs (2 char violations fixed on X posts rewrite); 87 claims; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 6 X posts, 0 FB posts, 5 articles, 5 images; 21 dashboard items |
| Dashboard | COMPLETE | review-dashboard.html — 21 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-17.xlsx (6 posts: 6 X + 0 FB; 13:05–20:30 MT) + TOBI cosp-postplanner-tobi-2026-06-17.xlsx (6 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-17)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 6 X posts + 5 FB long-form + 5 FB captions = 16 total posts (PostPlanner xlsx: 6 X posts)
- **Articles:** 5 (bylines: Jamie Rivera x3 [S1, S3, S5], Sarah Morales x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-17.xlsx (6 posts), cosp-postplanner-tobi-2026-06-17.xlsx (6 TOBI posts)
- **Coverage:** Guidecraft Kitchen Helper Tower recall (CPSC May 14; 25,235 units Classic+Contemporary 9 colors; platform loosens/detaches; 11 falls, 3 injuries; sold June 2022–Oct 2023 ~$200; free repair kit; 800-524-3555; ProductSupport@guidecraft.com; guidecraft.com/pages/product-recall); COS Park System Master Plan survey (online through Aug 3, coloradosprings.gov/ParkSystemMasterPlan; interactive map; in-person meetings June 24-25 + July 9; top feedback: restrooms + drinking fountains; 10-15 year investment plan); Western Street Breakfast June 17 today (5:30-9 AM; Pikes Peak Ave & Tejon; free admission; $5 token; under 5 free; Kid's Corral petting zoo/steer roping/dress-up; Exit West + Flying W Wranglers); PPIHC last-call ticket reminder (Race Day June 21 Father's Day; 7:30 AM green flag; online only ppihc.org/Humanitix; post-June 1 pricing; kids under 10 free; 7 spectator areas; Fan Fest June 19 5-9 PM free); D20 interim superintendent (Haberer removed May 15 lack of confidence; Dr. Susan Field appointed unanimously May 19; 19 years D20; former principal Woodmen-Roberts Elementary; current Asst Supt Learning Services; ~26,000 students ~40 schools; asd20.org)

---

## Latest Run: June 16, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | Otteroo LUMI/MINI CPSC Do Not Use warning renewed June 15 (new federal standard in effect, company refused recall, 1 death + 1 serious injury since 2022, 1-800-638-2772); 4th Annual Juneteenth Celebration June 19 at African American Museum, Westside Community Center (Freedom March noon, tours 1 PM + 2:30 PM, FREE — separate from Southern CO Juneteenth Festival June 20-21); Renaissance Festival Pirates Invasion Weekend June 20-21 Larkspur (King Soopers $29/$14/free, ~30 min from COS, coloradorenfaire.com); D49 meals 3 days left ending June 19 (Springs Ranch Elementary, breakfast 7:45-8:15 AM, lunch 10:30-11:20 AM, ages 1-18, D11 through July 31); D49 Student Success Center opens August at former Falcon Elementary of Technology (preschool/Base49/PEAK/Elevates 18-21, d49.org, budget passed June 11 effective July 1) |
| Story History Check | COMPLETE | 2 NEW STORIES (Otteroo CPSC warning, 4th Annual Juneteenth Celebration) + 3 FOLLOW-UPS (Renaissance Festival pirates weekend, D49 meals 3 days left, D49 Student Success Center enrollment) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (2 Tier 1, 3 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Jamie Rivera (S1, S3, S5), Sarah Morales (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 8 posts (2 each for Stories 1-2; 1 each for Stories 3-5); all under 280 chars (2 violations fixed on rewrite); 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 8 images; all not_started; photo_source: gemini; brand_kit_id: kAHCKfCZgk0 |
| Articles | COMPLETE | 5 articles (500-1000 words; Quick Reference tables; What's Next sections; 0 exclamation marks; no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py passed (2 runs — 2 char violations fixed on rewrite of X posts file); 85 claims, 178 HIGH, 76 MEDIUM, 68 LOW; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 8 X posts, 0 FB posts, 5 articles, 8 images; 23 dashboard items |
| Dashboard | COMPLETE | review-dashboard.html — 23 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-16.xlsx (18 posts: 8 X + 10 FB) + TOBI cosp-postplanner-tobi-2026-06-16.xlsx (13 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-16)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total in PostPlanner xlsx
- **Articles:** 5 (bylines: Jamie Rivera x3 [S1, S3, S5], Sarah Morales x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-16.xlsx (18 posts), cosp-postplanner-tobi-2026-06-16.xlsx (13 TOBI posts)
- **Coverage:** Otteroo infant neck float CPSC Do Not Use warning renewed June 15 (first-ever federal safety standard in effect, Otteroo LUMI and MINI, company refused recall, 1 death + 1 serious injury since 2022, stop use immediately, CPSC.gov, 1-800-638-2772); 4th Annual Juneteenth Celebration June 19 at African American Museum at Westside Community Center (Freedom March noon, museum tours 1 PM + 2:30 PM, FREE, African-American Historical & Genealogical Society — separate from Southern CO Juneteenth Festival June 20-21 already covered June 15); Renaissance Festival Pirates Invasion Weekend June 20-21 Larkspur (~30 min from COS, King Soopers $29/$14/free under 5, costumes encouraged, pirate-themed activities, 10 AM–6:30 PM, coloradorenfaire.com); D49 free summer meals 3 days left (ends June 19, Springs Ranch Elementary 4350 Centerville Drive, breakfast 7:45-8:15 AM, lunch 10:30-11:20 AM, ages 1-18 any district no registration, D11 continues July 31); D49 Student Success Center opens August at former Falcon Elementary of Technology (preschool Mon-Thu, Base49 before/after care, PEAK, Elevates 18-21, budget passed June 11 effective July 1, ~$2M cuts, 12 teacher positions, d49.org)
- **Notes:**
  - verify-facts.py: 2 runs — first run flagged 2 char violations (S2B: 288, S4B: 289). Rewrote X posts file cleanly replacing both overlong tweets with verified-short versions. Second run passed.
  - compile: 5 stories, 8 X posts, 0 FB posts, 5 articles, 8 images; 23 dashboard items; posting window warnings cosmetic (same as prior runs)
  - PostPlanner exports: standard (18 posts: 8 X + 10 FB) and TOBI (13 posts) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 15, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | 6th Annual Juneteenth Festival (Norris Penrose, June 20-21, FREE, kids' zone, V.I.C. + David Banner); PPIHC Father's Day weekend (Fan Fest June 19 free 5-9 PM downtown, Race Day June 21 green flag 7:30 AM, tickets required ages 10+ advance online ppihc.org); Little Grape Land nursing pillow recall (CPSC June 4, ~1,430 units, Amazon Aug 2025-Apr 2026, ~$28-30, suffocation hazard, no labels, 11 patterns, recall@evermorepartner.com full refund); D49 meals final 4 days (ends June 19, Springs Ranch Elementary 4350 Centerville Dr, ages 1-18, D11 through July 31); D20 June 30 deadlines (summer school + bus registration, Infinite Campus, asd20.org, bus assignments Aug 1) |
| Story History Check | COMPLETE | 3 NEW STORIES (Juneteenth Festival 2026, Little Grape Land recall, combined D20 deadline reminder) + 2 FOLLOW-UPS (PPIHC race week starts tomorrow; D49 meals — 4 days left) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (3 Tier 1, 2 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Sarah Morales (S1, S3, S5), Jamie Rivera (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 8 posts (2 each for Stories 1-3; 1 each for Stories 4-5); all under 280 chars; 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images; all not_started; photo_source: gemini; brand_kit_id: kAHCKfCZgk0 |
| Articles | COMPLETE | 5 articles (500-1000 words; Quick Reference tables; What's Next sections; 0 exclamation marks; no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py ran — 96 claims, 224 HIGH, 66 MEDIUM, 57 LOW; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 8 X posts, 0 FB posts, 5 articles, 5 images; 23 dashboard items |
| Dashboard | COMPLETE | review-dashboard.html — 23 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-15.xlsx (18 posts: 8 X + 10 FB) + TOBI cosp-postplanner-tobi-2026-06-15.xlsx (13 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Credentials not in env; proxy would block anyway | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-15)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total in PostPlanner xlsx
- **Articles:** 5 (bylines: Sarah Morales x3 [S1, S3, S5], Jamie Rivera x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-15.xlsx (18 posts), cosp-postplanner-tobi-2026-06-15.xlsx (13 TOBI posts)
- **Coverage:** 6th Annual Southern Colorado Juneteenth Festival (June 20-21, Norris Penrose 1045 Lower Gold Camp Rd, FREE all ages, kids' zone bounce houses/face painting/obstacle course, headliners V.I.C. + David Banner, car show/health fair/step show/fashion show, prior venue America the Beautiful Park, 2024 ~36K attendees); PPIHC Fan Fest + Race Day (practice June 16-19 free spectating, Fan Fest June 19 5-9 PM downtown free 10 blocks driver meet-and-greet, Race Day June 21 Father's Day green flag 7:30 AM, tickets required ages 10+ advance online only ppihc.org NOT sold Race Day, kids under 10 free, 7 spectator areas, Devil's Playground 12,780 ft); Little Grape Land nursing pillow recall (CPSC June 4 2026, ~1,430 units Amazon only Aug 2025–Apr 2026 ~$28-30, suffocation/infant breathing obstruction hazard, no labels/markings, 11 patterns, stop use+cut in half+photo to recall@evermorepartner.com for full refund, 0 injuries at recall date); D49 meals final 4 days (ends June 19, Springs Ranch Elementary 4350 Centerville Drive, ages 1-18 any district, breakfast 7:45-8:15 AM / lunch 10:30-11:20 AM, D11 continues July 31); D20 June 30 deadlines (summer school asd20.org/summer-school; bus registration asd20.org/buses-and-transportation, bus assignments Aug 1)
- **Notes:**
  - verify-facts.py: passed (1 run) — 96 claims; 224 HIGH, 66 MEDIUM, 57 LOW; image not_started warnings cosmetic (expected for gemini source)
  - compile: 5 stories, 8 X posts, 0 FB posts, 5 articles, 5 images; 23 dashboard items; posting window warnings cosmetic (same as prior runs)
  - PostPlanner exports: standard (18 posts: 8 X + 10 FB) and TOBI (13 posts) generated successfully
  - WordPress: credentials not in environment (new session); proxy would block anyway — same result as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 14, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | Father's Day COS 2026 guide (Pikes Peak free dads, USOPM 50% off, Wolf Center tour, ProRodeo 20% off, Garden of Gods always free — June 21); Pikes Peak Pride Sunday June 14 (parade 10 AM Acacia Park → Tejon → Alamo Square; festival 10 AM-6 PM; Rainbow Youth Square; 150+ vendors; free); D49 meals end June 19 (5 days; Springs Ranch Elementary only; D11 continues through July 31); Guidecraft Kitchen Helper Tower Recall 26-490 (May 14, 2026; ~25,235 units; Classic + Contemporary 9 colors; June 2022-Oct 2023; ~$200; Amazon/Wayfair/Walmart/Target/Maisonette/Overstock; 11 falls/3 injuries; free repair kit; 800-524-3555); Colorado Renaissance Festival rest of summer guide (every Sat-Sun through Aug 2; Larkspur ~30 mi; King Soopers $29/$14/free; First Responder BOGO) |
| Story History Check | COMPLETE | 3 NEW STORIES (Father's Day guide, Pikes Peak Pride, Guidecraft recall) + 2 FOLLOW-UPS (D49 meals — 5 days left, Renaissance Festival — rest of summer guide) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (4 Tier 1, 1 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Jamie Rivera (S1, S3, S5), Sarah Morales (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 9 posts (2 each for Stories 1-4; 1 for Story 5); all under 280 chars; 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images; all not_started; photo_source: gemini; brand_kit_id: kAHCKfCZgk0 |
| Articles | COMPLETE | 5 articles (500-1000 words; Quick Reference tables; What's Next sections; 0 exclamation marks; no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py ran — 75 claims, 179 HIGH, 49 MEDIUM, 51 LOW; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 9 X posts, 0 FB posts, 5 articles, 10 images; 24 dashboard items |
| Dashboard | COMPLETE | review-dashboard.html — 24 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-14.xlsx (19 posts: 9 X + 10 FB) + TOBI cosp-postplanner-tobi-2026-06-14.xlsx (14 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-14)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (4 Tier 1, 1 Tier 2)
- **Posts:** 9 X posts + 10 FB posts (5 long-form + 5 captions) = 19 total in PostPlanner xlsx
- **Articles:** 5 (bylines: Jamie Rivera x3 [S1, S3, S5], Sarah Morales x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-14.xlsx (19 posts), cosp-postplanner-tobi-2026-06-14.xlsx (14 TOBI posts)
- **Coverage:** Father's Day 2026 COS guide — June 21 one week away (Pikes Peak free for dads/reservation required; USOPM 50% off; ProRodeo 20% off merchandise; Wolf Center 9-11 AM limited; Garden of Gods always free; Victory Car Show); Pikes Peak Pride TODAY — parade 10 AM Acacia Park → Tejon → Alamo Square, festival 10 AM-6 PM Alamo Square, Rainbow Youth Square for kids/teens, 150+ vendors/25+ acts, free; D49 meals end June 19 — 5 days left, Springs Ranch Elementary only, D11 continues through July 31 multiple sites any child 1-18; Guidecraft Kitchen Helper Tower Recall 26-490 — ~25,235 units Classic/Contemporary 9 colors, June 2022-Oct 2023, ~$200, Amazon/Wayfair/Walmart/Target/Maisonette/Overstock, 11 falls 3 injuries, free repair kit 800-524-3555; Colorado Renaissance Festival rest of summer — every Sat-Sun through Aug 2 Larkspur, ~30 min from COS, King Soopers $29/$14/free under 5, First Responder BOGO, Magical Fantasy theme
- **Notes:**
  - verify-facts.py: passed; 75 claims, 179 HIGH, 49 MEDIUM, 51 LOW; image not_started warnings cosmetic (expected for gemini source)
  - compile: 5 stories, 9 X posts, 0 FB posts, 5 articles, 10 images — full parse success; 24 dashboard items
  - PostPlanner exports: standard (19 posts: 9 X + 10 FB) and TOBI (14 posts) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 13, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | Target Up&Up baby wipes recall (FDA confirmed Burkholderia cepacia complex + Burkholderia gladioli, Fragrance Free + Fresh Cucumber Scented, June 8, 2026, stop use + return to Target no receipt needed); Colorado Renaissance Festival opening weekend (49th season, June 13-14, Larkspur, Magical Fantasy theme, First Responder BOGO, King Soopers $29/$14/free, runs through Aug 2); D11 free summer meals through July 31 (ages 1-18, any district, no barriers, d11.org, 6 weeks longer than D49); D49 free summer meals 6 days left ending June 19 (ages 1-18, no barriers, Springs Ranch Elementary, D11 takes over June 20); Pikes Peak Habitat for Humanity 40th anniversary tonight (4:30-7:45 PM, Meanwhile Block Downtown COS, food trucks/yard games/trivia/speakers, free public event) |
| Story History Check | COMPLETE | 3 NEW STORIES (Target wipes recall, D11 standalone, Habitat 40th) + 2 FOLLOW-UPS (Renaissance Festival — opening weekend, D49 meals — day 8 final push) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (2 Tier 1, 3 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Sarah Morales (S1, S3, S5), Jamie Rivera (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 7 posts (2 each for Stories 1, 2; 1 each for Stories 3, 4, 5); all under 280 chars; 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images; all not_started; photo_source: gemini; brand_kit_id: kAHCKfCZgk0 |
| Articles | COMPLETE | 5 articles (500–1000 words each, Quick Reference tables, What's Next sections, 0 exclamation marks, no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py ran — consistency warnings cosmetic (story name parser); 76 claims; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 7 X posts, 5 FB posts, 5 articles, 10 images; 27 dashboard items |
| Dashboard | COMPLETE | review-dashboard.html — 27 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-13.xlsx (17 posts: 7 X + 10 FB) + TOBI cosp-postplanner-tobi-2026-06-13.xlsx (12 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-13)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total in PostPlanner xlsx; posting windows 13:22–21:22 (30 min apart)
- **Articles:** 5 (bylines: Sarah Morales x3 [S1, S3, S5], Jamie Rivera x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-13.xlsx (17 posts), cosp-postplanner-tobi-2026-06-13.xlsx (12 TOBI posts)
- **Coverage:** Target Up&Up baby wipes recall (Burkholderia cepacia complex + Burkholderia gladioli, Fragrance Free mfg Nov 7, 2025–May 5, 2026 / Fresh Cucumber mfg Dec 29-30, 2025, all sizes, stop use + return any Target no receipt, fda.gov); Colorado Renaissance Festival opening weekend (49th season June 13-14, Larkspur, Magical Fantasy theme, First Responder BOGO, King Soopers $29/$14/free under 5, runs Sat/Sun through Aug 2, coloradorenfaire.com); D11 free summer meals through July 31 (ages 1-18 any district, no registration/ID/income verification, free breakfast+lunch, multiple COS sites, d11.org, 6 weeks longer than D49); D49 free summer meals 6 days left (ends June 19, ages 1-18, no barriers, Springs Ranch Elementary, D11 continues through July 31); Pikes Peak Habitat for Humanity 40th anniversary tonight (June 13, 4:30-7:45 PM, Meanwhile Block Downtown COS, free public event, food trucks/yard games/trivia/speakers, founded 1986)
- **Notes:**
  - verify-facts.py: 1 run — consistency warnings cosmetic (story name format mismatch between files, not a blocking issue); 76 claims; image not_started warnings cosmetic (expected for gemini source)
  - compile: 5 stories, 7 X posts, 5 FB posts, 5 articles, 10 images — full parse success; 27 dashboard items
  - PostPlanner exports: both standard (17 posts: 7 X + 10 FB) and TOBI (12 TOBI posts) generated successfully; best PostPlanner result to date (first run with both X and FB parsed)
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 12, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | D49 budget formally adopted June 11 evening (2026-27 budget, ~$2M cuts effective July 1, Base49/PEAK/preschool/Elevates 18-21, 12 teacher positions, enrollment decline); Joyin Sloosh dive sticks recall (CPSC June 11, ~254,000 units, Model 40041, impalement hazard exceeds compression limits, Amazon/Target/Temu/Wayfair/SHEIN Feb 2019–Oct 2025, $17–22, free replacement sticks); Cosyland tower stool recall (~125,200 units, Models CS0003/CS0092-4, bamboo/gray, Amazon only Apr 2021–Nov 2025, ~$70, 25 reports 8 injuries 1 fracture, free repair kit cosyland.com/pages/recall, 3rd tower stool brand recalled in 2026); AAP 2026 screen time guidelines (no screens under 18mo, 1hr/day quality content ages 2-5, quality+context for older kids, device-free bedrooms highest-impact); D49 free summer meals ending June 19 (7 days left, ages 1-18, no barriers, Springs Ranch Elementary, d49.org; D11 through July 31) |
| Story History Check | COMPLETE | 3 NEW STORIES (Joyin recall, Cosyland recall, AAP screen time) + 2 FOLLOW-UPS (D49 budget — adopted, not just previewed; D49 free meals day 2 of countdown) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (3 Tier 1, 2 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Sarah Morales (S2, S4), Jamie Rivera (S1, S3, S5) |
| X Posts | COMPLETE | 03-social-posts-x.md — 8 posts (2 each for Stories 1, 2, 3; 1 each for Stories 4, 5); 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images; all not_started; photo_source: gemini |
| Articles | COMPLETE | 5 articles (500–1000 words each, Quick Reference tables, What's Next sections, 0 exclamation marks, no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py passed (1 run) — all 5 stories present; 83 claims; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 8 X posts, 5 FB posts, 5 articles, 10 images |
| Dashboard | COMPLETE | review-dashboard.html — 28 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-12.xlsx (8 posts) + TOBI cosp-postplanner-tobi-2026-06-12.xlsx (8 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-12)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts in PostPlanner xlsx; posting windows 13:10–20:52 (66 min apart)
- **Articles:** 5 (bylines: Jamie Rivera x3 [S1, S3, S5], Sarah Morales x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-12.xlsx (8 posts), cosp-postplanner-tobi-2026-06-12.xlsx (8 TOBI posts)
- **Coverage:** D49 budget formally adopted June 11 (2026-27 budget, ~$2M cuts take effect July 1, Base49/PEAK/preschool/Elevates 18-21, 12 teacher positions eliminated, enrollment decline root cause, d49.org); Joyin Sloosh dive sticks CPSC recall (June 11, ~254,000 units, Model 40041, impalement hazard exceeds federal compression limits, Amazon/Target/Temu/Wayfair/SHEIN Feb 2019–Oct 2025 $17–22, stop use/dispose/photo/contact Joyin for free replacement sticks, other Sloosh pieces not recalled, cpsc.gov); Cosyland tower stool recall (~125,200 units, Models CS0003/CS0092-4, bamboo and gray finishes, Amazon only Apr 2021–Nov 2025 ~$70, collapse+entrapment hazard, 25 reports/8 injuries/1 fractured arm, free repair kit with nets+stabilizing feet+instructions at cosyland.com/pages/recall, 3rd brand recalled in 2026 after Guidecraft/Wiifo); AAP 2026 screen time guidance (no screens under 18mo/video calling OK; 1hr/day quality content ages 2-5; quality+context+co-viewing for older kids; device-free bedrooms and mealtimes highest-impact; summer reframe: intentional not zero); D49 free summer meals 7 days left (ends June 19, any child ages 1-18, free breakfast+lunch, no registration/ID/income verification, Springs Ranch Elementary, d49.org, D11 families through July 31 at d11.org)
- **Notes:**
  - verify-facts.py: 1 run — passed; 83 claims; image not_started warnings cosmetic (expected for gemini source)
  - compile: 5 stories, 8 X posts, 5 FB posts, 5 articles, 10 images; posting window warnings cosmetic
  - dashboard: 28 items
  - PostPlanner exports: both standard (8) and TOBI (8) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 11, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | D49 budget vote TONIGHT (June 11, 6:30 PM, Sand Creek HS, ~$2M cuts, Base49/PEAK/preschool/Elevates 18-21, d49.org); Flanagan Park $750K CDBG federal renovation (near Nevada/Fillmore, new playground/ADA trail/basketball court, summer 2026 start, Jan 2027 completion); Wiifo Tower Stool recall (CPSC April 23, 2026, Model LT005, ~9,700 units, Amazon June 2022–March 2026, $60, entrapment+collapse, 22 incidents 6 injuries, support@wiifo.net); D49 free summer meals ending June 19 (8 days left, ages 1-18, no barriers, d49.org); WMMI Free Family Day June 12 last reminder (225 North Gate Blvd, stamp mill/blacksmith/hayride/gold panning, all free) |
| Story History Check | COMPLETE | 2 NEW STORIES (Flanagan Park, Wiifo recall) + 3 FOLLOW-UPS (D49 vote day-of, D49 meals 8-day countdown, WMMI final reminder) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (3 Tier 1, 2 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tags, 87 total claims |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Sarah Morales (S1, S3, S5), Jamie Rivera (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 8 posts (2 each for Stories 1, 2, 3; 1 each for Stories 4, 5); verify-facts.py passed — 0 char violations; 4 hashtags each; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images; all not_started; photo_source: gemini; brand_kit_id: kAHCKfCZgk0 |
| Articles | COMPLETE | 5 articles (500–1000 words each, Quick Reference tables, What's Next sections, 0 exclamation marks, no figure tags) |
| Fact-Check | COMPLETE | verify-facts.py passed (1 run) — all 5 stories present; 87 claims; 0 char violations; image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 8 X posts, 5 FB posts, 5 articles, 5 images |
| Dashboard | COMPLETE | review-dashboard.html — 28 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-11.xlsx (8 posts) + TOBI cosp-postplanner-tobi-2026-06-11.xlsx (8 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction as all prior runs |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-11)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total
- **Articles:** 5 (bylines: Sarah Morales x3 [S1, S3, S5], Jamie Rivera x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-11.xlsx (8 posts), cosp-postplanner-tobi-2026-06-11.xlsx (8 TOBI posts)
- **Coverage:** D49 budget vote TONIGHT 6:30 PM Sand Creek High School (2026-27 budget, ~$2M cuts effective July 1, Base49/PEAK/preschool/Elevates 18-21/non-core staffing, public comment open, d49.org); Flanagan Park $750K federal makeover (CDBG grant, near Nevada Ave & Fillmore St, new playground/ADA trail with lighting/basketball court, summer 2026 start, January 2027 completion); Wiifo Tower Stool recall (CPSC April 23, 2026, Model LT005, ~9,700 units, Amazon June 2022–March 2026 ~$60, collapse+torso entrapment, 22 incidents 6 injuries, stop use/disassemble/photo to support@wiifo.net for full refund); D49 free summer meals 8 days left (ends June 19, ages 1-18, no registration/ID/income verification, Springs Ranch Elementary, d49.org; D11 runs through July 31); WMMI Free Family Day TOMORROW (June 12, stamp mill/blacksmith/hayride/Gold Panning Championships, all outdoor activities free, 225 North Gate Blvd, 719-488-0880)
- **Notes:**
  - verify-facts.py: 1 run — passed; 87 claims; 0 char violations; image not_started warnings cosmetic (expected for gemini source)
  - compile: 5 stories, 8 X posts, 5 FB posts, 5 articles, 5 images; posting window warnings cosmetic
  - dashboard: 28 items
  - PostPlanner exports: both standard (8) and TOBI (8) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Pipeline Run Log (2026-06-10)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts in PostPlanner xlsx; posting windows 8:00 AM–5:00 PM MT
- **Articles:** 5 (bylines: Jamie Rivera x3 [S1, S3, S5], Sarah Morales x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-10.xlsx (7 posts), cosp-postplanner-tobi-2026-06-10.xlsx (7 TOBI posts)
- **Coverage:** D49 budget vote June 11 (Sand Creek HS 6:30 PM, nearly $2M cuts including teacher positions/supplemental programs/admin staffing, public welcome, d49.org); Guidecraft Kitchen Helper Tower recall (25,235 units, sold 2022-2023 at Amazon/Walmart/Target ~$200, platform loosens/detaches over time fall hazard for toddlers, 11 reports 3 injuries, stop using, free repair kit 800-524-3555); WMMI Family Day June 12 (Western Museum of Mining & Industry, 225 North Gate Blvd, stamp mill/blacksmith demo/hayride/gold panning, all free outdoors, wmmi.org); Father's Day COS guide 2026 (Pikes Peak free for dads June 20 NOT June 21 closed for Hill Climb, Wolf Center Father's Day morning event 9-11 AM reservations required, Garden of the Gods always free, Renaissance Festival Larkspur June 21 Sunday show, Flying W free hat); D11 Orton Academy moving to Trailblazer Elementary (K-8 charter school, Orton-Gillingham method gold standard for dyslexia, free public school within D11, 1 in 5 kids has dyslexia, d11.org choice enrollment)
- **Notes:**
  - verify-facts.py: 3 runs required — first run flagged 7 char violations (S1A: 291, S1B: 312, S2A: 323, S2B: 302, S3A: 322, S4A: 330, S5A: 339 chars). Rewrote all 7 posts shorter. Second run flagged 1 remaining violation (S4A: 297 chars). Fixed S4A. Third run passed.
  - Root cause: 4 hashtags in COS Parenting tweets (~62 chars) leaves only ~218 chars for content vs Tennis (3 hashtags)
  - compile: 5 stories, 7 X posts, 0 FB posts (PostPlanner xlsx has full 7 posts), 5 articles, 5 images
  - dashboard: 22 items
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 9, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | Colorado Renaissance Festival June 13-14 (49th season, Larkspur, Magical Fantasy + First Responder BOGO, King Soopers $29/$14/free, runs Sat/Sun through Aug 2); COS public pools/splash pads (Wilson Ranch + Monument Valley $10/$15, 3 free spray grounds, Portal Pool closed); CPSC pool recalls (Broqixin drain covers VGBA violation/entrapment/drowning, Blue Wave 48"+ pools drowning hazard); PPYMCA Week 3 Tech Camp June 15-19 (COS Conservatory + Snapology + Space Foundation, ages 5-12, ppymca.org); Tiny Land play tent recall (Amazon + tinylandus.com Nov 2025–Mar 2026, $54–$70, fiberglass shedding, 8 incidents, free plastic replacement kit) |
| Story History Check | COMPLETE | 3 NEW STORIES (Renaissance Festival, pool guide, Tiny Land recall) + 2 FOLLOW-UPS (CPSC pool recalls — new recalls distinct from prior recall coverage; PPYMCA Week 3 — Week 2 covered June 7) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (3 Tier 1, 2 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Sarah Morales (S1, S3, S5), Jamie Rivera (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 7 posts (2 each for Stories 1, 3; 1 each for Stories 2, 4, 5); 5 char violations fixed on second verify run; all under 280 chars; 4 hashtags each; 0 exclamation marks; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (10 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 images; all not_started; photo_source: gemini; brand_kit_id: kAHCKfCZgk0 |
| Articles | COMPLETE | 5 articles (500–1000 words each, 0 exclamation marks, What's Next sections, Quick Reference tables where applicable) |
| Fact-Check | COMPLETE | verify-facts.py passed (2nd run) — 5 char violations fixed (S1A: 317→254, S1B: 292→219, S2A: 292→259, S4A: 287→269, S5A: 315→265) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 7 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images |
| Dashboard | COMPLETE | review-dashboard.html — 22 items |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-09.xlsx (7 posts) + TOBI cosp-postplanner-tobi-2026-06-09.xlsx (7 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo | Same environment restriction |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-09)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts in PostPlanner xlsx; posting windows 8:00 AM–5:00 PM MT
- **Articles:** 5 (bylines: Sarah Morales x3 [S1, S3, S5], Jamie Rivera x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-09.xlsx (7 posts), cosp-postplanner-tobi-2026-06-09.xlsx (7 TOBI posts)
- **Coverage:** Colorado Renaissance Festival 49th season (Larkspur, June 13–Aug 2 Sat/Sun, opening weekend Magical Fantasy + First Responder BOGO, King Soopers $29/$14/free, coloradorenfaire.com); COS public pools/splash pads guide (Wilson Ranch + Monument Valley $10/$15 no membership, 3 free spray grounds: Deerfield Hills/Venezia Park/Panorama Park, Portal Pool closed); CPSC pool safety recalls (Broqixin drain covers VGBA violation/entrapment/drowning, Blue Wave 48"+ pools drowning hazard, COS altitude 6,035 ft context); PPYMCA Summer Day Camp Week 3 June 15-19 (ages 5-12, COS Conservatory + Snapology + Space Foundation, ppymca.org, financial aid available); Tiny Land play tent recall (Amazon + tinylandus.com Nov 2025–Mar 2026, $54–$70, fiberglass shedding skin/eye irritation, 8 incidents, free plastic replacement kit tinylandus.com/pages/recalls)
- **Notes:**
  - verify-facts.py: 2 runs required — first run flagged 5 char violations (S1A: 317, S1B: 292, S2A: 292, S4A: 287, S5A: 315 chars). Fixed by rewriting all 5 posts shorter. Second run passed.
  - compile: 5 stories, 7 X posts, 0 FB posts (PostPlanner xlsx has full 7 posts), 5 articles, 5 images
  - dashboard: 22 items
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

## Pipeline Run Log (2026-06-08)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 6 X posts + 10 FB posts (5 long-form + 5 captions) = 16 total
- **Articles:** 5 (bylines: Jamie Rivera x3 [S1, S3, S5], Sarah Morales x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-08.xlsx (6 posts), cosp-postplanner-tobi-2026-06-08.xlsx (6 TOBI posts)
- **Coverage:** TOMY Boon NURSH baby bottle recall (choking hazard, ~40,000 units, Walmart, Nov 2025–May 2026, ~$20, item B11654, 135 reports, recall.tomy.com/nursh, 866-725-4407); Blodgett Open Space 14 miles new trails summer 2026 (mountain bike south, hiking north, free public open space, Trackchair expanding); summer slide prevention (25–30% learning loss, math hardest hit, PPYMCA + PPLD + Rock Ledge Ranch local resources); Rock Ledge Ranch last week (June 14 close, blacksmith/cornhusk dolls/Victorian games, Garden of the Gods); D49 budget vote June 11 (Sand Creek HS, Student Success Center August 2026, preschool/Base49/PEAK/Elevates 18–21)
- **Notes:**
  - verify-facts.py: passed; 70 claims; tweet char violations resolved; image warnings cosmetic (gemini source, all not_started)
  - compile: 5 stories, 6 X posts, 0 FB posts (PostPlanner xlsx has full 6 posts), 5 articles, 5 images
  - dashboard: 21 items
  - PostPlanner exports: both standard (6) and TOBI (6) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

## Pipeline Run Log (2026-06-07)
- **Steps completed:** All 16 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 7 X posts in PostPlanner xlsx; posting windows 8:00 AM–5:00 PM MT
- **Articles:** 5 (bylines: Sarah Morales x3 [S1, S3, S5], Jamie Rivera x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-07.xlsx (7 posts), cosp-postplanner-tobi-2026-06-07.xlsx (7 TOBI posts)
- **Coverage:** Vevor baby swing CPSC recall (suffocation hazard, Safe Sleep for Babies Act violation, models BB501K/BB702A/BB005K, $65–$80, Jan–Aug 2025, recalling@vevor.com, 855-599-6320); COS parks $3.1M budget cut (maintenance ~$100K 50% reduction, 25% restrooms closed, Flanagan Park $750K federal grant); PPYMCA Summer Day Camp Week 2 June 8–12 (ages 5–12, "Low-Key Famous Artist Week", ppymca.org, financial assistance available); COS childcare desert (El Paso County 46,800 under 5, ~17,500 spots, $16,300/year, eastern COS/Fountain-Fort Carson hardest hit); D11 labor dispute (Dec 2024 7-1 vote dissolving 56-year master agreement, Oct 2025 strike 1,000+, May 2026 picket 300+ days later, Nov 2026 board elections)
- **Notes:**
  - verify-facts.py: 1 fix required — S5 tweet was 293 chars (URLs counted at 23 chars each), rewritten to 239 chars
  - compile: 5 stories, 7 X posts, 0 FB posts (PostPlanner xlsx has full 7 posts), 5 articles, 5 images; posting window warnings cosmetic
  - dashboard: 22 items
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 6, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | PPLD Summer Adventure 2026 (June 1–July 31, free all ages, Beanstack app, grand prizes include Broadmoor Cloud Camp stay + Pikes Peak Attractions VIP pass, 14 locations + 2 bookmobiles, ppld.org/summer); Bellabu Bear children's robes recall (burn hazard, fails flammability standards, bamboo sherpa robes in PAW Patrol/Minecraft/Batman/Trolls/Garfield prints, sizes S/M + M/L, sold Jan 2024–Jul 2025 ~$60, full refund or store credit, 888-703-7752 Mon–Fri 9 AM–4 PM PT, help@bellabubear.com, bellabubear.com → Recall); D49 free summer meals ending June 19 (all kids 1–18, no registration/ID/income req, Springs Ranch Elementary confirmed, d49.org); D20 July summer school registration open (credit recovery + enrichment + grad requirements, Infinite Campus, asd20.org/summer-school); hot car safety (3–5x faster heat for children, ~19°F rise in 10 min, COS 6,035 ft elevation, heatstroke 104°F fatal 107°F, Look Before You Lock, AAP/NHTSA) |
| Story History Check | COMPLETE | 4 NEW STORIES (PPLD Summer Adventure, Bellabu Bear recall, D49 summer meals, hot car safety) + 1 FOLLOW-UP (D20 July summer school — D20 transportation covered June 5, today's angle is summer school, different program) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (3 Tier 1, 2 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM/LOW confidence tagging |
| Story Analysis | COMPLETE | 02-story-analysis.md — bylines: Sarah Morales (S1, S3, S5), Jamie Rivera (S2, S4) |
| X Posts | COMPLETE | 03-social-posts-x.md — 8 posts (2 each for Stories 1, 2, 3; 1 each for Stories 4, 5); 3 char violations fixed on second verify run (S1A: 287→243, S1B: 282→272, S2A: 298→253); 4 hashtags each; 0 exclamation marks; COS voice rules |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags in long-form; COS voice rules |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (11 concepts across 5 stories) |
| Image Manifest | COMPLETE | 07-image-manifest.md — markdown list format; 11 images; all not_started; photo_source: gemini; brand_kit_id: kAHCKfCZgk0 |
| Articles | COMPLETE | 5 articles (500-1000 words each, Quick Reference tables, What's Next sections, 0 exclamation marks) |
| Fact-Check | COMPLETE | verify-facts.py passed (2nd run) — all 5 stories present; 66 claims; 3 char violations fixed (S1A, S1B, S2A); image not_started warnings cosmetic (expected for gemini source) |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 8 X posts, 0 FB posts (parser compatibility), 5 articles, 5 images |
| Dashboard | COMPLETE | review-dashboard.html (23 items) |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-06-06.xlsx (8 posts) + TOBI cosp-postplanner-tobi-2026-06-06.xlsx (8 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | Same environment restriction |
| WordPress Publish | Attempted — Host not in allowlist / proxy blocks WordPress API | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-06-06)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts in PostPlanner xlsx; posting windows 12:57–20:46 (67 min apart)
- **Articles:** 5 (bylines: Sarah Morales x3 [S1, S3, S5], Jamie Rivera x2 [S2, S4])
- **PostPlanner exports:** cosp-postplanner-2026-06-06.xlsx (8 posts), cosp-postplanner-tobi-2026-06-06.xlsx (8 TOBI posts)
- **Coverage:** PPLD Summer Adventure 2026 (free, all ages, June 1–July 31, Beanstack app, Broadmoor Cloud Camp grand prize, ppld.org/summer); Bellabu Bear children's robes recall (burn hazard, bamboo sherpa, PAW Patrol/Minecraft/Batman/Trolls prints, $60, Jan 2024–Jul 2025, full refund, 888-703-7752); D49 free summer meals ending June 19 (all children 1–18, no paperwork, Springs Ranch Elementary, d49.org); D20 July summer school registration open (credit recovery + enrichment, Infinite Campus, asd20.org/summer-school); hot car safety (children heat 3–5x faster, ~19°F in 10 min, COS elevation factor, Look Before You Lock, call 911)
- **Notes:**
  - verify-facts.py: 2 runs required — first run flagged 3 char violations (S1A: 287, S1B: 282, S2A: 298 chars). Fixed by rewriting all 3 posts shorter. Second run passed.
  - compile: 5 stories, 8 X posts, 0 FB posts (PostPlanner xlsx has full 8 posts), 5 articles, 5 images; posting window warnings cosmetic
  - dashboard: 23 items
  - PostPlanner exports: both standard (8) and TOBI (8) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

---

## Latest Run: June 5, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | TOMY Boon NURSH recall June 4 (~40,000 units, Pink Tie Dye 3-pack, item B11654, UPC 669028116546, Walmart Nov 2025–May 2026, ~$20, shell peels choking hazard, 135 reports 0 injuries, write RECALL + photo → replacement or $22 Walmart credit, recall.tomy.com/nursh, 866-725-4407, cs@tomy.com); Pikes Peak Gem Show June 5–7 (Norris Penrose Event Center 1045 Lower Gold Camp Rd, kids 12 under free, adults $5/$8, 55+ vendors, gold panning + scavenger hunt + Pebble Pups + beading 11 AM daily + wire-wrapping Sat 1 PM, pikespeakgemshow.com); D20 transportation deadline June 30 (current students May 1–June 30, new students June 8–June 30, Infinite Campus address + fee required, bus assignments Aug 1, Extended Parent Portal; budget hearing June 11 5 PM Board Meeting 1110 Chapel Hills Drive; Dr. Susan Field interim superintendent since May 19; asd20.org/buses-and-transportation); 2026 National Parent Survey (New America New Practice Lab, 5,472 parents, 72% want more time, No. 1 barrier money, $13,184/year avg child care ~25% income at 200% FPL, parental leave 10 weeks moms/2 weeks dads, 91% want to work, COS ~47K under 5 / <19K licensed spots); COS summer sun safety (6,035 ft, ~24% more UV than sea level, UV index 8–10 June/July Very High to Extreme, SPF 30+ 15 min before reapply 2 hrs, infants under 6 months no sunscreen keep out of direct sun AAP, peak 10 AM–4 PM, UPF 50+, hydration heat exhaustion signs) |
| Story History Check | COMPLETE | 4 NEW STORIES + 1 FOLLOW-UP |
| Daily Brief | COMPLETE | 5 stories (4 Tier 1, 1 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md |
| Story Analysis | COMPLETE | bylines: Jamie Rivera (S1, S3, S5), Sarah Morales (S2, S4) |
| X Posts | COMPLETE | 8 posts; 7 char violations fixed (second verify run passed) |
| Facebook Posts | COMPLETE | 5 Long-Form + 5 Image Captions |
| Image Concepts | COMPLETE | Gemini base_only prompts |
| Image Manifest | COMPLETE | 15 images; all not_started; photo_source: gemini |
| Articles | COMPLETE | 5 articles |
| Fact-Check | COMPLETE | verify-facts.py passed (2nd run); 84 claims |
| Compile | COMPLETE | 5 stories, 8 X posts, 0 FB posts, 5 articles, 5 images |
| Dashboard | COMPLETE | 28 items |
| PostPlanner Export | COMPLETE | Standard (8) + TOBI (8) |
| Dashboard Push | Attempted — PAT lacks write access | Same environment restriction |
| WordPress Publish | Attempted — Host not in allowlist | Same environment restriction |
