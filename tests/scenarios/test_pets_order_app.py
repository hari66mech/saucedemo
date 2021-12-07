from pytest_bdd import scenarios, when, given, parsers, then
from pytest_bdd.exceptions import StepDefinitionNotFoundError
from constants.constant import Constant
from pageobjectmodel.cart_page import Cart
from pageobjectmodel.confirm_page import Confirm
from pageobjectmodel.login_page import Login
from pageobjectmodel.registration_page import Registration
from pageobjectmodel.shopping_page import Shopping

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/pets_order_app.feature")


@given('The jpetstore demo login page is displayed')
def login_page(driver):
    """This method is used to go to the login page"""
    driver.get(Constant.LOGIN_PAGE_URL)


@when('I click the register link')
def click_register(driver):
    """This method used to click the 'register now' link"""
    Login(driver).click_register_now()


@when(parsers.parse("I register on jpetstore demo application"))
def login_standard_user(driver):
    """This method is used to register with user information"""
    global credential
    credential = Registration(driver).user_information()
    Registration(driver).account_information()
    Registration(driver).profile_information()
    Registration(driver).click_save_account_information()


@then("I validate the home page")
def validate_home_page(driver):
    """This method is used to validate page navigation"""
    assert driver.current_url == Constant.HOME_PAGE_URL


@when("I login with valid credential")
def login(driver):
    """This method is used to login with valid credential"""
    Login(driver).log_in(credential)


@when(parsers.parse("I add the {count} pet to the cart"))
def select_pet(driver, count):
    """This method is used to select pets randomly"""
    if count == "first":
        Shopping(driver).click_pets_category()
        Shopping(driver).click_pets_subcategory()
        Shopping(driver).click_specific_pet()
        Cart(driver).click_add_to_cart_button()
    elif count == "second":
        Shopping(driver).click_pets_category()
        Shopping(driver).click_pets_subcategory()
        Shopping(driver).click_specific_pet()
        Cart(driver).click_add_to_cart_button()
    else:
        try:
            raise StepDefinitionNotFoundError
        except StepDefinitionNotFoundError:
            pass


@when("I return to the home page")
def return_main_menu(driver):
    """This method is used to go to home page"""
    Shopping(driver).click_return_to_main_menu()


@when("I validate the total cost")
def calculate_total_price(driver):
    """This method is used to calculate the pets price and compare with total price"""
    Cart(driver).calculate_the_price()


@when("I order the pets")
def order_the_pets(driver):
    """This method used to confirm the order"""
    Cart(driver).click_checkout_button()
    Confirm(driver).click_continue_button()
    Confirm(driver).click_confirm_button()


@then("I validate the order status")
def verify_order(driver):
    """This method used to verify my order is placed"""
    Confirm(driver).verify_confirmation_message()
    Confirm(driver).check_total_bill_amount()
