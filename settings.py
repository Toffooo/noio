import json
import logging
import logging.config

from decouple import config


def setup_logging(path: str = "logging.json") -> None:
    with open(path, "rt") as f:
        _config = json.load(f)
    logging.config.dictConfig(_config)


setup_logging()
DB_LINK = config("DB_LINK", cast=str)
BOT_API_TOKEN = config("BOT_API_TOKEN", cast=str)
