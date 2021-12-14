import pytest
from faker import Faker
from pytest_bdd import given
from selenium import webdriver
from constants.constant import Constant
from driver.config import Config
from msedge.selenium_tools import Edge, EdgeOptions


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    try:
        if Config.DRIVER == "chrome":
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_argument('--headless')
            driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH, chrome_options=chromeOptions)
        elif Config.DRIVER == "firefox":
            fireFoxOptions = webdriver.FirefoxOptions()
            fireFoxOptions.add_argument('--headless')
            driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH, firefox_options=fireFoxOptions)
        elif Config.DRIVER == "msedge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument('--headless')
            driver = Edge(executable_path=Config.MS_EDGE_DRIVER_PATH, options=edge_options)
        else:
            raise RuntimeError
    except RuntimeError:
        pass
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def credential(driver):
    """This method is used to generate fake data for user details"""
    fake = Faker()
    credential = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "telephone": fake.msisdn(),
        "user_password": fake.password()
    }
    return credential


@given("The tutorialsninja index page is displayed")
def get_index_page(driver):
    """This method is used to get index page url"""
    driver.get(Constant.HOME_PAGE_URL)
