from pytest_bdd import scenarios, when
from pageobjectmodel.index_page import Index


scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/feature/automationpractice.feature")


@when("I select items on index page")
def choose_item(driver):
    """This method is used to select the item on index page"""
    Index(driver).select_item()
