class TestDataUrl:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
    CREATE_USER_URL = f"{BASE_URL}auth/register"
    AUTHORIZATION_URL = f"{BASE_URL}auth/login"
    AUTH_USER_URL = f"{BASE_URL}auth/user"
    CREATE_ORDER_URL = f"{BASE_URL}orders"


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
