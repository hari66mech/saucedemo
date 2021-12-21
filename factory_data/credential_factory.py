import factory
from factory_data import objects


class CredentialFactory(factory.Factory):
    class Meta:
        model = objects.Credential

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
