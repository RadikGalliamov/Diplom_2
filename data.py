import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_email():
    login = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    domain = random.choice(['ya.ru', 'yandex.ru', 'mail.ru', 'gmail.com'])
    email = login + '@' + domain
    return email


class TestDataUrl:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
    CREATE_USER_URL = f"{BASE_URL}auth/register"
    AUTHORIZATION_URL = f"{BASE_URL}auth/login"
    AUTH_USER_URL = f"{BASE_URL}auth/user"
    CREATE_ORDER_URL = f"{BASE_URL}orders"
    DELETE_USER_URL = f"{CREATE_USER_URL}/user"


class TestDataUser:
    user_exist = {
        "email": "user_for_stellar@yandex.ru",
        "password": "12345678",
        "name": "Userfortest2024"
    }

    create_user_without_one_required_field = {

        "password": "12345678",
        "name": "Userfortest2024"
    }

    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generate_email():
        login = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        domain = random.choice(['ya.ru', 'yandex.ru', 'mail.ru', 'gmail.com'])

        email = login + '@' + domain
        return email


class TestDataLogin:
    user_does_not_exist = {
        "email": "not_exist_user_for_stellar@yandex.ru",
        "password": "12345678"
    }

    valid_user_with_incorrect_password = {
        "email": "user12_for_stellar@yandex.ru",
        "password": "123456789"
    }


class TestCreateOrderData:
    ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6e"]
    }
    invalid_ingredient_hash = {
        "ingredients": ["61c0c5a71d1fbdaaa70231324324244"]
    }
    no_ingredients = {
        "ingredients": []
    }
