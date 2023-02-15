import inspect
import logging

import pytest

@pytest.mark.usefixtures("setup")
class Baseclass:
   def getlogger(self):


        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s:  %(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        logger.debug("debug statement executed")
        logger.info("information statement")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
        return logger
        