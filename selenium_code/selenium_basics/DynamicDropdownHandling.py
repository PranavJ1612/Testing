import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR,  "li[class='ui-menu-item'] a")
len(countries)

for country in countries:
    if country.text == "India":
        country.click()
        break

# for selecting dynamic values we need to use get_attribute("value")
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
