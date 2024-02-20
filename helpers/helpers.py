import allure
from faker import Faker


class CreateUser:
    @staticmethod
    @allure.step("Создать рандомного пользователя")
    def create_user():
        fake = Faker()
        user_random = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.user_name()
        }
        return user_random

    @staticmethod
    @allure.step("Создать данные для обновления")
    def user_update():
        fake = Faker()
        user_update = {
            "email": fake.email(),
            "name": fake.user_name()
        }
        return user_update
