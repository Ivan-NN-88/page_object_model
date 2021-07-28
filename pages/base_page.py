"""Базовая страница для проекта: BasePage."""
import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


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
        except NoSuchElementException:
            return False

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