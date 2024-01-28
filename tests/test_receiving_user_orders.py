import allure
import requests
from data import TestDataUrl, TestCreateOrderData

"""
авторизованный пользователь,
неавторизованный пользователь.
"""


class TestReceivingUserOrders:
    @allure.title("Тест получение заказов пользователя с авторизацией")
    def test_receiving_user_orders_with_authorization(self, create_user_delete_user):
        access_token = create_user_delete_user[2]
        response = requests.get(
            url=TestDataUrl.CREATE_ORDER_URL, headers={"Authorization": access_token})
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"