import logging


def getLogger():
    """Sets up my logging system to terminal."""
    log = logging.getLogger("mylogger")
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s - %(funcName)s - %(message)s"
    )
    ch.setFormatter(formatter)
    log.addHandler(ch)
    return log


log = getLogger()
