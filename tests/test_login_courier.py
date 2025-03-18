import allure
import requests
import pytest

from data_test import Users
from handles import Handle
from urls import Urls


class TestLoginCourier:

    @allure.title('Авторизация курьера проходит успешно, присваивается id')
    def test_check_successful_authorization(self):
        payload = dict(list(Users.correct_data.items())[:2])
        response = requests.post(f'{Urls.BASE_URL}{Handle.LOGIN_COURIER}', data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Авторизация без логина или пароля или оба поля пустые')
    @pytest.mark.parametrize(
        "login,password",
        [
            ("", Users.correct_data["password"]),
            (Users.correct_data["login"], ""),
            ("", ""),
            (None, None)
        ]
    )
    def test_check_create_account_without_login(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Urls.BASE_URL}{Handle.LOGIN_COURIER}', data=payload)
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text

    @allure.title('Авторизация с некорректным логином или паролем или оба поля некорректны')
    @pytest.mark.parametrize(
        "login,password",
        [
            (Users.incorrect_data["login"], Users.correct_data["password"]),
            (Users.correct_data["login"], Users.incorrect_data["password"]),
            (Users.incorrect_data["login"], Users.incorrect_data["password"])
        ]
    )
    def test_check_create_account_without_login(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Urls.BASE_URL}{Handle.LOGIN_COURIER}', data=payload)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

