"""Branch, pull request, and idempotency behavior for the Sooners day publish."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from datetime import date
from pathlib import Path

NICHE = Path(__file__).resolve().parents[1]
if str(NICHE) not in sys.path:
    sys.path.insert(0, str(NICHE))

import generate_daily  # noqa: E402
from scripts.run_daily import generate_phase, main as run_main, resolve_request  # noqa: E402
from sooners_brief.contract import verify_day  # noqa: E402
from sooners_brief.publish import day_branch, plan_publish, publish  # noqa: E402

DAY = "2026-10-26"
BRANCH = "sooners-daily/2026-10-26"

_FAKE_GH = """#!/usr/bin/env python3
import json
import os
import sys

args = sys.argv[1:]
log = os.environ["GH_LOG"]
with open(log, "a", encoding="utf-8") as handle:
    handle.write(json.dumps(args) + "\\n")
if "--auto" in args or "--admin" in args:
    sys.stderr.write("refusing bypass\\n")
    sys.exit(2)
if args[:2] == ["pr", "list"]:
    sys.stdout.write(os.environ.get("GH_PR_LIST", "[]").strip() + "\\n")
elif args[:2] == ["pr", "create"]:
    listed = os.environ.get("GH_PR_LIST", "[]").strip()
    if listed not in ("", "[]"):
        sys.stderr.write("a pull request for this branch already exists\\n")
        sys.exit(1)
    sys.stdout.write("https://github.com/fangearhq-boop/content-pipeline/pull/99\\n")
elif args[:2] == ["pr", "merge"]:
    if "--squash" not in args:
        sys.stderr.write("squash required\\n")
        sys.exit(3)
elif args:
    sys.stderr.write("unexpected gh\\n")
    sys.exit(4)
"""


@contextmanager
def _env(**values):
    previous = {key: os.environ.get(key) for key in values}
    for key, value in values.items():
        if value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = value
    try:
        yield
    finally:
        for key, value in previous.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def _git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    if check and completed.returncode != 0:
        raise AssertionError(f"git {args} -> {completed.returncode}\\n{completed.stderr}")
    return completed


def _init_repo(tmp: Path) -> Path:
    origin = tmp / "origin.git"
    repo = tmp / "repo"
    subprocess.run(["git", "init", "--bare", "-b", "main", str(origin)], check=True, capture_output=True)
    subprocess.run(["git", "init", "-b", "main", str(repo)], check=True, capture_output=True)
    _git(repo, "config", "user.name", "Test")
    _git(repo, "config", "user.email", "test@example.com")
    _git(repo, "config", "commit.gpgsign", "false")
    niche = repo / "Sooners"
    niche.mkdir()
    (niche / "story-history.md").write_text(
        "# Sooners Story History\n\n| Date | Slot | URL | Title |\n|------|------|-----|-------|\n",
        encoding="utf-8",
    )
    _git(repo, "add", "Sooners")
    _git(repo, "commit", "-m", "init")
    _git(repo, "remote", "add", "origin", str(origin))
    _git(repo, "push", "-u", "origin", "main")
    return repo


def _write_day(repo: Path, folder_date: str = DAY) -> None:
    on_date = date.fromisoformat(folder_date)
    code = generate_daily.run(on_date, False, loader=lambda _on: {}, niche_root=repo / "Sooners")
    if code != 0:
        raise AssertionError(f"generate_daily returned {code}")


def _gh_bin(tmp: Path) -> Path:
    bindir = tmp / "bin"
    bindir.mkdir()
    script = bindir / "gh"
    script.write_text(_FAKE_GH, encoding="utf-8")
    script.chmod(0o755)
    return bindir


def _calls(log: Path) -> list[list[str]]:
    if not log.is_file():
        return []
    return [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines() if line.strip()]


def _checkout_main(repo: Path) -> None:
    _git(repo, "checkout", "main")
    _git(repo, "reset", "--hard", "origin/main")
    _git(repo, "clean", "-fd")


class PublishPlanTests(unittest.TestCase):
    def test_branch_name_and_rejected_dates(self):
        self.assertEqual(day_branch("2026-10-28"), "sooners-daily/2026-10-28")
        for raw in ("2026-10-28;id", "2026-10-28 && true", "$(date)", "sooners-daily/2026-10-28", ""):
            with self.subTest(raw=raw):
                with self.assertRaises(ValueError):
                    day_branch(raw)

    def test_plan_covers_noop_reuse_and_no_second_pr(self):
        self.assertEqual(plan_publish(main_valid=True, open_pr=41, branch_valid=True), "noop")
        self.assertEqual(plan_publish(main_valid=False, open_pr=41, branch_valid=True), "merge-existing")
        self.assertEqual(plan_publish(main_valid=False, open_pr=None, branch_valid=True), "adopt")
        self.assertEqual(plan_publish(main_valid=False, open_pr=41, branch_valid=False), "reuse")
        self.assertEqual(plan_publish(main_valid=False, open_pr=None, branch_valid=False), "create")

    def test_resolve_request_and_bad_date_stay_out_of_git(self):
        with _env(INPUT_DATE="2026-10-28", EVENT_NAME="schedule", INPUT_COMMIT="false"):
            self.assertEqual(resolve_request(), ("2026-10-28", True))
        with _env(INPUT_DATE="2026-10-28", EVENT_NAME="workflow_dispatch", INPUT_COMMIT="false"):
            self.assertEqual(resolve_request(), ("2026-10-28", False))
        with _env(INPUT_DATE="2026-10-28", EVENT_NAME="workflow_dispatch", INPUT_COMMIT="true"):
            self.assertEqual(resolve_request(), ("2026-10-28", True))
        with _env(INPUT_DATE="2026-10-28;id", EVENT_NAME="schedule", INPUT_COMMIT="true"):
            self.assertEqual(run_main(["generate"]), 1)
        with _env(FOLDER_DATE="not-a-date", PUBLISH_ACTION="create"):
            self.assertEqual(run_main(["publish"]), 1)
        with _env(FOLDER_DATE=DAY, PUBLISH_ACTION="push-main"):
            self.assertEqual(run_main(["publish"]), 1)


class PublishGitTests(unittest.TestCase):
    def test_create_names_the_branch_and_squash_merges_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = _init_repo(root)
            log = root / "gh.log"
            bindir = _gh_bin(root)
            with _env(PATH=f"{bindir}{os.pathsep}{os.environ.get('PATH', '')}", GH_LOG=str(log), GH_PR_LIST="[]"):
                code, action = generate_phase(repo, DAY, True, loader=lambda _on: {})
                self.assertEqual((code, action), (0, "create"))
                self.assertEqual(publish(repo, DAY, action), "create")
            calls = _calls(log)
            created = [args for args in calls if args[:2] == ["pr", "create"]]
            self.assertEqual(len(created), 1)
            self.assertEqual(created[0][created[0].index("--head") + 1], BRANCH)
            self.assertEqual(created[0][created[0].index("--base") + 1], "main")
            self.assertEqual(created[0][created[0].index("--title") + 1], f"Sooners daily brief {DAY}")
            self.assertIn(["pr", "merge", "99", "--squash"], calls)
            for args in calls:
                self.assertNotIn("--auto", args)
                self.assertNotIn("--admin", args)
            tip = _git(repo, "log", "-1", "--format=%an%n%ae%n%s", BRANCH)
            self.assertEqual(
                tip.stdout.splitlines(),
                ["Content Pipeline Bot", "fangearhq@gmail.com", f"Sooners pipeline {DAY}: daily X brief"],
            )
            self.assertTrue(verify_day(repo / "Sooners" / f"sooners-content-{DAY}").ok)
            remote = _git(repo, "ls-remote", "origin", f"refs/heads/{BRANCH}")
            self.assertIn(f"refs/heads/{BRANCH}", remote.stdout)

    def test_valid_main_folder_is_a_noop(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = _init_repo(root)
            _write_day(repo)
            _git(repo, "add", "Sooners")
            _git(repo, "commit", "-m", "land the day on main")
            _git(repo, "push", "origin", "main")
            log = root / "gh.log"
            bindir = _gh_bin(root)

            def boom(_on):
                raise AssertionError("second run must not generate")

            with _env(PATH=f"{bindir}{os.pathsep}{os.environ.get('PATH', '')}", GH_LOG=str(log), GH_PR_LIST="[]"):
                code, action = generate_phase(repo, DAY, True, loader=boom)
                self.assertEqual((code, action), (0, "noop"))
                self.assertEqual(publish(repo, DAY, "create"), "noop")
            self.assertEqual(_calls(log), [])
            remote = _git(repo, "ls-remote", "origin", f"refs/heads/{BRANCH}")
            self.assertEqual(remote.stdout.strip(), "")

    def test_open_pr_is_reused_and_not_duplicated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = _init_repo(root)
            log = root / "gh.log"
            bindir = _gh_bin(root)
            env = {
                "PATH": f"{bindir}{os.pathsep}{os.environ.get('PATH', '')}",
                "GH_LOG": str(log),
                "GH_PR_LIST": "[]",
            }
            with _env(**env):
                code, action = generate_phase(repo, DAY, True, loader=lambda _on: {})
                self.assertEqual(action, "create")
                self.assertEqual(code, 0)
                self.assertEqual(publish(repo, DAY, "create"), "create")
                first = _git(repo, "rev-parse", BRANCH).stdout.strip()
            _checkout_main(repo)
            env["GH_PR_LIST"] = json.dumps([{"number": 99}])

            def boom(_on):
                raise AssertionError("open pull request must not generate again")

            with _env(**env):
                code, action = generate_phase(repo, DAY, True, loader=boom)
                self.assertEqual((code, action), (0, "merge-existing"))
                self.assertEqual(publish(repo, DAY, action), "merge-existing")
                second = _git(repo, "rev-parse", BRANCH).stdout.strip()
            self.assertEqual(first, second)
            calls = _calls(log)
            self.assertEqual(len([args for args in calls if args[:2] == ["pr", "create"]]), 1)
            self.assertGreaterEqual(calls.count(["pr", "merge", "99", "--squash"]), 1)
            self.assertEqual(calls[-2:], [["pr", "list", "--head", BRANCH, "--base", "main", "--state", "open", "--json", "number"], ["pr", "merge", "99", "--squash"]])

    def test_stale_open_pr_is_updated_without_a_second_pr(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = _init_repo(root)
            folder = repo / "Sooners" / f"sooners-content-{DAY}"
            folder.mkdir()
            (folder / "03-social-posts-x.md").write_text("not a brief\n", encoding="utf-8")
            (folder / "06-fact-check-log.md").write_text("nope\n", encoding="utf-8")
            _git(repo, "checkout", "-B", BRANCH)
            _git(repo, "add", "Sooners")
            _git(repo, "commit", "-m", "stale day")
            _git(repo, "push", "-u", "origin", BRANCH)
            stale = _git(repo, "rev-parse", BRANCH).stdout.strip()
            _checkout_main(repo)
            log = root / "gh.log"
            bindir = _gh_bin(root)
            with _env(
                PATH=f"{bindir}{os.pathsep}{os.environ.get('PATH', '')}",
                GH_LOG=str(log),
                GH_PR_LIST=json.dumps([{"number": 41}]),
            ):
                code, action = generate_phase(repo, DAY, True, loader=lambda _on: {})
                self.assertEqual((code, action), (0, "reuse"))
                self.assertEqual(publish(repo, DAY, action), "reuse")
            self.assertNotEqual(_git(repo, "rev-parse", BRANCH).stdout.strip(), stale)
            self.assertTrue(verify_day(repo / "Sooners" / f"sooners-content-{DAY}").ok)
            calls = _calls(log)
            self.assertEqual([args for args in calls if args[:2] == ["pr", "create"]], [])
            self.assertIn(["pr", "merge", "41", "--squash"], calls)
            pushed = _git(repo, "ls-remote", "origin", f"refs/heads/{BRANCH}")
            self.assertIn(_git(repo, "rev-parse", BRANCH).stdout.strip(), pushed.stdout)

    def test_valid_branch_without_a_pr_is_adopted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = _init_repo(root)
            _write_day(repo)
            _git(repo, "checkout", "-B", BRANCH)
            _git(repo, "add", "Sooners")
            _git(repo, "commit", "-m", "valid day already on the branch")
            _git(repo, "push", "-u", "origin", BRANCH)
            tip = _git(repo, "rev-parse", BRANCH).stdout.strip()
            _checkout_main(repo)
            log = root / "gh.log"
            bindir = _gh_bin(root)

            def boom(_on):
                raise AssertionError("a valid branch must not be regenerated")

            with _env(
                PATH=f"{bindir}{os.pathsep}{os.environ.get('PATH', '')}",
                GH_LOG=str(log),
                GH_PR_LIST="[]",
            ):
                code, action = generate_phase(repo, DAY, True, loader=boom)
                self.assertEqual((code, action), (0, "adopt"))
                self.assertEqual(publish(repo, DAY, action), "adopt")
            self.assertEqual(_git(repo, "rev-parse", BRANCH).stdout.strip(), tip)
            calls = _calls(log)
            self.assertEqual(len([args for args in calls if args[:2] == ["pr", "create"]]), 1)
            self.assertIn(["pr", "merge", "99", "--squash"], calls)


if __name__ == "__main__":
    unittest.main()
