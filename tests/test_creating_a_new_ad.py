from Sprint_5.pages import LoginPage, ProfilePage
from Sprint_5.locators import ProfileLocators, AuthModalLocators, LoginFormLocators, MainPageLocators
from Sprint_5.conftest import main_page,browser

class TestAdCreation:
    def test_check_ad_in_my_ads(self, main_page, browser):
        """Тест проверки объявления в профиле"""
        main_page.open()
        main_page.click(MainPageLocators.LOGIN_REGISTER_BUTTON)

        login_page = LoginPage(browser)
        login_page.login(email="sanek51532@gmail.com", password="281188sss")

        profile_page = ProfilePage(browser)
        profile_page.open_profile()

        ad_card = profile_page.get_first_ad()
        assert ad_card.find_element(*ProfileLocators.AD_TITLE).text
        assert ad_card.find_element(*ProfileLocators.AD_LOCATION).text
        assert ad_card.find_element(*ProfileLocators.AD_PRICE).text

    def test_create_ad_unauthorized_user(self, main_page):
        """Тест попытки создания объявления неавторизованным пользователем"""
        main_page.open()
        main_page.click(MainPageLocators.CREATE_AD_BUTTON, timeout=15)

        modal = main_page.get_element(AuthModalLocators.MODAL_FORM)
        modal_title = modal.find_element(*AuthModalLocators.MODAL_TITLE).text

        assert modal_title == "Чтобы разместить объявление, авторизуйтесь"
        assert main_page.is_element_visible(LoginFormLocators.LOGIN_BUTTON, timeout=5)
        assert main_page.is_element_visible(LoginFormLocators.NO_ACCOUNT_BUTTON, timeout=5)