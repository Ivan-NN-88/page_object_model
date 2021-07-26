"""Селектора основных элементов."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Селектора главной страницы."""
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    """Селектора страницы авторизации."""
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')