from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver):
        self.driver = driver

    first_name_loc = (By.XPATH, "//input[@id='input-firstname']")
    last_name_loc = (By.XPATH, "//input[@id='input-lastname']")
    email_loc = (By.XPATH, "//input[@id='input-email']")
    telephone_loc = (By.XPATH, "//input[@id='input-telephone']")
    password_loc = (By.XPATH, "//input[@id='input-password']")
    confirm_password_loc = (By.XPATH, "//input[@id='input-confirm']")
    privacy_policy_loc = (By.XPATH, "//input[@name='agree']")
    continue_button_loc = (By.XPATH, "//input[@value='Continue']")

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
    def telephone(self):
        return self.driver.find_element(*self.telephone_loc)

    @property
    def password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def confirm_password(self):
        return self.driver.find_element(*self.confirm_password_loc)

    @property
    def privacy_policy(self):
        return self.driver.find_element(*self.privacy_policy_loc)

    @property
    def continue_button(self):
        return self.driver.find_element(*self.continue_button_loc)

    def register(self, credential):
        """This method is used to create the account"""
        self.first_name.send_keys(credential["first_name"])
        self.last_name.send_keys(credential["last_name"])
        self.email.send_keys(credential["email"])
        self.telephone.send_keys(credential["telephone"])
        self.password.send_keys(credential["user_password"])
        self.confirm_password.send_keys(credential["user_password"])
        self.privacy_policy.click()
        self.continue_button.click()
