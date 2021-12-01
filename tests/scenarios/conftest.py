import pytest

from selenium import webdriver
from driver.config import Config


@pytest.fixture
def driver():
    driver = webdriver.Chrome(Config.DRIVER_PATH)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
