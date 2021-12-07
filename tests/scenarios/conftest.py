import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest_bdd import given
from constants.constant import Constant


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    global driver
    if Constant.DRIVER == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif Constant.DRIVER == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given('The jpetstore demo login page is displayed')
def login_page(driver):
    """This method is used to go to the login page"""
    driver.get(Constant.LOGIN_PAGE_URL)
