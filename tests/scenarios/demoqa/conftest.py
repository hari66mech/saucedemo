import pytest
from faker import Faker
from pytest_bdd import given
from constants.demoqa.constant import Constant

fake = Faker()


@pytest.fixture
def credential(driver):
    """This method is used to get fake details"""
    credential = {"first_name": fake.first_name(),
                  "last_name": fake.last_name(),
                  "email": fake.email(),
                  "mobile_number": fake.msisdn(),
                  "address": fake.address()
                  }
    return credential


@given("The demoqa practice_form page is displayed")
def get_login_page(driver):
    """This method is used get home page url"""
    driver.get(Constant.DEMOQA_PRACTICE_FORM_URL)
