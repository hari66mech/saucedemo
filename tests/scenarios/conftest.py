import pytest
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from driver.config import Config


class DriverError(Exception):
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
            firefoxOptions = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                firefoxOptions.add_argument('--headless')
            driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH, firefox_options=firefoxOptions)
        elif Config.DRIVER == "msedge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            if Config.HEADLESS:
                edge_options.add_argument('--headless')
            driver = Edge(executable_path=Config.MS_EDGE_DRIVER_PATH, options=edge_options)
        else:
            raise DriverError("the {driverName} driver is not found".format(driverName=Config.DRIVER))
    except DriverError:
        driver.quit()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
