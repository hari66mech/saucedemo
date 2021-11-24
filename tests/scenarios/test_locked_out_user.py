import time

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from constants.constant import Constant
from pageobjectmodel.login import Login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/saucedemo/tests/features/locked_out_user.feature")


@pytest.fixture
def driver():
    browser = webdriver.Chrome(Constant.DRIVER_PATH)
    yield browser
    browser.quit()


@given('I am launching chrome browser')
def home(driver):
    driver.get(Constant.HOME_PAGE_URL)


@when("Login as the locked_out_user credential", target_fixture="error_text")
def login(driver):
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    # userName
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(Login.locked_out_user_text)
    # password
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(Login.login_password_text)
    # login
    login_button = driver.find_element_by_xpath(Login.login_button_loc)
    login_button.click()
    # error text
    error = driver.find_element_by_xpath(Login.error_text_loc).text
    return error


@then("Validate error message")
def results(error_text):
    assert error_text == "Epic sadface: Sorry, this user has been locked out."