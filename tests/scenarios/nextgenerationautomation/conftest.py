import pytest
from faker import Faker
from pytest_bdd import given
from constants.nextgenerationautomation.constant import Constant

fake = Faker()


@pytest.fixture
def credential(driver):
    """This method is used to get fake details"""
    credential = {"first_name": fake.first_name(),
                  "last_name": fake.last_name(),
                  "email": fake.email(),
                  "password": fake.password(),
                  "mobile_number": fake.msisdn(),
                  "work_city": fake.city()
                  }
    return credential


@given("The nextgenerationautomation home_page is displayed")
def get_home_page(driver):
    """This method is used to get home page url"""
    driver.get(Constant.HOME_PAGE_URL)
