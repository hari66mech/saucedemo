from pytest_bdd import scenarios, when
from pageobjectmodel.index_page import Index
from pageobjectmodel.women_wear_index_page import Women_wear

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/feature/shopping.feature")


@when("I select items on index page")
def choose_item(driver):
    """This method is used to select the item on index page"""
    Index(driver).select_item()


@when("I select women wear items on index page")
def choose_women_wear_item(driver):
    """This method is used to select the women wear on women index page"""
    Women_wear(driver).click_women_wear()
    Women_wear(driver).select_offer_item()
