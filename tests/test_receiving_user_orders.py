import allure
import requests
from data import TestDataUrl


class TestReceivingUserOrders:
    @allure.title("Получение списка заказов пользователя с авторизацией")
    def test_receiving_user_orders_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response = requests.get(
            url=TestDataUrl.CREATE_ORDER_URL, headers={"Authorization": access_token})
        orders = response.json()['orders']
        total = response.json()['total']
        total_today = response.json()['totalToday']
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.text == f'{{"success":true,"orders":{orders},"total":{total},"totalToday":{total_today}}}'

    @allure.title('Получение списка заказов пользователя без авторизации')
    def test_get_orders_for_non_authorized_user(self):
        response = requests.get(url=TestDataUrl.CREATE_ORDER_URL)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
