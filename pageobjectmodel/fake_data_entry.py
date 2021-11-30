from selenium.webdriver.common.by import By
from factory.faker import faker


class Fake_data_entry:
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
        return self.driver.find_element(*self.full_name_loc)

    @property
    def email(self):
        return self.driver.find_element(*self.email_loc)

    @property
    def current_address(self):
        return self.driver.find_element(*self.current_address_loc)

    @property
    def permanent_address(self):
        return self.driver.find_element(*self.permanent_address_loc)

    @property
    def submit_button(self):
        return self.driver.find_element(*self.submit_button_loc)

    @property
    def output_box(self):
        return self.driver.find_element(*self.output_box_loc)

    def enter_full_name(self):
        self.full_name.send_keys(self.FAKE.name())

    def enter_email_id(self):
        self.email.send_keys(self.FAKE.email())

    def enter_current_address(self):
        self.current_address.send_keys(self.FAKE.address())

    def enter_permanet_address(self):
        self.permanent_address.send_keys(self.FAKE.address())

    def click_submit_button(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.submit_button.click()

    def out_put_box(self):
        assert self.output_box.is_displayed()
