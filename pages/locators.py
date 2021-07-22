from selenium.webdriver.common.by import By


class MainPageLocators():
    """
    Локаторы для главной страницы.
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """
    Локаторы для страницы логина и регистрации.
    """
    REGISTER_FORM = (By.CLASS_NAME, "register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocator():
    """
    Локаторы для страницы товара.
    """
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_TITLE = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    BOOK_TITLE_AFTER_ADDING = (By.XPATH, '//div[contains(@class, "alertinner")]/strong')