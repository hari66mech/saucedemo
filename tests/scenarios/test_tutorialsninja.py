from pytest_bdd import scenarios, when, then, parsers
from pageobjectmodel.register_page import Register
from pageobjectmodel.home_page import Home
from pageobjectmodel.success_page import Success

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features")


@when(parsers.parse("I click the {action} button"))
def click_button(driver, action):
    """This method is used to click button on specific action"""
    if action == "my_account":
        Home(driver).my_account.click()
    elif action == "register":
        Home(driver).register.click()
    else:
        raise NotImplementedError


@when("I register as a new user")
def user_registration(driver, credential):
    """This method is used to register as a user"""
    Register(driver).register(credential)


@then("I validate success message")
def validate_account_created_message(driver):
    """This method is used to validate the success message"""
    Success(driver).validate_success_message()
