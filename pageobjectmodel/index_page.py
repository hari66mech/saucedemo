from selenium.webdriver.common.by import By


class Index:
    def __init__(self, driver):
        self.driver = driver

    sign_in_loc = (By.XPATH, "//a[@title='Log in to your customer account']")

    @property
    def sign_in(self):
        return self.driver.find_element(*self.sign_in_loc)

    def click_signin(self):
        self.sign_in.click()
