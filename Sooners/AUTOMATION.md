# Sooners Fan Recap — Automation

`.github/workflows/sooners-daily.yml` has been removed.

That workflow was the only publisher of `Sooners/sooners-content-YYYY-MM-DD/`. Its publish step failed on every scheduled run that passed the Denver hour gate, because GitHub Actions is not permitted to open pull requests. No day folder from it is on `main`.

fangearhq-boop/sooners-x-bot now builds its own daily brief from its own feeds (PR #8, merge `7ff26dd`). It does not read this repo's Sooners output. Nothing else in content-pipeline, content-dashboards, or cubs-dashboards reads that output either.

`Sooners/scripts/` and `sooners_brief/` stay. They are Sooners-only and still covered by `.github/workflows/sooners-brief-ci.yml`, which runs the unit tests and `prove_accuracy_red.py` when `Sooners/**` or a `sooners-*.yml` workflow changes. That CI workflow has `contents: read` and does not publish a day folder.

Shared `_engine` scripts and every other school's workflow are unchanged. Do not restore the daily cron.
