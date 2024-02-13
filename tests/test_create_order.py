import allure
import requests
from data import TestDataUrl, TestCreateOrderData


class TestCreateOrder:
    @allure.title("Cоздание заказа авторизированным пользователем")
    def test_create_order_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers={
                "Authorization": access_token})
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"

    @allure.title("Создание заказа не авторизированным пользователем")
    def test_create_order_without_authorization(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.ingredients, headers=None)
        name = response.json()['name']
        order_number = response.json()["order"]["number"]
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.text == f'{{"success":true,"name":"{name}","order":{{"number":{order_number}}}}}'

    @allure.title("Cоздание заказа без ингредиентами не авторизированным пользователем")
    def test_create_order_with_ingredients(self):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.no_ingredients, headers=None)
        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title("Создание заказа без ингредиентов авторизированным пользователем")
    def test_create_order_without_ingredients(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.no_ingredients, headers=None)
        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title("Невозможность создать заказ с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, create_user_delete_user):
        response = requests.post(
            url=TestDataUrl.CREATE_ORDER_URL, json=TestCreateOrderData.invalid_ingredient_hash, headers=None)
        assert response.status_code == 500, f"Ожидался код 500, но получен {response.status_code}"

