import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


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


# Test 1 : Verify Page Title

def test_page_title(driver):
    assert "Try Testing This" in driver.title

    time.sleep(2)

# Test 2 : Alert Button

def test_alert_button(driver):
    wait = WebDriverWait(driver, 10)

    alert_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Alert')]")
        )
    )
    alert_button.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    assert alert.text is not None
    alert.accept()
    time.sleep(2)


# Test 3 : Input Text Field

def test_input_field(driver):
    input_box = driver.find_element(By.ID, "fname")
    input_box.send_keys("KEERTANA")
    time.sleep(1)
    assert input_box.get_attribute("value") == "KEERTANA"
    time.sleep(1)
    input_box = driver.find_element(By.ID, "lname")
    input_box.send_keys("N V")
    time.sleep(1)
    assert input_box.get_attribute("value") == "N V"
    time.sleep(1)

# Test 5: Radio Button
def test_radio_button(driver):
    radio = driver.find_element(By.ID, "male")
    radio.click()
    assert radio.is_selected()
    time.sleep(1)


# Test 6 : Checkbox

def test_checkbox(driver):
    time.sleep(1)
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()
    time.sleep(1)
    assert checkbox.is_selected()
    time.sleep(1)

# Test 7: Dropdown Test

def test_dropdown(driver):
    time.sleep(1)
    dropdown = Select(driver.find_element(By.ID, "option"))
    dropdown.select_by_visible_text("Option 2")
    assert dropdown.first_selected_option.text=="Option 2"
    time.sleep(1)

#Test 8: datalist
def test_datalist(driver):
    time.sleep(2)
    input =driver.find_element(By.NAME,"Options")
    input.send_keys("Strawberry")
    assert input.get_attribute("value")=="Strawberry"
    time.sleep(2)



