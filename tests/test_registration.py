from Sprint_5.pages import LoginPage, RegistrationPage, ProfilePage
from Sprint_5.locators import RegistrationFormLocators
from Sprint_5.helpers import generate_email
from Sprint_5.conftest import main_page,browser


class TestRegistration:
    def test_valid_registration(self, main_page, browser):
        """Тест успешной регистрации нового пользователя"""
        main_page.open()
        main_page.open_login_form()

        login_page = LoginPage(browser)
        login_page.open_registration_form()

        registration_page = RegistrationPage(browser)
        registration_page.fill_form(email=generate_email(), password='000')
        registration_page.submit_form()

        profile_page = ProfilePage(browser)
        assert "registration" not in browser.current_url.lower()
        assert profile_page.is_avatar_displayed()
        assert profile_page.is_username_displayed()

    def test_invalid_email_registration(self, main_page, browser):
        """Тест регистрации с невалидным email"""
        main_page.open()
        main_page.open_login_form()

        login_page = LoginPage(browser)
        login_page.open_registration_form()

        registration_page = RegistrationPage(browser)
        registration_page.fill_form(email="invalid_email")
        registration_page.submit_form()

        assert registration_page.is_element_visible(
            RegistrationFormLocators.ERROR_MESSAGE,
            timeout=5
        ), "Сообщение об ошибке не отображается"

    def test_existing_user_registration(self, main_page, browser):
        """Тест регистрации уже существующего пользователя"""
        main_page.open()
        main_page.open_login_form()

        login_page = LoginPage(browser)
        login_page.open_registration_form()

        registration_page = RegistrationPage(browser)
        registration_page.fill_form(email="sanek51532@gmail.com", password="281188sss")
        registration_page.submit_form()

        assert registration_page.is_element_visible(
            RegistrationFormLocators.ERROR_MESSAGE
        ), "Сообщение об ошибке не отображается"