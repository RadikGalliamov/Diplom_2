import allure
import requests

from data import TestDataUrl, TestDataCreateUser
from helpers.helpers import CreateUser


class TestUserRegistration:
    @allure.title("Регистрация пользователя")
    def test_create_uniq_user(self):
        random_data_for_create_user = CreateUser.create_user()
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=random_data_for_create_user)
        email = response.json()["user"]["email"]
        name = response.json()["user"]["name"]
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200, f"Запрос с ошибкой, статус код {response.status_code}"
        assert response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}},' \
                                f'"accessToken":"{access_token}","refreshToken":"{refresh_token}"}}'

    @allure.title("Регистрация пользователя, который уже зарегистрирован")
    def test_creating_user_who_is_already_registered(self):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=TestDataCreateUser.user_exist)
        assert response.status_code == 403, f"Запрос с ошибкой, статус код {response.status_code}"
        assert response.json()[
                   "message"] == "User already exists", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому"

    @allure.title("Регистрация пользователя, и не заполнение одного из обязательных полей.")
    def test_creating_user_abd_not_filling_out_one_field(self):
        response = requests.post(url=TestDataUrl.CREATE_USER_URL,
                                 data=TestDataCreateUser.create_user_without_one_required_field)
        assert response.status_code == 403, f"Запрос с ошибкой, статус код {response.status_code}"
        assert response.json()[
                   "message"] == "Email, password and name are required fields", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому"
