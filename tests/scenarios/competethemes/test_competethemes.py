import random
from pytest_bdd import scenarios, when, parsers, then
from pageobjectmodel.competethemes.home_page import Home
from pageobjectmodel.competethemes.product_page import Product
from pageobjectmodel.competethemes.cart_page import Cart

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/competethemes/select_item.feature")


@when(parsers.parse("I select an {product} randomly"))
def select_item(driver, product):
    """This method is used to select the product"""
    if product == "on-sale-product":
        product_details = Home(driver).select_on_sale_products()
    elif product == "top-rated-product":
        product_details = Home(driver).select_top_rated_products()
    elif product == "latest-product":
        product_details = Home(driver).select_latest_products()
    select_item_index = random.randint(1, product_details[1])
    driver.find_element_by_xpath(product_details[0].format(str(select_item_index))).click()


@when(parsers.parse("I add an {product} to the cart"))
def add_item(driver):
    """This method is used to add the product to cart"""
    Product(driver).add_to_cart.click()


@when("I click the view_cart button")
def click_view_cart(driver):
    """This method is used to click the view_cart button"""
    Product(driver).view_card.click()


@then("I validate the product_to_checkout button is clickable")
def click_checkout(driver):
    """This method is used to click the checkout button in cart page"""
    Cart(driver).validate_cart_page()
    Cart(driver).product_to_checkout.click()
