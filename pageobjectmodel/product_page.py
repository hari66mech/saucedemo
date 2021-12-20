from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product:
    def __init__(self, driver):
        self.driver = driver

    add_to_cart_loc = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    home_button_loc = (By.XPATH, "//li[@class='nav-item active']//a[@class='nav-link']")
    cart_button_loc = (By.XPATH, "//a[@id='cartur']")

    @property
    def add_to_cart(self):
        return self.driver.find_element(*self.add_to_cart_loc)

    @property
    def home_button(self):
        return self.driver.find_element(*self.home_button_loc)

    @property
    def cart_button(self):
        return self.driver.find_element(*self.cart_button_loc)

    def click_add_to_cart(self):
        "This method is used to click add to cart button and accept the alert message"
        self.add_to_cart.click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
