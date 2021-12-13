from pytest_bdd import scenarios, when, then
from pageobjectmodel.cart_page import Cart
from pageobjectmodel.index_page import Index
from pageobjectmodel.product_page import Product
from pageobjectmodel.sign_up_page import Sign_up
from pageobjectmodel.login_page import Login

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demoblaze/tests/features")


@when("I register as a user")
def sign_up_action(driver):
    """This method is used to sign_up as a user"""
    global credential
    Index(driver).signup.click()
    credential = Sign_up(driver).registration()


@then("I validate the user is logged in")
def verify_user_welcome_message(driver):
    "This method is used to validate the user is logged in"
    Index(driver).log_in.click()
    Login(driver).login(credential)
    Index(driver).verify_user_welcome_message(credential)


@when("I validate items added to the cart")
def validate_item(driver):
    """This method is used to valid item"""
    Product(driver).cart_button.click()
    Cart(driver).validate_added_item()
    Product(driver).home_button.click()


@when("I validate added items")
def validate_total_items(driver):
    """This method is used to validate total items"""
    Product(driver).cart_button.click()
    Cart(driver).validate_total_added_items()
    Product(driver).home_button.click()
