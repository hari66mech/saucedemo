from faker import Faker
from tests.factories import objects
import factory

fake = Faker()


class CredentialFactory(factory.Factory):
    class Meta:
        model = objects.Credential

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone_number = factory.Faker('random_number', digits=10)
    email = factory.Faker('email')
    password = factory.Faker('password')
