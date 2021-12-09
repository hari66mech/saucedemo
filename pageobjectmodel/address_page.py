from selenium.webdriver.common.by import By
from constants.constant import Constant


class Address:
    def __init__(self, driver):
        self.driver = driver

    address_page_heading_loc = (By.XPATH, "//h1[@class='page-heading']")
    checkout_loc = (By.XPATH, "//button[@type='submit']/span/i")

    @property
    def address_page_heading(self):
        return self.driver.find_element(*self.address_page_heading_loc)

    @property
    def checkout(self):
        return self.driver.find_element(*self.checkout_loc)

    def validate_address_page_heading(self):
        """This method is used to validate the address page"""
        assert self.address_page_heading.text == Constant.ADDRESS_PAGE_TITLE

    def click_address_page_checkout_button(self):
        """This method is used to click the checkout button on the address page"""
        self.checkout.click()
