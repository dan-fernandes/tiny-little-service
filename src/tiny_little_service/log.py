import logging


def do_default_logging_setup() -> None:
    # logger = logging.getLogger("__main__")
    logger = logging.getLogger("tiny_little_service")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("FOOOO {asctime}", style="{")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
