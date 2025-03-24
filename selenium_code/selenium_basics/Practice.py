from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
mailId = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
driver.close()

driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys(mailId)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CLASS_NAME, "alert-danger").text)

