from pytest_bdd import scenarios, when, then
from pageobjectmodel.index_page import Index
from pageobjectmodel.sign_in_page import Signin
from pageobjectmodel.sign_up_page import Signup
from pageobjectmodel.collections_page import Collections

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/ultimateQA/tests/features/ultimateqa")


@when("I register as a user")
def register_account(driver, credential):
    """This method is used to register the account as a user"""
    Index(driver).click_signin_button()
    Signin(driver).create_account_button.click()
    Signup(driver).registration(credential)


@when("I store the courses list in text file")
def get_course_name(driver):
    """This method is used to store the available courses in text file"""
    Collections(driver).keep_courses()


@then("I validate the collections page")
def validate_collections_page(driver):
    """This method is used to validate the collections page"""
    Collections(driver).validate_course_heading()
