from faker import Faker

fake = Faker()

def courier_registration():
    login = fake.user_name()
    password = fake.password()
    firstName = fake.first_name()
    data_registration = {
        "login": login,
        "password": password,
        "name": firstName
    }
    return data_registration

class TextError:
    login_used = 'Этот логин уже используется'
    account_not_found = 'Учетная запись не найдена'
    not_enough_data = 'Недостаточно данных для создания учетной записи'

class Users:
    correct_data = {
        "login": "olga18",
        "password": "123456789",
        "name": "testova"
    }
    incorrect_data = {
        "login": "0000000001",
        "password": "0000000001"
    }

class Orders:
    create_order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ""
}
