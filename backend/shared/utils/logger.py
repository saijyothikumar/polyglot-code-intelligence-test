import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("shared-utils")


def log_info(message: str, **kwargs):
    logger.info("%s | %s", message, kwargs)


def log_debug(message: str):
    # added for completeness; may stay unused
    logger.debug(message)
