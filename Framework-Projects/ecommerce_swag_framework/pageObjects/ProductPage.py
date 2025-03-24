from selenium.webdriver.common.by import By

from pageObjects.CartPage import CartPage


class ProductPage:
    dropdown_locator = (By.XPATH, "//select[@class='product_sort_container']")
    cardTitle = (By.CLASS_NAME, "inventory_item_name")
    cardAddButton = (By.ID, "add-to-cart-sauce-labs-backpack")
    cartButton = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*ProductPage.cardTitle)

    def getAddButton(self):
        return self.driver.find_element(*ProductPage.cardAddButton)

    def getFilter(self):
        return self.driver.find_element(*ProductPage.dropdown_locator)

    def clickCartButton(self):
        self.driver.find_element(*ProductPage.cartButton).click()
        cartPage = CartPage(self.driver)
        return cartPage
