from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestQ1DailyWise:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_open_practice_page(self):
        # Open page
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        # Print page title
        print("Page Title:", self.driver.title)

        # Print current URL
        print("Page URL:", self.driver.current_url)