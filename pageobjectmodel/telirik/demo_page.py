import random
from selenium.webdriver.common.by import By


class Demo:
    def __init__(self, driver):
        self.driver = driver

    your_account_icon_loc = (By.XPATH, "//a[@title='Your Account']")
    demos_subcategory_loc = (By.XPATH, "//div[@data-tlrk-plugin='navspy']/a")
    subcategory_loc = "//div[@data-tlrk-plugin='navspy']/a[{0}]"
    subcategory_heading_loc = "//h3[text()][{0}]"

    @property
    def your_account_icon(self):
        return self.driver.find_element(*self.your_account_icon_loc)

    @property
    def demos_subcategory(self):
        return self.driver.find_elements(*self.demos_subcategory_loc)

    def click_your_account_icon(self):
        """This method used to click the your account icon"""
        self.your_account_icon.click()

    def click_subcategory(self):
        """This method is used to click subcategory under demos"""
        global category_position
        global category_name
        subcategories_count = len(self.demos_subcategory)
        category_position = random.randrange(1, subcategories_count)
        category_name = self.driver.find_element_by_xpath(self.subcategory_loc.format(str(category_position)))
        category_name.click()

    def verify_header_title(self):
        """This method is used to validate the heading with selected category"""
        subcategory_heading = self.driver.find_element_by_xpath(self.subcategory_heading_loc.format(category_position))
        assert subcategory_heading.text == category_name.text
