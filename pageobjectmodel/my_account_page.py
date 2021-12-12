from selenium.webdriver.common.by import By
from constants.constant import Constant


class My_account:
    def __init__(self, driver):
        self.driver = driver

    page_title_loc = (By.XPATH, "//h1[@class='page-heading']")
    welcome_message_loc = (By.XPATH, "//p[@class='info-account']")
    home_button_loc = (By.XPATH, "//span[normalize-space()='Home']")

    @property
    def page_title(self):
        return self.driver.find_element(*self.page_title_loc)

    @property
    def welcome_message(self):
        return self.driver.find_element(*self.welcome_message_loc)

    @property
    def home_button(self):
        return self.driver.find_element(*self.home_button_loc)

    def validate_my_account_page(self):
        """This method is used to validate my account page"""
        assert self.page_title.text == Constant.MY_ACCOUNT_PAGE_TITLE
        assert self.welcome_message.text == Constant.WELCOME_MESSAGE

    def click_home_button(self):
        """This method is used to click home button on my account page"""
        self.home_button.click()
