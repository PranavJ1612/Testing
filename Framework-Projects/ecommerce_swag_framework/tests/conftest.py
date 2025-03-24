import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None


@pytest.fixture(scope='class')
def setup(request):
    global driver
    chromeOptions = Options()
    chromeOptions.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chromeOptions)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield
    driver.close()
