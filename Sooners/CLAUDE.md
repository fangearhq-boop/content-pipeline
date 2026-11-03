# Sooners niche

This folder is the college brief generator. It is not a 15-step engine run. sooners-x-bot builds its own brief and does not read this folder.

- Generator: `generate_daily.py` and `sooners_brief/`
- Contract the checker enforces: `sooners_brief/contract.py`
- Schedule: removed. `.github/workflows/sooners-daily.yml` is gone.
- Tests: `python -m unittest discover -s Sooners/tests -v`
- Red proof: `python Sooners/scripts/prove_accuracy_red.py`

Write the Chicago day folder only from the generator. A hand-edited score with no VERIFIED allowlisted row will be held.

The shared `_engine` tree stays as it is. Niche behavior lives here.
