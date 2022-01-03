from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Home:
    def __init__(self, driver):
        self.driver = driver

    __pricing_loc = (By.XPATH, "//a[normalize-space()='Pricing']")
    __features_button_loc = (By.XPATH, "//span[normalize-space()='Features']")
    __main_features_loc = (By.XPATH, "//a[normalize-space()='Main Features']")

    @property
    def pricing(self):
        return self.driver.find_element(*self.__pricing_loc)

    @property
    def features_button(self):
        return self.driver.find_element(*self.__features_button_loc)

    @property
    def main_features(self):
        return self.driver.find_element(*self.__main_features_loc)

    def click_main_features(self):
        """This method is used to click main_features sub-heading"""
        action = ActionChains(self.driver)
        action.move_to_element(self.features_button).click().perform()
        action.click(self.main_features).perform()
