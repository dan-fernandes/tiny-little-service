from typer.testing import CliRunner

from tiny_little_service import __version__
from tiny_little_service.cli import cli_app

runner = CliRunner()


def test_version():
    result = runner.invoke(cli_app, ["version"])
    assert result.exit_code == 0
    assert result.stdout.strip() == __version__
