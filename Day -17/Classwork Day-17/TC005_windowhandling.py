from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://letcode.in/window")
time.sleep(5)

driver.find_element(By.ID, "multi").click()
time.sleep(5)

windows = driver.window_handles

for child in windows:
    driver.switch_to.window(child)
    time.sleep(5)
    print("Title:", driver.title)
    print("URL:", driver.current_url)

driver.quit()