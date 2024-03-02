import allure
from helpers.orders_helpers import OrdersHelpers


class TestCreateOrder:
    @allure.title("Cоздание заказа авторизированным пользователем")
    def test_create_order_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        order_helpers = OrdersHelpers()
        response_raw = order_helpers.create_order(token=access_token)
        assert response_raw.status_code == 200, f"Ожидался код 200, но получен {response_raw.status_code}"

    @allure.title("Создание заказа не авторизированным пользователем")
    def test_create_order_without_authorization(self):
        order_helpers = OrdersHelpers()
        response_raw = order_helpers.create_order()
        name = response_raw.json()['name']
        order_number = response_raw.json()["order"]["number"]
        assert response_raw.status_code == 200, f"Ожидался код 200, но получен {response_raw.status_code}"
        assert response_raw.text == f'{{"success":true,"name":"{name}","order":{{"number":{order_number}}}}}'

    @allure.title("Cоздание заказа без ингредиентами не авторизированным пользователем")
    def test_create_order_with_ingredients(self):
        order_helpers = OrdersHelpers()
        response_raw = order_helpers.create_order_no_ingredient()
        assert response_raw.status_code == 400, f"Ожидался код 400, но получен {response_raw.status_code}"
        assert response_raw.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title("Создание заказа без ингредиентов авторизированным пользователем")
    def test_create_order_without_ingredients(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        order_helpers = OrdersHelpers()
        response_raw = order_helpers.create_order_no_ingredient(token=access_token)
        assert response_raw.status_code == 400, f"Ожидался код 400, но получен {response_raw.status_code}"
        assert response_raw.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title("Невозможность создать заказ с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        order_helpers = OrdersHelpers()
        response_raw = order_helpers.create_order_without_invalid_hash(token=access_token)
        assert response_raw.status_code == 500, f"Ожидался код 500, но получен {response_raw.status_code}"

