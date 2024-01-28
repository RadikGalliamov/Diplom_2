import allure
import requests
from data import TestDataUrl
from helpers.helpers import CreateUser

"""
с авторизацией,
без авторизации,

Для обеих ситуаций нужно проверить, что любое поле можно изменить. 
Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
"""


class TestChangingUserData:
    @allure.title("Тест изменение данных пользователя с авторизацией")
    def test_changing_user_data_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        data_for_update = CreateUser.user_update()
        response = requests.patch(
            url=TestDataUrl.AUTH_USER_URL, json=data_for_update, headers={
                "Authorization": access_token})
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["user"]["email"] == data_for_update["email"]
        assert response.json()["user"]["name"] == data_for_update["name"]
        assert response.json()["success"] == True, f"Значение поля 'success' {response.json()['success']} вместо True"

    @allure.title("Тест изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self, create_user_delete_user):
        data_for_update = CreateUser.user_update()
        response = requests.patch(
            url=TestDataUrl.AUTH_USER_URL, json=data_for_update, headers=None)
        assert response.status_code == 401, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] == False, f"Значение поля 'success' {response.json()['success']} вместо 'False'"
        assert response.json()["message"] == "You should be authorised", "Значение поля message {response.json()['message'] вместо 'You should be authorised'}"

