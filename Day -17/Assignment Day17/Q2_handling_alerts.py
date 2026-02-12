from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)
if not os.path.exists("screenshots"):
    os.mkdir("screenshots")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("JS Alert message:", alert.text)
alert.accept()
time.sleep(1)
driver.save_screenshot("screenshots/js_alert_accepted.png")
print(driver.find_element(By.ID, "result").text)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
confirm_alert = driver.switch_to.alert
print("Confirm Alert message:", confirm_alert.text)
confirm_alert.dismiss()
time.sleep(1)
driver.save_screenshot("screenshots/confirm_dismissed.png")

print(driver.find_element(By.ID, "result").text)

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt_alert = driver.switch_to.alert
print("Prompt Alert message:", prompt_alert.text)
prompt_alert.send_keys("Harsh")
prompt_alert.accept()
time.sleep(1)

driver.save_screenshot("screenshots/prompt_accepted.png")
print(driver.find_element(By.ID, "result").text)
driver.quit()