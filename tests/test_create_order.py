import allure
import requests


from data import Urls
from data import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.description("")
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        r = requests.post(f"{Urls.MAIN_URL}{Urls.MAKE_ORDER}", headers=token, data=Ingredient.valid_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("")
    @allure.title("Создание заказа не авторизованным пользователем")
    def test_create_order_not_auth(self):
        r = requests.post(f"{Urls.MAIN_URL}{Urls.MAKE_ORDER}", data=Ingredient.valid_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True


    @allure.description("")
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_with_ingridient(self):
        r = requests.post(f"{Urls.MAIN_URL}{Urls.MAKE_ORDER}")
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.description("")
    @allure.title("Создание с невалидным хешем ингредиента")
    def test_create_order_invalid_hash_ingridient(self):
        response = requests.post(Urls.MAIN_URL + Urls.MAKE_ORDER, headers=Urls.headers,
                                 json=Ingredient.not_valid_ingredients_data)
        assert response.status_code == 500 and 'Internal Server Error' in response.text