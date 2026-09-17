#!/usr/bin/env python3
"""Publish chapters 1-10 to GitHub branch `published`. Allowlist only."""

from __future__ import annotations

import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / ".publish-github"
BRANCH = "published"
NEVER = ("100_Notes.md", "_writing_style.md", "COPYRIGHT-REGISTRATION.md")


def die(msg: str) -> None:
    print(f"sync-github: {msg}", file=sys.stderr)
    sys.exit(1)


def load_book():
    spec = importlib.util.spec_from_file_location("build_pdf", ROOT / "build_pdf.py")
    if spec is None or spec.loader is None:
        die("cannot load build_pdf.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_version_md() -> str:
    text = (ROOT / "VERSION.md").read_text(encoding="utf-8")
    match = re.search(r"^\*\*Current version:\s*([0-9.]+)\*\*", text, re.M)
    if not match:
        die("VERSION.md is missing '**Current version: X**'")
    return match.group(1)


def read_readme_version() -> str:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    match = re.search(r"\*\*Version\s+([0-9.]+)\*\*", text)
    if not match:
        die("README.md is missing '**Version X**'")
    return match.group(1)


def git(args: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=check,
        capture_output=True,
        text=True,
    )


def remote_url() -> str:
    result = git(["remote", "get-url", "origin"], ROOT)
    return result.stdout.strip()


def sources_newer_than(pdf: Path, sources: list[Path]) -> bool:
    if not pdf.exists():
        return True
    pdf_mtime = pdf.stat().st_mtime
    return any(src.exists() and src.stat().st_mtime > pdf_mtime for src in sources)


def rebuild_pdf() -> None:
    print("sync-github: rebuilding PDF")
    subprocess.run(
        [sys.executable, str(ROOT / "build_pdf.py")],
        cwd=ROOT,
        check=True,
    )


def allowlist(mod) -> list[Path]:
    files = [ROOT / name for name, _ in mod.CHAPTERS]
    files.extend(
        [
            ROOT / "VERSION.md",
            ROOT / "LICENSE",
            ROOT / "README.md",
            ROOT / "build_pdf.py",
            ROOT / f"Backyard-{mod.VERSION}.pdf",
        ]
    )
    files.extend(sorted((ROOT / "diagrams").glob("*.svg")))
    missing = [p for p in files if not p.exists()]
    if missing:
        die("missing: " + ", ".join(str(p.relative_to(ROOT)) for p in missing))
    for name in NEVER:
        if (ROOT / name) in files:
            die(f"refusing to publish {name}")
    return files


def copy_tree(files: list[Path], version: str) -> None:
    if STAGING.exists():
        for child in STAGING.iterdir():
            if child.name == ".git":
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    else:
        STAGING.mkdir()

    for src in files:
        rel = src.relative_to(ROOT)
        dest = STAGING / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    for leftover in STAGING.glob("Backyard-*.pdf"):
        if leftover.name != f"Backyard-{version}.pdf":
            leftover.unlink()


def ensure_staging_repo(url: str) -> None:
    git_dir = STAGING / ".git"
    if git_dir.exists():
        git(["remote", "set-url", "origin", url], STAGING)
        git(["fetch", "origin", BRANCH], STAGING, check=False)
        has_branch = git(
            ["rev-parse", "--verify", BRANCH], STAGING, check=False
        ).returncode == 0
        has_remote = git(
            ["rev-parse", "--verify", f"origin/{BRANCH}"], STAGING, check=False
        ).returncode == 0
        if has_remote:
            git(["checkout", "-B", BRANCH, f"origin/{BRANCH}"], STAGING)
        elif not has_branch:
            git(["checkout", "--orphan", BRANCH], STAGING)
        return

    clone = subprocess.run(
        ["git", "clone", "--branch", BRANCH, "--single-branch", url, str(STAGING)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if clone.returncode == 0:
        return
    STAGING.mkdir(exist_ok=True)
    git(["init", "-b", BRANCH], STAGING)
    git(["remote", "add", "origin", url], STAGING)


def commit_and_push(version: str) -> None:
    git(["add", "-A"], STAGING)
    dirty = git(["status", "--porcelain"], STAGING).stdout.strip()
    if not dirty:
        print("sync-github: GitHub already matches")
        return
    git(
        [
            "commit",
            "-m",
            f"Sync Backyard Generating Station version {version}",
        ],
        STAGING,
    )
    git(["push", "-u", "origin", BRANCH], STAGING)
    print(f"sync-github: pushed version {version} to origin/{BRANCH}")


def main() -> None:
    for name in NEVER:
        print(f"sync-github: excluding {name}")

    mod = load_book()
    version = mod.VERSION
    vmd = read_version_md()
    vreadme = read_readme_version()
    if len({version, vmd, vreadme}) != 1:
        die(
            "version mismatch: "
            f"build_pdf.py={version} VERSION.md={vmd} README.md={vreadme}"
        )

    files = allowlist(mod)
    chapter_paths = [ROOT / name for name, _ in mod.CHAPTERS]
    pdf = ROOT / f"Backyard-{version}.pdf"
    sources = [
        ROOT / "build_pdf.py",
        *chapter_paths,
        *sorted((ROOT / "diagrams").glob("*.svg")),
    ]
    if sources_newer_than(pdf, sources):
        rebuild_pdf()
        files = allowlist(mod)

    url = remote_url()
    ensure_staging_repo(url)
    copy_tree(files, version)
    commit_and_push(version)


if __name__ == "__main__":
    main()
