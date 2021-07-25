"""Тест на основе Page Object."""

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    """Тест на основе Page Object."""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()