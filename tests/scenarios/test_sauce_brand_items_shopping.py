from pytest_bdd import scenarios, when

from pageobjectmodel.cart_page import Cart
from pageobjectmodel.home_page import Home

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/saucedemo.feature")


@when("I remove one item from cart page")
def remove_the_selected_item(driver):
    """This method is used to remove item from the cart"""
    Cart(driver).remove_item()


@when("I click the shopping icon")
def click_shopping_bucket_icon(driver):
    """This method is used to click shopping icon"""
    Home(driver).click_shopping_icon()


@when("I click the continue shopping button")
def continue_shopping(driver):
    """This method is used to click continue shopping button"""
    Cart(driver).click_continue_shopping()
