from pytest_bdd import scenarios, when, then, parsers
from pageobjectmodel.phptravels.order_page import Order
from pageobjectmodel.phptravels.order_confirm import Order_Confirm
from pageobjectmodel.phptravels.features_page import Features

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/phptravels")


@when(parsers.parse("I click the {button} button on {page}"))
def click_pricing_heading(driver, button):
    """This method is used to click the button"""
    global order
    order = Order(driver)
    if button == "pricing":
        order.pricing.click()
    elif button == "buy_now":
        order.buy_now_button.click()
    else:
        raise NotImplementedError


@when(parsers.parse("I select the {plan} on order page"))
def plans_selection(plan):
    """This method is used to select the plan randomly"""
    order.select_plan(plan)


@when("I select the main_features in features on home_page")
def click_main_features_under_features(driver):
    """This method is used to click main_features in sub-heading"""
    global feature
    feature = Features(driver)
    feature.click_main_features()


@when("I get the features on features_page")
def get_web_features():
    """This method is used to get features from the features_page"""
    feature.get_features()


@then("I validate the order_confirm page navigation")
def verify_order_confirm_text(driver):
    """This method is used to validate order confirmation text"""
    Order_Confirm(driver).validate_order_confirm_text()


@then("I validate the text summary features with the web features result")
def compare_text_features_with_web_features():
    """This method is used to compare text file data with web features"""
    feature.get_txt_file_features()
    feature.validate_features()
