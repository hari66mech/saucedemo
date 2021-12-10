from selenium.webdriver.common.by import By
from faker import Faker


class Sign_up:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker()

    user_name_loc = (By.XPATH, "//input[@id='sign-username']")
    password_loc = (By.XPATH, "//input[@id='sign-password']")
    sign_up_button_loc = (By.XPATH, "//button[normalize-space()='Sign up']")

    @property
    def user_name(self):
        return self.driver.find_element(*self.user_name_loc)

    @property
    def user_password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def sign_up_button(self):
        return self.driver.find_element(*self.sign_up_button_loc)

    def sign_up(self):
        "This method is used to enter the user data"
        user_name = self.fake.name()
        user_password = self.fake.password()
        credential = [user_name, user_password]
        self.user_name.send_keys(user_name)
        self.user_password.send_keys(user_password)
        self.sign_up_button.click()
        self.driver.switch_to.alert.accept()
        return credential
