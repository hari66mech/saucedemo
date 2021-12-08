import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from constants.config import Config
from constants.saucedemo.sauce_constant import Sauce_constant
from constants.telirik.telerik_constant import Telerik_constant
from pytest_bdd import given, parsers


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    if Config.DRIVER == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif Config.DRIVER == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given(parsers.parse("The {application} page is displayed"))
def get_login_page(driver, application):
    """This method is used get login page url"""
    if application == "saucedemo_login":
        driver.get(Sauce_constant.LOGIN_PAGE_URL)
    elif application == "telerik_demo":
        driver.get(Telerik_constant.DEMO_PAGE_URL)
