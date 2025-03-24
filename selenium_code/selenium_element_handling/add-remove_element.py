import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

baseUrl = 'https://the-internet.herokuapp.com'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(3)


driver.get(f"{baseUrl}/add_remove_elements/")

# Clicking Add button
driver.find_element(By.XPATH, "//div[@class='example']/button").click()
driver.find_element(By.XPATH, "//div[@class='example']/button").click()
driver.find_element(By.XPATH, "//div[@class='example']/button").click()

# Clicking Remove button
driver.find_element(By.CSS_SELECTOR, "#elements button:nth-child(3)").click()
driver.find_element(By.CSS_SELECTOR, "#elements button:nth-child(1)").click()

time.sleep(2)
print("Task Completed!")

driver.close()
