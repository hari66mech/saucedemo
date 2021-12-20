from pytest_bdd import scenarios, when, then
from pageobjectmodel.home_page import Home
from pageobjectmodel.product_page import Product

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/tutorialsninja/tests/features")


@when("I get product from the text file")
def get_text_summary_data(driver):
    "This method is used to get products from the product.txt file"
    Home(driver).get_products()


@then("I validate the text items summary with the web item results")
def verify_web_items(driver):
    "This method is used to compare text summary data with web items"
    Home(driver).validate_products()


@when("I click the product from the home_page")
def click_product(driver):
    "This method is used to select item"
    Home(driver).apple_cinema.click()


@when("I fill the product options for placing an order")
def fill_available_options(driver, fake_text):
    "This method is used to fill available options"
    Product(driver).fill_available_options(fake_text)


@then("I validate success message")
def validate_success_message(driver):
    "This method is used to validate success message"
    Product(driver).verify_success_message()
