"""Page Object для главной страницы сайта."""

from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """Page Object для главной страницы сайта."""
    def go_to_login_page(self):
        """Переходит на страницу авторизации."""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()