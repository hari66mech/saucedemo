from selenium.webdriver.common.by import By
from constants.constant import Constant


class Order_confirmation:
    def __init__(self, driver):
        self.driver = driver

    order_confirmation_page_heading_loc = (By.XPATH, "//span[@class='navigation_page']")
    order_confirmation_text_loc = (By.XPATH, "//strong[normalize-space()='Your order on My Store is complete.']")

    @property
    def order_confirmation_page_heading(self):
        return self.driver.find_element(*self.order_confirmation_page_heading_loc)

    @property
    def order_confirmation_text(self):
        return self.driver.find_element(*self.order_confirmation_text_loc)

    def validate_order_confirmation_page(self):
        """This method is used to validate the order confirmation page"""
        assert self.order_confirmation_page_heading.text == Constant.ORDER_CONFIRMATION_PAGE_TITLE
        assert self.order_confirmation_text.text == Constant.ORDER_CONFIRMATION_TEXT
