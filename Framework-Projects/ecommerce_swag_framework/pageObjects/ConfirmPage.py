from selenium.webdriver.common.by import By


class ConfirmPage:
    successMsg = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.successMsg).text
