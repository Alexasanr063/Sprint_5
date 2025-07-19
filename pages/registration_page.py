from Sprint_5.pages.base import BasePage
from ..locators import RegistrationFormLocators

class RegistrationPage(BasePage):
    def fill_form(self, email=None, password=None):
        """Заполняет форму регистрации"""
        if email:
            self.send_keys(RegistrationFormLocators.EMAIL_FIELD, email)
        if password:
            self.send_keys(RegistrationFormLocators.PASSWORD_FIELD, password)
            self.send_keys(RegistrationFormLocators.REPEAT_PASSWORD_FIELD, password)
    def submit_form(self):
        self.click(RegistrationFormLocators.SUBMIT_BUTTON)

    def is_element_visible(self, locator, timeout=10):
        return super().is_element_visible(locator, timeout)

    def is_error_message_visible(self, timeout=5):
        return self.is_element_visible(RegistrationFormLocators.ERROR_MESSAGE, timeout=timeout)