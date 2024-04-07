import allure

from checks.check_functions import CheckOrder
from helpers.orders_helpers import OrdersHelpers
from conftest import create_user_delete_user


class TestReceivingUserOrders:
    @allure.title("Получение списка заказов пользователя с авторизацией")
    def test_receiving_user_orders_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response_raw = OrdersHelpers().get_orders_list(token=access_token)
        check_response = CheckOrder(status_code=200)
        check_response.check_status_code(response_raw)
        orders = response_raw.json()['orders']
        total = response_raw.json()['total']
        total_today = response_raw.json()['totalToday']
        assert response_raw.text == f'{{"success":true,"orders":{orders},"total":{total},"totalToday":{total_today}}}'

    @allure.title('Получение списка заказов пользователя без авторизации')
    def test_get_orders_for_non_authorized_user(self):
        response_raw = OrdersHelpers().get_orders_list()
        check_response = CheckOrder(status_code=401, error_msg="You should be authorised")
        check_response.check_status_code(response_raw)
