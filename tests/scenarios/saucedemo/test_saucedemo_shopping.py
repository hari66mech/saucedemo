import time

from pytest_bdd import when, scenarios, parsers, then

from pageobjectmodel.saucedemo.cart_page import Cart
from pageobjectmodel.saucedemo.login_page import Login
from pageobjectmodel.saucedemo.shopping_page import Home
from constants.saucedemo.constant import Constant

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/saucedemo/saucedemo.feature")


@when('I login as standard user')
def log_in(driver):
    """This method used to login with standard user credential"""
    Login(driver).login()


@when("I validate the home page")
def validate_home_page(driver):
    """This method is used to validate the home page url"""
    Home(driver).validate_home_page()


@when(parsers.parse("I add {count} to the cart"))
def select_items(driver, count):
    global items
    if count == "an item":
        items = Home(driver).get_random_list(Constant.ONE_ITEM)
    elif count == "two items":
        items = Home(driver).get_random_list(Constant.TWO_ITEM)
    Home(driver).add_to_cart(items)


@when("I navigate to the cart page")
def navigate_cart_page(driver):
    """This method used to navigate to the cart page"""
    Home(driver).click_shopping_icon()


@when("I remove the item on cart page")
def remove_item(driver):
    """This method is used to remove item from the cart"""
    Cart(driver).remove_item()


@when("I click the continue shopping button on cart page")
def continue_shopping(driver):
    """This method is used to click continue shopping button"""
    Cart(driver).click_continue_shopping()
    time.sleep(3)


@then(parsers.parse('I validate the quantity on the cart page'))
def validate_items_count(driver):
    """This method is used to validate added items count"""
    Cart(driver).verify_shopping_items_count(Constant.TOTAL_COUNT)
