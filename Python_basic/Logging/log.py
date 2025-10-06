import logging
import os
from logging import Logger

# Ensure log file is created in the same directory as this module
LOG_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(LOG_DIR, 'app.log')

# Configure root logger to write to file 'app.log' and also show ERRORs on console
logging.basicConfig(
    filename=LOG_FILE,
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Provide a convenience function to get named loggers from other modules
def get_logger(name: str) -> Logger:
    return logging.getLogger(name)