import pytest
import requests
from data.data import TestDataUrl
from helpers.helpers import User


@pytest.fixture(scope='session')
def create_user_delete_user():
    try:
        new_user = User.create_user()
        response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=new_user)
        response.raise_for_status()  # Проверяем статус ответа
        access_token = response.json().get("accessToken")  # Получаем токен доступа, если он есть
        assert access_token, "Не удалось получить токен доступа из ответа сервера"
        yield response, new_user, access_token
    except Exception as e:
        pytest.fail(f"Ошибка при создании пользователя: {e}")
    finally:
        try:
            requests.delete(url=TestDataUrl.AUTH_USER_URL, headers={'Authorization': access_token})
        except Exception as e:
            pytest.fail(f"Ошибка при удалении пользователя: {e}")

