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

- 07:05 America/Denver.
- Two UTC crons, `5 13 * * *` and `5 14 * * *`. The job continues only when the Denver clock says 07, so daylight time and standard time each fire once.
- 7:05 AM Denver is 8:05 AM Chicago, before the 9:00 AM CT slot, on the same calendar date.

Secrets: `GITHUB_TOKEN` only, with `contents: write`, so the workflow can commit the day folder the way the other niches land on `main`. No new secret. The bot's `ANTHROPIC_API_KEY` is not used here. The generator does not call a model.

`workflow_dispatch` defaults `commit` to false. A click prints a dry run. A write is allowed only when the run is on `main` and `commit` is true, or when the schedule fires. Do not dispatch a committing run to put a day live. Steve decides when `main` gets the workflow.

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
