import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# -----------------------------
# PyTest Fixture (Setup & Teardown)
# -----------------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get("https://trytestingthis.netlify.app/")
    driver.maximize_window()
    yield driver
    driver.quit()
time.sleep(2)

# -----------------------------
# Test 1 : Verify Page Title
# -----------------------------
def test_page_title(driver):
    assert "Try Testing This" in driver.title

    time.sleep(2)


# -----------------------------
# Test 2 : Alert Button
# -----------------------------
def test_alert_button(driver):
    wait = WebDriverWait(driver, 10)

    alert_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Alert')]")
        )
    )
    alert_button.click()

    alert = driver.switch_to.alert
    assert alert.text is not None
    alert.accept()
time.sleep(2)

# -----------------------------
# Test 3 : Input Text Field
# -----------------------------
def test_input_field(driver):
    input_box = driver.find_element(By.ID, "fname")
    input_box.send_keys("Automation Test")

    assert input_box.get_attribute("value") == "Automation Test"

time.sleep(2)
# -----------------------------
# Test 4 : Radio Button
# -----------------------------
def test_radio_button(driver):
    radio = driver.find_element(By.ID, "male")
    radio.click()

    assert radio.is_selected()
time.sleep(2)

# -----------------------------
# Test 5 : Checkbox
# -----------------------------
def test_checkbox(driver):
    time.sleep(3)
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()
    time.sleep(3)

    assert checkbox.is_selected()
time.sleep(2)
# -----------------------------
# Test 6 : Dropdown Test
# -----------------------------
def test_dropdown(driver):
    time.sleep(2)
    dropdown = Select(driver.find_element(By.ID, "option"))
    dropdown.select_by_visible_text("Option 2")

    selected_option = dropdown.first_selected_option.text
    assert selected_option == "Option 2"
time.sleep(2)
# Test 6 : Dropdown Test
