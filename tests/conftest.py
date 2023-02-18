import pytest
import faker
from faker import Faker


@pytest.fixture()
def faker_locale():
    return ['it_IT']


@pytest.fixture()
def take_fake_email(faker):

    email = faker.unique.email()

    return email


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
