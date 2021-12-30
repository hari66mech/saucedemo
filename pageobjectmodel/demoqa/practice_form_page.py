import random
from selenium.webdriver.common.by import By


class PracticeForm:
    def __init__(self, driver):
        self.driver = driver

    first_name_loc = (By.XPATH, "//input[@id='firstName']")
    last_name_loc = (By.XPATH, "//input[@id='lastName']")
    email_loc = (By.XPATH, "//input[@id='userEmail']")
    gender_loc = (By.XPATH, "//div[@id='genterWrapper']//div/label")
    mobile_number_loc = (By.XPATH, "//input[@id='userNumber']")
    current_address_loc = (By.XPATH, "//textarea[@id='currentAddress']")
    submit_button_loc = (By.XPATH, "//button[@id='submit']")
    select_gender_loc = "//div[@id='genterWrapper']//div[{0}]/label"

    @property
    def first_name(self):
        return self.driver.find_element(*self.first_name_loc)

    @property
    def last_name(self):
        return self.driver.find_element(*self.last_name_loc)

    @property
    def email(self):
        return self.driver.find_element(*self.email_loc)

    @property
    def gender(self):
        return self.driver.find_elements(*self.gender_loc)

    @property
    def number_of_gender(self):
        return len(self.gender)

    @property
    def mobile_number(self):
        return self.driver.find_element(*self.mobile_number_loc)

    @property
    def current_address(self):
        return self.driver.find_element(*self.current_address_loc)

    @property
    def submit_button(self):
        return self.driver.find_element(*self.submit_button_loc)

    def fill_form(self, credential):
        """This method is used to fill the practice form"""
        self.first_name.send_keys(credential["first_name"])
        self.last_name.send_keys(credential["last_name"])
        self.email.send_keys(credential["email"])
        select_item_index = random.randint(1, self.number_of_gender)
        self.driver.find_element_by_xpath(self.select_gender_loc.format(str(select_item_index))).click()
        self.mobile_number.send_keys(credential["mobile_number"])
        self.current_address.send_keys(credential["address"])

    def click_submit(self):
        """this method is used to validate the submit button is clickable"""
        self.submit_button.click()
