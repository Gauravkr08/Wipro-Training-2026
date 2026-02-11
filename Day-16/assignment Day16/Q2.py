from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org")
print("Home Page Title:", driver.title)
time.sleep(2)

driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")
print("Second Page Title:", driver.title)
time.sleep(2)

driver.back()
print("After Back - Page Title:", driver.title)
time.sleep(2)

driver.forward()
print("After Forward - Page Title:", driver.title)
time.sleep(2)

driver.refresh()
print("After Refresh - Page Title:", driver.title)
time.sleep(2)

driver.quit()