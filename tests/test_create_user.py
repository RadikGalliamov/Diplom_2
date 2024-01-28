import allure
import requests

from data import TestDataUrl, TestDataCreateUser
from helpers.helpers import CreateUser

"""
создать уникального пользователя;
создать пользователя, который уже зарегистрирован;
создать пользователя и не заполнить одно из обязательных полей.
"""


class TestUserRegistration:
    @allure.title("Тест создание уникального пользователя")
    def test_create_uniq_user(self):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=CreateUser.create_user())
        assert response.status_code == 200, f"Запрос с ошибкой, статус код {response.status_code}"

    @allure.title("Тест создание пользователя, который уже зарегистрирован")
    def test_creating_user_who_is_already_registered(self):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=TestDataCreateUser.user_exist)
        assert response.status_code == 403, f"Запрос с ошибкой, статус код {response.status_code}"
        assert response.json()[
                   "message"] == "User already exists", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому"

    @allure.title("Тест создание пользователя и не заполнить одно из обязательных полей.")
    def test_creating_user_abd_not_filling_out_one_field(self):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL,
                                 data=TestDataCreateUser.create_user_without_one_required_field)
        assert response.status_code == 403, f"Запрос с ошибкой, статус код {response.status_code}"
        assert response.json()[
                   "message"] == "Email, password and name are required fields", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому"
