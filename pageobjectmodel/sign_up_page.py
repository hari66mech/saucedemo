from selenium.webdriver.common.by import By


class Signup:
    def __init__(self, driver):
        self.driver = driver

    first_name_loc = (By.XPATH, "//input[@id='user[first_name]']")
    last_name_loc = (By.XPATH, "//input[@id='user[last_name]']")
    email_loc = (By.XPATH, "//input[@id='user[email]']")
    password_loc = (By.XPATH, "//input[@id='user[password]']")
    agreement_checkbox_loc = (By.XPATH, "//input[@id='user[terms]']")
    sign_up_button_loc = (By.XPATH, "//input[@value='Sign up']")

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
    def password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def agreement_checkbox(self):
        return self.driver.find_element(*self.agreement_checkbox_loc)

    @property
    def sign_up_button(self):
        return self.driver.find_element(*self.sign_up_button_loc)

    def registration(self, credential):
        """This method is used to register as a user"""
        self.first_name.send_keys(credential["first_name"])
        self.last_name.send_keys(credential["last_name"])
        self.email.send_keys(credential["email"])
        self.password.send_keys(credential["password"])
        self.agreement_checkbox.click()
        self.sign_up_button.click()
