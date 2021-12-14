import random
import polling as polling
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.constant import Constant
from polling2 import TimeoutException


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
    samsung_galaxy_loc = (By.XPATH, "//a[normalize-space()='Samsung galaxy s6']")
    sony_vaio_loc = (By.XPATH, "//a[normalize-space()='Sony vaio i5']")
    apple_monitor_loc = (By.XPATH, "//a[normalize-space()='Apple monitor 24']")
    next_button_loc = (By.XPATH, "//button[@id='next2']")
    selected_item_loc = "//*[@id='tbodyid']/div[{0}]/div/div/h4/a"

    @property
    def signup(self):
        return self.driver.find_element(*self.sign_up_loc)

    @property
    def samsung_galaxy(self):
        return self.driver.find_element(*self.samsung_galaxy_loc)

    @property
    def sony_vaio(self):
        return self.driver.find_element(*self.sony_vaio_loc)

    @property
    def apple_monitor(self):
        return self.driver.find_element(*self.apple_monitor_loc)

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

    def click_next_button(self):
        "This method is used to validate the 'next' button with the help of polling method and click the 'next' button"
        try:
            polling.poll(lambda: self.next_button, step=2, timeout=20)
        except NoSuchElementException:
            raise NoSuchElementException
        self.next_button.click()

    def validate_samsung_galaxy_mobile(self):
        "This method is used to validate the samsung_galaxy mobile is present on the index page"
        try:
            polling.poll(lambda: self.samsung_galaxy, step=2, timeout=20)
        except TimeoutException:
            raise NoSuchElementException

    def validate_sony_vaio_laptop(self):
        "This method is used to validate the sony_vaio laptop is present on the index page"
        try:
            polling.poll(lambda: self.sony_vaio, step=2, timeout=20)
        except NoSuchElementException:
            raise NoSuchElementException

    def validate_apple_monitor(self):
        "This method is used to validate the apple_monitor is present on the index page"
        try:
            polling.poll(lambda: self.apple_monitor, step=2, timeout=20)
        except NoSuchElementException:
            raise NoSuchElementException

    def verify_user_welcome_message(self, credential):
        """This method is used to validate the welcome message
        and also polling method is used for handling NoSuchElementException for a few seconds"""
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.name_of_user_loc))
        except NoSuchElementException:
            raise NoSuchElementException
        assert self.name_of_user.text == Constant.WELCOME_MESSAGE + credential["user_name"]

    def select_item(self):
        """This method is used to select the item
           and also polling method is used for handling NoSuchElementException for a few seconds"""
        selected_item = self.selected_item_loc.format(random.randrange(1, self.total_items + 1))
        try:
            polling.poll(lambda: self.demoblaze_items, step=2, timeout=20)
        except NoSuchElementException:
            raise NoSuchElementException
        self.driver.find_element_by_xpath(selected_item).click()
