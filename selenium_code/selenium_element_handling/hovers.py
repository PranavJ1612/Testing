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

driver.get(f"{baseUrl}/hovers")
action = ActionChains(driver)

hover_element = driver.find_element(By.XPATH, "//div[@class='example']/div[2]")
action.move_to_element(hover_element).perform()           # This will hover to that element.

hover_user_name = hover_element.find_element(By.XPATH, 'div/h5').text
assert 'user2' in hover_user_name

hover_element.find_element(By.XPATH, 'div/a').click()

print(f"Hovering '{hover_user_name}' test passed")
driver.close()
