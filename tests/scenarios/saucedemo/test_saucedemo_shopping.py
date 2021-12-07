from pytest_bdd import when, scenarios, parsers, then
from pageobjectmodel.saucedemo.cart_page import Cart
from pageobjectmodel.saucedemo.login_page import Login
from pageobjectmodel.saucedemo.shopping_page import Home
from constants.saucedemo.sauce_constant import Sauce_constant

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/saucedemo/saucedemo.feature")


@when('I login as an standard user')
def log_in(driver):
    """This method used to login with standard user credential"""
    Login(driver).login()


@when("I validate the home page")
def home_page_validation(driver):
    """This method is used to validate the home page url"""
    Home(driver).validate_home_page()


@when(parsers.parse("I add {count} to the cart"))
def select_items(driver, count):
    global items
    if count == "an_item":
        items = Home(driver).get_random_list(Sauce_constant.ONE_ITEM)
    elif count == "two_items":
        items = Home(driver).get_random_list(Sauce_constant.TWO_ITEM)
    Home(driver).add_to_cart(items)


@when("I remove an item from the cart page")
def remove_an_item(driver):
    """This method is used to remove item from the cart page"""
    Home(driver).click_shopping_icon()
    Cart(driver).remove_item()


@when("I click the continue_shopping button on cart page")
def click_continue_shopping_button(driver):
    """This method is used to click continue shopping button"""
    Cart(driver).click_continue_shopping()


@then('I validate the quantity on the cart page')
def validate_items_count(driver):
    """This method is used to validate added items count"""
    Cart(driver).verify_shopping_items_count(Sauce_constant.TOTAL_COUNT)
