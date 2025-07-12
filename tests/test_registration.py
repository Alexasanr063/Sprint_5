from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages import MainPage, generate_email
from locators import RegistrationFormLocators, ProfileLocators


class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        yield

    def test_valid_registration(self, browser):
        """Тест успешной регистрации"""
        # 1. Регистрация нового пользователя
        profile_page = (self.main_page.open_login_form()
                        .open_registration_form()
                        .fill_form(email=generate_email(), password='000')
                        .submit_form())

        # 2. Проверки после регистрации
        assert "registration" not in browser.current_url.lower()

        # Проверка аватара
        avatar = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(ProfileLocators.USER_ICON)
        )
        assert avatar.is_displayed(), "Аватар не отображается после регистрации"

        # Проверка имени пользователя
        username = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(ProfileLocators.USERNAME_DISPLAY)
        )
        assert username.is_displayed(), "Имя пользователя не отображается после регистрации"

    def test_invalid_email_registration(self, browser):
        """Тест регистрации с невалидным email"""
        registration_page = (self.main_page.open_login_form()
                             .open_registration_form()
                             .fill_form(email="invalid_email")
                             .submit_form())

        error_message = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(RegistrationFormLocators.ERROR_MESSAGE)
        )
        assert error_message.text == "Ошибка"

    def test_existing_user_registration(self, browser):
        """Тест регистрации уже существующего пользователя"""
        registration_page = (self.main_page.open_login_form()
                             .open_registration_form()
                             .fill_form(email="sanek51532@gmail.com", password="281188sss")
                             .submit_form())

        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationFormLocators.ERROR_MESSAGE)
        )
        assert error_message.text == "Ошибка"