from selenium.webdriver.common.by import By
from faker import Faker


class Sign_in:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker()

    email_loc = (By.XPATH, "//input[@id='email_create']")
    create_an_account_button_loc = (By.XPATH, "//span[normalize-space()='Create an account']")

    @property
    def email(self):
        return self.driver.find_element(*self.email_loc)

    @property
    def create_an_account(self):
        return self.driver.find_element(*self.create_an_account_button_loc)

    def enter_email_id(self):
        """This method is used to enter email_id"""
        self.email.send_keys(self.fake.email())

    def click_account_create_button(self):
        """This method is used to click account create button"""
        self.create_an_account.click()
