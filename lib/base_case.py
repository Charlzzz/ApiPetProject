import json.decoder
from faker import Faker
from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can not find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Can not find header with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON, response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn`t have key '{name}'"

        return response_as_dict[name]

    # def take_fake_email(self):
    #     # fake = Faker()
    #     email = Faker().email()
    #     print(email)
    #     return email

    # def take_fake_first_name(self):
    #     first_name = fake.first_name()
    #     return first_name

    # def take_fake_last_name(self):
    #     last_name = fake.last_name()
    #     return last_name

    # def take_fake_password(self):
    #     passwd = fake.numerify(text='####')
    #     return passwd

    # def take_fake_username(self):
    #     login = fake.word()
    #     return login

    def prepare_registration_data(self, email):
        # if email is None:
        #     fake = Faker()
        #     email = fake.email()
        return {
            'password': '1234',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
