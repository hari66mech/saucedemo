from pytest_bdd import when, scenarios, then

from pageobjectmodel.telirik.demo_page import Demo
from pageobjectmodel.telirik.login_page import Login
from pageobjectmodel.telirik.registration_page import Registration
from pageobjectmodel.telirik.registration_successful_page import Registration_success

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/telerik/telirik.feature")


@when('I click the your account icon on demo page')
def click_account_icon(driver):
    """This method used to click the your account icon"""
    Demo(driver).click_your_account_icon()


@when("I click create an account for free on login page")
def click_create_account(driver):
    """This method is used to click the create an account for free"""
    Login(driver).click_create_account_link()


@when("I fill the details on account creation page")
def registration(driver):
    """This method used to fill the details for account creation"""
    Registration(driver).create_account()


@then("I validate the registration-successful message")
def validate_success_message(driver):
    """This method is used to validate the registration-successful message"""
    Registration_success(driver).validate_thank_you_message()
