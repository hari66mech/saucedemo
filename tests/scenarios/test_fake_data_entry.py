from pytest_bdd import scenarios, when, then, given, parsers
from constants.constant import Constant
from pageobjectmodel.fake_data_entry import Fake_data_entry

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/saucedemo/tests/features/fake_data_entry.feature")


@given("The demoqa text page is displayed")
def open_text_box_page(driver):
    """This method is used to go to the text box page"""
    driver.get(Constant.TEXT_BOX_PAGE)


@when(parsers.parse('I am entering {data}'))
def enter_user_data(driver, data):
    """This method is used to enter the user data"""
    if data == "user_name":
        Fake_data_entry(driver).enter_full_name()
    elif data == "email_id":
        Fake_data_entry(driver).enter_email_id()
    elif data == "current_address":
        Fake_data_entry(driver).enter_current_address()
    elif data == "permanent_address":
        Fake_data_entry(driver).enter_permanet_address()


@when('I am clicking submit button')
def click_submit_button(driver):
    """This method is used to click the submit button"""
    Fake_data_entry(driver).click_submit_button()


@then("I validate the output box")
def validate_output_box(driver):
    """This method is used to validate the output box"""
    Fake_data_entry(driver).out_put_box()
