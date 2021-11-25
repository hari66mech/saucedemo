from pytest_bdd import scenarios, when, then

from constants.constant import Constant
from pageobjectmodel.login import Login
import random

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/saucedemo/tests/features/login.feature")


@when("Login as the standard_user credential", target_fixture="home_page")
def login(driver):
    home_page_url = driver.current_url
    driver.maximize_window()
    # userName
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(Login.standard_user_text)
    # password
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(Login.login_password_text)
    # login
    login_button = driver.find_element_by_xpath(Login.login_button_loc)
    login_button.click()
    # random selection
    driver.find_element_by_xpath(Login.Add_card_loc.format(random.randrange(1, 7))).click()
    # navigate to card page
    driver.find_element_by_xpath(Login.shopping_bucket_icon_loc).click()
    return home_page_url


@when("Validate the home page")
def validate_home_page(home_page):
    assert home_page == Constant.HOME_PAGE_URL


@when("Login as the locked_out_user credential")
def login(driver):
    # userName
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(Login.locked_out_user_text)
    # password
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(Login.login_password_text)
    # login
    login_button = driver.find_element_by_xpath(Login.login_button_loc)
    login_button.click()


@then("Validate error message")
def results(driver):
    error_text = driver.find_element_by_xpath(Login.error_text_loc).text
    assert error_text == "Epic sadface: Sorry, this user has been locked out."


@then("Redirect to the cart page")
def results(driver):
    assert driver.title == Constant.CARD_PAGE_TITLE
    assert driver.current_url == Constant.CARD_PAGE_URL
