from selenium.webdriver.common.by import By
from constants.constant import Constant


class Success:
    def __init__(self, driver):
        self.driver = driver

    success_message_loc = (By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")

    @property
    def success_message(self):
        return self.driver.find_element(*self.success_message_loc)

    def validate_success_message(self):
        """This method is used to validate the success message"""
        assert self.success_message.text == Constant.SUCCESS_MESSAGE
