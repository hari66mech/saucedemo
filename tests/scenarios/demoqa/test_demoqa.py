from pytest_bdd import scenarios, when, then
from pageobjectmodel.demoqa.practice_form_page import PracticeForm

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/demoqa/sign_up.feature")


@when("I fill the practice_form")
def fill_practice_form(driver, credential):
    """This method is used to fill the practice form"""
    PracticeForm(driver).fill_form(credential)


@then("I validate submit button is clickable")
def verify_submit_button(driver):
    """this method is used to validate the submit button is clickable"""
    PracticeForm(driver).click_submit()
