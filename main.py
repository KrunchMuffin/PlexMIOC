import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

import scan
from config import load_config

# create logger with 'plexmoic'
logger = logging.getLogger('plexmoic')
logger.setLevel(logging.DEBUG)
# create file handler which logs debug messages
rfh = RotatingFileHandler(
    "/logs/plexmoic.log", mode="w", maxBytes=100000, backupCount=5
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


def check_config():
    logger.debug("Starting check config")
    return Path("config/config.ini").exists()


if __name__ == '__main__':
    if check_config():
        cfg = load_config()
        if cfg.getboolean('DEFAULT', 'enabled'):
            scan.start_scan()
        else:
            print("Script is not enabled. Exiting...")
    else:
        print("There is no config file located at config/config.ini. Exiting...")
