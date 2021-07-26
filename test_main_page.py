"""Тест на основе Page Object."""

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    """Тест на основе Page Object."""
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    """Тест должен увидеть ссылку на страницу авторизации."""
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_be_login_page(browser):
    """Тест самой страницы авторизации на селектора."""
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()