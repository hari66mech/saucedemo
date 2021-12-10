from pytest_bdd import scenarios, when
from pageobjectmodel.product_page import Product
from pageobjectmodel.cart_page import Cart

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demoblaze/tests/features/shopping.feature")


@when("I validate items added to the cart")
def validate_item(driver):
    """This method is used to valid item"""
    Product(driver).click_cart_button()
    Cart(driver).validate_added_item()
    Product(driver).click_home_button()


@when("I validate added items")
def validate_total_items(driver):
    """This method is used to validate total items"""
    Product(driver).click_cart_button()
    Cart(driver).validate_total_added_items()
    Product(driver).click_home_button()
