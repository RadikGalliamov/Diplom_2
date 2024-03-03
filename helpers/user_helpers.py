import allure

from conftest import create_user_delete_user
from data import TestDataUrl, TestDataLogin, TestDataCreateUser
from helpers.base_methods import BaseApi
from helpers.helpers import CreateUser


class UserHelpers(BaseApi):
    def __init__(self):
        super().__init__()
        self.users_url = TestDataUrl.AUTHORIZATION_URL
        self.create_user_url = TestDataUrl.CREATE_USER_URL
        self.changing_data_user_url = TestDataUrl.AUTH_USER_URL

    @allure.step("Авторизация пользователя")
    def auth_user(self, data=None, token=None):
        try:
            return self.post(url=self.users_url, json=data, token=token)
        except Exception as e:
            allure.attach(f"Ошибка при получении списка заказов: {e}", name="RequestException")
            raise

    @allure.step("Авторизация c неверным логином")
    def auth_user_without_invalid_login(self, token=None):
        try:
            return self.post(url=self.users_url, json=TestDataLogin.user_does_not_exist, token=token)
        except Exception as e:
            allure.attach(f"Ошибка при получении списка заказов: {e}", name="RequestException")
            raise

    @allure.step("Авторизация c неверным логином и неверным паролем")
    def auth_user_without_invalid_login_and_password(self, token=None):
        try:
            return self.post(url=self.users_url, json=TestDataLogin.valid_user_with_incorrect_password, token=token)
        except Exception as e:
            allure.attach(f"Ошибка при получении списка заказов: {e}", name="RequestException")
            raise

    @allure.step("Получить логин и пароль из ответа фикстуры create_user_delete_user")
    def get_email_password_user(self, create_user_delete_user):
        try:
            email_password = {"email": create_user_delete_user[1]["email"],
                              "password": create_user_delete_user[1]["password"]}
            return email_password
        except Exception as e:
            allure.attach(f"Ошибка при получении списка заказов: {e}", name="RequestException")
            raise

    @allure.step("Создание уникального пользователя в системе")
    def create_user(self):
        try:
            random_user = CreateUser.create_user()
            return random_user
        except Exception as e:
            allure.attach(f"Ошибка при получении списка заказов: {e}", name="RequestException")
            raise

    @allure.step("Регистрация пользователя в системе")
    def reg_user(self, token=None):
        try:
            return self.post(url=self.create_user_url, json=self.create_user(), token=token)
        except Exception as e:
            allure.attach(f"Ошибка при регистрации пользователя в системе: {e}", name="RequestException")
            raise

    @allure.step("Регистрация пользователя уже существующего в системе")
    def reg_exist_user(self, token=None):
        try:
            add_user = self.create_user()
            self.post(url=self.create_user_url, json=add_user, token=token)
            return self.post(url=self.create_user_url, json=add_user, token=token)
        except Exception as e:
            allure.attach(
                f"Ошибка при регистрации пользователя уже существующего в системе: {e}", name="RequestException")
            raise

    @allure.step("Регистрация пользователя в системе без одного из обязательных полей")
    def reg_user_without_one_need_field(self, token=None):
        try:
            return self.post(
                url=self.create_user_url, json=TestDataCreateUser.create_user_without_one_required_field, token=token)
        except Exception as e:
            allure.attach(
                f"Ошибка при регистрация пользователя в системе без одного из обязательных полей: {e}", name="RequestException")
            raise

    @allure.step("Изменение данных авторизованного пользователя в системе")
    def patch_user_data(self, create_user_delete_user):
        try:
            data_for_update = CreateUser.user_update()
            access_token = create_user_delete_user[2]
            return self.patch(url=self.changing_data_user_url, json=data_for_update, token=access_token)
        except Exception as e:
            allure.attach(
                f"Ошибка при изменение данных авторизованного пользователя в системе: {e}", name="RequestException")
            raise

    @allure.step("Изменение данных авторизованного пользователя в системе без токена")
    def patch_user_data_without_token(self):
        try:
            data_for_update = CreateUser.user_update()
            return self.patch(url=self.changing_data_user_url, json=data_for_update, token=None)
        except Exception as e:
            allure.attach(
                f"Ошибка при изменение данных авторизованного пользователя в системе без токена: {e}", name="RequestException")
            raise
