from selenium.webdriver.common.by import By


class Index:
    def __init__(self, driver):
        self.driver = driver

    gender_loc = (By.XPATH, "//div[@class='radio-inline']//input")
    first_name_loc = (By.XPATH, "//input[@id='customer_firstname']")
    last_name_loc = (By.XPATH, "//input[@id='customer_lastname']")
    password_loc = (By.XPATH, "//input[@id='passwd']")
    date_loc = (By.XPATH, "//select[@id='days']")


    @property
    def gender(self):
        return self.driver.find_element(*self.gender_loc)





