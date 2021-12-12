import random
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Account_creation:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker(locale='en_US')

    gender_loc = (By.XPATH, "//div[@class='radio-inline']//input")
    first_name_loc = (By.XPATH, "//input[@id='customer_firstname']")
    last_name_loc = (By.XPATH, "//input[@id='customer_lastname']")
    password_loc = (By.XPATH, "//input[@id='passwd']")
    date_dropdown_loc = (By.XPATH, "//select[@id='days']")
    days_loc = (By.XPATH, "//select[@id='days']/option")
    month_dropdown_loc = (By.XPATH, "//select[@id='months']")
    months_loc = (By.XPATH, "//select[@id='months']/option")
    year_dropdown_loc = (By.XPATH, "//select[@id='years']")
    years_loc = (By.XPATH, "//select[@id='years']/option")
    newsletter_box_loc = (By.XPATH, "//input[@id='newsletter']")
    special_offer_loc = (By.XPATH, "//input[@id='optin']")
    company_loc = (By.XPATH, "//input[@id='company']")
    address_1_loc = (By.XPATH, "//input[@id='address1']")
    address_2_loc = (By.XPATH, "//input[@id='address2']")
    city_loc = (By.XPATH, "//input[@id='city']")
    state_dropdown_loc = (By.XPATH, "//select[@id='id_state']")
    states_loc = (By.XPATH, "//select[@id='id_state']/option")
    postal_code_loc = (By.XPATH, "//input[@id='postcode']")
    additional_information_loc = (By.XPATH, "//textarea[@id='other']")
    home_phone_loc = (By.XPATH, "//input[@id='phone']")
    mobile_phone_loc = (By.XPATH, "//input[@id='phone_mobile']")
    register_button_loc = (By.XPATH, "//span[normalize-space()='Register']")
    gender_specific_loc = "//div[@class='radio-inline'][{0}]//input"

    @property
    def gender(self):
        return self.driver.find_elements(*self.gender_loc)

    @property
    def first_name(self):
        return self.driver.find_element(*self.first_name_loc)

    @property
    def last_name(self):
        return self.driver.find_element(*self.last_name_loc)

    @property
    def password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def date_dropdown(self):
        return self.driver.find_element(*self.date_dropdown_loc)

    @property
    def total_days(self):
        return self.driver.find_elements(*self.days_loc)

    @property
    def month_dropdown(self):
        return self.driver.find_element(*self.month_dropdown_loc)

    @property
    def total_months(self):
        return self.driver.find_elements(*self.months_loc)

    @property
    def year_dropdown(self):
        return self.driver.find_element(*self.year_dropdown_loc)

    @property
    def total_years(self):
        return self.driver.find_elements(*self.years_loc)

    @property
    def newsletter_box(self):
        return self.driver.find_element(*self.newsletter_box_loc)

    @property
    def specific_offer_box(self):
        return self.driver.find_element(*self.special_offer_loc)

    @property
    def company(self):
        return self.driver.find_element(*self.company_loc)

    @property
    def address_1(self):
        return self.driver.find_element(*self.address_1_loc)

    @property
    def address_2(self):
        return self.driver.find_element(*self.address_2_loc)

    @property
    def city(self):
        return self.driver.find_element(*self.city_loc)

    @property
    def state_dropdown(self):
        return self.driver.find_element(*self.state_dropdown_loc)

    @property
    def total_states(self):
        return self.driver.find_elements(*self.states_loc)

    @property
    def postal_code(self):
        return self.driver.find_element(*self.postal_code_loc)

    @property
    def additional_information(self):
        return self.driver.find_element(*self.additional_information_loc)

    @property
    def home_phone(self):
        return self.driver.find_element(*self.home_phone_loc)

    @property
    def mobile_phone(self):
        return self.driver.find_element(*self.mobile_phone_loc)

    @property
    def register_button(self):
        return self.driver.find_element(*self.register_button_loc)

    @property
    def gender_options(self):
        return len(self.gender)

    def enter_user_name(self, first_name, last_name):
        """This method is used to enter user name on the index page"""
        try:
            WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[TimeoutException]).until(
                EC.element_to_be_clickable(self.first_name_loc))
        except TimeoutException:
            pass
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)

    def enter_personal_information(self):
        """This method is used to enter personal information on the index page"""
        password = self.fake.password()
        self.driver.find_element_by_xpath(
            self.gender_specific_loc.format(str(random.randrange(1, self.gender_options + 1)))).click()
        self.password.send_keys(password)
        Select(self.date_dropdown).select_by_index(random.randrange(2, len(self.total_days)))
        Select(self.month_dropdown).select_by_index(random.randrange(2, len(self.total_months)))
        Select(self.year_dropdown).select_by_index(random.randrange(2, len(self.total_years)))
        self.newsletter_box.click()
        self.specific_offer_box.click()
        return password

    def keep_credentials(self, mail_id, password):
        """This method is used to write the credentials in .txt file"""
        file = open('credentials.txt', 'w')
        file.write(mail_id+","+password)
        file.close()

    def enter_address_information(self):
        """This method is used to enter address information on the index page"""
        self.company.send_keys(self.fake.company())
        self.address_1.send_keys(self.fake.street_name())
        self.address_2.send_keys(self.fake.building_number())
        self.city.send_keys(self.fake.city())
        Select(self.state_dropdown).select_by_index(random.randrange(2, len(self.total_states)))
        self.postal_code.send_keys(self.fake.postcode())
        self.additional_information.send_keys(self.fake.text())
        self.home_phone.send_keys(self.fake.msisdn())
        self.mobile_phone.send_keys(self.fake.msisdn())

    def click_register_button(self):
        """This method is used to click register button on the index page"""
        self.register_button.click()
