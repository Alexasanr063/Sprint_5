from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary')][contains(., 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and contains(., 'Разместить объявление')]")


class RegistrationFormLocators:
    #REGISTER_LINK = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Введите Email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password'][name='password']")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password'][name='submitPassword']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_CONTAINER = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'popUp_inputColumn__RgD8n')]//span[@class='input_span__yWPqB']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")


class LoginFormLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")


class ProfileLocators:
    USER_ICON = (By.CSS_SELECTOR, "svg.svgSmall")
    PROFILE_LINK = (By.CSS_SELECTOR, "h3.profileText.name")
    # Основной контейнер объявления
    AD_CARD = (By.CSS_SELECTOR, "div.card")

    # Заголовок объявления (более надежный вариант)
    AD_TITLE = (By.CSS_SELECTOR, "div.card h2.h2")

    # Местоположение
    AD_LOCATION = (By.CSS_SELECTOR, "div.card h3.h3")

    # Цена
    AD_PRICE = (By.CSS_SELECTOR, "div.card div.price h2.h2")

    # Кнопка редактирования
    EDIT_BUTTON = (By.CSS_SELECTOR, "div.card button.editButton")  # Цена
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    USERNAME_DISPLAY = (By.XPATH, "//h3[@class='profileText name' and contains(text(), 'User.')]")


class AuthModalLocators:
    MODAL = (By.CSS_SELECTOR, "div.modal")
    MODAL_FORM = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR")
    MODAL_TITLE = (By.CSS_SELECTOR, "h1.h1")