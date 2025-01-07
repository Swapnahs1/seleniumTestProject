from selenium import webdriver
import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

@pytest.fixture(scope="module")
def driver():
    # Set up the driver
    options = Options()
    # options.add_argument('--headless')  # Run in headless mode for CI
    # options.add_argument('--disable-gpu')  # Disable GPU for CI
    # options.add_argument('--no-sandbox')  # Necessary for CircleCI
    driver = webdriver.Chrome(options=options)
    yield driver
        # Teardown: Close the browser after tests
    driver.quit()

def test_register_user(driver):
    # Open the page
    driver.get('https://www.tutorialspoint.com/selenium/practice/alerts.php')

    # Maximize the window (optional)
    driver.maximize_window()

    # Wait for elements to load (optional)
    driver.implicitly_wait(10)
    # alertClcik = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[1]/button")
    # alertClcik.click()
    try:
        # Open the target URL
        driver.get('https://www.tutorialspoint.com/selenium/practice/alerts.php')

        # Click the button that triggers the alert
        driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div[1]/button").click()

        # Wait for the alert to appear (optional, can adjust sleep time)
        time.sleep(2)

        # Switch to the alert and assert its message
        alert = Alert(driver)
        
        # Assert the alert's text
        alert_text = alert.text
        assert alert_text == "Hello world!"

        # Accept the alert (click on OK)
        alert.accept()

        print("Alert is handled successfully!")

    except Exception as e:
            print(f"Error occurred: {e}")

    finally:
            # Close the browser
            driver.quit()