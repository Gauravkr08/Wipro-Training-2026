from selenium.webdriver.common.by import By

class OpencartLocators:
    DESKTOPS_MENU = (By.LINK_TEXT, "Desktops")
    MAC_SUBMENU = (By.LINK_TEXT, "Mac (1)")
    MAC_HEADER = (By.XPATH, "//h2[text()='Mac']")
    SORT_BY = (By.ID, "input-sort")
    ADD_TO_CART = (By.XPATH, "//button[contains(.,'Add to Cart')]")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_ICON = (By.CSS_SELECTOR, ".btn-lg")
    SEARCH_CRITERIA = (By.ID, "input-search")
    DESC_CHECKBOX = (By.ID, "description")
    SEARCH_SUBMIT_BTN = (By.ID, "button-search")