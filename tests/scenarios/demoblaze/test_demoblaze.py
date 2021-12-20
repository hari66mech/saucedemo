from pytest_bdd import scenarios, when, then, parsers
from pageobjectmodel.cart_page import Cart
from pageobjectmodel.index_page import Index
from pageobjectmodel.product_page import Product
from pageobjectmodel.sign_up_page import Sign_up
from pageobjectmodel.login_page import Login

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demoblaze/tests/features/demoblaze")


@when("I register as a user")
def sign_up_action(driver, credential):
    """This method is used to sign_up as a user"""
    Index(driver).signup.click()
    Sign_up(driver).keep_credentials(credential)
    Sign_up(driver).registration(credential)


@then("I validate the user is logged in")
def verify_user_welcome_message(driver, credential):
    "This method is used to validate the user is logged in"
    Index(driver).log_in.click()
    Login(driver).login()
    Index(driver).verify_user_welcome_message(credential)


@when(parsers.parse("I validate {item} added to the cart"))
def validate_selected_items(driver, item):
    Product(driver).cart_button.click()
    if item == "an_item":
        Cart(driver).validate_added_item()
    elif item == "three_items":
        Cart(driver).validate_total_added_items()
    else:
        raise NotImplementedError
    Product(driver).home_button.click()
