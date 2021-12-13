import pytest
from pytest_bdd import given, when, parsers, then
from selenium import webdriver
from driver.config import Config
from constants.constant import Constant
from pageobjectmodel.index_page import Index
from pageobjectmodel.product_page import Product
from pageobjectmodel.cart_page import Cart


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    try:
        if Config.DRIVER == "chrome":
            driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH)
        elif Config.DRIVER == "firefox":
            driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
        elif Config.DRIVER == "msedge":
            driver = webdriver.Edge(Config.MS_EDGE_DRIVER_PATH)
        else:
            raise RuntimeError
    except RuntimeError:
        pass
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given("The demoblaze index page is displayed")
def get_index_page(driver):
    """This method is used to get index page url"""
    driver.get(Constant.INDEX_PAGE)


@when(parsers.parse("I add an item from the {category}"))
def add_item(driver, category):
    "This method is used to add an item to the cart"
    if category == "first_page":
        pass
    elif category == "second_page":
        Index(driver).validate_mobile()
        Index(driver).click_next_button()
        Index(driver).validate_monitor()
    else:
        raise NotImplementedError
    Index(driver).select_item()
    Product(driver).click_add_to_cart()
    Product(driver).home_button.click()


@when(parsers.parse("I add an item to the cart from the {category}"))
def add_item_with_category(driver, category):
    "This method is used to add a given category item to the cart"
    if category == "mobile":
        Index(driver).phones_button.click()
        Index(driver).validate_mobile()
    elif category == "laptop":
        Index(driver).laptops_button.click()
        Index(driver).validate_laptop()
    elif category == "Monitor":
        Index(driver).monitors_button.click()
        Index(driver).validate_monitor()
    else:
        raise NotImplementedError
    Index(driver).select_item()
    Product(driver).click_add_to_cart()
    Product(driver).home_button.click()


@when("I click the cart button")
def click_cart_button(driver):
    "This method is used to click cart button"
    Product(driver).cart_button.click()


@when("I click the place order button")
def click_place_order_button(driver):
    "This method is used to click place order button"
    Cart(driver).place_to_add_button.click()


@when("I fill the user_info for placing an order")
def fill_the_details(driver):
    "This method is used to fill the user details"
    Cart(driver).fill_the_user_details()


@then("I validate the success message")
def validate_success_message(driver):
    "This method is used to validate success message"
    Cart(driver).validate_thank_you_message()
