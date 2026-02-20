import pytest
import os
import sys
import glob
import time
import configparser
import undetected_chromedriver as uc
import psutil
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

# Prevent undetected chromedriver destructor crash
def suppress_del(self):
    pass

uc.Chrome.__del__ = suppress_del

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from utilities.data_loader import load_kv_csv

DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

# ---------------- CONFIG READER ---------------- #

CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.ini")cd
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# ---------------- CLI OPTIONS ---------------- #

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        choices=["chrome", "edge"],
        help="Browser to use: chrome or edge (overrides config.ini)"
    )

# ---------------- TERMINAL LOG FILE ---------------- #

def pytest_configure(config):
    log_file = os.path.join(REPORT_DIR, "pytest_terminal_output.txt")
    with open(log_file, "w") as f:
        f.write(f"PYTEST EXECUTION LOG\nStarted: {time.ctime()}\n====================\n")

# ---------------- DYNAMIC CSV PARAMETRIZATION ---------------- #

def pytest_generate_tests(metafunc):
    if "setup" in metafunc.fixturenames:
        csv_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.csv")))
        metafunc.parametrize("setup", csv_files, indirect=True)

# ---------------- FORCE BROWSER TERMINATION ---------------- #

def kill_browser_process(driver):
    try:
        if driver and driver.service and driver.service.process:
            pid = driver.service.process.pid
            driver.quit()
            if psutil.pid_exists(pid):
                proc = psutil.Process(pid)
                for child in proc.children(recursive=True):
                    child.terminate()
                proc.terminate()
    except:
        pass

# ---------------- MAIN FIXTURE ---------------- #

@pytest.fixture(scope="class")
def setup(request):

    csv_path = request.param
    test_data = load_kv_csv(csv_path)

    # Browser priority: CLI > config.ini > default chrome
    cli_browser = request.config.getoption("--browser")
    if cli_browser:
        browser = cli_browser.lower()
    else:
        browser = config.get("DEFAULT", "browser", fallback="chrome").lower()

    driver = None

    if browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-popup-blocking")
        try:
            driver = webdriver.Edge(options=edge_options)
        except Exception:
            pytest.fail("FATAL: Could not initialize Edge driver.")
    else:
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")

        for _ in range(3):
            try:
                driver = uc.Chrome(options=options, version_main=144)
                break
            except Exception:
                time.sleep(2)

        if not driver:
            pytest.fail("FATAL: Could not initialize Chrome driver.")

    # Apply waits from config
    implicit_wait = config.getint("DEFAULT", "implicit_wait", fallback=5)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(implicit_wait)

    request.cls.driver = driver
    request.cls.data = test_data

    # Base URL priority: config.ini > CSV
    base_url = config.get("DEFAULT", "base_url", fallback=test_data.get("base_url"))

    try:
        driver.get(base_url)
    except Exception:
        pass

    yield

    kill_browser_process(driver)

# ---------------- LOG PASS/FAIL TO FILE ---------------- #

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call":
        log_path = os.path.join(REPORT_DIR, "pytest_terminal_output.txt")
        status = "PASS" if report.passed else "FAIL"
        try:
            with open(log_path, "a") as f:
                f.write(f"{status}: {report.nodeid}\n")
        except:
            pass
