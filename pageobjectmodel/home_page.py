from selenium.webdriver.common.by import By


class Home:
    def __init__(self, driver):
        self.driver = driver

    my_account_loc = (By.XPATH, "//span[normalize-space()='My Account']")
    register_loc = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']")

    @property
    def my_account(self):
        return self.driver.find_element(*self.my_account_loc)

    @property
    def register(self):
        return self.driver.find_element(*self.register_loc)
