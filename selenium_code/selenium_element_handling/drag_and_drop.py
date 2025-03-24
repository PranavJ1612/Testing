import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

baseUrl = 'https://the-internet.herokuapp.com'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get(f"{baseUrl}/drag_and_drop")
action = ActionChains(driver)

source_element = driver.find_element(By.ID, "column-a")
target_element = driver.find_element(By.ID, "column-b")

action.drag_and_drop(source_element, target_element).perform()

time.sleep(2)
print("Drag-Drop  Completed!")

driver.close()
