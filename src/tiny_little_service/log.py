import logging


class ServiceFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return super().format(record)


class ListTagger(logging.Filter):
    def filter(self, record: logging.LogRecord):
        record.l = getattr(record, "l", [1])
        return True


def do_default_logging_setup() -> None:
    logger = logging.getLogger("tiny_little_service")
    logger.setLevel(logging.DEBUG)

    logger.addFilter(ListTagger())

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.addFilter(ListTagger())

    logger.addHandler(handler)
