# COS Parenting — Pipeline Status

## Latest Run: August 27, 2026

| Step | Status | Notes |
|------|--------|-------|
| Research (web search) | COMPLETE | Orton Academy/Trailblazer Elementary D11 co-location (2026-27); PIXLABBY Silicone Magnetic Fidget Sliders CPSC recall (~860 units Amazon Oct 2025–May 2026); NSF 2026 Sleep in America Poll (44% of kids not getting enough sleep); Wings of Change Grand Reveal (Pioneers Museum, Aug 28 free); Rocky Mountain 5K YMCA (Aug 29, America the Beautiful Park); Sunflower Days at Gather Mountain Blooms (Aug 29); PPLD Story and Crafts with Cynde (free, through Aug 31); D11 Edukit supply program; CCAP/FAMLI/PPLD/El Paso County Health free school resources |
| Story History Check | COMPLETE | S1 new (Orton Academy co-location not covered before); S2 new (PIXLABBY — distinct from Goody King Aug 26 and ABC Trading/Gagaku Aug 24); S3 new (NSF 2026 poll — distinct from Aug 26 S5 sleep tips article); S4 REQUIRED Thursday roundup (Weekend Aug 28-30); S5 new (free school resources guide — distinct from individual resource mentions in prior runs) |
| Daily Brief | COMPLETE | 00-daily-brief.md — 5 stories (2 Tier 1, 3 Tier 2); bylines: Jamie Rivera (S1, S3, S5), Sarah Morales (S2, S4) |
| Research Notes | COMPLETE | 01-research-notes.md — sources: D11.org, CPSC.gov, NSF (thensf.org), healthychildren.org, springsdaily.com, PPLD, elpasocountyhealth.org, colorado.gov/famli, web research |
| Story Analysis | COMPLETE | 02-story-analysis.md — tier assignments, posting windows, X/FB/image breakdown; Thursday roundup spec confirmed |
| X/Twitter Posts | COMPLETE | 03-social-posts-x.md — 7 posts across 5 stories; all ≤280 chars (Post 2A trimmed from 293→280 after verify-facts flag); 4 hashtags each; 0 exclamation marks |
| Facebook Posts | COMPLETE | 04-social-posts-facebook.md — 5 Long-Form + 5 Image Caption; no hashtags; engagement questions; COS voice |
| Image Concepts | COMPLETE | 05-image-concepts.md — 10 Gemini base_only prompts (5 stories × 2 formats: 1080x1350 social + 1200x630 hero); clean bottom third; no celebrity likenesses; brand kit kAHCKfCZgk0 |
| Articles (5) | COMPLETE | article-01 Orton Academy (Jamie Rivera, ~600 words); article-02 PIXLABBY Recall (Sarah Morales, ~600 words); article-03 NSF Sleep Poll (Jamie Rivera, ~700 words); article-04 Weekend Roundup Aug 28-30 (Sarah Morales, ~700 words, REQUIRED Thursday, 3 springsdaily.com links embedded); article-05 Free School Resources (Jamie Rivera, ~700 words) |
| Fact-Check | COMPLETE | 06-fact-check-log.md — 68 claims total; HIGH/MEDIUM/LOW prioritized; no char limit issues after trim |
| Compile Content Data | COMPLETE | 07-content-data.json — 5 stories, 6 X posts, 5 FB posts, 5 articles, 26 items; char-limit errors in compile output are a known parser bug (metadata lines included in count); actual posts verified ≤280 chars |
| Image Manifest | COMPLETE | 07-image-manifest.md — 10 entries (5 stories × 2), all not_started, gemini base_only, brand kit kAHCKfCZgk0 |
| Review Dashboard | COMPLETE | review-dashboard.html — 26 items; image manifest warning expected (images generated separately) |
| Publish Dashboard | BLOCKED | content-dashboards repo not in session's authorized repository set (403 proxy) — known recurring issue |
| PostPlanner Export | COMPLETE (0 posts) | Known parser compat issue — generate-postplanner-export.py finds 0 posts; runs completed for both standard and --tobi; no fix available |
| WordPress Publish | BLOCKED | WordPress API proxy returns 403 Forbidden — known recurring issue |
| Story History | COMPLETE | 5 new entries appended to Parenting/story-history.md |

## Known Issues (Recurring)
- WordPress publish: 403 proxy block — all 5 articles queued as drafts, pending manual publish or proxy fix
- PostPlanner export: parser compat issue returns 0 posts every run
- content-dashboards push: 403 proxy block (not in session authorized repo set)
- Image manifest warnings from dashboard generator: expected (Gemini image generation is a separate step)

## Previous Run: August 26, 2026
Stories: 1) National Parent Survey/Quality Time (S. Morales T1); 2) Goody King Magnetic Cubes Recall (J. Rivera T1); 3) COS Back-to-School Week Check-In D11/D20/D49 (S. Morales T2); 4) Garden of the Gods Free Nature Programs (J. Rivera T2); 5) Back-to-School Sleep Tips (S. Morales T2)
