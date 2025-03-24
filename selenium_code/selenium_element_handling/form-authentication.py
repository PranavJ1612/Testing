import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

baseUrl = 'https://the-internet.herokuapp.com'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get(f"{baseUrl}/login")
action = ActionChains(driver)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys('tomsmith')
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('SuperSecretPassword!')
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_btn.click()

time.sleep(2)
success_text = driver.find_element(By.ID, 'flash').text
print(success_text)
assert "You logged into a secure area!" in success_text

time.sleep(2)
logout_btn = driver.find_element(By.LINK_TEXT, "Logout")
logout_btn.click()

time.sleep(2)
success_text2 = driver.find_element(By.ID, 'flash').text
print(success_text2)
assert "You logged out of the secure area!" in success_text2

time.sleep(2)
print("Authentication test passed")
driver.close()
