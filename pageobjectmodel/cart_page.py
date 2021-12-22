import random
from selenium.webdriver.common.by import By
from constants.constant import Constant


class Cart:
    def __init__(self, driver):
        self.Home = None
        self.driver = driver

    continue_shopping_loc = (By.XPATH, "//button[@id='continue-shopping']")
    cart_items_loc = (By.XPATH, "//div[@class='cart_item']")
    shopping_icon_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
    title_loc = (By.XPATH, "//span[@class='title']")
    added_items_loc = "//div[@class='cart_list']/div[@class='cart_item'][{0}]//button[text()]"

    @property
    def continue_shopping(self):
        return self.driver.find_element(*self.continue_shopping_loc)

    @property
    def cart_items(self):
        return self.driver.find_elements(*self.cart_items_loc)

    @property
    def shopping_icon(self):
        return self.driver.find_element(*self.shopping_icon_loc)

    @property
    def page_title(self):
        return self.driver.find_element(*self.title_loc)

    @property
    def total_added_items(self):
        return len(self.cart_items)

    def verify_shopping_items_count(self, count):
        """This method is used to validate added items count"""
        assert self.shopping_icon.text == str(count)

    def remove_item(self):
        """This method is used to remove item from the cart"""
        random_item = str(random.randrange(1, self.total_added_items+1))
        self.driver.find_element_by_xpath(self.added_items_loc.format(random_item)).click()

    def click_continue_shopping(self):
        """This method is used to click continue shopping button"""
        self.continue_shopping.click()

    def cart_page_title(self):
        """This method used to validate the cart page"""
        assert self.page_title.text == Constant.CART_PAGE_TITLE
