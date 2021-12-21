from selenium.webdriver.common.by import By


class Signin:
    def __init__(self, driver):
        self.driver = driver

    create_account_button_loc = (By.XPATH, "//a[normalize-space()='Create a new account']")

    @property
    def create_account_button(self):
        return self.driver.find_element(*self.create_account_button_loc)
    