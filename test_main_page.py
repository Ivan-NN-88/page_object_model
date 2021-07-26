"""Тест на основе Page Object."""

from .pages.main_page import MainPage


LINK = 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser):
    """Тест на основе Page Object."""
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    """Тест должен увидеть ссылку на страницу авторизации."""
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_login_link()