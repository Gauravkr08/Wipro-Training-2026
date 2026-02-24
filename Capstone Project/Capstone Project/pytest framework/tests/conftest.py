import pytest
import os
import sys
import glob
import time
import configparser
import argparse
import psutil
import re
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


def _first_existing_path(paths):
    for path in paths:
        if path and os.path.exists(path):
            return path
    return None


def _get_file_major_version(exe_path: str | None) -> int | None:
    if not exe_path or not os.path.exists(exe_path):
        return None
    try:
        cmd = [
            "powershell",
            "-NoProfile",
            "-Command",
            f"(Get-Item '{exe_path}').VersionInfo.ProductVersion",
        ]
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL).strip()
        m = re.match(r"^(\d+)\.", out)
        return int(m.group(1)) if m else None
    except Exception:
        return None


def _find_cached_driver(cache_root: str, driver_subdir: str, exe_name: str, major: int | None = None) -> str | None:
    base = os.path.join(cache_root, driver_subdir)
    if not os.path.isdir(base):
        return None

    matches: list[str] = []
    for root, _dirs, files in os.walk(base):
        if exe_name in files:
            exe_path = os.path.join(root, exe_name)
            if major is not None:
                if f"\\{major}." not in exe_path and f"/{major}." not in exe_path:
                    continue
            matches.append(exe_path)

    if not matches:
        return None

    matches.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return matches[0]


# ---------------- CHROME DRIVER ---------------- #

def _create_chrome_driver() -> webdriver.Chrome:
    chrome_exe = _first_existing_path(
        [
            os.path.join(os.environ.get("ProgramFiles", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "Application", "chrome.exe"),
        ]
    )

    chrome_major = _get_file_major_version(chrome_exe)
    cache_root = os.path.join(os.path.expanduser("~"), ".cache", "selenium")
    chromedriver_path = _find_cached_driver(cache_root, "chromedriver", "chromedriver.exe", major=chrome_major)

    options = ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-backgrounding-occluded-windows")

    options.page_load_strategy = "eager"  # IMPORTANT FIX

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if chrome_exe:
        options.binary_location = chrome_exe

    if chromedriver_path:
        service = ChromeService(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    try:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
        )
    except Exception:
        pass

    return driver


# ---------------- BRAVE DRIVER (REPLACED EDGE) ---------------- #

def _create_brave_driver() -> webdriver.Chrome:
    brave_exe = _first_existing_path(
        [
            os.path.join(os.environ.get("ProgramFiles", ""), "BraveSoftware", "Brave-Browser", "Application", "brave.exe"),
            os.path.join(os.environ.get("ProgramFiles(x86)", ""), "BraveSoftware", "Brave-Browser", "Application", "brave.exe"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "BraveSoftware", "Brave-Browser", "Application", "brave.exe"),
        ]
    )

    brave_major = _get_file_major_version(brave_exe)
    cache_root = os.path.join(os.path.expanduser("~"), ".cache", "selenium")
    chromedriver_path = _find_cached_driver(cache_root, "chromedriver", "chromedriver.exe", major=brave_major)

    options = ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-backgrounding-occluded-windows")

    options.page_load_strategy = "eager"  # IMPORTANT FIX

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if brave_exe:
        options.binary_location = brave_exe

    if chromedriver_path:
        service = ChromeService(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    try:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
        )
    except Exception:
        pass

    return driver


# ---------------- PROJECT PATH SETUP ---------------- #

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from utilities.data_loader import load_kv_csv

DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.ini")
config = configparser.ConfigParser()
config.read(CONFIG_PATH)


# ---------------- CLI OPTION ---------------- #

def pytest_addoption(parser):
    try:
        parser.addoption(
            "--browser",
            action="store",
            default=None,
            choices=["chrome", "brave", "both"],
            help="Browser to use: chrome, brave, or both (overrides config.ini)"
        )
    except argparse.ArgumentError:
        pass


# ---------------- PARAMETRIZATION ---------------- #

def pytest_generate_tests(metafunc):
    if "setup" in metafunc.fixturenames:
        csv_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.csv")))

        cli_browser = None
        if "--browser" in sys.argv or any(arg.startswith("--browser=") for arg in sys.argv):
            cli_browser = metafunc.config.getoption("--browser")

        cfg_browser = config.get("DEFAULT", "browser", fallback="chrome")
        requested = (cli_browser or cfg_browser or "chrome").strip().lower()

        if requested == "both":
            browsers = ["chrome", "brave"]
        else:
            browsers = [requested]

        params = [(csv_path, browser) for csv_path in csv_files for browser in browsers]
        metafunc.parametrize("setup", params, indirect=True)


# ---------------- FIXTURE ---------------- #

@pytest.fixture(scope="class")
def setup(request):

    if isinstance(request.param, (tuple, list)) and len(request.param) == 2:
        csv_path, browser = request.param
    else:
        csv_path, browser = request.param, None

    test_data = load_kv_csv(csv_path)

    if not browser:
        browser = config.get("DEFAULT", "browser", fallback="chrome").lower()

    driver = None

    implicit_wait = config.getint("DEFAULT", "implicit_wait", fallback=5)
    explicit_wait = config.getint("DEFAULT", "explicit_wait", fallback=10)
    base_url = config.get("DEFAULT", "base_url", fallback=test_data.get("base_url"))

    def _configure_driver(drv):
        drv.set_page_load_timeout(120)
        drv.implicitly_wait(implicit_wait)
        drv._explicit_wait = explicit_wait

    def _create_driver_for_browser():
        if browser == "brave":
            try:
                return _create_brave_driver()
            except Exception:
                return _create_chrome_driver()
        return _create_chrome_driver()

    driver = _create_driver_for_browser()
    _configure_driver(driver)

    request.cls.driver = driver
    request.cls.data = test_data

    driver.get(base_url)
    time.sleep(3)

    yield

    try:
        driver.quit()
    except:
        pass