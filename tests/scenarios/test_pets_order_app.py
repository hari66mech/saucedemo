import time

from pytest_bdd import scenarios, when, then, given, parsers
from pytest_bdd.exceptions import StepDefinitionNotFoundError

from constants.constant import Constant
from pageobjectmodel.pets_order_app import Pets_order

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/pytest_bdd_training/tests/features/pets_order_app.feature")


@given('The jpetstore demo login page is displayed')
def home(driver):
    driver.get(Constant.LOGIN_PAGE_URL)


@when(parsers.parse("I fill the {data} information"))
def login_standard_user(driver, data):
    if data == "user":
        Pets_order(driver).user_information()
    elif data == "account":
        Pets_order(driver).account_information()
    elif data == "profile":
        Pets_order(driver).profile_information()
    else:
        try:
            raise StepDefinitionNotFoundError
        except StepDefinitionNotFoundError:
            print("StepDefinitionNotFoundError")


@when("Validate i click save account information button, it navigate to jpetstore demo home page")
def validate_home_page(driver):
    Pets_order(driver).click_save_account_information()
    assert driver.current_url == Constant.HOME_PAGE_URL


@when("I click the pet from the pets category")
def click_pet_category(driver):
    Pets_order(driver).click_pets_category()
    time.sleep(5)
