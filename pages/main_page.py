"""Page Object для главной страницы сайта."""
from .base_page import BasePage


class MainPage(BasePage):
    """Page Object для главной страницы сайта."""

    # Заглушка класса.
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)