"""Тест на основе Page Object."""
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    """
    Тест на основе Page Object.
    :param browser: объект браузера.
    """

    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Проверка на то, что после перехода с главной страницы в корзину, не должно быть товаров в корзине.
    :param browser: объект браузера.
    """

    link = "http://selenium1py.pythonanywhere.com"
    print(f'Тестирую ссылку: [{link}]...')
    page = BasketPage(browser, link)
    page.open()
    page.is_cant_see_product_in_basket_opened_from_page()


def test_guest_should_be_login_page(browser):
    """Тест страницы авторизации."""
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    """
    Тест должен увидеть ссылку на страницу авторизации.
    :param browser: объект браузера.
    """

    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()