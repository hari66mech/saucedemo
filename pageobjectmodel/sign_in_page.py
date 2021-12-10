from selenium.webdriver.common.by import By
from faker import Faker


class Sign_in:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker()

    email_loc = (By.XPATH, "//input[@id='email_create']")
    create_an_account_button_loc = (By.XPATH, "//span[normalize-space()='Create an account']")
    registered_email_id_loc = (By.XPATH, "//input[@id='email']")
    registered_password_loc = (By.XPATH, "//input[@id='passwd']")
    sign_in_button_loc = (By.XPATH, "//span[normalize-space()='Sign in']")

    @property
    def email(self):
        return self.driver.find_element(*self.email_loc)

    @property
    def create_an_account(self):
        return self.driver.find_element(*self.create_an_account_button_loc)

    @property
    def registered_email_id(self):
        return self.driver.find_element(*self.registered_email_id_loc)

    @property
    def registered_password(self):
        return self.driver.find_element(*self.registered_password_loc)

    @property
    def sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_loc)

    def click_create_an_account(self):
        """This method is used to create an account"""
        mail = self.fake.email()
        self.email.send_keys(mail)

        self.create_an_account.click()
        return mail


    def get_credentials(self):
        """This method is used to get the credentials in .txt file"""
        global credentials
        file = open("credentials.txt", "r")
        credentials = file.read().split(",")
        file.close()

    def sign_in(self):
        """This method is used to perform the sign-in action"""
        self.registered_email_id.send_keys(credentials[0])
        self.registered_password.send_keys(credentials[1])
        self.sign_in_button.click()
