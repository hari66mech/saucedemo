from selenium.webdriver.common.by import By
from constants.constant import Constant


class Payment:
    def __init__(self, driver):
        self.driver = driver

    payment_page_heading_loc = (By.XPATH, "//span[@class='navigation_page']")
    confirm_order_button_loc = (By.XPATH, "//span[normalize-space()='I confirm my order']")

    @property
    def payment_page_heading(self):
        return self.driver.find_element(*self.payment_page_heading_loc)

    @property
    def confirm_order_button(self):
        return self.driver.find_element(*self.confirm_order_button_loc)

    def validate_payment_page_heading(self):
        """This method is used to validate payment page"""
        assert self.payment_page_heading.text == Constant.PAYMENT_PAGE_TITLE

    def click_confirm_order_button(self):
        """This method is used to click confirm order button on payment page"""
        self.confirm_order_button.click()
