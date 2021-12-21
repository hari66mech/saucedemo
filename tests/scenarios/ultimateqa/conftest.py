import pytest
from pytest_bdd import given
from selenium import webdriver
from constant.constant import Constant
from factory_data.credential_factory import CredentialFactory


@pytest.fixture
def driver():
    """This method is used to open and close the driver in BrowserStack"""
    desired_cap = {
        'os_version': '10',
        'resolution': '1920x1080',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'os': 'Windows',
        'name': 'demoblaze Test',
        'build': 'BStack Build Number 1'
    }
    driver = webdriver.Remote(
        command_executor='https://hari_cDyQgX:KK4yDhfEoVqqS9sXoBBh@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    return driver


@pytest.fixture()
def credential(driver):
    """This method is used to call the factory boy credential"""
    data = CredentialFactory()
    credential = {
        "first_name": data.first_name,
        "last_name": data.last_name,
        "email": data.email,
        "password": data.password
    }
    return credential


@given("The ultimateqa index page is displayed")
def get_index_page(driver):
    """This method is used to get index page url"""
    driver.get(Constant.INDEX_PAGE_URL)
