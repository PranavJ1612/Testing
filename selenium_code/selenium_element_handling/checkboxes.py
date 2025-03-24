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

driver.get(f"{baseUrl}/checkboxes")

for i in range(2):
    checkbox = driver.find_element(By.XPATH,f"//form[@id='checkboxes']/input[{i+1}]")
    if checkbox.is_selected():
        print(f"Checkbox {i+1} is selected")
    else:
        print(f"Checkbox {i+1} is not selected")
    checkbox.click()

time.sleep(2)
print("Task Completed!")

driver.close()
