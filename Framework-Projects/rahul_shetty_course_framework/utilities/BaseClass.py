import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # this helps in prinitng correct file name in log
        logger = logging.getLogger(loggerName)

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

        logger.setLevel(logging.DEBUG)  # So this will skip debug log level!
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
