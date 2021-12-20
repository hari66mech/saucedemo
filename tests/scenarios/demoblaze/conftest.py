import pytest
from pytest_bdd import given, when, parsers, then
from selenium import webdriver
from driver.config import Config
from constants.constant import Constant
from pageobjectmodel.index_page import Index
from pageobjectmodel.product_page import Product
from pageobjectmodel.cart_page import Cart
from msedge.selenium_tools import Edge, EdgeOptions
from factorie_data.credential_factory import CredentialFactory


class DriverError(Exception):
    def __init__(self, value):
        self.value = value


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    try:
        if Config.DRIVER == "chrome":
            chromeOptions = webdriver.ChromeOptions()
            if Config.HEADLESS:
                chromeOptions.add_argument('--headless')
            driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH, chrome_options=chromeOptions)
        elif Config.DRIVER == "firefox":
            firefoxOptions = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                firefoxOptions.add_argument('--headless')
            driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH, firefox_options=firefoxOptions)
        elif Config.DRIVER == "msedge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            if Config.HEADLESS:
                edge_options.add_argument('--headless')
            driver = Edge(executable_path=Config.MS_EDGE_DRIVER_PATH, options=edge_options)
        else:
            raise DriverError("the {driverName} driver is not found".format(driverName=Config.DRIVER))
    except DriverError:
        driver.quit()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def credential(driver):
    """This method is used to call the factory boy credential"""
    data = CredentialFactory()
    credential = {
        "user_name": data.name,
        "user_password": data.password,
        "country": data.country,
        "city": data.city,
        "credit_card_number": data.credit_card_number,
        "expire_date": data.credit_card_expiry_date
    }
    return credential


@given("The demoblaze index page is displayed")
def get_index_page(driver):
    """This method is used to get index page url"""
    driver.get(Constant.INDEX_PAGE)


@when(parsers.parse("I add an item from the {category}"))
def add_item(driver, category):
    "This method is used to add an item to the cart"
    if category == "second_page":
        Index(driver).validate_samsung_galaxy_mobile()
        Index(driver).click_next_button()
        Index(driver).validate_apple_monitor()
    Index(driver).select_item()
    Product(driver).click_add_to_cart()
    Product(driver).home_button.click()


@when(parsers.parse("I add an item to the cart from the {category} category"))
def add_item_with_category(driver, category):
    "This method is used to add a given category item to the cart"
    if category == "mobile":
        Index(driver).phones_button.click()
        Index(driver).validate_samsung_galaxy_mobile()
    elif category == "laptop":
        Index(driver).laptops_button.click()
        Index(driver).validate_sony_vaio_laptop()
    elif category == "Monitor":
        Index(driver).monitors_button.click()
        Index(driver).validate_apple_monitor()
    else:
        raise NotImplementedError
    Index(driver).select_item()
    Product(driver).click_add_to_cart()
    Product(driver).home_button.click()


@when(parsers.parse("I click the {action} button"))
def click_specific_button(driver, action):
    "This method is used to click cart button"
    if action == "cart":
        Product(driver).cart_button.click()
    elif action == "place_order":
        Cart(driver).place_to_add_button.click()
    else:
        raise NotImplementedError


@when("I fill the user_info for placing an order")
def fill_the_details(driver, credential):
    "This method is used to fill the user details"
    Cart(driver).fill_the_user_details(credential)


@then("I validate the success message")
def validate_success_message(driver):
    "This method is used to validate success message"
    Cart(driver).validate_thank_you_message()
