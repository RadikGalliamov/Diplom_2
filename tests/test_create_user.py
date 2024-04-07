import allure
import pytest

from checks.check_functions import CheckUser
from helpers.helpers import User
from helpers.user_helpers import UserHelpers
from data.data import TestDataUser as dtu


class TestUserRegistration:
    @allure.title("Создание пользователя")
    def test_create_uniq_user(self):
        random_user = User.create_user()
        response_raw = UserHelpers().reg_user(json=random_user)
        check_response = CheckUser(status_code=200, email=random_user["email"], name=random_user["name"])
        check_response.check_status_code(response=response_raw)
        check_response.assert_schema_is_valid(
            response=response_raw.json(), schema=check_response.body_user_schema())


class TestUserRegistrationNegative:
    @allure.title("Регистрация пользователя, который уже зарегистрирован")
    def test_creating_user_who_is_already_registered(self):
        response_raw = UserHelpers().reg_exist_user()
        check_response = CheckUser(status_code=403, error_msg="User already exists")
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(
            response=response_raw.json(), schema=check_response.error_user_already_exists_shema())

    @allure.title("Создание пользователя без обязательных полей")
    @pytest.mark.parametrize("email, password, name", [[None, dtu.generate_email(), dtu.generate_random_string(4)],
                                                       [dtu.generate_email(), None, dtu.generate_random_string(4)],
                                                       [dtu.generate_email(), dtu.generate_random_string(), None]],
                             ids=["Empty email", "Empty password", "Empty name"])
    def test_create_user_with_empty_fields(self, email, password, name):
        user = User(email, password, name)
        response_raw = UserHelpers().reg_user(json=user.data)
        check_response = CheckUser(status_code=403, error_msg="Email, password and name are required fields")
        check_response.check_status_code(response=response_raw)
        check_response.assert_schema_is_valid(
            response=response_raw.json(), schema=check_response.error_not_field_shema())
