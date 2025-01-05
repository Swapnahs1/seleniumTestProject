from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the driver
options = Options()
options.add_argument('--headless')  # Run in headless mode for CI
options.add_argument('--disable-gpu')  # Disable GPU for CI
options.add_argument('--no-sandbox')  # Necessary for CircleCI
driver = webdriver.Chrome(options=options)

# Open the page
driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')

# Maximize the window (optional)
driver.maximize_window()

# Wait for elements to load (optional)
driver.implicitly_wait(10)

# 1. Fill out the "Name" field
name_field = driver.find_element(By.NAME, "name")
name_field.send_keys("John Doe")

# 2. Fill out the "Email" field
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("johndoe@example.com")

# 3. Fill out the "Phone" field
phone_field = driver.find_element(By.NAME, "mobile")
phone_field.send_keys("1234567890")

# 4. Select a gender (Radio button)
gender_radio = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[3]/div/div/div[1]/input")
gender_radio.click()

# Wait to see the result (for demo purposes, you can wait before closing the browser)
time.sleep(5)

# Close the browser
driver.quit()