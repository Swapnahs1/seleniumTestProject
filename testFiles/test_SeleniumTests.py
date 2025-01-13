from selenium import webdriver
import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture(scope="module")
def driver():
    # Set up the driver
    options = Options()
    options.add_argument('--headless')  # Run in headless mode for CI
    options.add_argument('--disable-gpu')  # Disable GPU for CI
    options.add_argument('--no-sandbox')  # Necessary for CircleCI
    driver = webdriver.Chrome(options=options)
    yield driver
        # Teardown: Close the browser after tests
    driver.quit()

def test_register_user(driver):
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

    # 3. Fill out the DOB Field
    dob_field = driver.find_element(By.NAME, "dob")
    dob_field.send_keys("23-12-1994")

    sub_field = driver.find_element(By.ID,"subjects")
    sub_field.send_keys("Physics") 

    # Find the file input field using the name attribute and send the file path to it
    file_input = driver.find_element(By.ID, 'picture')  # Find file input field by 'name' attribute

    # Specify the path to the file you want to upload
    file_path = os.path.join(os.getcwd(),"picture", "DSCN1062.JPG")
    absolute_path = os.path.abspath(file_path)

    if os.path.exists(absolute_path):
        print("File exists.")
    else:
        print("File does not exist.")
        # Send the file path to the file input element
    file_input.send_keys(absolute_path)

    # Find the file input field using the name attribute and send the file path to it
    address = driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/div[9]/div/textarea')  # Find file input field by 'name' attribute
    address.send_keys("Bangalore - 123456")
    state_field = driver.find_element(By.ID,"state")
    select = Select(state_field)
    select.select_by_visible_text("Rajasthan")
    city_field = driver.find_element(By.ID,"city")
    select_city = Select(city_field)
    select_city.select_by_visible_text("Agra")
    # Wait to see the result (for demo purposes, you can wait before closing the browser)
    time.sleep(5)