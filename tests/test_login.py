from Sprint_5.pages import LoginPage, ProfilePage
from Sprint_5.locators import MainPageLocators
from Sprint_5.conftest import main_page,browser

class TestAuth:
    def test_successful_login(self, main_page, browser):
        """Тест успешной авторизации"""
        main_page.open()
        main_page.open_login_form()

        login_page = LoginPage(browser)
        login_page.login(email="sanek51532@gmail.com", password="281188sss")

        profile_page = ProfilePage(browser)
        assert "qa-desk.stand.praktikum-services.ru" in browser.current_url
        assert profile_page.is_avatar_displayed()
        assert profile_page.is_username_displayed()

    def test_successful_logout(self, main_page, browser):
        """Тест успешного выхода из системы"""
        main_page.open()
        main_page.open_login_form()

        login_page = LoginPage(browser)
        login_page.login(email="sanek51532@gmail.com", password="281188sss")

        profile_page = ProfilePage(browser)
        profile_page.logout()

        assert "qa-desk.stand.praktikum-services.ru" in browser.current_url
        assert main_page.is_login_register_button_visible()