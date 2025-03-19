import allure
import requests

from handles import Handle
from urls import Urls


class TestListOrders:

    @allure.title('Успешное получение списка заказов')
    def test_get_list_orders(self):
        response = requests.get(f'{Urls.BASE_URL}{Handle.CREATE_ORDER}')
        assert response.status_code == 200 and "orders" in response.json()
