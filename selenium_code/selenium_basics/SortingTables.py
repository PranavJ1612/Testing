from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
browserSortedList = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers/")

# click-on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedList
veggieElementList = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieElementList:
    browserSortedList.append(ele.text)

originalSortedList = browserSortedList.copy()

# Sort using python method this BrowserSortedList -> newSortedList
browserSortedList.sort()

# assert BrowserSortedList == newSortedList
assert browserSortedList == originalSortedList
