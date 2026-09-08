#!/usr/bin/env python3
"""Kilo post-tool-call hook: переводит docstrings и комментариев в изменённых файлах.

Используется в .kilo/hooks.toml и ~/.config/kilo/hooks.toml.
Проверяет git diff на изменённые .py и .md/.rst файлы, переводит их через
scripts/translate_docs.py.
"""

import json
import os
import subprocess
import sys
from pathlib import Path


def main():
    try:
        input_data = json.load(sys.stdin)
        cwd = input_data.get("cwd", os.getcwd())
    except Exception:
        cwd = os.getcwd()

    os.chdir(cwd)

    result = subprocess.run(
        ["git", "diff", "--name-only", "--", "*.py", "*.md", "*.rst"],
        capture_output=True,
        text=True,
    )
    changed = [f for f in result.stdout.strip().split('\n') if f]

    result_untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "--", "*.py", "*.md", "*.rst"],
        capture_output=True,
        text=True,
    )
    untracked = [f for f in result_untracked.stdout.strip().split('\n') if f]

    all_files = changed + untracked
    if not all_files:
        return

    project_root = Path(cwd)
    translate_script = project_root / "scripts" / "translate_docs.py"
    if not translate_script.exists():
        print("[translate-hook] scripts/translate_docs.py не найден, пропуск")
        return

    for filepath in all_files:
        full_path = project_root / filepath
        if full_path.exists():
            print(f"[translate-hook] Перевожу: {filepath}")
            subprocess.run(
                [sys.executable, str(translate_script), str(full_path)],
                cwd=str(project_root),
            )


if __name__ == '__main__':
    main()
