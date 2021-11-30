import pytest

from selenium import webdriver
from constants.constant import Constant


@pytest.fixture
def driver():
    """This method is used to open and close the chrome driver"""
    driver = webdriver.Chrome(Constant.DRIVER_PATH)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
