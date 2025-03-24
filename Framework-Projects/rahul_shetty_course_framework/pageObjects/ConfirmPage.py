from selenium.webdriver.common.by import By


class ConfirmPage:
    indText = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def getIndiaText(self):
        return self.driver.find_element(*ConfirmPage.indText)

    def getCheckboxClicked(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def submitButton(self):
        return self.driver.find_element(*ConfirmPage.submit)