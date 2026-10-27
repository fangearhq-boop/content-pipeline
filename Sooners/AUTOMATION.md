# Sooners Fan Recap — Automation

```
Sooners/sooners-content-YYYY-MM-DD/
  03-social-posts-x.md
  06-fact-check-log.md
        │
        │  raw GitHub, main branch, America/Chicago date
        ▼
fangearhq-boop/sooners-x-bot
  polls about every 15 minutes
  posts the six slots via api.x.com
        ▼
@SoonersFanRecap
```

This repo only writes the brief. It does not hold X tokens and it does not call the X API.

## Schedule

`.github/workflows/sooners-daily.yml`

- 07:05 America/Denver, with hour 08 accepted so a delayed cron still writes.
- Two UTC crons, `5 13 * * *` and `5 14 * * *`. The job continues when the Denver hour is 07 or 08.
- 7:05 AM Denver is 8:05 AM Chicago, before the 9:00 AM CT slot, on the same calendar date.
- The job does not push to `main`. Ruleset 25839983 requires a pull request. The run pushes `sooners-daily/YYYY-MM-DD`, opens one pull request, and squash-merges it with `gh pr merge --squash`. Auto-merge stays off.
- A later run in the same window does not generate again when `main` already has a valid folder, or when an open pull request for that date already has one. It squash-merges that open pull request instead of opening a second one. A stale open pull request (the branch folder does not verify) is updated on the same branch.

Secrets: `GITHUB_TOKEN` only. Permissions are `contents: write` and `pull-requests: write`. No new secret. The bot's `ANTHROPIC_API_KEY` is not used here. The generator does not call a model.

The workflow token does not start other workflows, and this ruleset has no required checks. The daily job runs the Sooners unit tests and `prove_accuracy_red.py` before it merges.

`workflow_dispatch` defaults `commit` to false. A click prints a dry run and does not open a pull request. A write is allowed only when the run is on `main` and `commit` is true, or when the schedule fires. A committing dispatch on `main` does open and squash-merge a live day. Do not dispatch one unless that day should land.

If the first real run fails opening the pull request, the usual cause is a repo setting this workflow cannot read or change: **Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests**. Leave the ruleset alone. If merge instead asks for a review even though the ruleset requires zero approvals, the ruleset flag `require_extra_approval_for_unattributed_changes` is the thing to clear on ruleset "main: pull requests (admins + service-tokens app exempt)". If that flag has to stay, the fallback is an unprotected branch such as `sooners-briefs` (the ruleset covers only the default branch) and a one-line sooners-x-bot loader change to read that ref instead of `main`. That bot change is not in this repo.

## What the bot posts

Six fenced tweets, Chicago times:

| Chicago | Denver | Slot |
| --- | --- | --- |
| 9:00 AM | 8:00 AM | Football morning recap |
| 10:30 AM | 9:30 AM | Football next look |
| 12:30 PM | 11:30 AM | Basketball |
| 3:00 PM | 2:00 PM | Recruiting |
| 6:00 PM | 5:00 PM | Softball |
| 8:30 PM | 7:30 PM | Baseball |

If a sport has no fresh allowlisted number, that slot is a number-free fan line. The fact-check log still has to say `VERIFIED` and `Acceptable for social`.

## First live day

Merging this niche does not create today's folder. The schedule writes the next 7:05 AM Denver folder. sooners-x-bot keeps skipping until that folder is on `main`. After it is there, the next poll (about 15 minutes) can post slots whose Chicago time has arrived.

## Nested workflows

`Sooners/` does not ship a Pages workflow. Sibling `*/.github/workflows/deploy-pages.yml` files are not the GitHub Actions entry point for this monorepo. The runs that matter are the two workflows at the repo root: `sooners-daily.yml` and `sooners-brief-ci.yml`.
