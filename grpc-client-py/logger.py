import logging

# PYTHON LOGGING LEVELS
# NOTSET    = 0
# DEBUG     = 10
# INFO      = 20
# WARN      = 30
# ERROR     = 40
# CRITICAL  = 50

logging.basicConfig(
    # filename='app.log',
    level=logging.DEBUG,
    # format='%(asctime)s | %(levelname)s | %(module)s | %(message)s',
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger()
