from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, ".//button")  # Use relative XPath for each card
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self, product):
        # Find the footer within the given product element
        return product.find_element(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
