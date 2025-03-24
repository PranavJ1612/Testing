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

driver.get(f"{baseUrl}/disappearing_elements")
home_ele = driver.find_element(By.LINK_TEXT, "About")
home_ele.click()


time.sleep(2)
print("Task Completed!")

driver.close()
