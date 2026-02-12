from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)
print("Implicit wait set to 10 seconds")

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

try:
    explicit_wait = WebDriverWait(driver, 15)

    enable_button = explicit_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Enable']"))
    )

    print("Explicit Wait: Enable button is clickable")
    enable_button.click()

except TimeoutException:
    print("Explicit Wait: Enable button not clickable")

try:
    fluent_wait = WebDriverWait(
        driver,
        timeout=20,
        poll_frequency=2,
        ignored_exceptions=[NoSuchElementException]
    )

    textbox = fluent_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input"))
    )

    print("Fluent Wait: Textbox is available for interaction")
    textbox.clear()
    textbox.send_keys("Selenium Waits Demo")

except TimeoutException:
    print("Fluent Wait: Element not available")

time.sleep(3)
driver.quit()
