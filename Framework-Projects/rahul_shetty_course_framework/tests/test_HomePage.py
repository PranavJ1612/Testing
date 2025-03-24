import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("The email is is "+getData["emailId"])
        homePage.getEmail().send_keys(getData['emailId'])
        homePage.getPassword().send_keys(getData['password'])
        homePage.getName().send_keys(getData['fullName'])

        homePage.getCheckbox().click()
        # Static Dropdown (using SELECT)
        self.selectOptionByText(homePage.getGender(), getData['gender'])

        homePage.getSubmitBtn().click()
        msg = homePage.getSuccessMessage().text

        assert "Success" in msg
        self.driver.refresh()

    # @pytest.fixture(params=[("pranav@gmail.com","12345","Pranav Jagdale","Male"),("maitra@gmail.com","54321",
    # "Maitra J", "Female")])
    @pytest.fixture(params=HomePageData.getTestData("Test2"))
    def getData(self, request):
        return request.param
