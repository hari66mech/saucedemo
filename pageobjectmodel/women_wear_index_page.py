import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from constants.page_action import Page_action


class Women_wear:
    def __init__(self, driver):
        self.driver = driver

    women_wear_button_loc = (By.XPATH, "//a[@title='Women']")
    offer_items_loc = (By.XPATH, "//ul[@class='product_list grid row']/li//div[@class='right-block']//span[@class='price-percent-reduction']")
    selected_item_loc = "//div[@class='right-block']//span[@class='price-percent-reduction'][normalize-space()='{0}']/parent::div/parent::div//parent::div/div[@class='left-block']/div"
    add_to_cart_loc = "//div[@class='right-block']//span[@class='price-percent-reduction'][text()='{0}']//parent::div/parent::div//a/span[text()='Add to cart']"
    checkout_loc = (By.XPATH, "//span[normalize-space()='Proceed to checkout']")

    @property
    def women_wear_button(self):
        return self.driver.find_element(*self.women_wear_button_loc)

    @property
    def offer_items(self):
        return self.driver.find_elements(*self.offer_items_loc)

    @property
    def total_offer_items(self):
        return len(self.offer_items)

    @property
    def checkout(self):
        return self.driver.find_element(*self.checkout_loc)

    def click_women_wear(self):
        """This method is used to select women wear"""
        self.women_wear_button.click()

    def select_offer_item(self):
        """This method is used to select women offer wear"""
        select_item = random.randrange(0, self.total_offer_items)
        self.driver.execute_script(Page_action.SCROLL_DOWN_800_PIXELS)
        offer = self.offer_items[select_item].text
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.selected_item_loc.format(offer))).perform()
        self.driver.find_element_by_xpath(self.add_to_cart_loc.format(offer)).click()
        self.checkout.click()
