from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRID_URL = "http://localhost:4444"


def getdriver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_capability("browserName", "firefox")
    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    # 🔹 Print browser & platform details
    caps = driver.capabilities
    print(f"Browser: {caps.get('browserName')} | Platform: {caps.get('platformName')}")

    return driver
