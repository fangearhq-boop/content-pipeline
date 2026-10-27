"""Land a Sooners day folder through a pull request.

main requires a pull request (ruleset 25839983). This module pushes
`sooners-daily/YYYY-MM-DD`, opens one pull request, and squash-merges it.
It does not bypass the ruleset and it does not use auto-merge.

Actions:

- noop: origin/main already has a valid folder for that date
- merge-existing: an open pull request already has a valid folder; merge it
- adopt: that branch is valid and has no open pull request; open one and merge
- reuse: an open pull request exists but the branch folder is not valid
- create: no branch and no open pull request
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

from sooners_brief.contract import FACT_NAME, POSTS_NAME, content_folder_name, verify_brief, verify_day

DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
PUBLISH_ACTIONS = frozenset({"noop", "merge-existing", "adopt", "reuse", "create"})
_TOKEN_RE = re.compile(r"(x-access-token:)[^\s@]+|(ghp_[A-Za-z0-9]+)|(github_pat_[A-Za-z0-9_]+)")


class CommandFailed(RuntimeError):
    def __init__(self, argv: list[str], returncode: int, stderr: str):
        self.argv = argv
        self.returncode = returncode
        self.stderr = stderr
        super().__init__(_explain(argv, stderr))


def require_date(folder_date: str) -> str:
    if not DATE_RE.fullmatch(folder_date or ""):
        raise ValueError("date must be YYYY-MM-DD")
    return folder_date


def day_branch(folder_date: str) -> str:
    return f"sooners-daily/{require_date(folder_date)}"


def pr_title(folder_date: str) -> str:
    return f"Sooners daily brief {require_date(folder_date)}"


def pr_body(folder_date: str) -> str:
    date = require_date(folder_date)
    return (
        f"Sooners day folder for {date} (America/Chicago).\n\n"
        "The daily workflow opens this pull request because main requires one. "
        "Sooners unit tests and the red-proof guards ran in that same job before merge. "
        "A pull request opened with the workflow token does not start other workflows.\n"
    )


def plan_publish(*, main_valid: bool, open_pr: int | None, branch_valid: bool) -> str:
    """Choose one publish action. An open pull request is never duplicated."""
    if main_valid:
        return "noop"
    if branch_valid and open_pr is not None:
        return "merge-existing"
    if branch_valid:
        return "adopt"
    if open_pr is not None:
        return "reuse"
    return "create"


def decide_action(repo: Path, folder_date: str) -> str:
    branch = day_branch(folder_date)
    _fetch_main(repo)
    if _folder_valid(repo, "origin/main", folder_date):
        return "noop"
    sha = _remote_sha(repo, branch)
    branch_valid = False
    if sha:
        _fetch_branch(repo, branch)
        branch_valid = _folder_valid(repo, f"refs/remotes/origin/{branch}", folder_date)
    return plan_publish(
        main_valid=False,
        open_pr=_open_pr_number(repo, branch),
        branch_valid=branch_valid,
    )


def publish(repo: Path, folder_date: str, action: str) -> str:
    """Carry out `action`. A valid folder already on main becomes a no-op."""
    folder_date = require_date(folder_date)
    if action not in PUBLISH_ACTIONS:
        raise ValueError(f"unknown publish action {action}")
    branch = day_branch(folder_date)
    _fetch_main(repo)
    if _folder_valid(repo, "origin/main", folder_date):
        return "noop"
    if action == "noop":
        return "noop"
    if action in ("create", "reuse"):
        _commit_and_push(repo, folder_date, branch)
    number = _open_pr_number(repo, branch)
    if number is None:
        number = _create_pr(repo, branch, folder_date)
    _merge_squash(repo, number)
    return action


def _commit_and_push(repo: Path, folder_date: str, branch: str) -> None:
    existing = _remote_sha(repo, branch)
    if existing:
        _fetch_branch(repo, branch)
    snap = _snapshot(repo, folder_date)
    folder_prefix = f"Sooners/{content_folder_name(_as_date(folder_date))}/"
    if not any(path.startswith(folder_prefix) for path in snap):
        raise RuntimeError(f"day folder is not in the worktree for {folder_date}")
    _run(repo, ["git", "checkout", "--force", "-B", branch, "origin/main"])
    _run(repo, ["git", "clean", "-fd", "--", "Sooners"])
    _restore(repo, snap)
    hold = verify_day(repo / "Sooners" / content_folder_name(_as_date(folder_date)))
    if not hold.ok:
        raise RuntimeError(hold.summary())
    _run(repo, ["git", "add", "--", *sorted(snap)])
    staged = _run(repo, ["git", "diff", "--cached", "--quiet"], check=False)
    if staged.returncode == 0:
        raise RuntimeError("day folder produced no changes against main")
    if staged.returncode != 1:
        raise CommandFailed(["git", "diff", "--cached", "--quiet"], staged.returncode, _redact(staged.stderr))
    _run(
        repo,
        [
            "git",
            "-c",
            "user.name=Content Pipeline Bot",
            "-c",
            "user.email=fangearhq@gmail.com",
            "commit",
            "-m",
            f"Sooners pipeline {folder_date}: daily X brief",
        ],
    )
    refspec = f"HEAD:refs/heads/{branch}"
    if existing:
        _run(repo, ["git", "push", "--force-with-lease", "origin", refspec])
    else:
        _run(repo, ["git", "push", "-u", "origin", refspec])


def _create_pr(repo: Path, branch: str, folder_date: str) -> int:
    try:
        completed = _run(
            repo,
            [
                "gh",
                "pr",
                "create",
                "--base",
                "main",
                "--head",
                branch,
                "--title",
                pr_title(folder_date),
                "--body",
                pr_body(folder_date),
            ],
        )
    except CommandFailed:
        number = _open_pr_number(repo, branch)
        if number is not None:
            return number
        raise
    return _pr_number(completed.stdout)


def _merge_squash(repo: Path, number: int) -> None:
    _run(repo, ["gh", "pr", "merge", str(number), "--squash"])


def _open_pr_number(repo: Path, branch: str) -> int | None:
    completed = _run(
        repo,
        [
            "gh",
            "pr",
            "list",
            "--head",
            branch,
            "--base",
            "main",
            "--state",
            "open",
            "--json",
            "number",
        ],
    )
    try:
        rows = json.loads(completed.stdout or "[]")
    except json.JSONDecodeError as exc:
        raise RuntimeError("gh pr list did not return JSON") from exc
    if not rows:
        return None
    return int(rows[0]["number"])


def _folder_valid(repo: Path, ref: str, folder_date: str) -> bool:
    folder = f"Sooners/{content_folder_name(_as_date(folder_date))}"
    posts = _git_show(repo, f"{ref}:{folder}/{POSTS_NAME}")
    facts = _git_show(repo, f"{ref}:{folder}/{FACT_NAME}")
    if posts is None or facts is None:
        return False
    return verify_brief(posts, facts).ok


def _git_show(repo: Path, spec: str) -> str | None:
    completed = _run(repo, ["git", "show", spec], check=False)
    if completed.returncode != 0:
        return None
    return completed.stdout


def _fetch_main(repo: Path) -> None:
    _run(repo, ["git", "fetch", "origin", "main"])


def _fetch_branch(repo: Path, branch: str) -> None:
    _run(repo, ["git", "fetch", "origin", f"+refs/heads/{branch}:refs/remotes/origin/{branch}"])


def _remote_sha(repo: Path, branch: str) -> str | None:
    completed = _run(repo, ["git", "ls-remote", "origin", f"refs/heads/{branch}"])
    line = completed.stdout.strip()
    if not line:
        return None
    return line.split()[0]


def _snapshot(repo: Path, folder_date: str) -> dict[str, bytes]:
    niche = repo / "Sooners"
    folder = niche / content_folder_name(_as_date(folder_date))
    paths: list[Path] = []
    if folder.is_dir():
        paths.extend(path for path in folder.rglob("*") if path.is_file())
    for name in ("story-history.md", "pipeline-status.md"):
        path = niche / name
        if path.is_file():
            paths.append(path)
    return {path.relative_to(repo).as_posix(): path.read_bytes() for path in paths}


def _restore(repo: Path, snap: dict[str, bytes]) -> None:
    for rel, data in snap.items():
        dest = repo / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)


def _as_date(folder_date: str):
    return datetime.strptime(require_date(folder_date), "%Y-%m-%d").date()


def _pr_number(text: str) -> int:
    match = re.search(r"/pull/(\d+)\s*$", text.strip())
    if not match:
        raise RuntimeError(f"could not read pull request number from {text.strip()!r}")
    return int(match.group(1))


def _run(repo: Path, args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        args,
        cwd=repo,
        env=os.environ.copy(),
        capture_output=True,
        text=True,
        check=False,
    )
    if check and completed.returncode != 0:
        raise CommandFailed(args, completed.returncode, _redact(completed.stderr))
    return completed


def _redact(text: str) -> str:
    return _TOKEN_RE.sub(lambda match: (match.group(1) or "") + "REDACTED" if match.group(1) else "REDACTED", text)


def _explain(argv: list[str], stderr: str) -> str:
    text = stderr.casefold()
    hint = ""
    if "create or approve pull request" in text or "not permitted to create" in text:
        hint = (
            "GitHub refused to let this workflow open a pull request. "
            'Steve: Settings → Actions → General → Workflow permissions → enable '
            '"Allow GitHub Actions to create and approve pull requests". '
            "This workflow does not change that setting.\n"
        )
    elif any(token in text for token in ("review required", "approving review", "code owner")):
        hint = (
            "The pull request is open but merge wants a review. Ruleset 25839983 "
            "requires 0 approvals and has require_extra_approval_for_unattributed_changes "
            "enabled. GitHub documents that flag as applying to unattributed Copilot "
            "changes and as inert when required approvals are 0. If merge still asks "
            'for a review, Steve clears "Require approval for unattributed changes" on '
            'ruleset "main: pull requests (admins + service-tokens app exempt)". '
            "Do not bypass the ruleset. If that flag has to stay, push the day folders "
            "to an unprotected branch such as sooners-briefs (the ruleset targets only "
            "the default branch) and point sooners-x-bot's raw-content ref at that "
            "branch instead of main. This workflow does not change the bot.\n"
        )
    shown = " ".join(argv)
    detail = stderr.strip()
    return f"{hint}{shown} failed.\n{detail}".strip()
