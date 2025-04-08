"""Interface for ``python -m tiny_little_service``."""

import typer

from tiny_little_service.main import start

from . import __version__

cli_app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@cli_app.callback()
def common(
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass


@cli_app.command()
def serve():
    start()
