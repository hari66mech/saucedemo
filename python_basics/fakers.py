from factory.faker import faker
from python_basics.base_fakers import Base_faker_data


class Faker_data(Base_faker_data):
    """This class is used to generate fake data and also the Base_Faker_Data class inherited in this class."""
    def fake_data(self):
        """This method is used to generate fake address and email"""
        FAKE = faker.Faker()
        print(FAKE.address())
        print(FAKE.email())
