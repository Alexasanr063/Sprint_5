from Sprint_5.pages import LoginPage, ProfilePage
from Sprint_5.locators import ProfileLocators, AuthModalLocators, LoginFormLocators, MainPageLocators
from Sprint_5.conftest import main_page,browser

class TestAdCreation:
    def test_check_ad_in_my_ads(self, main_page, browser):
        """Тест проверки объявления в профиле"""
        main_page.open()
        main_page.open_login_form()

        login_page = LoginPage(browser)
        login_page.login(email="sanek51532@gmail.com", password="281188sss")

        profile_page = ProfilePage(browser)
        profile_page.open_profile()

        ad_card = profile_page.get_first_ad()
        assert profile_page.get_first_ad_title()
        assert profile_page.get_first_ad_location()
        assert profile_page.get_first_ad_price()

    def test_create_ad_unauthorized_user(self, main_page):
        """Тест попытки создания объявления неавторизованным пользователем"""
        main_page.open()
        main_page.click_create_ad()

        assert main_page.get_auth_modal_title() == "Чтобы разместить объявление, авторизуйтесь"
        assert main_page.is_login_button_visible()
        assert main_page.is_no_account_button_visible()
