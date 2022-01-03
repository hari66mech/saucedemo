import pytest
from pytest_bdd import given
from selenium import webdriver
from constants.phptravels.constant import Constant


@pytest.fixture
def driver():
    """This method is used to open and close the driver in BrowserStack"""
    desired_cap = {
        'os_version': '10',
        'resolution': '1920x1080',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'os': 'Windows',
        'name': 'phptravels Test',
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


@given("The phptravels home page is displayed")
def get_home_page(driver):
    """This method is used to get home page url"""
    driver.get(Constant.HOME_PAGE)
