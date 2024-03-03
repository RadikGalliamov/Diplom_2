import allure
import requests
from typing import Optional, Dict, Any


class BaseApi:
    @staticmethod
    @allure.title("GET")
    def get(url: str = None, token: str = None) -> requests.Response:
        try:
            response = requests.get(url=url, headers={"Authorization": token})
            r"""Sends a GET request.

            :param url: URL for the new :class:`Request` object.
            :param params: (optional) Dictionary, list of tuples or bytes to send
                in the query string for the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        except requests.RequestException as e:
            allure.attach(str(e), name="RequestException")  # Логируем ошибку
            raise  # Перевызываем исключение для корректного отображения в отчете
        return response

    @staticmethod
    @allure.title("GET_ID")
    def get_id(url: str = None, token: str = None) -> requests.Response:
        try:
            response = requests.get(f"{url}{id}", headers={"Authorization": token})
            r"""Sends a GET request.

            :param url: URL for the new :class:`Request` object.
            :param params: (optional) Dictionary, list of tuples or bytes to send
                in the query string for the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        except requests.RequestException as e:
            allure.attach(str(e), name="RequestException")  # Логируем ошибку
            raise  # Перевызываем исключение для корректного отображения в отчете
        return response

    @staticmethod
    @allure.title("POST")
    def post(url: str, json: Optional[Dict[str, Any]] = None, data: Any = None, token: str = None) -> requests.Response:
        try:
            response = requests.post(url=url, json=json, data=data, headers={"Authorization": token})
            r"""Sends a POST request.

            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        except requests.RequestException as e:
            allure.attach(str(e), name="RequestException")  # Логируем ошибку
            raise  # Перевызываем исключение для корректного отображения в отчете
        return response

    @staticmethod
    @allure.title("PUT")
    def put(url: str, id: str, data: Any = None, token: str = None) -> requests.Response:
        try:
            response = requests.put(f"{url}{id}", json=data, headers={"Authorization": token})
            r"""Sends a PUT request.

            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        except requests.RequestException as e:
            allure.attach(str(e), name="RequestException")  # Логируем ошибку
            raise  # Перевызываем исключение для корректного отображения в отчете
        return response

    @staticmethod
    @allure.title("DELETE")
    def delete(url: str, id: str, token: str = None) -> requests.Response:
        try:
            response = requests.delete(f"{url}{id}", headers={"Authorization": token})
            r"""Sends a DELETE request.

            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        except requests.RequestException as e:
            allure.attach(str(e), name="RequestException")  # Логируем ошибку
            raise  # Перевызываем исключение для корректного отображения в отчете
        return response

    @staticmethod
    @allure.title("PUT-SEND")
    def put_send(url: str, data: Any = None, token: str = None) -> requests.Response:
        try:
            response = requests.put(f"{url}", json=data, headers={"Authorization": token})
            r"""Sends a PUT request.

            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        except requests.RequestException as e:
            allure.attach(str(e), name="RequestException")  # Логируем ошибку
            raise  # Перевызываем исключение для корректного отображения в отчете
        return response

    @staticmethod
    @allure.title("PATCH")
    def patch(url: str, json: Optional[Dict[str, Any]] = None, token: str = None) -> requests.Response:
        try:
            response = requests.patch(url=url, json=json, headers={"Authorization": token})
            r"""Sends a PATCH request.

            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        except requests.RequestException as e:
            allure.attach(f"Ошибка при выполнении метода POST {e}", name="RequestException")  # Логируем ошибку
            raise  # Перевызываем исключение для корректного отображения в отчете
        return response
