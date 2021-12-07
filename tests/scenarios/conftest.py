import pytest
from pytest_bdd.exceptions import StepDefinitionNotFoundError

from selenium import webdriver
from driver.config import Driver
from pytest_bdd import when, given, parsers, then
from constants.constant import Constant
from pageobjectmodel.home_page import Home
from pageobjectmodel.cart_page import Cart
from pageobjectmodel.login_page import Login


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    driver = webdriver.Chrome(Driver.DRIVER_PATH)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given("The saucedemo login page is displayed")
def get_login_page(driver):
    """This method is used get login page url"""
    driver.get(Constant.LOGIN_PAGE_URL)


@when('I login with standard user credential')
def log_in(driver):
    """This method used to login with standard user credential"""
    Login(driver).login()


@when("I validate the home page")
@then("I validate the home page")
def validate_home_page(driver):
    """This method is used to validate the home page"""
    Home(driver).validate_home_page()


@when(parsers.parse('I add {count} to the cart'))
def add_items(driver, count):
    """This method is used to add items to cart"""

    global items
    if count == "an item":
        items = Home(driver).get_random_list(Constant.ONE_ITEM)
    elif count == "two items":
        items = Home(driver).get_random_list(Constant.TWO_ITEM)
    elif count == "three items":
        items = Home(driver).get_random_list(Constant.THREE_ITEM)
    else:
        try:
            raise StepDefinitionNotFoundError
        except StepDefinitionNotFoundError:
            pass
    Home(driver).add_to_cart(items)


@then(parsers.parse('I validate the {item_count} added to cart'))
def validate_items_count(driver, item_count):
    """This method is used to validate added item count"""
    if item_count == "three items":
        Cart(driver).verify_shopping_items_count(Constant.THREE_ITEM)
    elif item_count == "one item":
        Cart(driver).verify_shopping_items_count(Constant.ONE_ITEM)
    else:
        try:
            raise StepDefinitionNotFoundError
        except StepDefinitionNotFoundError:
            pass
