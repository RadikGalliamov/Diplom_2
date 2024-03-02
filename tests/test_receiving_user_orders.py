import allure
from helpers.orders_helpers import OrdersHelpers


class TestReceivingUserOrders:
    @allure.title("Получение списка заказов пользователя с авторизацией")
    def test_receiving_user_orders_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        get_user_orders = OrdersHelpers()
        response_raw = get_user_orders.get_orders_list(token=access_token)
        orders = response_raw.json()['orders']
        total = response_raw.json()['total']
        total_today = response_raw.json()['totalToday']
        assert response_raw.status_code == 200, f"Ожидался код 200, но получен {response_raw.status_code}"
        assert response_raw.text == f'{{"success":true,"orders":{orders},"total":{total},"totalToday":{total_today}}}'

    @allure.title('Получение списка заказов пользователя без авторизации')
    def test_get_orders_for_non_authorized_user(self):
        get_user_orders = OrdersHelpers()
        response_raw = get_user_orders.get_orders_list()
        assert response_raw.status_code == 401
        assert response_raw.text == '{"success":false,"message":"You should be authorised"}'
