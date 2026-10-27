# Sooners Fan Recap

X-only daily brief for @SoonersFanRecap. sooners-x-bot reads:

`Sooners/sooners-content-YYYY-MM-DD/03-social-posts-x.md`
`Sooners/sooners-content-YYYY-MM-DD/06-fact-check-log.md`

The date is America/Chicago.

Generate with:

```bash
python Sooners/generate_daily.py --dry-run --date YYYY-MM-DD
python Sooners/generate_daily.py --date YYYY-MM-DD
```

The scheduled run is `.github/workflows/sooners-daily.yml` at 7:05 AM America/Denver. It opens `sooners-daily/YYYY-MM-DD` and squash-merges that pull request. It does not push to `main`. A manual run writes only on `main` with `commit` set to true.

Do not cite mlb.com, statsapi.mlb.com, or baseball-reference.com.
