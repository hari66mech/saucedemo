from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Index:
    def __init__(self, driver):
        self.driver = driver

    sign_in_button_loc = (By.XPATH, "//section[@class='header__user-menu']//a")

    @property
    def sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_loc)

    def click_signin_button(self):
        """This method is used to check signin button is clickable and click the signin button"""
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.sign_in_button_loc))
        except NoSuchElementException:
            raise NoSuchElementException
        self.sign_in_button.click()
