"""Страница товара."""
from selenium.webdriver.common.by import By
import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Страница товара."""
    def should_be_product_page(self):
        # Получаю изначальное наименование товара на странице
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # Получаю изначальную цену товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        # Нажимаю на кнопку "Добавить в корзину".
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BUSKET).click()
        # Высчитываем результат математического выражения из диалогового окна
        self.solve_quiz_and_get_code()

        # Проверяю что изначальное наименование товара соответствует товару добавленному в корзину
        self.should_be_product_name(product_name)
        # Проверяю что изначальная цена товара соответствует цене в корзине
        self.should_be_product_price(product_price)

    def should_be_product_name(self, start_product_name: str):
        """
        Проверяю cообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который действительно добавили.
        :param start_product_name: Изначальное наименование товара, перед добавлением в корзину.
        """

        assert start_product_name in self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text, \
            "PRODUCT NAME - Message is not found or product name not correct!"

    def should_be_product_price(self, start_product_price: str):
        """
        Проверяю cообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        :param start_product_price: Изначальная цена товара, перед добавлением в корзину.
        """

        assert start_product_price in self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text, \
            "PRICE - Message is not found or product name not correct!"
