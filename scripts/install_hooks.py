"""Install git hooks for this repository."""

import os
import shutil
import stat
import subprocess
from pathlib import Path

scripts_dir = Path(__file__).parent
hooks_src = scripts_dir / "hooks" / "pre-commit"

# Resolve the real git directory (handles worktrees where .git is a file, not a dir)
git_dir = subprocess.check_output(
    ["git", "rev-parse", "--git-common-dir"],
    cwd=scripts_dir.parent,
    text=True,
).strip()

hooks_dst_dir = Path(git_dir) / "hooks"
hooks_dst = hooks_dst_dir / "pre-commit"

hooks_dst_dir.mkdir(parents=True, exist_ok=True)
shutil.copy(hooks_src, hooks_dst)
os.chmod(
    hooks_dst,
    stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH,
)

print("Installed pre-commit hook")
