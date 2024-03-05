import allure
from helpers.user_helpers import UserHelpers


class TestUserRegistration:
    @allure.title("Создание пользователя")
    def test_create_uniq_user(self):
        response_raw = UserHelpers().reg_user()
        email = response_raw.json()["user"]["email"]
        name = response_raw.json()["user"]["name"]
        access_token = response_raw.json()["accessToken"]
        refresh_token = response_raw.json()["refreshToken"]
        assert response_raw.status_code == 200, f"Запрос с ошибкой, статус код {response_raw.status_code}"
        assert response_raw.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}},' \
                                f'"accessToken":"{access_token}","refreshToken":"{refresh_token}"}}'

    @allure.title("Регистрация пользователя, который уже зарегистрирован")
    def test_creating_user_who_is_already_registered(self):
        response_raw = UserHelpers().reg_exist_user()
        assert response_raw.status_code == 403, f"Запрос с ошибкой, статус код {response_raw.status_code}"
        assert response_raw.json()[
                   "message"] == "User already exists", f"Текст сообщения {response_raw.json()['message']} не соответствует ожидаемому"

    @allure.title("Регистрация пользователя, и не заполнение одного из обязательных полей.")
    def test_creating_user_and_not_filling_out_one_field(self):
        response_raw = UserHelpers().reg_user_without_one_need_field()
        assert response_raw.status_code == 403, f"Запрос с ошибкой, статус код {response_raw.status_code}"
        assert response_raw.json()[
                   "message"] == "Email, password and name are required fields", f"Текст сообщения {response_raw.json()['message']} не соответствует ожидаемому"
