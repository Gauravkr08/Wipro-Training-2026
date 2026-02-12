from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OpencartLocators

class OpencartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def take_screenshot(self, name):
        self.driver.save_screenshot(f"{name}.png")

    def navigate_to_mac_section(self):
        self.wait.until(EC.element_to_be_clickable(OpencartLocators.DESKTOPS_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(OpencartLocators.MAC_SUBMENU)).click()

    def get_mac_heading_text(self):
        return self.wait.until(EC.visibility_of_element_located(OpencartLocators.MAC_HEADER)).text

    def sort_products(self, visible_text):
        dropdown = Select(self.driver.find_element(*OpencartLocators.SORT_BY))
        dropdown.select_by_visible_text(visible_text)

    def click_add_to_cart(self):
        self.driver.find_element(*OpencartLocators.ADD_TO_CART).click()

    def search_for_product(self, product_name):
        search_box = self.driver.find_element(*OpencartLocators.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(product_name)
        self.driver.find_element(*OpencartLocators.SEARCH_ICON).click()

    def refined_search(self):
        self.wait.until(EC.presence_of_element_located(OpencartLocators.SEARCH_CRITERIA)).clear()
        self.driver.find_element(*OpencartLocators.DESC_CHECKBOX).click()
        self.driver.find_element(*OpencartLocators.SEARCH_SUBMIT_BTN).click()