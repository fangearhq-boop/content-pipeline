# Sooners Pipeline Status

No Chicago day folder has been committed yet.

The first folder is written by `.github/workflows/sooners-daily.yml` at 7:05 AM America/Denver after this niche is on `main`. That run uses the America/Chicago date, which is the same morning.

Manual generation:

```bash
python Sooners/generate_daily.py --dry-run
```

A dry run prints the brief and does not write `sooners-content-YYYY-MM-DD/`.
