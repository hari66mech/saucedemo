from pytest_bdd import scenarios, when, parsers, then
from pageobjectmodel.sign_in_page import Sign_in
from pageobjectmodel.account_creation_page import Account_creation
from pageobjectmodel.my_account_page import My_account

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/feature/registration.feature")


@when("I create user account on signin page")
def create_user_account(driver):
    """This method is used to fill mail_id and click account create button on the sign_in page"""
    global mail_id
    mail_id = Sign_in(driver).click_create_an_account()


@when(parsers.parse("I fill the user {first_name} and {last_name}"))
def fill_the_user_name(driver, first_name, last_name):
    """This method is used to enter user name on the account create page"""
    Account_creation(driver).enter_user_name(first_name, last_name)


@when("I fill the user details on the account_creation page")
def fill_the_user_information(driver):
    """This method is used to enter user information on the account create page"""
    password = Account_creation(driver).enter_personal_information()
    Account_creation(driver).enter_address_information()
    Account_creation(driver).click_register_button()
    Account_creation(driver).keep_credentials(mail_id, password)


@then("I validate the my_account page")
def verify_my_account_page(driver):
    """This method is used to validate the my-account page"""
    My_account(driver).validate_my_account_page()
