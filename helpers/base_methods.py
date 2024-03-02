import allure
import requests
import json


class BaseApi:
    @staticmethod
    @allure.title("GET")
    def get(url=None, token=None):
        try:
            response = requests.get(url=url, headers={"Authorization": token})
        except AssertionError as e:
            # Обработка ошибки, если она произошла
            print(f"Тест завершился с ошибкой: {e}")
        return response

    @staticmethod
    @allure.title("GET_ID")
    def get_id(url=None, id=None, token=None):
        try:
            response = requests.get(f"{url}{id}", headers={"Authorization": token})
        except AssertionError as e:
            # Обработка ошибки, если она произошла
            print(f"Тест завершился с ошибкой: {e}")
        return response

    @staticmethod
    @allure.title("POST")
    def post(url, json=None, data=None, token=None):
        try:
            response = requests.post(url=url, json=json, data=data, headers={"Authorization": token})
        except AssertionError as e:
            # Обработка ошибки, если она произошла
            print(f"Тест завершился с ошибкой: {e}")
        return response

    @staticmethod
    @allure.title("PUT")
    def put(url, id=None, data=None, token=None):
        try:
            response = requests.put(f"{url}{id}", json=data, headers={"Authorization": token})
        except AssertionError as e:
            # Обработка ошибки, если она произошла
            print(f"Тест завершился с ошибкой: {e}")
        return response

    @staticmethod
    @allure.title("DELETE")
    def delete(url=None, id=None, token=None):
        try:
            response = requests.delete(f"{url}{id}", headers={"Authorization": token})
        except AssertionError as e:
            # Обработка ошибки, если она произошла
            print(f"Тест завершился с ошибкой: {e}")
        return response

    @staticmethod
    @allure.title("PUT-SEND")
    def put_send(url, data=None, token=None):
        try:
            response = requests.put(f"{url}", json=data, headers={"Authorization": token})
        except AssertionError as e:
            # Обработка ошибки, если она произошла
            print(f"Тест завершился с ошибкой: {e}")
        return response

    @staticmethod
    @allure.title("PATCH")
    def patch(url, json=None, token=None):
        try:
            response = requests.patch(url=url, json=json, headers={"Authorization": token})
        except AssertionError as e:
            # Обработка ошибки, если она произошла
            print(f"Тест завершился с ошибкой: {e}")
        return response