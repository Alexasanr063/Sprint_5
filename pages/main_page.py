from selenium.webdriver.common.by import By
from .base import BasePage
from ..locators import MainPageLocators,AuthModalLocators,LoginFormLocators,RegistrationFormLocators
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    def open(self, url="https://qa-desk.stand.praktikum-services.ru"):
        self.driver.get(url)

    def open_login_form(self):
        self.click(MainPageLocators.LOGIN_REGISTER_BUTTON)

    def get_auth_modal_title(self):
        return self.get_element_text(AuthModalLocators.MODAL_TITLE)

    def is_login_button_visible(self):
        return self.is_element_visible(LoginFormLocators.LOGIN_BUTTON)

    def is_no_account_button_visible(self):
        return self.is_element_visible(LoginFormLocators.NO_ACCOUNT_BUTTON)

    def click_create_ad(self):
        self.click(MainPageLocators.CREATE_AD_BUTTON)

    def is_login_register_button_visible(self, timeout=5):
        try:
            return self.is_element_visible(MainPageLocators.LOGIN_REGISTER_BUTTON, timeout=timeout)
        except TimeoutException:
            return False

