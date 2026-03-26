# Daily Content Pipeline — Operational Runbook

> This is the concise operational checklist for running the daily content pipeline.
> For full format specs and creative guidance, see `SKILL.md`.
> For error fixes, see the troubleshooting section at the bottom.

## Pre-Flight (Run EVERY session before any content work)

### 1. Read State
```
Read: {NICHE}/pipeline-status.md
Read: {NICHE}/niche-config.yaml
Read: {NICHE}/seasonal-calendar.md
Read: _engine/CLAUDE.md
```
- Check if today's pipeline has already been started (partially or fully)
- If resuming, pick up from the last incomplete step

### 2. Verify Git Health (for each niche with a dashboard repo)
```bash
cd {NICHE_ROOT}
git fetch origin main
git status
```
- If local is behind remote: `git merge origin/main --no-edit`
- If untracked files from yesterday: commit or clean up before starting

### 3. Verify GitHub Pages Deployment
```bash
gh api repos/{ORG}/{REPO}/pages --jq '{build_type, status}'
```
- `build_type` MUST be `"workflow"` (not `"legacy"`)
- If `"legacy"`: switch with `gh api -X PUT repos/{ORG}/{REPO}/pages -f build_type="workflow"`
- `.nojekyll` MUST exist in repo root
- `.github/workflows/deploy-pages.yml` MUST exist
- If missing either: `publish-dashboard.py` will create them automatically

---

## Pipeline Execution (15 Steps)

### Phase 1: Research & Planning (Steps 1-4, SEQUENTIAL)

**Step 1 — Research**
- Run 10+ web searches across 6+ categories
- Categories: scores/results, tournament updates, rankings, upsets/performances, coaching/transfers, previews, features
- Reference: `{NICHE}/api-reference.md` for sources
- Output: 8+ candidate stories with source URLs

**Step 2 — Story History Check**
- Read `{NICHE}/story-history.md`
- Classify each candidate: NEW STORY | FOLLOW UP (cite prev date) | SKIP
- Drop SKIPs, keep at least 5 stories

**Step 3 — Daily Brief** → `00-daily-brief.md`
- Select 5-7 stories, assign Tiers (1/2/3)
- GAME RESULTS AND PREVIEWS GO FIRST (earliest time slots)
- Assign posting windows from `niche-config.yaml` schedule
- **GATE: If <5 stories, STOP → go back to Step 1**

**Step 4 — Research Notes** → `01-research-notes.md`
- 2+ sources per Tier 1 story (cross-verify stats)
- Freshness justification for each story

### Phase 2: Content Creation (Steps 5-9)

**Step 5 — Story Analysis** → `02-story-analysis.md`
- Deep analysis per story: angles, hooks, headlines

**Steps 6-8 — Social Posts + Image Concepts** (CAN RUN IN PARALLEL)
- Step 6 → `03-social-posts-x.md` (ALL tweets ≤280 chars, URLs=23)
- Step 7 → `04-social-posts-facebook.md` (blank lines between paragraphs!)
- Step 8 → `05-image-concepts.md` (skip if `photo_source: none`)
- Skip Step 7 if platform config has no facebook
- Skip Step 8 if `photo_source: none`

**Step 9 — Articles** → `articles/article-NN-slug.html`
- Minimum 5 articles (if `article_word_count_max > 0`)
- Skip entirely if articles disabled in config

### Phase 3: Validation (Step 10)

**Step 10 — Fact-Check & Consistency**
```bash
python _engine/scripts/verify-facts.py --niche {NICHE} {DATE}
```
- Fix ALL consistency errors before proceeding
- Fix ALL character count violations (>280 chars)
- Verify HIGH priority claims for Tier 1-2 stories
- Output: `06-fact-check-log.md`
- **GATE: Must pass before Step 13**

### Phase 4: Images (Step 11, OPTIONAL)

**Step 11 — Image Production**
- Initialize `07-image-manifest.md` with story entries
- Search/generate images per niche photo_source config
- Skip entirely if `photo_source: none`

### Phase 5: Finalize & Publish (Steps 12-15)

**Step 12 — Story History Update**
- Append today's stories to `{NICHE}/story-history.md`
- Include: title, tier, angle, platforms, follow-up ideas

**Step 12b — Refresh Traffic Data (Softball only)**
```bash
python _engine/scripts/query-fanrumor-traffic.py --niche {NICHE}
```
- Requires `GA4_SERVICE_ACCOUNT_JSON` env var (base64-encoded service account from sports-digest Railway project)
- Outputs `{NICHE}/fanrumor-traffic.json` with 7d/30d pageviews, top articles, traffic sources
- Dashboard generator auto-detects this file and renders the Content Performance panel
- Skip for niches that don't publish to fanrumor.com

**Step 13 — Generate Dashboard**
```bash
python _engine/scripts/generate-review-dashboard.py --niche {NICHE} {DATE}
```
- Output: `review-dashboard.html`
- If `fanrumor-traffic.json` exists, dashboard includes Content Performance panel
- Verify: check reported item count matches expected

**Step 14 — Review & Export**
- Review dashboard in browser (or verify via code)
- Approve items
- Export PostPlanner XLSX:
```bash
python _engine/scripts/generate-postplanner-export.py --niche {NICHE} {DATE}
```
- For TOBI (Facebook text-on-image):
```bash
python _engine/scripts/generate-postplanner-export.py --niche {NICHE} {DATE} --tobi
```

**Step 15 — Publish to GitHub Pages**
```bash
python _engine/scripts/publish-dashboard.py --niche {NICHE} {DATE}
```
- Script handles: git sync, .nojekyll, deploy workflow, index.html regeneration
- Verify deploy:
```bash
gh api repos/{ORG}/{REPO}/pages --jq '{status}'
# Should show: {"status":"built"}
```
- Verify content:
```bash
curl -s {GITHUB_PAGES_URL}/index.html | grep {DATE}
```

### Post-Pipeline — Update Status
- Update `{NICHE}/pipeline-status.md` with today's results
- Note any issues encountered for future reference

---

## Multi-Niche Daily Sequence

When running multiple niches in one session:

1. **Softball** first (more complex — FB + images + articles)
2. **Cubs** second (simpler — X/Twitter text-only)

For each niche, run the full pipeline Steps 1-15 before moving to the next.

---

## Troubleshooting

### GitHub Pages Build Stuck in "building" or "errored"

**Cause**: Legacy Jekyll builder or stale Actions runs
**Fix**:
```bash
# 1. Ensure repo has .nojekyll and deploy workflow
# (publish-dashboard.py handles this automatically)

# 2. Switch to workflow build type if still on legacy
gh api -X PUT repos/{ORG}/{REPO}/pages -f build_type="workflow"

# 3. Cancel stale Actions runs
for id in $(gh api repos/{ORG}/{REPO}/actions/runs --jq '.workflow_runs[] | select(.status == "queued" or .status == "in_progress") | .id'); do
  gh api -X POST repos/{ORG}/{REPO}/actions/runs/$id/cancel 2>/dev/null || true
done

# 4. Trigger fresh build
gh api -X POST repos/{ORG}/{REPO}/pages/builds

# 5. If still stuck, push an empty commit to re-trigger
git commit --allow-empty -m "Trigger Pages rebuild" && git push origin main
```

### Push Rejected (non-fast-forward)

**Cause**: Another session pushed to the same repo
**Fix**: `publish-dashboard.py` handles this via `git_sync_remote()`. If manual:
```bash
git fetch origin main
git merge origin/main --no-edit -X theirs
git push origin main
```

### TOBI Export Button Not Working

**Cause**: `parsePostingTime()` or `windowToTime` scoped inside wrong function
**Fix**: These functions MUST be at the outer scope in `generate-review-dashboard.py`, NOT inside `generateAndDownload()`.

### Dashboard Shows Wrong Date as "Latest"

**Cause**: `index.html` wasn't regenerated, or deploy failed
**Fix**: Re-run `publish-dashboard.py --niche {NICHE}` which regenerates index.html

### verify-facts.py Character Count Mismatch

**Cause**: URLs not normalized to 23 chars, or hidden characters
**Fix**: Check for invisible Unicode chars, ensure URLs treated as 23 chars

### Context Running Out Mid-Pipeline

**Prevention**: Update `pipeline-status.md` after each major step completes
**Recovery**: New session reads `pipeline-status.md`, resumes from last completed step

---

## Niche Reference

| Niche | Repo | Content Prefix | Photo Source | Platforms | Articles |
|-------|------|----------------|-------------|-----------|----------|
| Softball | `fangearhq-boop/ilovesoftball-dashboards` | `softball-content` | imagn | X + FB | Yes (400-800w) |
| Cubs | `fangearhq-boop/cubs-dashboards` | `cubs-content` | none | X only | No |
