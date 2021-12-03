from pytest_bdd import scenarios, when, given, parsers, then
from pytest_bdd.exceptions import StepDefinitionNotFoundError

from constants.constant import Constant
from pageobjectmodel.pets_order_app import Pets_order

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/pytest_bdd_training/tests/features/pets_order_app.feature")


@given('The jpetstore demo login page is displayed')
def login_page(driver):
    """This method is used to go to the login page"""
    driver.get(Constant.LOGIN_PAGE_URL)


@when('I click the register link')
def click_register_now(driver):
    """This method used to click the 'register now' link"""
    Pets_order(driver).click_register_now()


@when(parsers.parse("I fill the user information"))
def login_standard_user(driver):
    """This method is used to register with user information"""
    global credential
    credential = Pets_order(driver).user_information()
    Pets_order(driver).account_information()
    Pets_order(driver).profile_information()


@then("I navigate to jpetstore demo home page")
def validate_home_page(driver):
    """This method is used to validate page navigation"""
    Pets_order(driver).click_save_account_information()
    assert driver.current_url == Constant.HOME_PAGE_URL


@when("I login with valid credential")
def login(driver):
    """This method is used to login with valid credential"""
    Pets_order(driver).log_in(credential)


@when(parsers.parse("I select the {count} pet"))
def select_pet(driver, count):
    """This method is used to select pets randomly"""
    if count == "first":
        Pets_order(driver).click_pets_category()
        Pets_order(driver).click_pets_subcategory()
        Pets_order(driver).click_specific_pet()
    elif count == "second":
        Pets_order(driver).click_pets_category()
        Pets_order(driver).click_pets_subcategory()
        Pets_order(driver).click_specific_pet()
    else:
        try:
            raise StepDefinitionNotFoundError
        except StepDefinitionNotFoundError:
            print("StepDefinitionNotFoundError")


@when(parsers.parse("I add the {count} pet to the cart"))
def add_to_cart(driver, count):
    """This method is used to add pets to cart"""
    if count == "first":
        Pets_order(driver).click_add_card()
    elif count == "second":
        Pets_order(driver).click_add_card()
    else:
        try:
            raise StepDefinitionNotFoundError
        except StepDefinitionNotFoundError:
            print("StepDefinitionNotFoundError")


@when("I return to the home page")
def return_main_menu(driver):
    """This method is used to go to home page"""
    Pets_order(driver).click_return_to_main_menu()


@then("I validate the total amount")
def calculate_total_price(driver):
    """This method is used to calculate the pets price and compare with total price"""
    Pets_order(driver).calculate_the_price()


@then("I order the pets")
def order_the_pets(driver):
    """This method used to confirm the order"""
    Pets_order(driver).click_checkout_button()
    Pets_order(driver).click_continue_button()
    Pets_order(driver).click_confirm_button()


@then("I validate my order is placed")
def verify_order(driver):
    """This method used to verify my order is placed"""
    Pets_order(driver).verify_confirmation_message()
    Pets_order(driver).check_total_bill_amount()
