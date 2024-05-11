from pytemplate.utils.logger import logger

def test_demo():
    logger.success("success message")
    logger.trace("trace message")
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")