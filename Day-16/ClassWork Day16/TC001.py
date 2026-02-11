from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# Navigate to Google
driver.get("https://www.google.com")
time.sleep(2)

box = driver.find_element(By.NAME, "q")
box.send_keys("selenium (software)")
time.sleep(2)
box.submit()

time.sleep(5)

# Navigate actions
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

# Close browser
driver.quit()