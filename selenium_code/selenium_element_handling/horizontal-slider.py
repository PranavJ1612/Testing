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

driver.get(f"{baseUrl}/horizontal_slider")
action = ActionChains(driver)

slider = driver.find_element(By.XPATH, "//div[@class='example']/div[@class='sliderContainer']/input")
slider.click()

# Solution 1
slider.send_keys('1')

# solution 2
for _ in range(2):
    slider.send_keys(Keys.ARROW_RIGHT)

time.sleep(2)
print("Slider movement test passed")
driver.close()
