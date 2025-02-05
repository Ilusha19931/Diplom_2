import pytest
import requests

from data import Urls
from data import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.create_data_user()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_USER}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.MAIN_URL}{Urls.DELETE_USER}", headers={'Authorization': f'{token}'})