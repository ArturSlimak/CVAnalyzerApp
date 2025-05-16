import logging
import os


def setup_logger(name: str = "analyzer"):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    env = os.getenv('ENVIRONMENT', 'development').lower()

    level = logging.DEBUG if env == "development" else logging.INFO

    logger.setLevel(level)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(name)s: %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
