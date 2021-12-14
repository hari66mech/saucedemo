from selenium.webdriver.common.by import By
from faker import Faker


class Login:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker()

    user_name_loc = (By.XPATH, "//input[@id='loginusername']")
    password_loc = (By.XPATH, "//input[@id='loginpassword']")
    login_button_loc = (By.XPATH, "//button[normalize-space()='Log in']")

    @property
    def user_name(self):
        return self.driver.find_element(*self.user_name_loc)

    @property
    def user_password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_loc)

    def login(self, credential):
        "This method is used to login as a valid user"
        self.user_name.send_keys(credential["user_name"])
        self.user_password.send_keys(credential["user_password"])
        self.login_button.click()
