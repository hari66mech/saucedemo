from factory import Factory, Faker
from collections import namedtuple

Dataset = namedtuple("Dataset", ["name"])


class DatasetFactory(Factory):
    """Factory creating test datasets"""

    class Meta:
        model = Dataset

    names = Faker("name")

    print(names)


