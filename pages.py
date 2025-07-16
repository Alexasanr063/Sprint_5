from selenium.webdriver.common.by import By
from .base import BasePage

from Sprint_5.locators import (
    ProfileLocators,
    AuthModalLocators,
    LoginFormLocators,
    MainPageLocators,
    RegistrationFormLocators,
)


class MainPage(BasePage):
    def open(self, url="https://qa-desk.stand.praktikum-services.ru"):
        self.driver.get(url)

    def open_login_form(self):
        self.click(MainPageLocators.LOGIN_REGISTER_BUTTON)

class LoginPage(BasePage):
    def open_registration_form(self):
        self.click(LoginFormLocators.NO_ACCOUNT_BUTTON)

    def login(self, email, password):
        self.send_keys(LoginFormLocators.EMAIL_FIELD, email)
        self.send_keys(LoginFormLocators.PASSWORD_FIELD, password)
        self.click(LoginFormLocators.LOGIN_BUTTON)

class RegistrationPage(BasePage):
    def fill_form(self, email=None, password=None):
        if email:
            self.send_keys(RegistrationFormLocators.EMAIL_FIELD, email)
        if password:
            self.send_keys(RegistrationFormLocators.PASSWORD_FIELD, password)
            self.send_keys(RegistrationFormLocators.REPEAT_PASSWORD_FIELD, password)

    def submit_form(self):
        self.click(RegistrationFormLocators.SUBMIT_BUTTON)

    def is_element_visible(self, locator, timeout=10):
        return super().is_element_visible(locator, timeout)

class ProfilePage(BasePage):
    def open_profile(self):
        self.click(ProfileLocators.PROFILE_LINK)

    def is_avatar_displayed(self):
        return self.is_element_visible(ProfileLocators.USER_ICON)

    def is_username_displayed(self):
        return self.is_element_visible(ProfileLocators.USERNAME_DISPLAY)

    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)

    def get_first_ad(self, timeout=20):
        return self.get_element(ProfileLocators.AD_CARD, timeout)

    def get_ad_title(self, ad_element):
        return ad_element.find_element(*ProfileLocators.AD_TITLE).text

    def get_ad_location(self, ad_element):
        return ad_element.find_element(*ProfileLocators.AD_LOCATION).text

    def get_ad_price(self, ad_element):
        return ad_element.find_element(*ProfileLocators.AD_PRICE).text

    def get_first_ad_info(self, timeout=20):
        """Получает информацию о первом объявлении"""
        ad_card = self.get_element(ProfileLocators.AD_CARD, timeout)
        return {
            'title': ad_card.find_element(*ProfileLocators.AD_TITLE).text,
            'location': ad_card.find_element(*ProfileLocators.AD_LOCATION).text,
            'price': ad_card.find_element(*ProfileLocators.AD_PRICE).text
        }