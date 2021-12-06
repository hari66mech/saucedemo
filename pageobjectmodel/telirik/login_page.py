from selenium.webdriver.common.by import By
from constants.telirik.constant import Constant


class Login:
    def __init__(self, driver):
        self.driver = driver

    create_account_link_loc = (By.XPATH, "//a[contains(@class,'u-ff-sans1 u-pr2 js-open-register-panel')]")

    @property
    def create_account_link(self):
        return self.driver.find_element(*self.create_account_link_loc)

    def click_create_account_link(self):
        """This method is used to click create account link"""
        self.driver.execute_script(Constant.WINDOW_SCROLL_SCRIPT)
        self.create_account_link.click()
