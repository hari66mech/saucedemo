from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from constants.constant import Constant


class Pokeman:
    def __init__(self, driver):
        self.driver = driver

    # locator
    search_box_loc = (By.XPATH, "//input[@id='monsters-search-bar']")
    pokeman_list_loc = (By.XPATH, "//ul[@id='monsters-list']/child::li")
    Pikachu_loc = (By.XPATH, "//button[@class='monster-sprite sprite-25']")

    @property
    def search_text_box(self):
        return self.driver.find_element(*self.search_box_loc)

    @property
    def search_Pikachu(self):
        return self.driver.find_element(*self.Pikachu_loc)

    @property
    def get_pokeman_list(self):
        return self.driver.find_elements(*self.pokeman_list_loc)

    def search_pokeman(self, text):
        self.search_text_box.send_keys(text)

    def length_of_the_list(self):
        assert len(self.get_pokeman_list) >= Constant.TOTAL_POKEDEXS

    def search_pikachu(self):
        try:
            assert self.search_Pikachu.is_displayed()
        except AssertionError:
            print("AssertionError is occur")
        except TimeoutError:
            print("TimeoutError is occur")

    def click_pikachu(self):
        self.search_Pikachu.click()

    def verify_url(self):
        assert self.driver.current_url == Constant.PIKACHU_URL_PAGE
