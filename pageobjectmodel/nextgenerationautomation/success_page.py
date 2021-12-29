from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class Success:
    def __init__(self, driver):
        self.driver = driver

    success_message_loc = (By.XPATH, "//div[@data-testid='description']")

    @property
    def success_message(self):
        return self.driver.find_element(*self.success_message_loc)

    def validate_success_message(self, credential):
        """This method used to validate success message"""
        assert Constant.SUCCESS_MESSAGE.format(credential["email"]) == self.success_message.text
