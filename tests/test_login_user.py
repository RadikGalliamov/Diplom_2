import allure
from conftest import create_user_delete_user
from checks.check_functions import CheckAuthorization
from helpers.user_helpers import UserHelpers


class TestLoginUser:
    @allure.title("Авторизация существующего в системе пользователя")
    def test_login_user(self, create_user_delete_user):
        email_password_user = UserHelpers().get_email_password_user(create_user_delete_user)
        response_raw = UserHelpers().auth_user(email_password_user)
        check_response = CheckAuthorization(status_code=200)
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(response_raw.json(), check_response.body_authorization_schema())
        email = response_raw.json()["user"]["email"]
        name = response_raw.json()["user"]["name"]
        access_token = response_raw.json()["accessToken"]
        refresh_token = response_raw.json()["refreshToken"]
        assert response_raw.status_code == 200, f"Ожидался код 200, но получен {response_raw.status_code}"
        assert response_raw.text == f'{{"success":true,"accessToken":"{access_token}","refreshToken":"{refresh_token}",' \
                                    f'"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Тест авторизация с неверным логином")
    def test_login_with_incorrect_login(self):
        response_raw = UserHelpers().auth_user_without_invalid_login()
        check_response = CheckAuthorization(status_code=401)
        check_response.check_status_code(response_raw)
        check_response.error_shema()

    @allure.title("Тест авторизация с верным логином и неверным паролем")
    def test_login_with_correct_login_and_incorrect_password(self):
        response_raw = UserHelpers().auth_user_without_invalid_login_and_password()
        check_response = CheckAuthorization(status_code=401)
        check_response.check_status_code(response_raw)
        check_response.error_shema()
