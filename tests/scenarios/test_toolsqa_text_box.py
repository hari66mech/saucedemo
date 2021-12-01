from pytest_bdd import scenarios, when, then, given, parsers
from pytest_bdd.exceptions import StepDefinitionNotFoundError

from constants.constant import Constant
from pageobjectmodel.toolsqa_text_box import Toolsqa_text_box

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/pytest_bdd_training/tests/features/toolsqa_text_box.feature")


@given("The demoqa text page is displayed")
def open_text_box_page(driver):
    """This method is used to go to the text box page"""
    driver.get(Constant.TEXT_BOX_PAGE)


@when(parsers.parse('I fill the {data}'))
def enter_user_data(driver, data):
    """This method is used to enter the user data"""
    if data == "user_name":
        Toolsqa_text_box(driver).enter_full_name()
    elif data == "email_id":
        Toolsqa_text_box(driver).enter_email_id()
    elif data == "current_address":
        Toolsqa_text_box(driver).enter_current_address()
    elif data == "permanent_address":
        Toolsqa_text_box(driver).enter_permanent_address()
    else:
        try:
            raise StepDefinitionNotFoundError
        except StepDefinitionNotFoundError:
            print("StepDefinitionNotFoundError")


@when('I am clicking submit button')
def click_submit_button(driver):
    """This method is used to click the submit button"""
    Toolsqa_text_box(driver).click_submit_button()


@then("I validate the output box field is displayed")
def validate_output_box(driver):
    """This method is used to validate the output box is displayed"""
    Toolsqa_text_box(driver).out_put_box()
