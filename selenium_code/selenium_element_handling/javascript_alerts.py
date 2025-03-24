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

driver.get(f"{baseUrl}/javascript_alerts")

# For Alert
alert_btn = driver.find_element(By.XPATH, "//div[@class='example']/ul/li[1]/button")
alert_btn.click()
alert = driver.switch_to.alert
time.sleep(1)
alert.accept()

result1 = driver.find_element(By.ID, 'result').text
assert 'alert' in result1
print("Alert test Passed")


# For Confirm
confirm_btn = driver.find_element(By.XPATH, "//div[@class='example']/ul/li[2]/button")
confirm_btn.click()
confirm = driver.switch_to.alert
time.sleep(1)
confirm.accept()

result2 = driver.find_element(By.ID, 'result').text
assert 'Ok' in result2
print("Confirm test Passed")


# For Prompt
prompt_btn = driver.find_element(By.XPATH, "//div[@class='example']/ul/li[3]/button")
prompt_btn.click()
prompt = driver.switch_to.alert
time.sleep(1)
prompt.send_keys("Pranav Jagdale")
prompt.accept()

result3 = driver.find_element(By.ID, 'result').text
# print(result3)
assert 'Pranav' in result3
print("Prompt test Passed")


time.sleep(2)
driver.close()
