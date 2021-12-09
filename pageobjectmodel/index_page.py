import random
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.page_action import Page_action


class Index:
    def __init__(self, driver):
        self.driver = driver

    sign_in_loc = (By.XPATH, "//div[@class='header_user_info']")
    available_items_loc = (By.XPATH, "//ul[@id='homefeatured']/li")
    selected_item_loc = "//ul[@id='homefeatured']/li[{0}]/div[@class='product-container']/div/div[@class='product-image-container']"
    add_to_cart_loc = "//ul[@id='homefeatured']/li[{0}]//span[text()='Add to cart']"
    checkout_loc = (By.XPATH, "//a[@class='btn btn-default button button-medium']/span[normalize-space()='Proceed to checkout']")

    @property
    def sign_in(self):
        return self.driver.find_element(*self.sign_in_loc)

    @property
    def available_items(self):
        return self.driver.find_elements(*self.available_items_loc)

    @property
    def total_available_items(self):
        return len(self.available_items)

    @property
    def add_to_cart(self):
        return self.driver.find_element(*self.add_to_cart_loc)

    @property
    def checkout(self):
        return self.driver.find_element(*self.checkout_loc)

    def click_signin(self):
        """This method is used to click sign-in button"""
        try:
            WebDriverWait(self.driver, 20, poll_frequency=2, ignored_exceptions=[ElementClickInterceptedException]).until(
                EC.element_to_be_clickable(self.sign_in_loc))
        except ElementClickInterceptedException:
            pass
        self.sign_in.click()

    def select_item(self):
        """This method is used to select items on the intex page"""
        select_item = random.randrange(1, self.total_available_items+1)
        self.driver.execute_script(Page_action.SCROLL_DOWN_800_PIXELS)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.selected_item_loc.format(select_item))).perform()
        self.driver.find_element_by_xpath(self.add_to_cart_loc.format(select_item)).click()
        self.checkout.click()
