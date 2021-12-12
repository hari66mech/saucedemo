from selenium.webdriver.common.by import By
from constants.constant import Constant


class Shopping_cart:
    def __init__(self, driver):
        self.driver = driver

    shopping_cart_heading_loc = (By.XPATH, "//span[@class='navigation_page']")
    checkout_loc = (By.XPATH,
                    "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]")

    @property
    def shopping_cart_heading(self):
        return self.driver.find_element(*self.shopping_cart_heading_loc)

    @property
    def checkout(self):
        return self.driver.find_element(*self.checkout_loc)

    def validate_shopping_cart_heading(self):
        """This method is used to validate shopping cart page"""
        assert self.shopping_cart_heading.text == Constant.SHOPPING_CART_HEADING

    def click_checkout_button(self):
        """This method is used to click checkout button on the shopping cart page"""
        self.checkout.click()
