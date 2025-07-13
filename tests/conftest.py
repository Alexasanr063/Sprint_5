import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from pages import MainPage  # Изменяем импорт


@pytest.fixture
def browser():
    # Настройка Edge WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    # Инициализация драйвера
    driver = webdriver.Edge(service=Service(), options=options)
    yield driver

    # Закрытие браузера после теста
    driver.quit()


@pytest.fixture
def main_page(browser):  # Переименовываем фикстуру
    return MainPage(browser)