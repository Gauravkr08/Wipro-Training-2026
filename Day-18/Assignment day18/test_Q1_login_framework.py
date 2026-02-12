import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
BROWSER = "firefox"

class CommonActions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def select_by_text(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)
class LoginPage(CommonActions):

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")

    def login(self, user, pwd):
        self.input_text(self.username, user)
        self.input_text(self.password, pwd)
        self.click(self.login_btn)
@pytest.fixture
def setup():
    if BROWSER == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
def test_login(setup):
    driver = setup
    driver.get(URL)

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    assert "dashboard" in driver.current_url
    print("Login test executed successfully")