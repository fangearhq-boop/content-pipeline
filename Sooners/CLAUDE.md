# Sooners niche

This folder is the college brief for sooners-x-bot. It is not a 15-step engine run.

- Generator: `generate_daily.py` and `sooners_brief/`
- Contract the bot-shaped checker enforces: `sooners_brief/contract.py`
- Schedule: repo-root `.github/workflows/sooners-daily.yml`
- Tests: `python -m unittest discover -s Sooners/tests -v`
- Red proof: `python Sooners/scripts/prove_accuracy_red.py`

Write the Chicago day folder only from the generator. A hand-edited score with no VERIFIED allowlisted row will be held.

The shared `_engine` tree stays as it is. Niche behavior lives here.
