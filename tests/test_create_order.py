import allure
import requests
from data import TestDataUrl, TestCreateOrderData

"""
Создание заказа:
с авторизацией,
без авторизации,
с ингредиентами,
без ингредиентов,
с неверным хешем ингредиентов.
"""


class TestCreateOrder:
    @allure.title("Тест создание заказа с авторизацией")
    def test_create_order_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers={
                "Authorization": access_token})
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert "name" in response.json(), "Поля 'name' нет в теле ответа"
        assert "order" in response.json(), "Поля 'order' нет в теле ответа"
        assert "number" in response.json()['order'], "Поля 'number' нет в словаре 'order' теле ответа"

        # assert response["success"] == True, f"Значение поля 'success' {response['success']} вместо 'True'"
        # assert "accessToken" in response_body, "Поля accessToken нет в теле ответа"
        # assert response_body["accessToken"] != "", "Поле 'accessToken' пустое"
        # assert "refreshToken" in response_body, "Поля refreshToken нет в теле ответа"
        # assert response_body["refreshToken"] != "", "Поле 'refreshToken' пустое"
        # assert "user" in response_body, "Поля user нет в теле ответа"
        # assert "email" in response_body["user"], "Поля email нет в словаре user тела ответа"
        # assert "name" in response_body["user"], "Поля name нет в словаре user тела ответа"

    @allure.title("Тест создание заказа без авторизацией")
    def test_create_order_without_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers=None)
        assert response.status_code == 403, f"Ожидался код 403, но получен {response.status_code}"
        assert "name" in response.json(), "Поля 'name' нет в теле ответа"
        assert "order" in response.json(), "Поля 'order' нет в теле ответа"
        assert "number" in response.json()['order'], "Поля 'number' нет в словаре 'order' теле ответа"
        # добавить проверки

    @allure.title("Тест создание заказа с ингредиентами")  # доделать
    def test_create_order_without_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers=None)
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert "name" in response.json(), "Поля 'name' нет в теле ответа"
        assert "order" in response.json(), "Поля 'order' нет в теле ответа"
        assert "number" in response.json()['order'], "Поля 'number' нет в словаре 'order' теле ответа"

    @allure.title("Тест создание заказа без ингредиентов")  # доделать
    def test_create_order_without_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers=None)
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert "name" in response.json(), "Поля 'name' нет в теле ответа"
        assert "order" in response.json(), "Поля 'order' нет в теле ответа"
        assert "number" in response.json()['order'], "Поля 'number' нет в словаре 'order' теле ответа"

    @allure.title("Тест создание заказа с неверным хешем ингредиентов")  # доделать
    def test_create_order_without_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers=None)
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert "name" in response.json(), "Поля 'name' нет в теле ответа"
        assert "order" in response.json(), "Поля 'order' нет в теле ответа"
        assert "number" in response.json()['order'], "Поля 'number' нет в словаре 'order' теле ответа"
