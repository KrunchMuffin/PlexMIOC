import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

import config
import scan
from config import load_config

# create logger with 'plexmoic'
logger = logging.getLogger('plexmoic')
logger.setLevel(logging.DEBUG)
# create file handler which logs debug messages
rfh = RotatingFileHandler(
    "logs/plexmoic.log", mode="w", maxBytes=100000, backupCount=5
)
rfh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
rfh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(rfh)
logger.addHandler(ch)


def check_config() -> bool:
    logger.info("Starting check config")
    ok = Path("config/config.ini").exists()
    if ok:
        logger.debug("Config file exists.")
        cfg = load_config()
        has_default = cfg.has_section('MAIN')
        has_plex = cfg.has_section('PLEX')
        has_options = cfg.has_section('OPTIONS')
        has_logos = cfg.has_section('LOGOS')
        if not has_default or not has_plex or not has_options or not has_logos:
            logger.debug(f"MAIN ${has_default} | PLEX ${has_plex} | OPTIONS ${has_options} | LOGOS ${has_logos}")
            logger.info(
                "There is config file issue. One or more of the following sections are missing: MAIN, PLEX, "
                "OPTIONS, LOGOS")
            ok = False
    else:
        logger.info(
            "Config file does not exist. Creating config. Please open config/config.ini and adjust accordingly.")
        ok = config.create_config()
    return ok


if __name__ == '__main__':
    logger.debug("##################### STARTING NEW SESSION ##############################")
    logger.info("Starting up...")
    if check_config():
        cfg = load_config()
        if cfg.getboolean('MAIN', 'enabled'):
            logger.debug("Script enabled")
            has_movies = cfg.getboolean('MAIN', 'enable_movies')
            if has_movies:
                logger.info("Movies enabled")
            has_tv = cfg.getboolean('MAIN', 'enable_tvshows')
            if has_tv:
                logger.info("TV Shows enabled")
            scan.start_scan(has_movies, has_tv)
        else:
            logger.info("Script is not enabled. Exiting...")
    else:
        logger.info("There is no config file located at config/config.ini and I was not able to create one. Exiting...")
