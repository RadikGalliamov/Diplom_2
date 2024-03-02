import allure
from helpers.user_helpers import UserHelpers


class TestLoginUser:
    @allure.title("Авторизация существующего в системе пользователя")
    def test_login_user(self, create_user_delete_user):
        user_helpers = UserHelpers()
        email_password_user = user_helpers.get_email_password_user(create_user_delete_user)
        response_raw = user_helpers.auth_user(email_password_user)
        email = response_raw.json()["user"]["email"]
        name = response_raw.json()["user"]["name"]
        access_token = response_raw.json()["accessToken"]
        refresh_token = response_raw.json()["refreshToken"]
        assert response_raw.status_code == 200, f"Ожидался код 200, но получен {response_raw.status_code}"
        assert response_raw.text == f'{{"success":true,"accessToken":"{access_token}","refreshToken":"{refresh_token}",' \
                                    f'"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Тест авторизация с неверным логином")
    def test_login_with_incorrect_login(self):
        user_helpers = UserHelpers()
        response_raw = user_helpers.auth_user_without_invalid_login()
        assert response_raw.status_code == 401, f"Ожидался код 401, но получен {response_raw.status_code}"
        assert response_raw.json()[
                   "message"] == "email or password are incorrect", f"Текст сообщения {response_raw.json()['message']} не соответствует ожидаемому 'email or password are incorrect'"
        assert response_raw.json()[
                   "success"] == False, f"Текст сообщения {response_raw.json()['success']} не соответствует ожидаемому 'false'"

    @allure.title("Тест авторизация с верным логином и неверным паролем")
    def test_login_with_correct_login_and_incorrect_password(self):
        user_helpers = UserHelpers()
        response_raw = user_helpers.auth_user_without_invalid_login_and_password()
        assert response_raw.status_code == 401, f"Ожидался код 401, но получен {response_raw.status_code}"
        assert response_raw.json()[
                   "message"] == "email or password are incorrect", f"Текст сообщения {response_raw.json()['message']} не соответствует ожидаемому 'email or password are incorrect'"
        assert response_raw.json()[
                   "success"] == False, f"Текст сообщения {response_raw.json()['success']} не соответствует ожидаемому 'false'"
