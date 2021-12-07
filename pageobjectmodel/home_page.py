import random
from selenium.webdriver.common.by import By
from constants.constant import Constant


class Home:
    def __init__(self, driver):
        self.driver = driver

    items_list_loc = (By.XPATH, "//div[@class='inventory_list']//button")
    shopping_icon_loc = (By.XPATH, "//a[@class='shopping_cart_link']")
    product_page_title_loc = (By.XPATH, "//span[@class='title']")

    @property
    def items_list(self):
        return self.driver.find_elements(*self.items_list_loc)

    @property
    def shopping_icon(self):
        return self.driver.find_element(*self.shopping_icon_loc)

    @property
    def product_page_title(self):
        return self.driver.find_element(*self.product_page_title_loc)

    def get_random_list(self, count):
        """This method is used to get total items and create random items list"""
        random_list = []
        items_count = len(self.items_list)
        for item_position in range(1, items_count + 1):
            random_list.append(item_position)
        random_list = random.sample(random_list, count)
        return random_list

    def add_to_cart(self, items):
        """This method is used to add items to cart"""
        for item in items:
            item_xpath = "//div[@class='inventory_list']/child::div[" + str(item) + "]//child::button"
            self.driver.find_element_by_xpath(item_xpath).click()

    def click_shopping_icon(self):
        """This method is used to click shopping icon"""
        self.shopping_icon.click()

    def validate_home_page(self):
        """This method is used to validate the home page"""
        assert self.driver.current_url == Constant.HOME_PAGE_URL
        assert self.product_page_title.text == Constant.PRODUCT_PAGE_TITLE
