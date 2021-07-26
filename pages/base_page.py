"""Базовая страница для проекта: BasePage."""

from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """Базовая страница для проекта: BasePage."""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открывает нужную страницу в браузере."""
        self.browser.get(self.url)

    def is_element_present(self, how, what: str):
        """
        Ищет элемент и перехватывает исключение.
        :param how: как искать (css, id, xpath и тд: By.CSS_SELECTOR)
        :param what: что искать (строка-селектор)
        """

        try:
            self.browser.find_element(how, what)
            return True
        except (NoSuchElementException):
            return False