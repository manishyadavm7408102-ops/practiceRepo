"""
      logging in Python

1) Logging vs Printing
2) Logging levels
3) Logging to files
4) Logging exceptions


"""
from loguru import logger

logger.add("file_{time}.log",level="TRACE",rotation="100 MB")

logger.debug("This is debug")
logger.info("This is an info")
logger.success("This is success")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")

@logger.catch
def dev_by_zero(num):
    return 100/num

dev_by_zero(100)
dev_by_zero(2)

