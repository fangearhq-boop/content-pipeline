# Sooners Pipeline Status

`.github/workflows/sooners-daily.yml` has been removed. The publish step failed on every run that reached it, and no `sooners-content-YYYY-MM-DD/` folder is on main.

sooners-x-bot (PR #8, `7ff26dd`) builds its own daily brief and does not read this folder. Leave the cron retired.

A manual dry run prints a brief and does not write a folder:

```bash
python Sooners/generate_daily.py --dry-run
```
