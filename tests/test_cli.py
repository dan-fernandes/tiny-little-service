import subprocess
import sys

from tiny_little_service import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "tiny_little_service", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
