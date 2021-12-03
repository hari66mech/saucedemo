from faker import Faker
from selenium.webdriver.common.by import By


class Registration:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker(locale='en_IN')

    user_id_loc = (By.XPATH, "//input[@name='username']")
    new_password_loc = (By.XPATH, "//input[@name='password']")
    repeat_password_loc = (By.XPATH, "//input[@name='repeatedPassword']")
    first_name_loc = (By.XPATH, "//input[@name='account.firstName']")
    last_name_loc = (By.XPATH, "//input[@name='account.lastName']")
    email_id_loc = (By.XPATH, "//input[@name='account.email']")
    phone_number_loc = (By.XPATH, "//input[@name='account.phone']")
    address_1_loc = (By.XPATH, "//input[@name='account.address1']")
    address_2_loc = (By.XPATH, "//input[@name='account.address2']")
    city_loc = (By.XPATH, "//input[@name='account.city']")
    state_loc = (By.XPATH, "//input[@name='account.state']")
    zip_loc = (By.XPATH, "//input[@name='account.zip']")
    country_loc = (By.XPATH, "//input[@name='account.country']")
    enable_mylist_loc = (By.XPATH, "//input[@name='account.listOption']")
    enable_mybanner_loc = (By.XPATH, "//input[@name='account.bannerOption']")
    save_account_information_loc = (By.XPATH, "//input[@name='newAccount']")

    @property
    def user_id(self):
        """This property used to find the user id field XPath"""
        return self.driver.find_element(*self.user_id_loc)

    @property
    def new_password(self):
        """This property used to find the new password field XPath"""
        return self.driver.find_element(*self.new_password_loc)

    @property
    def repeat_password(self):
        """This property used to find the repeat password field XPath"""
        return self.driver.find_element(*self.repeat_password_loc)

    @property
    def first_name(self):
        """This property used to find the first name field XPath"""
        return self.driver.find_element(*self.first_name_loc)

    @property
    def last_name(self):
        """This property used to find the last name field XPath"""
        return self.driver.find_element(*self.last_name_loc)

    @property
    def email(self):
        """This property used to find the email id field XPath"""
        return self.driver.find_element(*self.email_id_loc)

    @property
    def phone_number(self):
        """This property used to find the phone number field XPath"""
        return self.driver.find_element(*self.phone_number_loc)

    @property
    def address_1(self):
        """This property used to find the first address field XPath"""
        return self.driver.find_element(*self.address_1_loc)

    @property
    def address_2(self):
        """This property used to find the second address field XPath"""
        return self.driver.find_element(*self.address_2_loc)

    @property
    def city(self):
        """This property used to find the city field XPath"""
        return self.driver.find_element(*self.city_loc)

    @property
    def state(self):
        """This property used to find the state field XPath"""
        return self.driver.find_element(*self.state_loc)

    @property
    def zip(self):
        """This property used to find the zip field XPath"""
        return self.driver.find_element(*self.zip_loc)

    @property
    def country(self):
        """This property used to find the country field XPath"""
        return self.driver.find_element(*self.country_loc)

    @property
    def mylist(self):
        """This property used to find the enable mylist checkbox XPath"""
        return self.driver.find_element(*self.enable_mylist_loc)

    @property
    def mybanner(self):
        """This property used to find the enable mybanner checkbox XPath"""
        return self.driver.find_element(*self.enable_mybanner_loc)

    @property
    def save_account_information(self):
        """This property used to find the 'save account information' button XPath"""
        return self.driver.find_element(*self.save_account_information_loc)

    def user_information(self):
        """This method used to fill the user information"""
        password = self.fake.password()
        user_id = self.fake.random_int()
        credential = [user_id, password]
        self.user_id.send_keys(user_id)
        self.new_password.send_keys(password)
        self.repeat_password.send_keys(password)
        return credential

    def account_information(self):
        """This method used to fill the account information"""
        self.first_name.send_keys(self.fake.first_name())
        self.last_name.send_keys(self.fake.last_name())
        self.email.send_keys(self.fake.email())
        self.phone_number.send_keys(self.fake.phone_number())
        self.city.send_keys(self.fake.city())
        self.address_1.send_keys(self.fake.street_address())
        self.state.send_keys(self.fake.state())
        self.address_2.send_keys(self.fake.street_address())
        self.zip.send_keys(self.fake.postcode())
        self.country.send_keys(self.fake.country())

    def profile_information(self):
        """This method used to fill the profile information"""
        self.mylist.click()
        self.mybanner.click()

    def click_save_account_information(self):
        """This method used to click the 'save account information' button"""
        self.save_account_information.click()
