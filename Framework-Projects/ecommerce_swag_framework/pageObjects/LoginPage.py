from selenium.webdriver.common.by import By
from pageObjects.ProductPage import ProductPage


class LoginPage:
    username = (By.ID, 'user-name')
    password = (By.ID, 'password')
    loginBtn = (By.CSS_SELECTOR, '#login-button')

    def __init__(self, driver):
        self.driver = driver

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickLoginBtn(self):
        self.driver.find_element(*LoginPage.loginBtn).click()
        productPage = ProductPage(self.driver)
        return productPage
