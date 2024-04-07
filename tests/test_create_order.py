import allure
from conftest import create_user_delete_user
from checks.check_functions import CheckOrder
from helpers.orders_helpers import OrdersHelpers


class TestCreateOrder:
    @allure.title("Cоздание заказа авторизированным пользователем")
    def test_create_order_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response_raw = OrdersHelpers().create_order(token=access_token)
        check_response = CheckOrder(status_code=200)
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(response_raw.json(), check_response.body_order_schema())


class TestCreateOrderNegativ:
    @allure.title("Создание заказа не авторизированным пользователем")
    def test_create_order_without_authorization(self):
        order = OrdersHelpers()
        response_raw = order.create_order(token=None)
        check_response = CheckOrder(status_code=401, error_msg="You should be authorised")
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(response_raw.json(), check_response.error_shema())

    @allure.title("Cоздание заказа без ингредиентов не авторизированным пользователем")
    def test_create_order_with_ingredients(self):
        response_raw = OrdersHelpers().create_order_no_ingredient()
        check_response = CheckOrder(status_code=400, error_msg="Ingredient ids must be provided")
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(response_raw.json(), check_response.error_order_shema())

    @allure.title("Создание заказа без ингредиентов авторизированным пользователем")
    def test_create_order_without_ingredients(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response_raw = OrdersHelpers().create_order_no_ingredient(token=access_token)
        check_response = CheckOrder(status_code=400, error_msg="Ingredient ids must be provided")
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(response_raw.json(), check_response.body_order_schema())

    @allure.title("Невозможность создать заказ с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response_raw = OrdersHelpers().create_order_without_invalid_hash(token=access_token)
        check_response = CheckOrder(status_code=500, error_msg="Ingredient ids must be provided")
        check_response.check_status_code(response_raw)
        check_response.assert_schema_is_valid(response_raw.json(), check_response.body_order_schema())
