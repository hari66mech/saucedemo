import pytest
from pytest_bdd import given
from selenium import webdriver
from constants.constant import Constant
from driver.config import Config


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    try:
        if Config.DRIVER == "chrome":
            driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH)
        elif Config.DRIVER == "firefox":
            driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
        elif Config.DRIVER == "msedge":
            driver = webdriver.Edge(Config.MS_EDGE_DRIVER_PATH)
        else:
            raise RuntimeError
    except RuntimeError:
        pass
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given("The automationpractice index page is displayed")
def get_index_page(driver):
    """This method is used get index page url"""
    driver.get(Constant.INDEX_PAGE)
