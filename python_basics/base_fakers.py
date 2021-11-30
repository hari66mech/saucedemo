from factory.faker import faker


class Base_faker_data:

    def fake_name_data(self):
        """This method is used to generate a fake names"""
        FAKE = faker.Faker()
        print(FAKE.name())
        print(FAKE.first_name())
        print(FAKE.last_name())