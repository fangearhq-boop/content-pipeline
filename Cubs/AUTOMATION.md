# Chicago Cubs Fan HQ — Automation Setup

## Overview

The Cubs pipeline can be automated to run 1-2x daily with email alerts. Two components:

1. **GitHub Actions reminder** — sends email/Discord alerts on a schedule
2. **Local runner** (optional) — runs Claude Code headlessly on your machine

---

## 1. GitHub Actions Email Alerts

A GitHub Actions workflow in `fangearhq-boop/cubs-dashboards` sends email reminders twice daily prompting you to run the pipeline.

### Schedule

| Time (CT) | Purpose |
|-----------|---------|
| 6:00 AM | Morning batch — overnight news, game recaps, daily content |
| 4:00 PM | Afternoon refresh — midday developments, evening preview |

### Setup Steps

1. **Add secrets** to the `cubs-dashboards` repo:

   Go to: `github.com/fangearhq-boop/cubs-dashboards/settings/secrets/actions`

   | Secret | Value |
   |--------|-------|
   | `EMAIL_USERNAME` | Gmail address to send from (e.g., `fangearhq@gmail.com`) |
   | `EMAIL_PASSWORD` | Gmail App Password (not your regular password) |
   | `NOTIFY_EMAIL` | Email to receive alerts (can be the same address) |

2. **Create a Gmail App Password** (required if using Gmail):
   - Go to `myaccount.google.com/apppasswords`
   - Select "Mail" and "Windows Computer"
   - Copy the 16-character password → use as `EMAIL_PASSWORD`

3. **Test it**: Go to the Actions tab in the repo → select "Daily Cubs Pipeline Reminder" → click "Run workflow"

### Optional: Discord Alerts

Uncomment the Discord step in `.github/workflows/daily-pipeline-reminder.yml` and add a `DISCORD_WEBHOOK` secret with your Discord webhook URL.

---

## 2. Running the Pipeline

When you get the alert:

### Quick (Cubs only)
Open Claude Code in your Fan_HQ project and type:
```
Run the Cubs content pipeline for today
```

### Full (all niches)
Copy the contents of `daily-pipeline-prompt.md` into Claude Code to run all three pipelines (Softball, Parenting, Cubs) simultaneously.

### After the pipeline runs
1. Review the dashboard at: https://fangearhq-boop.github.io/cubs-dashboards/
2. Approve/reject tweets in the dashboard
3. Run PostPlanner export: `python generate-postplanner-csv.py YYYY-MM-DD`
4. Upload the CSV to PostPlanner → "Create multiple posts" → spreadsheet upload

---

## 3. Future: Full Automation via Claude CLI

When ready to go fully hands-free, you can use Windows Task Scheduler + Claude CLI:

```powershell
# Save as run-cubs-pipeline.ps1
$env:ANTHROPIC_API_KEY = "your-api-key"
cd "C:\Users\srshi\FanHQ Dropbox\Steve Shideler\Claude\Fan_HQ"
claude -p "Run the Cubs content pipeline for today" --dangerously-skip-permissions
```

Then create a Windows Task Scheduler task:
- **Trigger**: Daily at 6:00 AM
- **Action**: Run `powershell.exe -File run-cubs-pipeline.ps1`
- **Condition**: Start only if computer is on AC power

> **Note**: `--dangerously-skip-permissions` runs without approval prompts. Review output carefully the first few times. Consider using `--allowedTools` for finer control.

---

## File Locations

| File | Location |
|------|----------|
| GitHub Actions workflow | `fangearhq-boop/cubs-dashboards/.github/workflows/daily-pipeline-reminder.yml` |
| This doc | `Niche_Launches/Cubs/AUTOMATION.md` |
| Pipeline prompt | `Fan_HQ/daily-pipeline-prompt.md` |
| PostPlanner export | `Niche_Launches/Cubs/generate-postplanner-csv.py` |
| Review dashboard | `https://fangearhq-boop.github.io/cubs-dashboards/` |
