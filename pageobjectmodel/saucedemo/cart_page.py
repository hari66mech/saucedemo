import random
from selenium.webdriver.common.by import By
from pageobjectmodel.saucedemo.shopping_page import Home


class Cart(Home):
    def __init__(self, driver):
        super().__init__(driver)

    continue_shopping_loc = (By.XPATH, "//button[@id='continue-shopping']")
    cart_items_loc = (By.XPATH, "//div[@class='cart_item']")
    shopping_icon_loc = (By.XPATH, "//a[@class='shopping_cart_link']")

    @property
    def continue_shopping(self):
        return self.driver.find_element(*self.continue_shopping_loc)

    @property
    def cart_items(self):
        return self.driver.find_elements(*self.cart_items_loc)

    @property
    def shopping_icon(self):
        return self.driver.find_element(*self.shopping_icon_loc)

    def verify_shopping_items_count(self, count):
        """This method is used to validate added items count"""
        assert self.shopping_icon.text == str(count)

    def remove_item(self):
        """This method is used to remove item from the cart"""
        random_item = random.randrange(1, len(self.cart_items) + 1)
        random_item_xpath = "//div[@class='cart_list']/div[@class='cart_item'][" + str(
            random_item) + "]//button[text()]"
        self.driver.find_element_by_xpath(random_item_xpath).click()

    def click_continue_shopping(self):
        """This method is used to click continue shopping button"""
        self.continue_shopping.click()
