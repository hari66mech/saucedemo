import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.constant import Constant


class Index:
    def __init__(self, driver):
        self.driver = driver

    sign_up_loc = (By.XPATH, "//a[@id='signin2']")
    login_loc = (By.XPATH, "//a[@id='login2']")
    name_of_user_loc = (By.XPATH, "//a[@id='nameofuser']")
    phones_button_loc = (By.XPATH, "//div[@id='contcont']//a[text()='Phones']")
    laptops_button_loc = (By.XPATH, "//div[@id='contcont']//a[text()='Laptops']")
    monitors_button_loc = (By.XPATH, "//div[@id='contcont']//a[text()='Monitors']")
    demoblaze_items_loc = (By.XPATH, "//div[@id='tbodyid']/div")
    next_button_loc = (By.XPATH, "//button[@id='next2']")
    selected_item_loc = "//div[@id='tbodyid']/div[{0}]//a"

    @property
    def signup(self):
        return self.driver.find_element(*self.sign_up_loc)

    @property
    def log_in(self):
        return self.driver.find_element(*self.login_loc)

    @property
    def name_of_user(self):
        return self.driver.find_element(*self.name_of_user_loc)

    @property
    def phones_button(self):
        return self.driver.find_element(*self.phones_button_loc)

    @property
    def laptops_button(self):
        return self.driver.find_element(*self.laptops_button_loc)

    @property
    def monitors_button(self):
        return self.driver.find_element(*self.monitors_button_loc)

    @property
    def demoblaze_items(self):
        return self.driver.find_elements(*self.demoblaze_items_loc)

    @property
    def total_items(self):
        return len(self.demoblaze_items)

    @property
    def next_button(self):
        return self.driver.find_element(*self.next_button_loc)

    def validate_welcome_message(self, credential):
        """This method is used to validate welcome message
        and also polling method is used for handling NoSuchElementException for a few seconds"""

        try:
            WebDriverWait(self.driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException]).until(
                EC.element_to_be_clickable(self.name_of_user_loc))
        except NoSuchElementException:
            raise NoSuchElementException
        assert self.name_of_user.text == Constant.WELCOME_MESSAGE+credential[0]

    def select_item(self):
        """This method is used to fill the user details
           and also polling method is used for handling NoSuchElementException for a few seconds"""

        selected_item = self.selected_item_loc.format(random.randrange(1, self.total_items+1))
        try:
            WebDriverWait(self.driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException]).until(
                EC.presence_of_all_elements_located(self.demoblaze_items_loc))
        except NoSuchElementException:
            raise NoSuchElementException
        self.driver.find_element_by_xpath(selected_item).click()
