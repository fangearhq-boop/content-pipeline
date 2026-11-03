# Sooners Fan Recap

Local generator for a Chicago-dated X brief. The folder date is America/Chicago. The generator writes:

`Sooners/sooners-content-YYYY-MM-DD/03-social-posts-x.md`
`Sooners/sooners-content-YYYY-MM-DD/06-fact-check-log.md`

sooners-x-bot builds its own brief and does not read those files.

Generate with:

```bash
python Sooners/generate_daily.py --dry-run --date YYYY-MM-DD
python Sooners/generate_daily.py --date YYYY-MM-DD
```

There is no scheduled run. `.github/workflows/sooners-daily.yml` was removed.

Do not cite mlb.com, statsapi.mlb.com, or baseball-reference.com.
