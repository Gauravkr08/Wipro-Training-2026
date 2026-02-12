from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
text_box = driver.find_element(By.ID, "tinymce")
text_box.send_keys(Keys.CONTROL + "a")
text_box.send_keys("Hello from Selenium iframe")

time.sleep(2)
driver.switch_to.default_content()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

time.sleep(2)

parent_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()
driver.switch_to.window(parent_window)
time.sleep(2)
driver.quit()