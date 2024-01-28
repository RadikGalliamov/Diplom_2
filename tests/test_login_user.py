import allure
import requests
from data import TestDataUrl, TestDataLogin

"""
логин под существующим пользователем,
логин с неверным логином и паролем.
"""


class TestLoginUser:
    @allure.title("Тест авторизация под существующим пользователем")
    def test_login_user(self, create_user_delete_user):
        """Из объекта фикстуры create_user_delete_user возьмем почту и пароль для логина"""
        new_user = {"email": create_user_delete_user[1]["email"],
                    "password": create_user_delete_user[1]["password"]}
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, new_user)
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        response_body = response.json()
        assert response_body["success"] == True, f"Значение поля 'success' {response_body['success']} вместо 'True'"
        assert "accessToken" in response_body, "Поля accessToken нет в теле ответа"
        assert response_body["accessToken"] != "", "Поле 'accessToken' пустое"
        assert "refreshToken" in response_body, "Поля refreshToken нет в теле ответа"
        assert response_body["refreshToken"] != "", "Поле 'refreshToken' пустое"
        assert "user" in response_body, "Поля user нет в теле ответа"
        assert "email" in response_body["user"], "Поля email нет в словаре user тела ответа"
        assert "name" in response_body["user"], "Поля name нет в словаре user тела ответа"
        assert response_body["user"]["email"] == new_user[
            "email"], f"Значение поля 'email' {response_body['user']['email']}, не соотвествует ожидаемому {new_user['email']}"

    @allure.title("Тест авторизация с неверным логином")
    def test_login_with_incorrect_login(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.user_does_not_exist)
        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому 'email or password are incorrect'"
        assert response.json()["success"] == False, f"Текст сообщения {response.json()['success']} не соответствует ожидаемому 'false'"

    @allure.title("Тест авторизация с верным логином и неверным паролем")
    def test_login_with_correct_login_and_incorrect_password(self):
        response = requests.post(TestDataUrl.AUTHORIZATION_URL, TestDataLogin.valid_user_with_incorrect_password)
        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect", f"Текст сообщения {response.json()['message']} не соответствует ожидаемому 'email or password are incorrect'"
        assert response.json()["success"] == False, f"Текст сообщения {response.json()['success']} не соответствует ожидаемому 'false'"