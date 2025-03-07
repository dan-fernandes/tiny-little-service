"""Interface for ``python -m tiny_little_service``."""

from collections.abc import Sequence

import typer

from . import __version__

__all__ = ["main"]

cli_app = typer.Typer()


def main(args: Sequence[str] | None = None) -> None:
    cli_app()


@cli_app.command()
def version():
    print(__version__)
