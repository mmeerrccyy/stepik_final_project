from selenium.common.exceptions import NoSuchElementException


class BasePage():
    """
    Класс для инициализации browser.
    """
    def __init__(self, browser, url, timeout=10):
        """
        :param browser: инициализация браузера
        :param url: инициализация ссылки для браузера
        :param timeout: инициализация ожидания элемента для браузера
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открытие браузера.
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        :param how: по какому селектору ищем
        :param what: что ищем
        :return: возвращает True, если элемент найден, в противном случае -- False.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
