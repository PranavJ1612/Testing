from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")  # necessary to switch to frame in order to work with frame

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()    # .default_content() is used to switch back to default driver scope
print(driver.find_element(By.TAG_NAME, "h3").text)
