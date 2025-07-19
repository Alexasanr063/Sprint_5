from selenium.webdriver.common.by import By
from .base import BasePage
from ..locators import LoginFormLocators


class LoginPage(BasePage):
    def open_registration_form(self):
        self.click(LoginFormLocators.NO_ACCOUNT_BUTTON)

    def login(self, email, password):
        self.send_keys(LoginFormLocators.EMAIL_FIELD, email)
        self.send_keys(LoginFormLocators.PASSWORD_FIELD, password)
        self.click(LoginFormLocators.LOGIN_BUTTON)