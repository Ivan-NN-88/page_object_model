"""Селектора основных элементов."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Содержит основные селектора."""
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')