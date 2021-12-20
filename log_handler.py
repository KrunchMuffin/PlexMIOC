# create logger with 'plexmioc'
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('plexmioc')
logger.setLevel(logging.DEBUG)
# create file handler which logs debug messages
rfh = RotatingFileHandler(
    "logs/plexmioc.log", mode="w", maxBytes=100000, backupCount=5
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
