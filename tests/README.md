# Автоматизированное тестирование веб-сайта https://qa-desk.stand.praktikum-services.ru/

## Описание проекта

Этот проект содержит автоматизированные тесты для веб-приложения QA Desk. Тесты охватывают следующие функциональности:
- Регистрация новых пользователей
- Авторизация существующих пользователей
- Выход из системы (logout)
- Работа с объявлениями (создание, просмотр)

## Структура проекта
tests/
├── pages/ 
│ └── init.py
├── locators/ 
│ └── init.py
├── fixtures/ 
│ └── init.py
├── registration/ 
│ └── test_.py
├── auth/ 
│ └── test_.py
├── conftest.py 
└── requirements.txt 


## Технологический стек

- Python 3.9+
- pytest - фреймворк для тестирования
- Selenium WebDriver - автоматизация браузера
- Edge WebDriver - драйвер для браузера Microsoft Edge
- Page Object Pattern - паттерн проектирования тестов

## Требования

1. Установленный Python 3.9+
2. Браузер Microsoft Edge
3. Microsoft Edge WebDriver (совместимая версия с вашим браузером)

## Установка

1. Клонировать репозиторий:
   ```bash
   git clone <repository-url>
   cd <project-directory>
2.Создать и активировать виртуальное окружение:
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate      # Windows 

запуск тестов:
pytest tests/