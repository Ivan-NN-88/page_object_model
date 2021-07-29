"""Селектора основных элементов."""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Селектора главной страницы."""
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    """Селектора страницы авторизации."""
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    """Селектора страницы товара."""
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "col-sm-6 product_main")]//h1')
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, '//div[@id="messages"]//div[1]//div[1]')
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRODUCT_PRICE_IN_MESSAGE = (By.XPATH, '//div[@id="messages"]//div[3]//div[1]//p[1]')
    BUTTON_ADD_TO_BASKET = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="messages"]//div[1]')