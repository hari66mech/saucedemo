import random
from faker import Faker
from selenium.webdriver.common.by import By
from constants.constant import Constant


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
    return_to_main_menu_loc = (By.XPATH, "//div[@id='BackLink']/a[@href]")
    pets_price_loc = (By.XPATH, "//form[@method='post']/table[1]/tbody[1]//tr/td[6]")
    total_price_loc = (By.XPATH, "//*[contains(text(),'Sub Total')]")
    proceed_to_checkout_loc = (By.XPATH, "//a[normalize-space()='Proceed to Checkout']")
    continue_button_loc = (By.XPATH, "//input[@name='newOrder']")
    confirm_button_loc = (By.XPATH, "//a[@class='Button']")
    total_bill_amount_loc = (By.XPATH, "//th[contains(text(),'Total:')]")
    thank_you_text_loc = (By.XPATH, "//li[normalize-space()='Thank you, your order has been submitted.']")

    @property
    def user_id(self):
        """This method used to find the user id field XPath"""
        return self.driver.find_element(*self.user_id_loc)

    @property
    def new_password(self):
        """This method used to find the new password field XPath"""
        return self.driver.find_element(*self.new_password_loc)

    @property
    def repeat_password(self):
        """This method used to find the repeat password field XPath"""
        return self.driver.find_element(*self.repeat_password_loc)

    @property
    def first_name(self):
        """This method used to find the first name field XPath"""
        return self.driver.find_element(*self.first_name_loc)

    @property
    def last_name(self):
        """This method used to find the last name field XPath"""
        return self.driver.find_element(*self.last_name_loc)

    @property
    def email(self):
        """This method used to find the email id field XPath"""
        return self.driver.find_element(*self.email_id_loc)

    @property
    def phone_number(self):
        """This method used to find the phone number field XPath"""
        return self.driver.find_element(*self.phone_number_loc)

    @property
    def address_1(self):
        """This method used to find the first address field XPath"""
        return self.driver.find_element(*self.address_1_loc)

    @property
    def address_2(self):
        """This method used to find the second address field XPath"""
        return self.driver.find_element(*self.address_2_loc)

    @property
    def city(self):
        """This method used to find the city field XPath"""
        return self.driver.find_element(*self.city_loc)

    @property
    def state(self):
        """This method used to find the state field XPath"""
        return self.driver.find_element(*self.state_loc)

    @property
    def zip(self):
        """This method used to find the zip field XPath"""
        return self.driver.find_element(*self.zip_loc)

    @property
    def country(self):
        """This method used to find the country field XPath"""
        return self.driver.find_element(*self.country_loc)

    @property
    def mylist(self):
        """This method used to find the enable mylist checkbox XPath"""
        return self.driver.find_element(*self.enable_mylist_loc)

    @property
    def mybanner(self):
        """This method used to find the enable mybanner checkbox XPath"""
        return self.driver.find_element(*self.enable_mybanner_loc)

    @property
    def save_account_information(self):
        """This method used to find the 'save account information' button XPath"""
        return self.driver.find_element(*self.save_account_information_loc)

    @property
    def select_pets_category(self):
        """This method used to find the common pets category XPath"""
        return self.driver.find_elements(*self.select_pets_category_loc)

    @property
    def select_sub_pets_category(self):
        """This method used to find the common sub pets category XPath"""
        return self.driver.find_elements(*self.select_sub_pets_loc)

    @property
    def select_specific_pet(self):
        """This method used to find the common pets XPath"""
        return self.driver.find_elements(*self.select_specific_pet_loc)

    @property
    def add_cart(self):
        """This method used to find the add cart button XPath"""
        return self.driver.find_element(*self.add_cart_loc)

    @property
    def return_to_main_menu(self):
        """This method used to find the 'return to main menu' button XPath"""
        return self.driver.find_element(*self.return_to_main_menu_loc)

    @property
    def pets_price(self):
        """This method used to find the pets price XPath"""
        return self.driver.find_elements(*self.pets_price_loc)

    @property
    def total_price(self):
        """This method used to find the total price XPath"""
        return self.driver.find_element(*self.total_price_loc)

    @property
    def proceed_to_checkout(self):
        """This method used to find the checkout button XPath"""
        return self.driver.find_element(*self.proceed_to_checkout_loc)

    @property
    def continue_button(self):
        """This method used to find the continue button XPath"""
        return self.driver.find_element(*self.continue_button_loc)

    @property
    def confirm_button(self):
        """This method used to find the confirm button XPath"""
        return self.driver.find_element(*self.confirm_button_loc)

    @property
    def thank_you_text(self):
        """This method used to find the thank you message text XPath"""
        return self.driver.find_element(*self.thank_you_text_loc)

    @property
    def total_bill_amount(self):
        """This method used to find the total bill XPath"""
        return self.driver.find_element(*self.total_bill_amount_loc)

    def user_information(self):
        """This method used to fill the user information"""
        password = self.fake.password()
        user_id = random.randrange(1000, 9999)
        self.user_id.send_keys(user_id)
        self.new_password.send_keys(password)
        self.repeat_password.send_keys(password)

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

    def click_pets_category(self):
        """This method is used to click the pet category using random function"""
        pets_list_element = self.select_pets_category
        pets = self.select_pets_category_loc[1]
        pet = pets + "[" + str(random.randint(2, len(pets_list_element))) + "]"
        self.driver.find_element_by_xpath(pet).click()

    def click_pets_subcategory(self):
        """This method is used to click the pets subcategory using random function"""
        pets_list = []
        pets_sub_list = self.select_sub_pets_category
        for pet in pets_sub_list:
            pets_list.append(pet.text)
        pet = pets_list[random.randrange(1, len(pets_list))]
        pet_loc = "//a[text()='" + pet + "']"
        self.driver.find_element_by_xpath(pet_loc).click()

    def click_specific_pet(self):
        """This method is used to click the pet using random function"""
        selected_pets_list = []
        pets_list = self.select_specific_pet
        for pet in pets_list:
            selected_pets_list.append(pet.text)
        if len(selected_pets_list) > 1:
            specific_pet = selected_pets_list[random.randrange(1, len(selected_pets_list))]
        else:
            specific_pet = selected_pets_list[0]
        specific_pet_loc = "//a[text()='" + specific_pet + "']"
        self.driver.find_element_by_xpath(specific_pet_loc).click()

    def click_add_card(self):
        """This method is used to add the pets to cart"""
        self.add_cart.click()

    def click_return_to_main_menu(self):
        """This method is used to click the 'return to main menu' button"""
        self.return_to_main_menu.click()

    def click_checkout_button(self):
        """This method is used to click the 'proceed to checkout' button"""
        self.proceed_to_checkout.click()

    def click_continue_button(self):
        """This method is used to click the 'continue' button"""
        self.continue_button.click()

    def click_confirm_button(self):
        """This method is used to click the 'confirm' button"""
        self.confirm_button.click()

    def verify_confirmation_message(self):
        """This method is used to verify the confirmation message"""
        assert self.thank_you_text.is_displayed()

    def calculate_the_price(self):
        """This method is used to calculate the pets price and compare with total price"""
        pets_price = self.pets_price
        total_price = self.total_price.text[12:]
        prices = 0
        for pet_price in pets_price:
            price = pet_price.text[1:]
            prices = float(price)+prices
        assert prices == float(total_price)

    def check_total_bill_amount(self):
        """This method is used to check the total bill amount is displayed in order page"""
        self.total_bill_amount.is_displayed()
