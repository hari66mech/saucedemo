import factory
from factorie_data import objects


class CredentialFactory(factory.Factory):
    class Meta:
        model = objects.Credential

    name = factory.Faker('name')
    password = factory.Faker('password')
    country = factory.Faker('country')
    city = factory.Faker('city')
    credit_card_number = factory.Faker('random_number', digits=16)
    credit_card_expiry_date = "07/25"
