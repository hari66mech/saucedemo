import random
from faker import Faker
from selenium.webdriver.common.by import By


class Pets_order:
    def __init__(self, driver):
        self.driver = driver

    fake = Faker(locale='en_IN')

    # locator
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
    select_pets_category_loc = (By.XPATH, "//*[@id='MainImageContent']/map/area[@shape='RECT']")
    select_sub_pets_loc = (By.XPATH, "//*[@id='Catalog']/table/tbody//a")
    select_specific_pet_loc = (By.XPATH, "//*[@id='Catalog']/table/tbody//td[1]/a")
    add_cart_loc = (By.XPATH, "//*[@id='Catalog']/table/tbody//td[1]/a")
    return_to_main_menu_loc = (By.XPATH, "//a[normalize-space()='Return to Main Menu']")
    pets_price_loc = (By.XPATH, "//form[@method='post']/table[1]/tbody[1]//tr/td[6]")
    total_price_loc = (By.XPATH, "//*[contains(text(),'Sub Total')]")
    proceed_to_checkout_loc = (By.XPATH, "//a[normalize-space()='Proceed to Checkout']")
    continue_button_loc = (By.XPATH, "//input[@name='newOrder']")
    confirm_button_loc = (By.XPATH, "//a[@class='Button']")
    total_bill_loc = (By.XPATH, "//th[contains(text(),'Total:')]")
    thank_you_text_loc = (By.XPATH, "//li[normalize-space()='Thank you, your order has been submitted.']")

    @property
    def user_id(self):
        return self.driver.find_element(*self.user_id_loc)

    @property
    def new_password(self):
        return self.driver.find_element(*self.new_password_loc)

    @property
    def repeat_password(self):
        return self.driver.find_element(*self.repeat_password_loc)

    @property
    def first_name(self):
        return self.driver.find_element(*self.first_name_loc)

    @property
    def last_name(self):
        return self.driver.find_element(*self.last_name_loc)

    @property
    def email(self):
        return self.driver.find_element(*self.email_id_loc)

    @property
    def phone_number(self):
        return self.driver.find_element(*self.phone_number_loc)

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
    def state(self):
        return self.driver.find_element(*self.state_loc)

    @property
    def zip(self):
        return self.driver.find_element(*self.zip_loc)

    @property
    def country(self):
        return self.driver.find_element(*self.country_loc)

    @property
    def mylist(self):
        return self.driver.find_element(*self.enable_mylist_loc)

    @property
    def mybanner(self):
        return self.driver.find_element(*self.enable_mybanner_loc)

    @property
    def save_account_information(self):
        return self.driver.find_element(*self.save_account_information_loc)

    @property
    def select_pets_category(self):
        return self.driver.find_elements(*self.select_pets_category_loc)

    @property
    def select_sub_pets_category(self):
        return self.driver.find_elements(*self.select_sub_pets_loc)

    @property
    def select_specific_pet(self):
        return self.driver.find_element(*self.select_specific_pet_loc)

    @property
    def add_cart(self):
        return self.driver.find_element(*self.add_cart_loc)

    @property
    def return_to_main_menu(self):
        return self.driver.find_element(*self.return_to_main_menu_loc)

    @property
    def pets_price(self):
        return self.driver.find_elements(*self.pets_price_loc)

    @property
    def total_price(self):
        return self.driver.find_element(*self.total_price_loc)

    @property
    def proceed_to_checkout(self):
        return self.driver.find_element(*self.proceed_to_checkout_loc)

    @property
    def continue_button(self):
        return self.driver.find_element(*self.continue_button_loc)

    @property
    def confirm_button(self):
        return self.driver.find_element(*self.continue_button_loc)

    @property
    def total_bill(self):
        return self.driver.find_element(*self.total_bill_loc)

    @property
    def thank_you_text(self):
        return self.driver.find_element(*self.thank_you_text_loc)

    def user_information(self):
        password = self.fake.password()
        user_id = random.randrange(1000, 9999)
        self.user_id.send_keys(user_id)
        self.new_password.send_keys(password)
        self.repeat_password.send_keys(password)

    def account_information(self):
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
        self.mylist.click()
        self.mybanner.click()

    def click_save_account_information(self):
        self.save_account_information.click()

    def click_pets_category(self):
        pets_list = self.select_pets_category
        pets = self.select_pets_category_loc[1]
        pet = pets + "[" + str(random.randint(2, len(pets_list))) + "]"
        self.driver.find_element_by_xpath(pet).click()
