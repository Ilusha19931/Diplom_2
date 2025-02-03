from faker import Faker

class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    MAKE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    headers = {"Content-Type": "application/json"}

class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        user_create = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return user_create

    data_valid = {
        "email": 'pokemon_444@anime.ru',
        "password": "пароль"}

    data_not_valid = {
        "email": 'pokemon_4@anime.ru',
        "password": "пароль"}

    data_doubled = {
        "email": 'pokemon_444@anime.ru',
        "password": "пароль",
        "name": "Пикачу"}

    data_without_email = {
        "email": '',
        "password": "пароль",
        "name": "Пикачу"}

    data_without_password = {
        "email": 'pokemon_444@anime.ru',
        "password": "",
        "name": "Пикачу"}

    data_without_name = {
        "email": 'pokemon_444@anime.ru',
        "password": "пароль",
        "name": ""}

    data_updated = {
        "email": 'pokemon_444@anime.ru',
        "password": "пароль",
        "name": "nety"}



class Ingredient:
    valid_ingredients_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

    not_valid_ingredients_data = {
        "ingredients": ["60d3b41abdacab0026a733c6g", "609646e4dc916e00276b2870g"]}