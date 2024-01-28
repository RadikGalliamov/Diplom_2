import random
import string


class TestDataUrl:
    BASE_URL = ""
    CREATE_USER_URL = "https://stellarburgers.nomoreparties.site/api/auth/register"
    AUTHORIZATION_URL = "https://stellarburgers.nomoreparties.site/api/auth/login"
    AUTH_USER_URL = "https://stellarburgers.nomoreparties.site/api/auth/user"
    CREATE_ORDER_URL = "https://stellarburgers.nomoreparties.site/api/orders"


class TestDataCreateUser:
    user_exist = {
        "email": "user_for_stellar@yandex.ru",
        "password": "12345678",
        "name": "Userfortest2024"
    }

    create_user_without_one_required_field = {

        "password": "12345678",
        "name": "Userfortest2024"
    }


class TestDataLogin:
    user_does_not_exist = {
        "email": "not_exist_user_for_stellar@yandex.ru",
        "password": "12345678"
    }

    valid_user_with_incorrect_password = {
        "email": "user12_for_stellar@yandex.ru",
        "password": "123456789"
    }


class TestDataChangingUserData:
    pass
    # random_numbers = ''.join(random.choices(string.digits, k=5))
    #
    # email = f"update_user_for_stellar{random_numbers}@yandex.ru"
    # name = f"update_user_for_stellar{random_numbers}"
    #
    # user_update = {
    #     "email": email,
    #     "name": name
    # }


class TestCreateOrderData:
    ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6e"]
    }
