from selenium.webdriver.common.by import By


class Product:
    def __init__(self, driver):
        self.driver = driver

    add_to_cart_loc = (By.XPATH, "//button[@name='add-to-cart']")
    view_card_loc = (By.XPATH, "//a[@class='button wc-forward']")

    @property
    def add_to_cart(self):
        return self.driver.find_element(*self.add_to_cart_loc)

    @property
    def view_card(self):
        return self.driver.find_element(*self.view_card_loc)
