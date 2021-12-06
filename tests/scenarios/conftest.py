import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from constants.constant import Constant


@pytest.fixture
def driver():
    """This method is used to open and close the driver"""
    if Constant.DRIVER == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif Constant.DRIVER == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
