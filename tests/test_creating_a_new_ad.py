import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, AuthModalLocators, ProfileLocators, LoginFormLocators
from pages import MainPage, LoginPage, ProfilePage  # Изменяем импорты


def test_check_ad_in_my_ads(browser, main_page):
    """Проверить, что в блоке 'Мои объявления' отображается созданное объявление"""
    # 1. Авторизация
    profile_page = main_page.open_login_form().login(
        email="sanek51532@gmail.com",
        password="281188sss"
    )

    # 2. Переход в профиль
    profile_page.open_profile()

    # 3. Проверка объявления
    ad_card = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(ProfileLocators.AD_CARD)
    )

    # Проверки элементов объявления
    assert ad_card.find_element(*ProfileLocators.AD_TITLE).text == "Тестовое объявление Selenium"
    assert ad_card.find_element(*ProfileLocators.AD_LOCATION).text == "Москва"
    assert ad_card.find_element(*ProfileLocators.AD_PRICE).text == "2 500 ₽"


def test_create_ad_unauthorized_user(browser, main_page):
    """Проверка отображения модального окна авторизации при попытке создать объявление неавторизованным пользователем"""
    # 1. Открываем главную страницу
    browser.get("https://qa-desk.stand.praktikum-services.ru")

    # 2. Нажимаем кнопку "Разместить объявление"
    create_ad_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON)
    )
    create_ad_button.click()

    # 3. Проверяем появление модального окна авторизации
    modal = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(AuthModalLocators.MODAL_FORM)
    )

    # 4. Проверяем заголовок модального окна
    modal_title = modal.find_element(*AuthModalLocators.MODAL_TITLE).text
    assert modal_title == "Чтобы разместить объявление, авторизуйтесь", \
        f"Заголовок модального окна не совпадает. Ожидалось: 'Чтобы разместить объявление, авторизуйтесь', Фактически: '{modal_title}'"

    # 5. Проверяем наличие кнопки "Вход и регистрация" в модальном окне
    login_button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginFormLocators.LOGIN_BUTTON)
    )
    assert login_button.is_displayed(), "Кнопка 'Войти' не отображается"

    # 6. Проверяем наличие кнопки "Нет аккаунта"
    register_button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginFormLocators.NO_ACCOUNT_BUTTON)
    )
    assert register_button.is_displayed(), "Кнопка 'Нет аккаунта' не отображается"