"""Страница авторизации."""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Страница авторизации."""
    def register_new_user(self, email, password):
        """
        Регистрирует нового пользователя.
        :param email: электронная почта.
        :param password: пароль.
        """

        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_SUBMIT).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка на корректный url адрес."""
        assert "login" in self.browser.current_url, 'This is not login page!'

    def should_be_login_form(self):
        """Проверка, что есть форма логина."""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented!'

    def should_be_register_form(self):
        """Проверка, что есть форма регистрации на странице."""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented!'