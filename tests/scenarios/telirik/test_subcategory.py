import time
from pytest_bdd import when, scenarios, then
from pageobjectmodel.telirik.demo_page import Demo

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/telerik/telirik.feature")


@when('I click the demos subcategory in demo page')
def click_subcategory(driver):
    """This method used to click the subcategory"""
    Demo(driver).click_subcategory()


@then("I validate the selected category heading")
def validate_heading(driver):
    """This method is used to validate the heading with selected category"""
    Demo(driver).verify_header()
