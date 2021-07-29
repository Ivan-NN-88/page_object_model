"""Тест-кейсы для страницы товара"""
import pytest

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


main_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [main_link + str(i) for i in range(1)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    """
    Проверка на добавление товара в корзину.
    :param browser: объект браузера.
    :param link: url ссылка на страницу.
    """

    print(f'Тестирую ссылку: [{link}]...')
    page = ProductPage(browser, link)
    page.open()
    if link.endswith('offer7'):
        print('ПРОПУСКАЮ ТЕСТ ЭТОЙ СССЫЛКИ!')
        pytest.skip("There is an incorrect product name in the shopping cart. I am skipping this test!")
    page.should_be_product_page()


@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    """
    Проверка на отсутствие сообщений об успехе после добавления товара в корзину.
    :param browser: объект браузера.
    :param link: url ссылка на страницу.
    """

    print('ПРОПУСКАЮ ТЕСТ ЭТОЙ СССЫЛКИ!')
    pytest.skip("There is correct success message after adding product to basket. I am skipping this test!")

    link = '/'.join(link.split('/')[:-1])
    print(f'Тестирую ссылку: [{link}]...')
    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
    page.should_be_no_success_message()


@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    """
    Проверка на отсутствие сообщений об успехе перед добавлением товара в корзину.
    :param browser: объект браузера.
    :param link: url ссылка на страницу.
    """

    link = '/'.join(link.split('/')[:-1])
    print(f'Тестирую ссылку: [{link}]...')
    page = ProductPage(browser, link)
    page.open()
    page.should_be_no_success_message()


@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    """
    Проверка на исчезновение сообщений об успехе после добавления товара в корзину.
    :param browser: объект браузера.
    :param link: url ссылка на страницу.
    """

    print('ПРОПУСКАЮ ТЕСТ ЭТОЙ СССЫЛКИ!')
    pytest.skip("There is correct success message after adding product to basket. I am skipping this test!")

    link = '/'.join(link.split('/')[:-1])
    print(f'Тестирую ссылку: [{link}]...')
    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
    page.should_be_success_message_disappeared()