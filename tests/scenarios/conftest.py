import pytest

from selenium import webdriver
from driver.config import Config
from pytest_bdd import given
from constants.constant import Constant


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    driver = webdriver.Chrome(Config.DRIVER_PATH)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given('The jpetstore demo login page is displayed')
def login_page(driver):
    """This method is used to go to the login page"""
    driver.get(Constant.LOGIN_PAGE_URL)
