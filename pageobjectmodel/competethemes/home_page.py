from selenium.webdriver.common.by import By


class Home:
    def __init__(self, driver):
        self.driver = driver

    on_sale_products_loc = (By.XPATH, "//div[@id='on-sale-products']//ul[@class='products count-4']/li")
    top_rated_products_loc = (By.XPATH, "//div[@id='top-rated-products']//ul[@class='products count-4']/li")
    latest_products_loc = (By.XPATH, "//div[@id='latest-products']//ul[@class='products count-7']//li")
    on_sale_product_loc = "//div[@id='on-sale-products']//ul[@class='products count-4']/li[{0}]"
    top_rated_product_loc = "//div[@id='top-rated-products']//ul[@class='products count-4']/li[{0}]"
    latest_product_loc = "//div[@id='latest-products']//ul[@class='products count-7']//li[{0}]"

    @property
    def on_sale_products(self):
        return self.driver.find_elements(*self.on_sale_products_loc)

    @property
    def top_rated_products(self):
        return self.driver.find_elements(*self.top_rated_products_loc)

    @property
    def latest_products(self):
        return self.driver.find_elements(*self.latest_products_loc)

    @property
    def total_on_sale_products(self):
        return len(self.on_sale_products)

    @property
    def total_top_rated_products(self):
        return len(self.top_rated_products)

    @property
    def total_latest_products(self):
        return len(self.latest_products)

    def select_on_sale_products(self):
        """This method is used to return the on_sale_products details"""
        return [self.on_sale_product_loc, self.total_on_sale_products]

    def select_top_rated_products(self):
        """This method is used to return the top_rated_products details"""
        return [self.top_rated_product_loc, self.total_top_rated_products]

    def select_latest_products(self):
        """This method is used to return the latest_products details"""
        return [self.latest_product_loc, self.total_latest_products]
