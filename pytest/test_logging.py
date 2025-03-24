import logging

# This function on running will create a log file named 'logFile.log

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    # This creates the file for logs & then we pass this fileHandler obj to addHandler().
    fileHandler = logging.FileHandler('logFile.log')

    # This is format of logs.
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    # We need to pass the info to this method such as what format we want to log & for what file.
    logger.addHandler(fileHandler)


    # NOTE-> Following log order is the level of logs and if u want a specific log for eg: error
    # then u need to set level to error so that error log and it's higher logs will be displayed
    # and rest will be ignored.

    logger.setLevel(logging.INFO)   # So this will skip debug log level!
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")

# When u have to use this logging for multiple test cases then simply create a new file in that a
# BaseClass and move this method inside that class and,
# you are ready to go for multiple cases now by reusing the code.
