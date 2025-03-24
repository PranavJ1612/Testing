from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class CartPage:
    itemName = (By.CSS_SELECTOR, "div[class='inventory_item_name']")
    checkout = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        self.driver = driver

    def getItemName(self):
        return self.driver.find_element(*CartPage.itemName).text

    def checkoutItems(self):
        self.driver.find_element(*CartPage.checkout).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
