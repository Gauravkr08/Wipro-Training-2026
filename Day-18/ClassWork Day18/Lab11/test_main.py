import sys
import unittest
import time
import os
from selenium import webdriver
from pages import OpencartPage

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Lab_POM_Output.txt", "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger()


class TestLabPOM(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://tutorialsninja.com/demo/")
        self.page = OpencartPage(self.driver)

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filepath = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")

    def test_opencart_flow(self):
        print(f"--- Execution Started: {time.ctime()} ---")

        self.take_screenshot("Screenshot1_Home")

        print("Step 1: Navigating to Mac section...")
        self.page.navigate_to_mac_section()

        self.take_screenshot("Screenshot2_MacPage")

        print("Step 2: Verifying Heading and Sorting...")
        self.assertEqual(self.page.get_mac_heading_text(), "Mac")
        self.page.sort_products("Name (A - Z)")

        print("Step 3: Adding product to cart...")
        self.page.click_add_to_cart()

        print("Step 4: Performing search for 'Monitors'...")
        self.page.search_for_product("Monitors")

        self.take_screenshot("Screenshot3_SearchMonitors")

        print("Step 5: Executing refined search with descriptions...")
        self.page.refined_search()

        self.take_screenshot("Screenshot4_FinalState")

        print("Result: Test Passed successfully. All evidence captured.")

    def tearDown(self):
        print(f"--- Execution Finished: {time.ctime()} ---")
        self.driver.quit()

        if hasattr(sys.stdout, 'log'):
            sys.stdout.log.close()


if __name__ == "__main__":
    unittest.main()
