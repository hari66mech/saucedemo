from pytest_bdd import scenarios, when, then

from constants.constant import Constant
from pageobjectmodel.login import Login
import random

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/saucedemo/tests/features/login.feature")


@when("I login with the standard_user credentials", target_fixture="home_page")
def login_standard_user(driver):
    driver.maximize_window()
    # userName
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(Constant.STANDARD_USER)
    # password
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(Constant.PASSWORD)
    # login
    login_button = driver.find_element_by_xpath(Login.login_button_loc)
    login_button.click()
    home_page_url = driver.current_url
    return home_page_url


@when("I validate the home page")
def validate_home_page(home_page):
    assert home_page == Constant.HOME_PAGE_URL


@when("I add random item to cart")
def add_random_item(driver):
    # random selection
    driver.find_element_by_xpath(Login.add_card_loc.format(random.randrange(1, 7))).click()
    # navigate to card page
    driver.find_element_by_xpath(Login.shopping_bucket_icon_loc).click()


@when("I Login with the locked_out_user credential")
def login_locked_out_user(driver):
    # userName
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(Constant.LOCKED_OUT_USER)
    # password
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(Constant.PASSWORD)
    # login
    login_button = driver.find_element_by_xpath(Login.login_button_loc)
    login_button.click()


@then("I validate the error message")
def results(driver):
    error_text = driver.find_element_by_xpath(Login.error_text_loc).text
    assert error_text == Constant.ERROR_TEXT


@then("I validate the cart page")
def results(driver):
    assert driver.title == Constant.CART_PAGE_TITLE
    assert driver.current_url == Constant.CART_PAGE_URL
