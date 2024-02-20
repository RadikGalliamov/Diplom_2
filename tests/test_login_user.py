import allure
import requests
from data import TestDataUrl, TestDataLogin


class TestLoginUser:
    @allure.title("Авторизация существующего в системе пользователя")
    def test_login_user(self, create_user_delete_user):
        """Из объекта фикстуры create_user_delete_user возьмем почту и пароль для логина"""
        new_user = {"email": create_user_delete_user[1]["email"],
                    "password": create_user_delete_user[1]["password"]}
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, new_user)
        email = response.json()["user"]["email"]
        name = response.json()["user"]["name"]
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.text == f'{{"success":true,"accessToken":"{access_token}","refreshToken":"{refresh_token}",' \
                                f'"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Тест авторизация с неверным логином")
    def test_login_with_incorrect_login(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.user_does_not_exist)
        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()[
                   "message"] == "email or password are incorrect", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому 'email or password are incorrect'"
        assert response.json()[
                   "success"] == False, f"Текст сообщения {response.json()['success']} не соответствует ожидаемому 'false'"

    @allure.title("Тест авторизация с верным логином и неверным паролем")
    def test_login_with_correct_login_and_incorrect_password(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.valid_user_with_incorrect_password)
        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()[
                   "message"] == "email or password are incorrect", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому 'email or password are incorrect'"
        assert response.json()[
                   "success"] == False, f"Текст сообщения {response.json()['success']} не соответствует ожидаемому 'false'"
