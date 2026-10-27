# Sooners Pipeline Status

No Chicago day folder is on main yet. The 2026-10-27 run wrote a folder and GitHub rejected the push to main.

The next folder is written by `.github/workflows/sooners-daily.yml` at 7:05 AM America/Denver after the pull-request publish path is on main. That run uses the America/Chicago date. 2026-10-27 can be skipped.

Manual generation:

```bash
python Sooners/generate_daily.py --dry-run
```

A dry run prints the brief and does not write `sooners-content-YYYY-MM-DD/`.
