"""Селектора основных элементов."""
from selenium.webdriver.common.by import By


class BasePageLocators():
    """Общие селектора."""
    BUTTON_GO_TO_BASKET = (By.XPATH, '//span[@class="btn-group"]/a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    """Селектора страницы корзины товаров."""
    BASKET_ITEMS = (By.XPATH, '//div[@class="basket-items"]')
    TEXT_BASKET_IS_EMPTY = (By.XPATH, '//div[@id="content_inner"]/p')


class LoginPageLocators:
    """Селектора страницы авторизации."""
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.XPATH, '//div[@class="col-sm-6 register_form"]//input[@type="email"]')
    REGISTER_PASSWORD1 = (By.XPATH, '//div[@class="col-sm-6 register_form"]//input[@name="registration-password1"]')
    REGISTER_PASSWORD2 = (By.XPATH, '//div[@class="col-sm-6 register_form"]//input[@name="registration-password2"]')
    REGISTER_BUTTON_SUBMIT = (By.XPATH, '//div[@class="col-sm-6 register_form"]//button[@type="submit"]')


class ProductPageLocators:
    """Селектора страницы товара."""
    BUTTON_ADD_TO_BASKET = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "col-sm-6 product_main")]/h1')
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]/div[1]')
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRODUCT_PRICE_IN_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[3]/div[1]/p[1]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]')