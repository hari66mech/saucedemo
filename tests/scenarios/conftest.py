import pytest
from pytest_bdd import given
from selenium import webdriver
from constants.constant import Constant
from driver.config import Config
from msedge.selenium_tools import Edge, EdgeOptions

from tests.factories.factories import CredentialFactory


class BrowserError(Exception):
    def __init__(self, value):
        self.value = value


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    try:
        if Config.DRIVER == "chrome":
            chromeOptions = webdriver.ChromeOptions()
            if Config.HEADLESS:
                chromeOptions.add_argument('--headless')
            driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH, chrome_options=chromeOptions)
        elif Config.DRIVER == "firefox":
            fireFoxOptions = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                fireFoxOptions.add_argument('--headless')
            driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH, firefox_options=fireFoxOptions)
        elif Config.DRIVER == "msedge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            if Config.HEADLESS:
                edge_options.add_argument('--headless')
            driver = Edge(executable_path=Config.MS_EDGE_DRIVER_PATH, options=edge_options)
        else:
            raise BrowserError(Config.DRIVER + " browser is not found")
    except BrowserError:
        driver.quit()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def credential(driver):
    """This method is used to get fake data with help of factory-boy"""
    data = CredentialFactory()
    credential = {
        "first_name": data.first_name,
        "last_name": data.last_name,
        "email": data.email,
        "telephone": data.phone_number,
        "user_password": data.password
    }
    return credential


@given("The tutorialsninja index page is displayed")
def get_index_page(driver):
    """This method is used to get index page url"""
    driver.get(Constant.HOME_PAGE_URL)
