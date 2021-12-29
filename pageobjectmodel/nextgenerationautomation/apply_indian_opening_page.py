from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class ApplyIndianOpening:
    def __init__(self, driver):
        self.driver = driver

    grow_india_model_loc = (By.XPATH, "//span[@class='color_24']//span[contains(text(),'Grow India Model')]")

    @property
    def grow_india_model(self):
        return self.driver.find_element(*self.grow_india_model_loc)

    def validate_apply_india_opening_title(self):
        """This method is used to validate apply_indian_opening page title"""
        assert self.grow_india_model.text == Constant.APPLY_INDIAN_OPENING_TEXT
