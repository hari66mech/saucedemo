from selenium.webdriver.common.by import By
from constants.constant import Constant


class Login:
    def __init__(self, driver):
        self.driver = driver

    user_name_loc = (By.XPATH, "//input[@id='user-name']")
    password_loc = (By.XPATH, "//input[@id='password']")
    login_button_loc = (By.XPATH, "//input[@id='login-button']")

    @property
    def user_name(self):
        return self.driver.find_element(*self.user_name_loc)

    @property
    def password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_loc)

    def login(self):
        """This method is used to login with standard credential"""
        self.user_name.send_keys(Constant.STANDARD_USER)
        self.password.send_keys(Constant.PASSWORD)
        self.login_button.click()
        