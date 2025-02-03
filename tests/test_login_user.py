import allure
import requests

from data import Urls
from data import User


@allure.suite('Авторизация пользователя')
class TestLogin:

    @allure.title('Авторизация с пользователем из БД')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.LOGIN}', data=User.data_valid)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Авторизация с некорректными данными(пароль/логин)')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.LOGIN}', data=User.data_not_valid)
        assert response.status_code == 401 and response.json().get('success') == False