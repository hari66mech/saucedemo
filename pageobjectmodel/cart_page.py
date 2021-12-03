from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, driver):
        self.driver = driver

    add_cart_loc = (By.XPATH, "//*[@id='Catalog']/table/tbody//td[1]/a")
    pets_price_loc = (By.XPATH, "//form[@method='post']/table[1]/tbody[1]//tr/td[6]")
    total_price_loc = (By.XPATH, "//*[contains(text(),'Sub Total')]")
    proceed_to_checkout_loc = (By.XPATH, "//a[normalize-space()='Proceed to Checkout']")

    @property
    def add_cart(self):
        """This property used to find the add cart button XPath"""
        return self.driver.find_element(*self.add_cart_loc)

    @property
    def pets_price(self):
        """This property used to find the pets price XPath"""
        return self.driver.find_elements(*self.pets_price_loc)

    @property
    def total_price(self):
        """This property used to find the total price XPath"""
        return self.driver.find_element(*self.total_price_loc)

    @property
    def proceed_to_checkout(self):
        """This property used to find the checkout button XPath"""
        return self.driver.find_element(*self.proceed_to_checkout_loc)

    def click_add_card(self):
        """This method is used to add the pets to cart"""
        self.add_cart.click()

    def click_checkout_button(self):
        """This method is used to click the 'proceed to checkout' button"""
        self.proceed_to_checkout.click()

    def calculate_the_price(self):
        """This method is used to calculate the pets price and compare with total price"""
        pets_price = self.pets_price
        total_price = self.total_price.text[12:]
        prices = 0
        for pet_price in pets_price:
            price = pet_price.text[1:]
            prices = float(price) + prices
        assert prices == float(total_price)
