from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    name = (By.CSS_SELECTOR, "input[name='name']")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMsg = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMsg)