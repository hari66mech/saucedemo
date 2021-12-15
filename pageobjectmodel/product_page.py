from selenium.webdriver.common.by import By
from constant.constant import Constant


class Product:
    def __init__(self, driver):
        self.driver = driver

    item_size_loc = (By.XPATH, "//input[@name='option[218]']")
    checkboxs_loc = (By.XPATH, "//div[@class='checkbox']")
    checkbox_loc = "//div[@class='checkbox'][{0}]//input"
    select_colours_loc = (By.XPATH, "//select[@id='input-option217']")
    selected_colour_loc = "//select[@id='input-option217']/option[{0}]"
    text_area_loc = (By.XPATH, "//textarea[@id='input-option209']")
    file_upload_loc = (By.XPATH, "//button[@id='button-upload222']")
    add_to_cart_button_loc = (By.XPATH, "//button[@id='button-cart']")
    success_message_loc = (By.XPATH, "//div[contains(text(),'Success')]")

    @property
    def item_size(self):
        return self.driver.find_element(*self.item_size_loc)

    @property
    def checkboxs(self):
        return self.driver.find_elements(*self.checkboxs_loc)

    @property
    def total_checkbox(self):
        return len(self.checkboxs)

    @property
    def success_message(self):
        return self.driver.find_element(*self.success_message_loc)

    @property
    def select_colours(self):
        return self.driver.find_elements(*self.select_colours_loc)

    @property
    def total_colours(self):
        return len(self.select_colours)

    @property
    def selected_colour(self):
        return self.driver.find_element(*self.selected_colour_loc)

    @property
    def text_area(self):
        return self.driver.find_element(*self.text_area_loc)

    @property
    def file_upload(self):
        return self.driver.find_element(*self.file_upload_loc)

    @property
    def add_to_cart_button(self):
        return self.driver.find_element(*self.add_to_cart_button_loc)

    def fill_available_options(self, fake_text):
        "This method is used to fill available options"
        self.item_size.click()
        self.driver.find_element_by_xpath(self.checkbox_loc.format(1, self.total_checkbox + 1)).click()
        self.driver.find_element_by_xpath(self.selected_colour_loc.format(1, self.total_colours + 1)).click()
        self.text_area.send_keys(fake_text["text"])
        self.file_upload.send_keys(r"C:\Music\hth.txt")
        self.add_to_cart_button.click()

    def verify_success_message(self):
        "This method is used to validate success message"
        assert self.success_message.text == Constant.SUCCESS_MESSAGE
