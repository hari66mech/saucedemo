from selenium.webdriver.common.by import By
from constants.constant import Constant


class Shipping:
    def __init__(self, driver):
        self.driver = driver

    shipping_page_heading_loc = (By.XPATH, "//h1[@class='page-heading']")
    checkout_loc = (By.XPATH, "//button[@name='processCarrier']//i[@class='icon-chevron-right right']")
    agreement_accept_box_loc = (By.XPATH, "//input[@id='cgv']")

    @property
    def shipping_page_heading(self):
        return self.driver.find_element(*self.shipping_page_heading_loc)

    @property
    def checkout(self):
        return self.driver.find_element(*self.checkout_loc)

    @property
    def agreement_accept_box(self):
        return self.driver.find_element(*self.agreement_accept_box_loc)

    def click_agreement_box(self):
        """This method is used to select agreement box on the shipping page"""
        self.agreement_accept_box.click()

    def validate_shipping_page_heading(self):
        """This method is used to validate shipping page"""
        assert self.shipping_page_heading.text == Constant.SHIPPING_PAGE_TITLE

    def click_shipping_page_checkout_button(self):
        """This method is used to click checkout button on the shipping page"""
        self.checkout.click()
