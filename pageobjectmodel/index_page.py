from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Index:
    def __init__(self, driver):
        self.driver = driver

    sign_in_loc = (By.XPATH, "//div[@class='header_user_info']")

    @property
    def sign_in(self):
        return self.driver.find_element(*self.sign_in_loc)

    def click_signin(self):
        """This method is used to click sign-in button"""
        try:
            WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[ElementClickInterceptedException]).until(
                EC.element_to_be_clickable(self.sign_in_loc))
        except ElementClickInterceptedException:
            pass
        self.sign_in.click()
