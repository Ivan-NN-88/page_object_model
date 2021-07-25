"""Базовая страница для проекта: BasePage."""

class BasePage:
    """Базовая страница для проекта: BasePage."""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Открывает нужную страницу в браузере."""
        self.browser.get(self.url)