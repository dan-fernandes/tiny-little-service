from tiny_little_service.cli import cli_app
from tiny_little_service.log import do_default_logging_setup


def main():
    do_default_logging_setup()
    cli_app()


if __name__ == "__main__":
    main()
