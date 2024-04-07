import allure

from checks.check_functions import CheckUser
from helpers.user_helpers import UserHelpers


class TestChangingUserData:
    # @allure.title("Изменение данных авторизованного пользователя")
    # def test_changing_user_data_with_authorization(self, create_user_delete_user):
    #     response_raw = UserHelpers().patch_user_data(token=create_user_delete_user)
    #     check_response = CheckUser(status_code=200, email=random_user["email"], name=random_user["name"])
    #
    #     check_response = CheckUser(status_code=200, email=create_new_user[0], name=name)
    #     check_response.check_status_code(response_raw)
    #     check_response.assert_schema_is_valid(response_raw.json(), check_response.body_user_schema())

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self):
        response_raw = UserHelpers().patch_user_data_without_token()
        check_response = CheckUser(status_code=401, error_msg="You should be authorised")
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(response_raw.json(), check_response.body_user_schema())
