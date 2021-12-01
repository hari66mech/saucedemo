import faker
from selenium.webdriver.common.by import By



class Toolsqa_text_box:
    def __init__(self, driver):
        self.driver = driver

    FAKE = faker.Faker()

    # locator
    full_name_loc = (By.XPATH, "//input[@id='userName']")
    email_loc = (By.XPATH, "//input[@id='userEmail']")
    current_address_loc = (By.XPATH, "//textarea[@id='currentAddress']")
    permanent_address_loc = (By.XPATH, "//textarea[@id='permanentAddress']")
    submit_button_loc = (By.XPATH, "//button[@id='submit']")
    output_box_loc = (By.XPATH, "//div[@id='output']")

    @property
    def full_name(self):
        """This method used to find the full name field XPath"""
        return self.driver.find_element(*self.full_name_loc)

    @property
    def email(self):
        """This method used to find the email field XPath"""
        return self.driver.find_element(*self.email_loc)

    @property
    def current_address(self):
        """This method used to find the current address field XPath"""
        return self.driver.find_element(*self.current_address_loc)

    @property
    def permanent_address(self):
        """This method used to find the permanent address field XPath"""
        return self.driver.find_element(*self.permanent_address_loc)

    @property
    def submit_button(self):
        """This method used to find the submit button XPath"""
        return self.driver.find_element(*self.submit_button_loc)

    @property
    def output_box(self):
        """This method used to find the output box XPath"""
        return self.driver.find_element(*self.output_box_loc)

    def enter_full_name(self):
        """This method is used to enter name in full name field"""
        self.full_name.send_keys(self.FAKE.name())

    def enter_email_id(self):
        """This method is used to enter email id in email field"""
        self.email.send_keys(self.FAKE.email())

    def enter_current_address(self):
        """This method is used to enter current address in current address field"""
        self.current_address.send_keys(self.FAKE.address())

    def enter_permanent_address(self):
        """This method is used to enter permanent address in permanent address"""
        self.permanent_address.send_keys(self.FAKE.address())

    def click_submit_button(self):
        """This method is used to click the submit button"""
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.submit_button.click()

    def out_put_box(self):
        """This method is used to validate output box is displayed or not"""
        assert self.output_box.is_displayed()
