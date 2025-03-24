import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

driver.implicitly_wait(2)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
product_list = []


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for item in results:
    product_list.append(item.find_element(By.XPATH, "h4").text)
    item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(totalAmount)
assert sum == totalAmount
########################

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()


# NOTE -> Explicit Wait of 10sec only for element with class = "promoInfo".
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,  ".promoInfo")))

print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)

##################################
discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(discountAmount)
assert discountAmount < totalAmount

