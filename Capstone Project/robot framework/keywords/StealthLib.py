import csv
import os
import undetected_chromedriver as uc
from robot.api.deco import keyword
from selenium import webdriver


class StealthLib:
    def __init__(self):
        self.driver = None

    @keyword("Get Csv Data")
    def get_csv_data(self, file_path):
        data = {}
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    data[row[0].strip()] = row[1].strip()
        return data

    @keyword("Open Stealth Browser")
    def open_stealth_browser(self, url, browser="chrome"):
        """
        Open a browser for Robot tests.

        Default is Chrome via undetected_chromedriver.
        Pass browser=edge to use Microsoft Edge.
        """
        browser = str(browser).lower()

        if browser == "edge":
            from selenium.webdriver.edge.options import Options as EdgeOptions

            edge_options = EdgeOptions()
            edge_options.add_argument("--start-maximized")
            edge_options.add_argument("--disable-popup-blocking")
            self.driver = webdriver.Edge(options=edge_options)
        else:
            options = uc.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--disable-popup-blocking')
            # Use version_main=144 to match your successful Pytest run
            self.driver = uc.Chrome(options=options, version_main=144)

        self.driver.get(url)
        # Register the driver with Robot's SeleniumLibrary
        from robot.libraries.BuiltIn import BuiltIn

        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        sl.register_driver(self.driver, 'stealth_browser')
        return self.driver

    @keyword("Close Stealth Browser")
    def close_stealth_browser(self):
        if self.driver:
            self.driver.quit()