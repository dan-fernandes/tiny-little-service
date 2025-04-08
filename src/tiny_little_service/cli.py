"""Interface for ``python -m tiny_little_service``."""

from collections.abc import Sequence

import typer

from tiny_little_service.log import do_default_logging_setup
from tiny_little_service.main import start

from . import __version__

__all__ = ["main"]

cli_app = typer.Typer()


def main(args: Sequence[str] | None = None) -> None:
    do_default_logging_setup()
    cli_app()


@cli_app.command()
def version():
    print(__version__)


@cli_app.command()
def serve():
    start()
