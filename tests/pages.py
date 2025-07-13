from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import MainPageLocators, RegistrationFormLocators, LoginFormLocators, ProfileLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.get("https://qa-desk.stand.praktikum-services.ru")
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)
        ).click()
        return LoginPage(self.driver)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginFormLocators.EMAIL_FIELD)
        ).send_keys(email)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginFormLocators.PASSWORD_FIELD)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginFormLocators.LOGIN_BUTTON)
        ).click()
        return ProfilePage(self.driver)

    def open_registration_form(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(RegistrationFormLocators.REGISTER_LINK)
        ).click()
        return RegistrationPage(self.driver)


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, email, password=None):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegistrationFormLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

        if password:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(RegistrationFormLocators.PASSWORD_FIELD)
            )
            password_field.send_keys(password)

            repeat_password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(RegistrationFormLocators.REPEAT_PASSWORD_FIELD)
            )
            repeat_password_field.send_keys(password)
        return self

    def submit_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RegistrationFormLocators.SUBMIT_BUTTON)
        ).click()
        return ProfilePage(self.driver)


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def open_profile(self):
        user_icon = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(ProfileLocators.USER_ICON)
        )
        user_icon.click()

        profile_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(ProfileLocators.PROFILE_LINK)
        )
        profile_link.click()
        return self
    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)
        ).click()
        return MainPage(self.driver)

    def is_avatar_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProfileLocators.USER_ICON)
        ).is_displayed()

    def is_username_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProfileLocators.USERNAME_DISPLAY)
        ).is_displayed()


def generate_email():
    return f"testuser{random.randint(1000, 9999)}@example.com"