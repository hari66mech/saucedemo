from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants.constant import Constant
from faker import Faker


class Cart:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker()

    total_selected_items_loc = (By.XPATH, "//tbody[@id='tbodyid']/tr")
    place_to_add_button_loc = (By.XPATH, "//button[normalize-space()='Place Order']")
    name_loc = (By.XPATH, "//input[@id='name']")
    country_loc = (By.XPATH, "//input[@id='country']")
    city_loc = (By.XPATH, "//input[@id='city']")
    credit_card_loc = (By.XPATH, "//input[@id='card']")
    month_loc = (By.XPATH, "//input[@id='month']")
    year_loc = (By.XPATH, "//input[@id='year']")
    purchase_button_loc = (By.XPATH, "//button[normalize-space()='Purchase']")
    thank_you_message_loc = (By.XPATH, "//h2[normalize-space()='Thank you for your purchase!']")
    ok_button_loc = (By.XPATH, "//button[contains(@class,'confirm btn btn-lg btn-primary')]")

    @property
    def total_selected_items(self):
        return self.driver.find_elements(*self.total_selected_items_loc)

    @property
    def selected_items_count(self):
        return len(self.total_selected_items)

    @property
    def place_to_add_button(self):
        return self.driver.find_element(*self.place_to_add_button_loc)

    @property
    def name(self):
        return self.driver.find_element(*self.name_loc)

    @property
    def country(self):
        return self.driver.find_element(*self.country_loc)

    @property
    def city(self):
        return self.driver.find_element(*self.city_loc)

    @property
    def credit_card(self):
        return self.driver.find_element(*self.credit_card_loc)

    @property
    def month(self):
        return self.driver.find_element(*self.month_loc)

    @property
    def year(self):
        return self.driver.find_element(*self.year_loc)

    @property
    def purchase_button(self):
        return self.driver.find_element(*self.purchase_button_loc)

    @property
    def thank_you_message(self):
        return self.driver.find_element(*self.thank_you_message_loc)

    @property
    def ok_button(self):
        return self.driver.find_element(*self.ok_button_loc)

    def validate_added_item(self):
        "This method is used to validate the added item"
        assert self.selected_items_count == Constant.ADDED_ITEM

    def fill_the_user_details(self, credential):
        "This method is used to fill the user details"
        expire_date = credential["expire_date"].split("/")
        self.name.send_keys(credential["user_name"])
        self.country.send_keys(credential["country"])
        self.city.send_keys(credential["city"])
        self.credit_card.send_keys(credential["credit_card_number"])
        self.month.send_keys(expire_date[0])
        self.year.send_keys(expire_date[1])
        self.purchase_button.click()

    def validate_thank_you_message(self):
        "This method is used to validate the thank you message"
        assert self.thank_you_message.text == Constant.THANK_YOU_MESSAGE
        self.ok_button.click()

    def validate_total_added_items(self):
        """This method is used to validate the total added items
            and also polling method is used for handling NoSuchElementException for a few seconds"""
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.total_selected_items_loc))
        except NoSuchElementException:
            raise NoSuchElementException
        assert self.selected_items_count == Constant.TOTAL_SELECTED_ITEMS
