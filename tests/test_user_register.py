import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):

    def test_create_user_success(self, take_fake_email):
        email = take_fake_email
        data = self.prepare_registration_data(email)
        print(email)
        url = 'https://playground.learnqa.ru/api/user/'
        response = requests.post(url, data=data)

        Assertions.assert_code_status(response, 200)
        print(response.content)
        Assertions.assert_json_has_key(response, 'id')

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        url = 'https://playground.learnqa.ru/api/user/'
        response = requests.post(url, data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f'Unexpected response content {response.content}'



