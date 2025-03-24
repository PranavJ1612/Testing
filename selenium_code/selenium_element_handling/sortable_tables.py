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

driver.get(f"{baseUrl}/tables")

# Table 1 sort by due handling
table_1 = driver.find_element(By.XPATH, "//table[@id='table1']")
Due_ele = table_1.find_element(By.XPATH, "//span[text()='Due']")
time.sleep(1)
Due_ele.click()
print("Table 1 Sorting Completed by due element!")

time.sleep(1)

# Table 2 sort by first name
table_2 = driver.find_element(By.CSS_SELECTOR, "#table2")
lastName_ele = table_2.find_element(By.XPATH, "//span[@class='last-name']")
time.sleep(1)
lastName_ele.click()
print("Table 2 Sorting Completed by last name element!")

time.sleep(2)
driver.close()
