import allure
from helpers.user_helpers import UserHelpers


class TestChangingUserData:
    @allure.title("Изменение данных авторизованного пользователя")
    def test_changing_user_data_with_authorization(self, create_user_delete_user):
        response_raw = UserHelpers().patch_user_data(create_user_delete_user)
        email = response_raw.json()['user']['email']
        name = response_raw.json()['user']['name']
        assert response_raw.status_code == 200, f"Ожидался код 200, но получен {response_raw.status_code}"
        assert response_raw.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self):
        response_raw = UserHelpers().patch_user_data_without_token()
        assert response_raw.status_code == 401, f"Ожидался код 400, но получен {response_raw.status_code}"
        assert response_raw.text == '{"success":false,"message":"You should be authorised"}'
