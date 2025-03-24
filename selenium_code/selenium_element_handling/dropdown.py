import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

baseUrl = 'https://the-internet.herokuapp.com'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get(f"{baseUrl}/dropdown")

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_value("2")

time.sleep(2)
print("Dropdown selection Completed!")

driver.close()
