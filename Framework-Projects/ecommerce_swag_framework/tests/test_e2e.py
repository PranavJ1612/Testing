from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        global selectedProduct
        log = self.getLogger()

        loginPage = LoginPage(self.driver)

        loginPage.getUsername().send_keys('standard_user')
        loginPage.getPassword().send_keys('secret_sauce')
        productPage = loginPage.clickLoginBtn()

        log.info("Logged in successfully")

        self.selectOptionByText(productPage.getFilter(), 'hilo')

        products = productPage.getCardTitles()
        for product in products:
            productName = product.text
            if productName == 'Sauce Labs Backpack':
                log.info(f"Name of product in cart:{productName}")
                selectedProduct = productName
                productPage.getAddButton().click()
                break

        cartPage = productPage.clickCartButton()

        log.info("Moving to checkout")

        if selectedProduct == cartPage.getItemName():
            log.info("Correct product in cart")

        checkoutPage = cartPage.checkoutItems()

        checkoutPage.getFirstName().send_keys('Test')
        checkoutPage.getLastName().send_keys('Demo')
        checkoutPage.getZipCode().send_keys('4110433')
        checkoutPage2 = checkoutPage.clickContinueBtn()

        log.info("Checking Out")
        confirmPage = checkoutPage2.finishCheckout()

        successMessage = confirmPage.getSuccessMsg()
        log.info("Got success message")

        assert "Thank you for your order!" in successMessage
        log.info("E2E test passed for shopping a product")

