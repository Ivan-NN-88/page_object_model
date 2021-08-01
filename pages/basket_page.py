"""Страница корзины товаров."""
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Страница корзины товаров."""
    def is_cant_see_product_in_basket_opened_from_page(self):
        """Проверка на то, что после перехода в корзину, не должно быть товаров в корзине."""
        self.go_to_basket()
        self.not_should_be_basket_items()
        self.should_be_text_about_empty_basket()

    def not_should_be_basket_items(self):
        """Проверка на отсутствие товаров в корзине."""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be!"

    def should_be_text_about_empty_basket(self):
        """Проверка, что есть текст о пустой корзине."""
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), 'No text about empty basket!'