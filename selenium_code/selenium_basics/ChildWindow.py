from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()


windowsOpened = driver.window_handles  # .window_handles creates a list of open tabs with index.

driver.switch_to.window(windowsOpened[1])  # switching to window indexed 1.i.e. child window

print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()     # this will close your current opened tab.

driver.switch_to.window(windowsOpened[0])  # switching back to tab with indexed 0 .i.e parent
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
