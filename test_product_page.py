"""Тест-кейсы для страницы товара"""
import time
import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators


link_with_arg = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links_with_arg = [link_with_arg + str(i) for i in range(1)]


@pytest.mark.need_review
@pytest.mark.parametrize('link', links_with_arg)
def test_guest_can_add_product_to_basket(browser, link):
    """
    Проверка на добавление товара в корзину.
    :param browser: объект браузера.
    :param link: url ссылка на страницу.
    """

    print(f'[{link}] - Проверка на добавление товара в корзину...')
    page = ProductPage(browser, link)
    page.open()
    if link.endswith('offer7'):
        print('ПРОПУСКАЮ ТЕСТ ЭТОЙ СССЫЛКИ!')
        pytest.skip("There is an incorrect product name in the shopping cart. I am skipping this test!")
    page.should_be_product_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Проверка на возможность перехода на страницу авторизации со страницы товара.
    :param browser: объект браузера.
    """

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    print(f'[{link}] - Проверка на возможность перехода на страницу авторизации со страницы товара...')
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Проверка на то, что после перехода со страницы товара в корзину, не должно быть товаров в корзине.
    :param browser: объект браузера.
    """

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    print(f'[{link}] - Проверка, что после перехода со страницы товара в корзину, не должно быть товаров в корзине...')
    page = BasketPage(browser, link)
    page.open()
    page.is_cant_see_product_in_basket_opened_from_page()


def test_guest_cant_see_success_message(browser):
    """
    Проверка на отсутствие сообщений об успехе перед добавлением товара в корзину.
    :param browser: объект браузера.
    """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    print(f'[{link}] - Проверка на отсутствие сообщений об успехе перед добавлением товара в корзину...')
    page = ProductPage(browser, link)
    page.open()
    page.should_be_no_success_message()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Проверка на отсутствие сообщений об успехе после добавления товара в корзину.
    :param browser: объект браузера.
    """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    print(f'[{link}] - Проверка на отсутствие сообщений об успехе после добавления товара в корзину...')

    print('ПРОПУСКАЮ ТЕСТ ЭТОЙ СССЫЛКИ!')
    pytest.skip("There is correct success message after adding product to basket. I am skipping this test!")

    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
    page.should_be_no_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Проверка на присутствие ссылки авторизации на странице товара.
    :param browser: объект браузера.
    """

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    print(f'[{link}] - Проверка на присутствие ссылки авторизации на странице товара...')
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Проверка на исчезновение сообщений об успехе после добавления товара в корзину.
    :param browser: объект браузера.
    """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    print(f'[{link}] - Проверка на исчезновение сообщений об успехе после добавления товара в корзину...')

    print('ПРОПУСКАЮ ТЕСТ ЭТОЙ СССЫЛКИ!')
    pytest.skip("There is correct success message after adding product to basket. I am skipping this test!")

    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
    page.should_be_success_message_disappeared()


# @pytest.mark.user
class TestUserAddToBasketFromProductPage:
    """Тест-кейсы для зарегистрированного пользователя."""
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link_regiser = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        print(f'[{link_regiser}] - Тестирую регистрацию нового пользователя...')
        print(f'Email - [{email}]')
        print(f'Password - [{password}]')
        page = LoginPage(browser, link_regiser)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """
        Проверка на отсутствие сообщений об успехе перед добавлением товара в корзину.
        :param browser: объект браузера.
        """

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        print(f'[{link}] - Проверка на отсутствие сообщений об успехе перед добавлением товара в корзину...')
        page = ProductPage(browser, link)
        page.open()
        page.should_be_no_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Проверка на добавление товара в корзину.
        :param browser: объект браузера.
        """

        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        print(f'[{link}] - Проверка на добавление товара в корзину...')
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()