#!/usr/bin/env python3
"""Publish chapters 1-10 to GitHub branch `published`. Allowlist only."""

from __future__ import annotations

import importlib.util
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / ".publish-github"
BRANCH = "published"
NEVER = ("100_Notes.md", "_writing_style.md", "COPYRIGHT-REGISTRATION.md")
GITHUB_NOREPLY = "121400468+MichaelCyger@users.noreply.github.com"


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
    env = os.environ.copy()
    if cwd == STAGING:
        env["GIT_AUTHOR_NAME"] = "Michael Cyger"
        env["GIT_AUTHOR_EMAIL"] = GITHUB_NOREPLY
        env["GIT_COMMITTER_NAME"] = "Michael Cyger"
        env["GIT_COMMITTER_EMAIL"] = GITHUB_NOREPLY
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=check,
        capture_output=True,
        text=True,
        env=env,
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


def chapter_nav(chapters: list[tuple[str, str]], index: int, version: str) -> tuple[str, str]:
    """GitHub-only prev/next and jump list. Not written into the PDF sources."""
    n = len(chapters)
    pdf = f"Backyard-{version}.pdf"
    start = "[Start](README.md)"
    pdf_link = f"[Whole book as a PDF]({pdf})"
    bits = []
    for j, (fn, title) in enumerate(chapters):
        if j == index:
            bits.append(f"**{title}**")
        else:
            bits.append(f"[{title}]({fn})")
    toc = "**Chapters:** " + " · ".join(bits)

    prev = chapters[index - 1] if index > 0 else None
    nxt = chapters[index + 1] if index + 1 < n else None
    bar = []
    if prev:
        bar.append(f"← [Previous: {prev[1]}]({prev[0]})")
    bar.append(start)
    bar.append(pdf_link)
    if nxt:
        next_big = f"**Next chapter:** [{nxt[1]}]({nxt[0]})"
        bar.append(f"**Next:** [{nxt[1]}]({nxt[0]}) →")
    else:
        next_big = f"**That was the last chapter.** {start} · {pdf_link}"
        bar.append("**End of the book.**")
    trail = " · ".join(bar)

    top = f"{toc}\n\n{trail}\n\n---\n"
    bottom = (
        "\n---\n\n"
        f"You have finished chapter {index + 1} of {n}.\n\n"
        f"{next_big}\n\n"
        f"{trail}\n\n"
        f"{toc}\n"
    )
    return top, bottom


def inject_github_nav(chapters: list[tuple[str, str]], version: str) -> None:
    for i, (filename, _title) in enumerate(chapters):
        path = STAGING / filename
        text = path.read_text(encoding="utf-8")
        top, bottom = chapter_nav(chapters, i, version)
        lines = text.splitlines()
        if lines and lines[0].startswith("# "):
            rest = "\n".join(lines[1:]).lstrip("\n")
            out = f"{lines[0]}\n\n{top}\n{rest}\n{bottom}\n"
        else:
            out = f"{top}\n{text.rstrip()}\n{bottom}\n"
        path.write_text(out, encoding="utf-8")


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


def replace_github_history(url: str, version: str) -> None:
    """Orphan the published branch so old blobs (including email) are not reachable."""
    git_dir = STAGING / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)
    git(["init", "-b", BRANCH], STAGING)
    git(["remote", "add", "origin", url], STAGING)
    git(["add", "-A"], STAGING)
    git(
        [
            "commit",
            "-m",
            f"Backyard Generating Station version {version}",
        ],
        STAGING,
    )
    git(["push", "--force", "-u", "origin", BRANCH], STAGING)
    print(f"sync-github: replaced origin/{BRANCH} history with version {version}")


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
    inject_github_nav(mod.CHAPTERS, version)
    if "--replace-history" in sys.argv:
        replace_github_history(url, version)
    else:
        commit_and_push(version)


if __name__ == "__main__":
    main()
