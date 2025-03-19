import allure
import pytest
import requests
import json

from data_test import Orders
from handles import Handle
from urls import Urls


class TestCreateOrder:

    @allure.title('Создание заказа с указанием разных данных в поле цвет')
    @pytest.mark.parametrize("color", ["BLACK", "GREY", ("BLACK", "GREY"), ""])
    def test_color_in_create_order(self, color):
        payload = {**Orders.create_order, "color": color}
        json_string = json.dumps(payload)
        response = requests.post(f'{Urls.BASE_URL}{Handle.CREATE_ORDER}', data=json_string)
        assert 'track' in response.json()
