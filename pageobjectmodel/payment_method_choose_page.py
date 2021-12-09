from selenium.webdriver.common.by import By
from constants.constant import Constant


class Payment_method:
    def __init__(self, driver):
        self.driver = driver

    payment_method_choose_page_heading_loc = (By.XPATH, "//h1[@class='page-heading']")
    pay_by_bank_wire_method_loc = (By.XPATH, "//a[@title='Pay by bank wire']")

    @property
    def payment_method_choose_page_heading(self):
        return self.driver.find_element(*self.payment_method_choose_page_heading_loc)

    @property
    def pay_by_bank_wire_method(self):
        return self.driver.find_element(*self.pay_by_bank_wire_method_loc)

    def validate_payment_method_page_heading(self):
        """This method is used to validate payment method choose page"""
        assert self.payment_method_choose_page_heading.text == Constant.PAYMENT_METHOD_PAGE_TITLE

    def click_payment_method(self):
        """This method is used to click pay by bank wire method"""
        self.pay_by_bank_wire_method.click()
