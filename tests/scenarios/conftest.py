import pytest
from pytest_bdd import given
from selenium import webdriver
from constants.constant import Constant
from driver.config import Config
from pytest_bdd import when, then
from pageobjectmodel.sign_in_page import Sign_in
from pageobjectmodel.index_page import Index
from pageobjectmodel.my_account_page import My_account
from pageobjectmodel.shopping_cart_page import Shopping_cart
from pageobjectmodel.address_page import Address
from pageobjectmodel.shipping_page import Shipping
from pageobjectmodel.payment_method_choose_page import Payment_method
from pageobjectmodel.payment_page import Payment
from pageobjectmodel.order_confirmation_page import Order_confirmation


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


@given("The automationpractice index page is displayed")
def get_index_page(driver):
    """This method is used get index page url"""
    driver.get(Constant.INDEX_PAGE)


@when("I click the sign_in button on the index page")
def click_sign_in_button(driver):
    """This method is used to click the sign_in on the index page"""
    Index(driver).click_signin()


@when("I signin as a user on the signin page")
def sign_in_action(driver):
    """This method is used to sign in as a user on the sign_in page"""
    Sign_in(driver).get_credentials()
    Sign_in(driver).sign_in()
    My_account(driver).validate_my_account_page()
    My_account(driver).click_home_button()


@when("I accept the checkout process")
def checkout_process(driver):
    """This method is used to process the items checkout"""
    Shopping_cart(driver).validate_shopping_cart_heading()
    Shopping_cart(driver).click_checkout_button()
    Address(driver).validate_address_page_heading()
    Address(driver).click_address_page_checkout_button()
    Shipping(driver).validate_shipping_page_heading()
    Shipping(driver).click_agreement_box()
    Shipping(driver).click_shipping_page_checkout_button()


@when("I select payment method")
def select_payment_option(driver):
    """This method is used to perform the payment action"""
    Payment_method(driver).validate_payment_method_page_heading()
    Payment_method(driver).click_payment_method()
    Payment(driver).validate_payment_page_heading()
    Payment(driver).click_confirm_order_button()


@then("I validate order confirmation on order confirmation page")
def validate_order_confirmation(driver):
    """This method is used to validate the order confirmation"""
    Order_confirmation(driver).validate_order_confirmation_page()
