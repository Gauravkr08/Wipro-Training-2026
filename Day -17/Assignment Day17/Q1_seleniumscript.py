from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, "firstName").send_keys("Gaurav")
driver.find_element(By.ID, "lastName").send_keys("kumar")
driver.find_element(By.ID, "userEmail").send_keys("gaurav@gmail.com")

driver.execute_script("arguments[0].click();",
    driver.find_element(By.XPATH, "//label[text()='Male']"))

time.sleep(1)

sports_checkbox = driver.find_element(By.XPATH, "//label[text()='Sports']")
driver.execute_script("arguments[0].scrollIntoView(true);", sports_checkbox)
time.sleep(1)
driver.execute_script("arguments[0].click();", sports_checkbox)

time.sleep(1)

driver.execute_script("window.scrollBy(0,500)", "")
driver.find_element(By.ID, "submit").click()

time.sleep(2)

print("Form submitted successfully")
driver.save_screenshot("Day17_Form_Submitted.png")
driver.quit()