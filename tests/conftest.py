

import pytest
import faker
from faker import Faker


@pytest.fixture()
def faker_locale():
    return ['it_IT']


@pytest.fixture()
def take_fake_email():
    def take_fake_email():
        fake = Faker()
        return fake.email()
    return take_fake_email()


@pytest.fixture()
def take_fake_first_name(faker):
    return faker.first_name()


@pytest.fixture()
def take_fake_last_name(faker):
    return faker.last_name()


@pytest.fixture()
def take_fake_password(faker):
    return faker.numerify(text='####')


@pytest.fixture()
def take_fake_username(faker):
    return faker.word()
