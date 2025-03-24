from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage2:
    finishBtn = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def finishCheckout(self):
        self.driver.find_element(*CheckoutPage2.finishBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
