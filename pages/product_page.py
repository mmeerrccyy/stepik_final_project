from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    """
    Класс тестов для страницы товара.
    Степик: https://stepik.org/lesson/201964/step/2?unit=176022
    """

    def add_book_to_basket(self):
        """
        Добавление товара в корзину и взятия текста с alert.
        """
        self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()
        self.check_title_of_book_after_adding_to_basket()

    def check_title_of_book_after_adding_to_basket(self):
        """
        Проверка, совпадает ли название книги с добавленной.
        :return:
        """
        book_title = self.browser.find_element(*ProductPageLocator.BOOK_TITLE).text
        book_title_after_adding = self.browser.find_element(*ProductPageLocator.BOOK_TITLE_AFTER_ADDING).text
        if book_title != book_title_after_adding:
            assert False, f"Название книг не совпадает! В заголовке указано {book_title}, " \
                          f"а в корзине -- {book_title_after_adding}"
        assert True
