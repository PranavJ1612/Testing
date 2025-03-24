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

driver.get(f"{baseUrl}/context_menu")
action = ActionChains(driver)

div_block = driver.find_element(By.ID, "hot-spot")

action.context_click(div_block).perform()

alert = driver.switch_to.alert
alert.accept()

time.sleep(2)
print("Task Completed!")

driver.close()
