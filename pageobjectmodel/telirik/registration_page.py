import random

from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.select import Select
from constants.telirik.constant import Constant


class Registration:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker()

    email_loc = (By.XPATH, "//input[@id='Email-1']")
    first_name_loc = (By.XPATH, "//input[@id='Textbox-1']")
    last_name_loc = (By.XPATH, "//input[@id='Textbox-2']")
    company_name_loc = (By.XPATH, "//input[@id='Textbox-3']")
    country_commen_loc = (By.XPATH, "//select[@id='Country-1']")
    countries_loc = (By.XPATH, "//select[@id='Country-1']/option")
    phone_number_loc = (By.XPATH, "//input[@id='Textbox-4']")
    create_account_button_loc = (By.XPATH, "//button[normalize-space()='Create account']")

    @property
    def email(self):
        return self.driver.find_element(*self.email_loc)

    @property
    def first_name(self):
        return self.driver.find_element(*self.first_name_loc)

    @property
    def last_name(self):
        return self.driver.find_element(*self.last_name_loc)

    @property
    def company_name(self):
        return self.driver.find_element(*self.company_name_loc)

    @property
    def common_country(self):
        return self.driver.find_element(*self.country_commen_loc)

    @property
    def countries(self):
        return self.driver.find_elements(*self.countries_loc)

    @property
    def phone_number(self):
        return self.driver.find_element(*self.phone_number_loc)

    @property
    def create_account_button(self):
        return self.driver.find_element(*self.create_account_button_loc)

    def create_account(self):
        """This method is used to create account"""
        self.email.send_keys(self.fake.email())
        self.first_name.send_keys(self.fake.first_name())
        self.last_name.send_keys(self.fake.last_name())
        self.company_name.send_keys(self.fake.company())
        sel = Select(self.common_country)
        sel.select_by_index(random.randrange(1, len(self.countries)))
        self.phone_number.send_keys(self.fake.phone_number())
        self.driver.execute_script(Constant.WINDOW_SCROLL_SCRIPT)
        self.create_account_button.click()
