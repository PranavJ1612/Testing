from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_argument("headless")  # execution of automated tests without a graphical user interface (GUI).

driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# For executing javascript with selenium u use .execute_script
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")