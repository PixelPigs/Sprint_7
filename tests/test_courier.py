import allure
import requests
import pytest
from data_test import *
from handles import Handle
from urls import Urls


class TestCreateCourier:

    @allure.title('Успешное создание учетной записи')
    def test_check_create_account_true(self):
        payload = courier_registration()
        response = requests.post(f'{Urls.BASE_URL}{Handle.CREATE_COURIER}', data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        payload = {
            'login': payload.get('login'),
            'password': payload.get('password')
        }
        response = requests.post(f'{Urls.BASE_URL}{Handle.LOGIN_COURIER}', data=payload)
        courier = response.json()
        user_id = response.json().get('id')
        requests.delete(f'{Urls.BASE_URL}{Handle.CREATE_COURIER}/{user_id}', data=courier)

    @allure.title('Запрос с повторяющимся логином')
    def test_check_create_identical_accounts(self):
        payload = Users.correct_data
        response = requests.post(f'{Urls.BASE_URL}{Handle.CREATE_COURIER}', data=payload)
        assert response.status_code == 409 and TextError.login_used in response.text

    @allure.title('Запрос без логина или пароля')
    @pytest.mark.parametrize(
        "login,password,name",
    [
        ("", Users.correct_data["password"], Users.correct_data["name"]),
        (Users.correct_data["login"], "", Users.correct_data["name"])
    ]
    )
    def test_check_create_account_without_login(self, login, password, name):
        payload = {
            "login": login,
            "password": password,
            "name": name
        }
        response = requests.post(f'{Urls.BASE_URL}{Handle.CREATE_COURIER}', data=payload)
        assert response.status_code == 400 and TextError.not_enough_data in response.text
