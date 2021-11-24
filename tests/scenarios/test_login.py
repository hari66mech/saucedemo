from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

import pytest
from constants.constant import Constant
from pageobjectmodel.login import Login
import random

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/saucedemo/tests/features/login.feature")


@pytest.fixture
def driver():
    browser = webdriver.Chrome(Constant.DRIVER_PATH)
    yield browser
    browser.quit()


@given('I am launching chrome browser')
def home(driver):
    driver.get(Constant.HOME_PAGE_URL)


@when("Login as the standard_user credential")
def login(driver):
    driver.maximize_window()
    # userName
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(Login.student_user_text)
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


@then("Redirect to the card page")
def results(driver):
    assert driver.title == Constant.CARD_PAGE_TITLE
    assert driver.current_url == Constant.CARD_PAGE_URL
