from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Loginpage import loginpage
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

loginobj = loginpage(driver)
loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()

# wait until dashboard loads
wait.until(EC.url_contains("dashboard"))

time.sleep(3)
driver.quit()
