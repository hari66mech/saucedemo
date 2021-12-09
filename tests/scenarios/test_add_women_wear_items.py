from pytest_bdd import scenarios, when
from pageobjectmodel.women_wear_index_page import Women_wear


scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/feature/automationpractice.feature")


@when("I select items on women wear index page")
def choose_women_wear_item(driver):
    """This method is used to select the women wear on women index page"""
    Women_wear(driver).click_women_wear()
    Women_wear(driver).select_offer_item()
