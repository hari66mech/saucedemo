from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class SignUp:
    def __init__(self, driver):
        self.driver = driver

    first_name_loc = (By.XPATH, "//input[@id='input_comp-kaoxkn4j']")
    last_name_loc = (By.XPATH, "//input[@id='input_comp-kaoxkn4o']")
    email_loc = (By.XPATH, "//input[@id='input_comp-kaoxkn4s']")
    password_loc = (By.XPATH, "//input[@id='input_comp-kaoxkn4w']")
    mobile_number_loc = (By.XPATH, "//input[@id='input_comp-kaoxr1ae']")
    work_city_loc = (By.XPATH, "//input[@id='input_comp-karpvdv0']")
    sign_up_button_loc = (By.XPATH, "//button[@class='_1fbEI']")
    login_button_loc = (By.XPATH, "//span[@class='color_15']//span//span[contains(text(),'Log In')]")
    sign_up_title_loc = (By.XPATH, "//span[normalize-space()='Sign Up']")

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
    def mobile_number(self):
        return self.driver.find_element(*self.mobile_number_loc)

    @property
    def work_city(self):
        return self.driver.find_element(*self.work_city_loc)

    @property
    def sign_up_button(self):
        return self.driver.find_element(*self.sign_up_button_loc)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_loc)

    @property
    def sign_up_title(self):
        return self.driver.find_element(*self.sign_up_title_loc)

    def validate_sign_up_title(self):
        """This method is used to validate signup page title"""
        assert self.sign_up_title.text == Constant.SIGN_UP_TEXT

    def registration(self, credential):
        """This method is used to register as a new user"""
        self.first_name.send_keys(credential["first_name"])
        self.last_name.send_keys(credential["last_name"])
        self.email.send_keys(credential["email"])
        self.password.send_keys(credential["password"])
        self.mobile_number.send_keys(credential["mobile_number"])
        self.work_city.send_keys(credential["work_city"])
        self.sign_up_button.click()
