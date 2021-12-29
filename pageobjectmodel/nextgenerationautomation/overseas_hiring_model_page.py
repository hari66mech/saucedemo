from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class OverseasHiringModel:
    def __init__(self, driver):
        self.driver = driver

    overseas_hiring_model_loc = (By.XPATH, "//span[@class='color_24']//span[contains(text(),'Overseas Hiring Model')]")

    @property
    def overseas_hiring_model(self):
        return self.driver.find_element(*self.overseas_hiring_model_loc)

    def validate_overseas_hiring_model_title(self):
        """This method is used to validate overseas_hiring_model page title"""
        assert self.overseas_hiring_model.text == Constant.OVERSEAS_HIRING_MODEL_TEXT
