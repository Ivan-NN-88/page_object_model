"""Тест-кейсы для страницы товара"""
import pytest

from .pages.product_page import ProductPage


main_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [main_link + str(i) for i in range(10)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    """Проверка на добавление товара в корзину."""
    print(f'Тестирую ссылку: [{link}]...')
    page = ProductPage(browser, link)
    page.open()
    if link.endswith('offer7'):
        print('ПРОПУСКАЮ ТЕСТ ЭТОЙ СССЫЛКИ!')
        pytest.skip("There is an incorrect product name in the shopping cart. I am skipping this test!")
    page.should_be_product_page()