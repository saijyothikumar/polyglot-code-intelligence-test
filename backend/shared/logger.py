import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("polyglot-backend")

# Unused helper left here to bait dead-code detection

def log_structured(event: str, **fields):
    logger.info("%s | %s", event, fields)
