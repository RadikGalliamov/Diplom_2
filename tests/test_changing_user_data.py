import allure
import requests
from data import TestDataUrl
from helpers.helpers import CreateUser


class TestChangingUserData:
    @allure.title("Изменение данных авторизованного пользователя")
    def test_changing_user_data_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        data_for_update = CreateUser.user_update()
        response = requests.patch(
            url=TestDataUrl.AUTH_USER_URL, json=data_for_update, headers={
                "Authorization": access_token})
        email = response.json()['user']['email']
        name = response.json()['user']['name']
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self, create_user_delete_user):
        data_for_update = CreateUser.user_update()
        response = requests.patch(
            url=TestDataUrl.AUTH_USER_URL, json=data_for_update, headers=None)
        assert response.status_code == 401, f"Ожидался код 400, но получен {response.status_code}"
        assert response.text == '{"success":false,"message":"You should be authorised"}'
