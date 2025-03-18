import logging


class ServiceFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.service_name = "tiny_little_service"
        return super().format(record)


def do_default_logging_setup() -> None:
    logger = logging.getLogger("tiny_little_service")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(ServiceFormatter())
    logger.addHandler(handler)
