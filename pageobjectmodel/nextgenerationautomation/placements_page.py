from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class Placements:
    def __init__(self, driver):
        self.driver = driver

    placements_loc = (By.XPATH, "//span[contains(text(),'Placements')]")

    @property
    def placements(self):
        return self.driver.find_element(*self.placements_loc)

    def validate_placements_title(self):
        """This method is used to validate placements page title"""
        assert self.placements.text == Constant.PLACEMENTS_TEXT
