from selenium.webdriver.common.by import By
from constants.telirik.telerik_constant import Telerik_constant


class Registration_success:
    def __init__(self, driver):
        self.driver = driver

    thank_you_message_loc = (By.XPATH, "//h1[@class='Title Title--xxxl Title--slim u-mt4']")

    @property
    def thank_you_message(self):
        return self.driver.find_element(*self.thank_you_message_loc)

    def validate_thank_you_message(self):
        """This method is used to validate the success message"""
        assert self.thank_you_message.text == Telerik_constant.THANK_YOU_MESSAGE
