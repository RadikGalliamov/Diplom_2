# Дипломный проект. Задание 2: API-автотесты

## Автотесты для проверки ручек API программы Stellar Burgers.

## Реализованные сценарии

### Созданы тесты, покрывающие ручки

- создания пользователя
- авторизации пользователя
- изменение данных пользователя
- создания заказа 
- получение заказов по конкретному пользователю

### Структура проекта

  - `test_create_order.py` - тесты на проверку создания заказа
  - `test_receiving_user_orders.py` - тесты на проверку получения списка заказов конкретного пользователя 
  - `test_login_user.py` - тесты на проверку авторизации пользователей
  - `test_create_user.py` - тесты на проверку создания пользователя
  - `test_changing_user_data.py` - тесты на проверку изменения данных пользователя

### Запуск автотестов

- `pytest` - Запуск всех тестов     
- `pytest -v` - Запуск всех тестов c деталями прохождения
- `pytest -s` - Запуск всех тестов c деталями прохождения (отображение print)
- `pytest --durations=1` - Запуск тестов, отмечаем тесты которые проходят больше чем 1 сек
- `pytest --durations=0 -vv` - Запуск тестов, отмечаем тесты которые проходят больше чем 1 сек, плюс отчет
- `pytest -k development` - Запуск тестов для dev окружения
- `pytest -k "not development"` - Запуск тестов не отмеченных для dev окружения

**Установка зависимостей**

- `pip install -r requirements.txt`

**Отчет о покрытии**

- `pytest tests --alluredir=allure_results` - генерировать Allure-отчёт
- `Remove-Item -Recurse -Force allure_results ; pytest tests --alluredir=allure_results` - удалить старый отчет и 
генерировать новый Allure-отчёт
- `allure serve allure_results` - формирования отчета в формате HTML-страницы

## Документация API
https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89