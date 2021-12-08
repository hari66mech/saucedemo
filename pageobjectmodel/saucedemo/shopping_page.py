import random
from selenium.webdriver.common.by import By
from constants.saucedemo.sauce_constant import Sauce_constant


class Home:
    def __init__(self, driver):
        self.driver = driver

    items_list_loc = (By.XPATH, "//div[@class='inventory_list']//button")
    shopping_icon_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
    select_item_loc = "//div[@class='inventory_list']/child::div[{0}]//child::button"

    @property
    def items_list(self):
        return self.driver.find_elements(*self.items_list_loc)

    @property
    def total_item(self):
        return len(self.items_list)

    @property
    def shopping_icon(self):
        return self.driver.find_element(*self.shopping_icon_loc)

    def get_random_list(self, count):
        """This method is used to get total items and create random items list"""
        random_list = []
        for item_position in range(1, self.total_item + 1):
            random_list.append(item_position)
        random_list = random.sample(random_list, count)
        return random_list

    def add_to_cart(self, items):
        """This method is used to add items to cart"""
        for item in items:
            self.driver.find_element_by_xpath(self.select_item_loc.format(str(item))).click()

    def click_shopping_icon(self):
        """This method is used to click shopping icon"""
        self.shopping_icon.click()

    def validate_home_page(self):
        """This method is used to validate the home page url"""
        assert self.driver.current_url == Sauce_constant.HOME_PAGE_URL
