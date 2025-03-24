import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

name = "Pranav"

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# switch_to.alert method allows ur driver to handle pop-ups
alert = driver.switch_to.alert
alertText = alert.text
# print(alert.text)
assert name in alertText
time.sleep(2)
alert.accept()
# alert.dismiss()   ->  this can be used for confirm box!

