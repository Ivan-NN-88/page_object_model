"""Базовая страница для проекта: BasePage."""
import math

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:
    """Базовая страница для проекта: BasePage."""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет, что элемент исчез на странице в течение заданного времени.
        :param how: как искать (css, id, xpath и тд: By.CSS_SELECTOR).
        :param what: что искать (строка-селектор).
        :param timeout: время ожидания элемента.
        """

        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what: str):
        """
        Ищет элемент и перехватывает исключение.
        :param how: как искать (css, id, xpath и тд: By.CSS_SELECTOR).
        :param what: что искать (строка-селектор).
        """

        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяет, что элемент не появляется на странице в течение заданного времени.
        :param how: как искать (css, id, xpath и тд: By.CSS_SELECTOR).
        :param what: что искать (строка-селектор).
        :param timeout: время ожидания элемента.
        """

        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def go_to_basket(self):
        """Переходит в корзину."""
        basket_link = self.browser.find_element(*BasePageLocators.BUTTON_GO_TO_BASKET)
        basket_link.click()

    def go_to_login_page(self):
        """Переходит на страницу авторизации."""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def open(self):
        """Открывает нужную страницу в браузере."""
        self.browser.get(self.url)

    def should_be_login_link(self):
        """Проверка ссылки на страницу авторизации."""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented!'

    def solve_quiz_and_get_code(self):
        """Высчитывает результат математического выражения из диалогового окна."""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")