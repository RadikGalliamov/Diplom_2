import pytest
import requests
from data import TestDataUrl
from helpers.helpers import CreateUser


@pytest.fixture
def create_user_delete_user():
    new_user = CreateUser.create_user()
    response = requests.post(url=TestDataUrl.CREATE_USER_URL, data=new_user)
    access_token = response.json()["accessToken"]
    yield response, new_user, access_token
    requests.delete(url=TestDataUrl.AUTH_USER_URL, headers={'Authorization': access_token})

