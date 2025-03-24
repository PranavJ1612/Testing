from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)


driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#Xpath, CSSSelector for child elements
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("123456")

# Xpath with text => //tagname[text()='xcndnc']
driver.find_element(By.XPATH, '//button[text()="Save New Password"]').click()