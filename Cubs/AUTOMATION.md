# Chicago Cubs Fan HQ — Automation

## Overview

The Cubs X/Twitter account (@CubsFanRecap) is posted by **two separate
Railway services**, NOT by manual PostPlanner uploads. This file documents
how the pieces fit together.

```
┌──────────────────────────────┐       ┌──────────────────────────────┐
│ content-pipeline/Cubs/       │       │ fangearhq-boop/cubs-x-bot    │
│ cubs-content-YYYY-MM-DD/     │  ──►  │ (Railway: "Cubs X Bot")      │
│   07-content-data.json       │       │ cron every 15 min            │
└──────────────────────────────┘       │ ingests brief, falls back    │
                                       │ to RSS if brief is exhausted │
                                       └──────────┬───────────────────┘
                                                  │ posts via
                                                  │ api.x.com/2/tweets
                                                  ▼
                                       ┌──────────────────────────────┐
                                       │ @CubsFanRecap on X           │
                                       └──────────▲───────────────────┘
                                                  │ posts via
                                                  │ api.x.com/2/tweets
┌──────────────────────────────┐                  │
│ fangearhq-boop/game-monitor  │  live MLB events │
│ (Railway: "lucid-essence")   │──────────────────┘
│ long-running poll loop,      │
│ MLB StatsAPI every 45s       │
│ during active games          │
└──────────────────────────────┘
```

Both services share X OAuth tokens via the `cubsbot_tokens` table in
Supabase. Either can refresh; both read the same row.

## Daily Operation

### 1. Run the pipeline

Open Claude Code in this repo and invoke the content engine for Cubs:

```
Run the Cubs content pipeline for today
```

This produces `Cubs/cubs-content-YYYY-MM-DD/` with all 15 pipeline outputs.
The one file that matters for auto-posting is `07-content-data.json` — that's
the consumption format cubs-x-bot reads.

### 2. Review the dashboard

Pipeline step 13 publishes a review dashboard to
`https://fangearhq-boop.github.io/cubs-dashboards/`.
Approve/edit tweets in the dashboard as normal.

### 3. Commit and push

```bash
git add Cubs/cubs-content-YYYY-MM-DD/
git commit -m "Cubs YYYY-MM-DD: <summary>"
git push origin main
```

**This push is the deploy step.** cubs-x-bot's next cron tick (within 15 min)
will fetch the new brief from `raw.githubusercontent.com/fangearhq-boop/content-pipeline/main/Cubs/cubs-content-YYYY-MM-DD/07-content-data.json` and post any tweets whose CT posting_time falls inside the current cron window.

**You do NOT need to touch PostPlanner.** The xlsx export in `postplanner-imports/` is legacy and not read by the auto-poster.

## How Brief Ingestion Works

`cubs-x-bot/brief_monitor.py` runs at the top of every cron cycle:

1. Fetch `07-content-data.json` from GitHub raw for today's CT date
2. Walk `stories[].x_posts[]`
3. For each post, compute its scheduled time in CT
4. Fire the post if:
   - `scheduled_time <= now_ct`
   - `now_ct - scheduled_time <= BRIEF_GRACE_MINUTES` (default 60 min)
   - The tweet text hash is not in `cubsbot_tweets` yet
   - We haven't hit `MAX_POSTS_PER_DAY` (default 12)
   - We haven't hit the current window cap
   - No Cubs game is currently live (quiet mode defers to game-monitor)

So a 7:00 AM CT slot fires on the first cron tick between 7:00 and 8:00 AM CT,
not at exactly 7:00:00. Grace window is forgiving enough to handle cron misfires.

## Posting Windows and Caps

cubs-x-bot has two safety rails that cap both brief and RSS posts:

| Setting | Default | What it caps |
|---|---|---|
| `MAX_POSTS_PER_DAY` | 12 | All posts in a UTC day |
| `POST_WINDOWS` | 5/4/3 | Morning/afternoon/evening slots in CT |
| `MAX_POSTS_PER_TOPIC` | 2 | Posts sharing a topic_key (RSS only — brief is exempt) |
| `NEWSWORTHINESS_THRESHOLD` | 7 | RSS score floor for the editorial LLM filter |

Brief posts compete for the same cap as RSS posts, but brief runs first in
each cycle so curated content has priority.

## What game-monitor Handles (Automatically, No Human Input)

`fangearhq-boop/game-monitor` polls MLB StatsAPI continuously and fires tweets
for Cubs games only:

- **Game preview** — once per game, ~2 hours before first pitch
- **Home runs** — Cubs batters only (opponent HRs are detected but not posted)
- **Lead changes** — only when Cubs TAKE the lead (not when they tie, not when opponent leads)
- **Game final** — every Cubs game, with winning/losing/save pitcher

Budget is `GAMEDAY_POST_BUDGET` (default 10) and is **separate from cubs-x-bot's
daily cap**, so a 12-post news day plus a 5-event game day is fine.

## Troubleshooting

| Symptom | First thing to check |
|---|---|
| No brief tweets posting | Has today's `cubs-content-YYYY-MM-DD/07-content-data.json` been pushed to main? |
| Brief 404 in logs | Date mismatch (CT vs UTC), or the pipeline output wasn't committed |
| Tweets are generic RSS filler | Brief wasn't pushed, so bot fell back to RSS path |
| No tweets posting at all | Check `MAX_POSTS_PER_DAY` cap via `railway logs --service "Cubs X Bot"` |
| 401 on X API in logs | `cubsbot_tokens` table token drift — usually self-heals on next run |
| No game-day tweets during Cubs game | Check `railway logs --service "lucid-essence"` for "Cubs game(s)" in the schedule line |

## Infrastructure Pointers

- **cubs-x-bot repo:** `fangearhq-boop/cubs-x-bot`, Railway project `Cubs X Bot`
- **game-monitor repo:** `fangearhq-boop/game-monitor`, Railway project `lucid-essence` (auto-generated name)
- **Both services auto-deploy on push to master** — Railway GitHub App is wired via `deploymentTriggerCreate` mutation
- **Shared Supabase tables:** `cubsbot_tweets`, `cubsbot_tokens`, `cubsbot_settings`
- **Review dashboard:** `https://fangearhq-boop.github.io/cubs-dashboards/`

## Deprecated

- PostPlanner manual xlsx upload workflow. `generate-postplanner-export.py` still
  exists and still produces xlsx files in `Cubs/postplanner-imports/`, but the
  auto-poster does not read them. If you stop needing PostPlanner entirely, that
  script and folder can be deleted in a future cleanup.
- GitHub Actions email reminder workflow (`fangearhq-boop/cubs-dashboards/.github/workflows/daily-pipeline-reminder.yml`)
  still runs but is less necessary now that the pipeline output flows directly
  to auto-posters on push.
