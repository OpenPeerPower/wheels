"""Some utils for builder."""
import os
from pathlib import Path
import subprocess
import sys
from typing import Dict, Optional


def alpine_version() -> str:
    """Return alpine version for index server."""
    version = Path("/etc/alpine-release").read_text().split(".")

    return f"alpine-{version[0]}.{version[1]}"


def build_arch() -> str:
    """Return build arch for wheels."""
    return os.environ["ARCH"]


def run_command(
    cmd: str, env: Optional[Dict[str, str]] = None, timeout: Optional[int] = None
) -> None:
    """Implement subprocess.run but handle timeout different."""
    subprocess.run(
        cmd,
        shell=True,
        check=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
        env=env,
        timeout=timeout,
    )
