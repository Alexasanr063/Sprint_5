from selenium.webdriver.common.by import By
from .base import BasePage

from Sprint_5.locators import (
    ProfileLocators,
    AuthModalLocators,
    LoginFormLocators,
    MainPageLocators,
    RegistrationFormLocators,
)




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

    def get_first_ad_title(self):
            ad = self.get_first_ad()
            return ad.find_element(*ProfileLocators.AD_TITLE).text

    def get_first_ad_location(self):
            ad = self.get_first_ad()
            return ad.find_element(*ProfileLocators.AD_LOCATION).text

    def get_first_ad_price(self):
            ad = self.get_first_ad()
            return ad.find_element(*ProfileLocators.AD_PRICE).text
