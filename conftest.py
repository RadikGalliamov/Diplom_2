import pytest
import requests
from data import TestDataUrl
from helpers.helpers import CreateUser


@pytest.fixture
def create_user_delete_user():
    new_user = CreateUser.create_user()
    response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=new_user)
    assert response.status_code == 200, f"Запрос с ошибкой, статус код {response.status_code}"
    access_token = response.json()["accessToken"]
    yield response, new_user, access_token
    delete_new_user = requests.delete(url=TestDataUrl.AUTH_USER_URL, headers={'Authorization': access_token})
    assert delete_new_user.status_code == 202, f"Запрос с ошибкой, статус код {delete_new_user.status_code}"
