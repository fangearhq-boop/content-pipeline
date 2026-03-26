# Run Daily Content Pipeline

Run the full 15-step content pipeline for a niche. Usage: `/run-pipeline <niche>` where niche is `softball` or `cubs`.

## Instructions

You are running the daily content pipeline. Follow these steps exactly:

### 1. Load Context (do ALL of these before any content work)

Read these files based on the niche argument ($ARGUMENTS):
- If `softball`: niche root = `Niche_Launches/Softball`, config = `Softball/niche-config.yaml`
- If `cubs`: niche root = `Niche_Launches/Cubs`, config = `Cubs/niche-config.yaml`

```
Read: {NICHE_ROOT}/pipeline-status.md
Read: {NICHE_ROOT}/niche-config.yaml
Read: {NICHE_ROOT}/seasonal-calendar.md
Read: _engine/CLAUDE.md
Read: _engine/daily-runbook.md
```

Check pipeline-status.md to see if today's pipeline has already been started. If resuming, pick up from the last incomplete step.

### 2. Pre-Flight Checks

For niches with a dashboard repo, verify:
```bash
cd {DASHBOARD_REPO_PATH}
git fetch origin main
git status
```
- If behind remote: `git merge origin/main --no-edit`
- If untracked files: commit or clean up

Verify GitHub Pages:
```bash
gh api repos/{ORG}/{REPO}/pages --jq '{build_type, status}'
```
- `build_type` MUST be `"workflow"` — if `"legacy"`, fix it before proceeding

### 3. Execute Pipeline

Follow the 15-step pipeline from `_engine/daily-runbook.md`. Key reminders:
- Steps are SEQUENTIAL (except 6-8 which can run concurrently)
- GAME RESULTS AND PREVIEWS go FIRST (earliest time slots)
- Gate at Step 3: need at least 5 stories
- Gate at Step 10: fact-check must pass before dashboard generation
- Skip Facebook (Step 7) if platform config has no facebook
- Skip images (Steps 8, 11) if `photo_source: none`
- Skip articles (Step 9) if articles disabled in config

### 4. After Each Major Phase

Update `{NICHE_ROOT}/pipeline-status.md` with progress. This protects against context loss — if the session ends mid-pipeline, the next session can resume from the last completed step.

### 5. Post-Pipeline

After Step 15 completes:
1. Update `pipeline-status.md` with final results
2. Note any issues encountered
3. If running multiple niches, proceed to the next niche (Softball first, then Cubs)
