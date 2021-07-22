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
