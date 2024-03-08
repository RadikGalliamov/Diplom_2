import allure
from faker import Faker


class User:
    def __init__(self, email=None, password=None, name=None):
        self.data = {
            'email': email,
            'password': password,
            'name': name
        }

    @classmethod
    @allure.step("Создать рандомного пользователя")
    def create_user(cls):
        fake = Faker()
        user_random = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.user_name()
        }
        return user_random

    @classmethod
    @allure.step("Создать данные для обновления")
    def user_update(cls):
        fake = Faker()
        user_update = {
            "email": fake.email(),
            "name": fake.user_name()
        }
        return user_update
