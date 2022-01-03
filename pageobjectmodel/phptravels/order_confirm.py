from selenium.webdriver.common.by import By
from constants.phptravels.constant import Constant


class Order_Confirm:
    def __init__(self, driver):
        self.driver = driver

    __order_confirm_loc = (By.XPATH, "//div[contains(text(),'Confirm Order')]")

    @property
    def order_confirm(self):
        return self.driver.find_element(*self.__order_confirm_loc)

    def validate_order_confirm_text(self):
        """This method is used to validate order confirmation text"""
        assert self.order_confirm.text == Constant.ORDER_CONFIRM_TEXT
