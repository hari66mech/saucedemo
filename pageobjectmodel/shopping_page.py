import random
from selenium.webdriver.common.by import By


class Shopping:
    def __init__(self, driver):
        self.driver = driver

    select_pets_category_loc = (By.XPATH, "//*[@id='MainImageContent']/map/area[@shape='RECT']")
    select_sub_pets_loc = (By.XPATH, "//*[@id='Catalog']/table/tbody//a")
    select_specific_pet_loc = (By.XPATH, "//*[@id='Catalog']/table/tbody//td[1]/a")
    return_to_main_menu_loc = (By.XPATH, "//div[@id='BackLink']/a[@href]")

    @property
    def select_pets_category(self):
        """This property used to find the common pets category XPath"""
        return self.driver.find_elements(*self.select_pets_category_loc)

    @property
    def select_sub_pets_category(self):
        """This property used to find the common sub pets category XPath"""
        return self.driver.find_elements(*self.select_sub_pets_loc)

    @property
    def select_specific_pet(self):
        """This property used to find the common pets XPath"""
        return self.driver.find_elements(*self.select_specific_pet_loc)

    @property
    def return_to_main_menu(self):
        """This property used to find the 'return to main menu' button XPath"""
        return self.driver.find_element(*self.return_to_main_menu_loc)

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

    def click_return_to_main_menu(self):
        """This method is used to click the 'return to main menu' button"""
        self.return_to_main_menu.click()
