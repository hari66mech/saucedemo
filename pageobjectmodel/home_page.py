from selenium.webdriver.common.by import By


class ValueMisMatchError(Exception):
    def __init__(self, value):
        self.value = value


class Home:
    def __init__(self, driver):
        self.driver = driver

    apple_cinema_loc = (By.XPATH, "//a[contains(text(),'Apple Cinema 30')]")
    total_items_loc = (By.XPATH, "//div[@class='product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12']//a[text()]")

    @property
    def apple_cinema(self):
        return self.driver.find_element(*self.apple_cinema_loc)

    @property
    def total_items(self):
        return self.driver.find_elements(*self.total_items_loc)

    @property
    def items_count(self):
        return len(self.total_items)

    def get_products(self):
        "This method is used to get products from the product.txt file"
        global products_summery
        file = open("C:/Users/harikrishna.manokara/PycharmProjects/tutorialsninja/product.txt", "r")
        products_summery = file.read().split(",")
        file.close()

    def validate_products(self):
        "This method is used to compare text summary data with web items"
        for product in range(self.items_count):
            if self.total_items[product].text == products_summery[product]:
                continue
            else:
                raise ValueMisMatchError(str(product) + " position mismatch between text summary data vs web items")
