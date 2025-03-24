from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Username and password for authentication
username = "admin"
password = "admin"

# Construct URL with credentials
auth_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

# Setup WebDriver
driver = webdriver.Chrome()
driver.get(auth_url)

time.sleep(2)  # Wait for page to load

# Verify successful login
success_message = driver.find_element(By.TAG_NAME, "p").text
assert "Congratulations" in success_message, "Login failed!"

print("✅ Authentication successful!")