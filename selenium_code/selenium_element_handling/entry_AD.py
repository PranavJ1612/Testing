# This is for closing modal

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

driver.get(f"{baseUrl}/entry_ad")

modal_window = driver.find_element(By.ID, "modal").find_element(By.CLASS_NAME,"modal-footer")
modal_close = modal_window.find_element(By.TAG_NAME, "p")
time.sleep(4)
modal_close.click()

time.sleep(1)
print("Modal Close Completed!")

driver.close()
