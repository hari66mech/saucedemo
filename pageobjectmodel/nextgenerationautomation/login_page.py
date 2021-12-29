from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    email_loc = (By.XPATH, "//input[@id='input_input_emailInput_SM_ROOT_COMP17']")
    password_loc = (By.XPATH, "//input[@id='input_input_passwordInput_SM_ROOT_COMP17']")
    login_button_loc = (By.XPATH, "//button[@class='_1fbEI']")
    login_with_email_loc = (By.XPATH, "//span[normalize-space()='Log in with Email']")

    @property
    def email(self):
        return self.driver.find_element(*self.email_loc)

    @property
    def password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_loc)

    @property
    def login_with_email(self):
        return self.driver.find_element(*self.login_with_email_loc)

    def login(self, email, password):
        """This method used to login as a user credential"""
        self.email.send_keys(email)
        self.password.send_keys(password)
