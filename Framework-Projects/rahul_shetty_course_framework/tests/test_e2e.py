from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()

        log.info("getting all the product card titles")
        products = checkoutPage.getCardTitles()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                # Call getCardFooter() with the specific product element
                checkoutPage.getCardFooter(product).click()
                break

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage = checkoutPage.checkOutItems()

        log.info("Entering the country name as ind")
        self.driver.find_element(By.ID, "country").send_keys('ind')
        self.verifyLinkPresence("India")

        confirmPage.getIndiaText().click()
        confirmPage.getCheckboxClicked().click()
        confirmPage.submitButton().click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is "+successText)

        assert "Success! Thank you!" in successText
        self.driver.close()
