import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # this helps in printing correct file name in log
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logFile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)  # So this will skip debug log level!
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, value):
        dropdown = Select(locator)
        dropdown.select_by_value(value)
