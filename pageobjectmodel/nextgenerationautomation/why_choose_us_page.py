from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class WhyChooseUs:
    def __init__(self, driver):
        self.driver = driver

    why_choose_us_loc = (By.XPATH, "//span[contains(text(),'Why Choose Us ?')]")

    @property
    def why_choose_us(self):
        return self.driver.find_element(*self.why_choose_us_loc)

    def validate_why_choose_us_title(self):
        """This method is used to validate why_choose_us page title"""
        assert self.why_choose_us.text == Constant.WHY_CHOOSE_US_TEXT
