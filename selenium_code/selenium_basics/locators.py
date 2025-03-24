from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# LOCATORS
# ID, name, Xpath, Classname,CSSSelector,  linkText

driver.find_element(By.NAME, "email").send_keys("pranav@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")

# CSS_Selector -> tagname[attribute='value'], #id_value, .class_name
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Pranav Jagdale")

driver.find_element(By.ID, "exampleCheck1").click()

# Xpath-> //tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Static Dropdown (using SELECT)
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
# dropdown.select_by_value()

# CLASSNAME
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)
assert "Success" in msg

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
