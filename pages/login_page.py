from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """
    Класс тестов для страницы входа и регистрации.
    """
    def should_be_login_page(self):
        """
        Запуск всех тестов.
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Проверка, есть ли 'login' в ссылке.
        Если нету -- сработает assert
        """
        assert 'login' in self.browser.current_url, f"login in {self.browser.current_url} is not presented"

    def should_be_login_form(self):
        """
        Проверка, есть ли форма для входа на странице.
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """
        Проверка, есть ли форма для регистрации на странице.
        """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
