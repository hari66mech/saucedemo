from pytest_bdd import scenarios, when, then
from pageobjectmodel.index_page import Index
from pageobjectmodel.sign_up_page import Sign_up
from pageobjectmodel.login_page import Login

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demoblaze/tests/features/login.feature")


@when("I sign_up as a user")
def sign_up_action(driver):
    """This method is used to sign_up as a user"""
    global credential
    Index(driver).click_sign_up_button()
    credential = Sign_up(driver).sign_up()


@when("I login with valid credential")
def login_action(driver):
    """This method is used to login with valid user credential"""
    Index(driver).click_login_button()
    Login(driver).login(credential)


@then("I validate the user is logged in")
def verify_user_welcome_message(driver):
    "This method is used to validate the user is logged in"
    Index(driver).validate_welcome_message(credential)
