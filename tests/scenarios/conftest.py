import pytest

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


@then("I validate home page")
@when("I validate home page")
def validate_home_page(driver):
    """This method is used to validate the home page url"""
    Home(driver).validate_home_page()


@when(parsers.parse('I select {count} randomly'))
def add_items(driver, count):
    """This method is used to add items to cart"""
    lists = Home(driver).get_random_list()
    if count == "one item" or count == "two items" or count == "three items":
        Home(driver).add_to_cart(lists[0])
    if count == "two items" or count == "three items":
        Home(driver).add_to_cart(lists[1])
    if count == "three items":
        Home(driver).add_to_cart(lists[2])


@then(parsers.parse('I validate the {items_count} added to cart'))
def validate_items_count(driver, items_count):
    """This method is used to validate added items count"""
    if items_count == "three items":
        Cart(driver).verify_shopping_items_count(3)
    elif items_count == "one item":
        Cart(driver).verify_shopping_items_count(1)
