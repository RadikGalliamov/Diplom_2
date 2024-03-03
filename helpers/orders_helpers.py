import allure
from typing import Optional
from data import TestDataUrl, TestCreateOrderData
from helpers.base_methods import BaseApi


class OrdersHelpers(BaseApi):
    def __init__(self):
        super().__init__()
        self.orders_url = TestDataUrl.CREATE_ORDER_URL

    @allure.step("Получить список заказов")
    def get_orders_list(self, token: Optional[str] = None):
        try:
            return self.get(url=self.orders_url, token=token)
        except Exception as e:
            allure.attach(f"Ошибка при получении списка заказов: {e}", name="RequestException")
            raise

    @allure.step("Создать заказ c ингредиентами")
    def create_order(self, token: Optional[str] = None):
        try:
            return self.post(url=self.orders_url, json=TestCreateOrderData.ingredients, token=token)
        except Exception as e:
            allure.attach(f"Ошибка при создании заказа c ингредиентами: {e}", name="RequestException")
            raise

    @allure.step("Создать заказ без ингредиентов")
    def create_order_no_ingredient(self, token: Optional[str] = None):
        try:
            return self.post(url=self.orders_url, json=TestCreateOrderData.no_ingredients, token=token)
        except Exception as e:
            allure.attach(
                f"Ошибка при создании заказа без ингредиентов: {e}", name="RequestException")
            raise

    @allure.step("Создать заказ с неверным хешем ингредиентов")
    def create_order_without_invalid_hash(self, token: Optional[str] = None):
        try:
            return self.post(url=self.orders_url, json=TestCreateOrderData.invalid_ingredient_hash, token=token)
        except Exception as e:
            allure.attach(
                f"Ошибка при создании заказа с неверным хешем ингредиентов: {e}", name="RequestException")
            raise
