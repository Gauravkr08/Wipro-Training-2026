import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
        except Exception:
            # Fallback
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception:
            element = self.driver.find_element(*locator)
            self.driver.execute_script(f"arguments[0].value = '{text}';", element)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", element)

    def get_element_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def capture_screenshot(self, name):
        timestamp = int(time.time())
        base_dir = os.path.join(os.getcwd(), "screenshots", "Pytest screenshots")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        filename = f"{name}_{timestamp}.png"
        full_path = os.path.join(base_dir, filename)
        time.sleep(0.5) 
        self.driver.save_screenshot(full_path)
        return full_path