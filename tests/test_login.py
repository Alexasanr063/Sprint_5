import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import MainPage
from locators import MainPageLocators, ProfileLocators


class TestAuth:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        yield

    def test_successful_login(self, browser):
        """Тест успешной авторизации пользователя"""
        profile_page = self.main_page.open_login_form().login(
            email="sanek51532@gmail.com",
            password="281188sss"
        )

        assert "qa-desk.stand.praktikum-services.ru" in browser.current_url
        assert profile_page.is_avatar_displayed()
        assert profile_page.is_username_displayed()

    def test_successful_logout(self, browser):
        """Тест успешного выхода из системы"""
        profile_page = self.main_page.open_login_form().login(
            email="sanek51532@gmail.com",
            password="281188sss"
        )
        main_page = profile_page.logout()

        assert "qa-desk.stand.praktikum-services.ru" in browser.current_url
        login_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON)
        )
        assert login_button.is_displayed()