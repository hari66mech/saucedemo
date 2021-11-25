import pytest
from selenium import webdriver
from constants.constant import Constant
from pytest_bdd import given


@pytest.fixture
def driver():
    driver = webdriver.Chrome(Constant.DRIVER_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()


@given('The saucedemo login page is displayed')
def home(driver):
    driver.get(Constant.LOGIN_PAGE_URL)
