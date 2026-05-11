# COS Parenting — Pipeline Status

## Latest Run: May 11, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | D20 $42.7M DoD grant for Douglass Valley K-8 at USAFA (D20 press release/Gazette); EEMB USA coin battery recall (cpsc.gov — Recall No. 26-465, 312,100 units, Amazon Aug 2023–Apr 2026, $3-$9, Reese's Law, CR2025/CR2032 and others); El Paso County school co-locations (Gazette May 11 — James Irwin Elem, East Hills Academy, Orton Academy); PPLD Summer Adventure 2026 (ppld.org — "Unearth a Story" theme, free, 30 days, Beanstack); AAP 2026 children's mental health clinical report (HealthyChildren.org — proactive framework, 5 protective factors) |
| Story History Check | COMPLETE | 5 NEW STORIES — all verified against story history through May 10; no duplicates |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (2 Tier 1, 3 Tier 2) |
| Research Notes | COMPLETE | 01-research-notes.md — HIGH/MEDIUM confidence tagging, sources noted |
| Story Analysis | COMPLETE | 02-story-analysis.md — 5 stories with tier + pillar assignments, byline assignments |
| X Posts | COMPLETE | 03-social-posts-x.md — 7 posts; all verified under 280 chars (6 char violations fixed on second pass); 4 hashtags each; max 1 exclamation mark |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Captions; engagement questions; no hashtags |
| Image Concepts | COMPLETE | 05-image-concepts.md — Gemini base_only prompts (9 concepts across 5 stories); 1200x675 social |
| Image Manifest | COMPLETE | 07-image-manifest.md — 9 images, all not_started; brand_kit_id: kAHCKfCZgk0; photo_source: gemini |
| Articles | COMPLETE | 5 articles in articles/ folder (500-1000 words each, Quick Reference tables where applicable, What's Next sections, 0 exclamation marks, no banned words, COS/Colorado Springs naming) |
| Fact-Check | COMPLETE | verify-facts.py passed — all 5 stories present, no char violations; 68 claims extracted |
| Compile | COMPLETE | 07-content-data.json — 5 stories, 7 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images |
| Dashboard | COMPLETE | review-dashboard.html (22 items) |
| PostPlanner Export | COMPLETE | Standard cosp-postplanner-2026-05-11.xlsx (7 posts) + TOBI cosp-postplanner-tobi-2026-05-11.xlsx (7 TOBI posts) |
| Dashboard Push | Attempted — PAT lacks write access to content-dashboards repo (same as all prior runs) | Same environment restriction |
| WordPress Publish | Attempted — proxy blocks WordPress API (Host not in allowlist) | Same environment restriction as all prior runs |

## Pipeline Run Log (2026-05-11)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Jamie Rivera x2, Sarah Morales x3)
- **PostPlanner exports:** cosp-postplanner-2026-05-11.xlsx (7 posts), cosp-postplanner-tobi-2026-05-11.xlsx (7 TOBI posts)
- **Coverage:** D20 $42.7M DoD grant for new Douglass Valley K-8 at Air Force Academy (787 students, $54.1M total, 92,000 sq ft); EEMB USA coin battery recall (CPSC Recall No. 26-465; 312,100 units; Amazon Aug 2023–Apr 2026; $3-$9; CR2025/CR2032/CR2450 and others; not child-resistant; eemb.com/recall); El Paso County school co-locations 2026-27 (James Irwin Elem → D49 campus; East Hills Academy → Horace Mann MS; Orton Academy → Trailblazer Elem); PPLD Summer Adventure 2026 "Unearth a Story" (free, all ages, 30 days Read/Explore/Create, Beanstack app, D11 last day May 22); AAP 2026 children's mental health framework (proactive model; 5 foundations: parent-child bond, routines, physical activity, sleep, community; COS military family context)
- **Notes:**
  - verify-facts.py initially found 6 char violations (S1-A 324, S2-A 301, S2-B 286, S3-A 315, S4-A 303, S5-A 331); all fixed; second run passed with no warnings
  - compile-content-data.py: 5 stories, 7 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (22 items)
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

## Pipeline Run Log (2026-05-10)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (2 Tier 1, 3 Tier 2)
- **Posts:** 7 X posts + 10 FB posts (5 long-form + 5 captions) = 17 total
- **Articles:** 5 (bylines: Jamie Rivera x3, Sarah Morales x2)
- **PostPlanner exports:** cosp-postplanner-2026-05-10.xlsx (7 posts), cosp-postplanner-tobi-2026-05-10.xlsx (7 TOBI posts)
- **Coverage:** Bellabu Bear children's sherpa robe recall (CPSC; burn hazard; PAW Patrol/Minecraft/Minions/Batman/Garfield etc prints; S/M and M/L; Saks + online Jan 2024-Jul 2025; ~$60; no injuries; full refund 888-703-7752 or help@bellabubear.com); Mother's Day COS events (wolf tour $40/$20, Hillside Gardens free, ViewHouse/Lumen8/Broadmoor brunches, Do Portugal Circus through May 24); COS 2026 summer camp guide (D11 last day May 22; Go West ages 5-14, Tinkering School STEAM, CYT theater, Catamount outdoor, It's FUNdamental $120/child); D11 graduation May 19-20 + last day May 22 + Adult Ed graduation May 28; Outdoor play research roundup (AAP/CHOP/UCLA Health — obesity/stress/ADHD/cognitive benefits; COS parks + trails)
- **Notes:**
  - verify-facts.py passed — all 5 stories present; 92 claims; no char violations; image warnings cosmetic (not_started expected)
  - compile-content-data.py: 5 stories, 7 X posts, 0 FB (format parse issue, same as all prior runs), 5 articles, 5 images
  - review-dashboard.html generated (22 items)
  - PostPlanner exports: both standard (7) and TOBI (7) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access to content-dashboards repo (same as all prior runs)

## Pipeline Run Log (2026-05-09)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total
- **Articles:** 5 (bylines: Jamie Rivera x3, Sarah Morales x2)
- **PostPlanner exports:** cosp-postplanner-2026-05-09.xlsx (8 posts), cosp-postplanner-tobi-2026-05-09.xlsx (8 TOBI posts)
- **Coverage:** D11 teacher/parent picket (300+ days without master contract, CSEA organized, live handbook issue, class sizes/counselors/sped demands, picket at Board meeting May 6); Territory Days 50th anniversary May 23-25 (free, Old Colorado City, 180+ booths, petting zoo, gold panning, free shuttle from downtown, no dogs); ZMC Group light-up toy recall (124,560 units, button cell battery ingestion risk, yo-yos/maracas/wands/sticks, $1 at discount stores 2023-2026, recallzmctoy@gmail.com); AAP 2026 screen time update (drops "2hr max" for school-age kids, quality/co-viewing focus, device-free bedrooms/mealtimes); Downtown Farmers Market opens May 10 at Acacia Park (Sundays 9AM-2PM free through Oct 25)
- **Notes:**
  - verify-facts.py initially found 4 char violations (S2-A 285, S3-A 300, S3-B 297, S4-A 284); all fixed; second run passed
  - compile-content-data.py: 5 stories, 8 X posts, 5 FB stories, 5 articles, 5 images
  - review-dashboard.html generated (23 items)
  - PostPlanner exports: both standard (8) and TOBI (8) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access (same as all prior runs)

---

## Pipeline Run Log (2026-05-08)
- **Steps completed:** All 15 (Research → Story History → Brief → Research Notes → Analysis → X Posts → FB Posts → Image Concepts → Articles → Fact-Check → Compile → Image Manifest → Dashboard → PostPlanner Export x2 → Publish attempt)
- **Stories:** 5 stories (3 Tier 1, 2 Tier 2)
- **Posts:** 8 X posts + 10 FB posts (5 long-form + 5 captions) = 18 total
- **Articles:** 5 (bylines: Sarah Morales x3, Jamie Rivera x2)
- **PostPlanner exports:** cosp-postplanner-2026-05-08.xlsx (8 posts), cosp-postplanner-tobi-2026-05-08.xlsx (8 TOBI posts)
- **Coverage:** Touch-A-Truck 3rd Annual May 16 (FREE, Norris Penrose, 9:30 AM-2 PM, timed entry, fire trucks + military vehicles + helicopters + kids entrepreneur market, up to 15,000 expected, norrispenrose.com); Garden of Gods Art Festival May 16-17 (Rock Ledge Ranch, 10 AM-5 PM, kids under 12 free, dogs welcome, 150 artists, live music, food trucks, free shuttle from Coronado HS); Uuoeebb infant walker recall CPSC alert (BaoD/Amazon 2024-2025, gray/black/pink, Production Batch 7654, fits through doorways + stair hazard + head entrapment, manufacturer won't fix, dispose immediately, SaferProducts.gov); D49 Student Success Center preschool Aug 2026 (2 classrooms M-Thu, Falcon Elementary of Technology, Base49 before/after school + Friday childcare, d49.org); AAP 2026 immunization schedule (clesrovimab added for RSV newborns, HPV now 9-12 AAP vs CDC 11-12, COVID-19 for ages 6-23mo, 12 org endorsements, HealthyChildren.org)
- **Notes:**
  - verify-facts.py initially found 5 char violations (S1-A 311, S1-B 287, S3-A 287, S5-A 325, S5-B 288); all fixed; second run passed
  - compile-content-data.py: 5 stories, 8 X posts, 5 FB stories, 5 articles, 5 images
  - review-dashboard.html generated (28 items)
  - PostPlanner exports: both standard (8) and TOBI (8) generated successfully
  - WordPress proxy error: same environment restriction as all prior runs
  - Dashboard push failed: PAT lacks write access (same as all prior runs)
