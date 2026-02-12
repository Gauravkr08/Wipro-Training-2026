import pytest
from day20.driverfactory import getdriver


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_page_title(browser):
    driver = getdriver(browser)
    try:
        driver.get("https://www.wikipedia.org/")
        assert "Wikipedia" in driver.title
    finally:
        driver.quit()
