from selenium.webdriver.common.by import By
from constants.competethemes.constant import Constant


class Cart:
    def __init__(self, driver):
        self.driver = driver

    cart_title_loc = (By.XPATH, "//h1[@class='post-title']")
    product_to_checkout_loc = (By.XPATH, "//a[@class='checkout-button button alt wc-forward']")

    @property
    def cart_title(self):
        return self.driver.find_element(*self.cart_title_loc)

    @property
    def product_to_checkout(self):
        return self.driver.find_element(*self.product_to_checkout_loc)

    def validate_cart_page(self):
        """This method is used to validate the cart page"""
        assert self.cart_title.text == Constant.CART_PAGE_TITLE
