from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
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

def test_Drag_Drop(driver):
    # Open the page
    driver.get('https://www.tutorialspoint.com/selenium/practice/alerts.php')

    # Maximize the window (optional)
    driver.maximize_window()

    # Wait for elements to load (optional)
    driver.implicitly_wait(10)
    # alertClcik = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[1]/button")
    # alertClcik.click()
    try:

        # Open the target page
        driver.get('https://www.tutorialspoint.com/selenium/practice/droppable.php')

        # Maximize the browser window
        driver.maximize_window()

        # Allow the page to load fully
        time.sleep(2)

        # Locate the draggable and droppable elements
        draggable = driver.find_element(By.ID, 'draggable')
        droppable = driver.find_element(By.ID, 'droppable')

        # Perform the drag and drop action
        action = ActionChains(driver)
        action.drag_and_drop(draggable, droppable).perform()

        # Wait for a few seconds to visually confirm the action
        time.sleep(2)

    except Exception as e:
            print(f"Error occurred: {e}")

    finally:
            # Close the browser
            driver.quit()