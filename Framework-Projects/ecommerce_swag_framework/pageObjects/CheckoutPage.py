from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage2 import CheckoutPage2


class CheckoutPage:
    firstName = (By.NAME, "firstName")
    lastName = (By.XPATH, "//input[@id='last-name']")
    zipCode = (By.ID, "postal-code")
    continueBtn = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def getFirstName(self):
        return self.driver.find_element(*CheckoutPage.firstName)

    def getLastName(self):
        return self.driver.find_element(*CheckoutPage.lastName)

    def getZipCode(self):
        return self.driver.find_element(*CheckoutPage.zipCode)

    def clickContinueBtn(self):
        self.driver.find_element(*CheckoutPage.continueBtn).click()
        checkoutPage2 = CheckoutPage2(self.driver)
        return checkoutPage2
