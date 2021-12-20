from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sign_up:
    def __init__(self, driver):
        self.driver = driver

    user_name_loc = (By.XPATH, "//input[@id='sign-username']")
    password_loc = (By.XPATH, "//input[@id='sign-password']")
    sign_up_button_loc = (By.XPATH, "//button[normalize-space()='Sign up']")

    @property
    def user_name(self):
        return self.driver.find_element(*self.user_name_loc)

    @property
    def user_password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def sign_up_button(self):
        return self.driver.find_element(*self.sign_up_button_loc)

    def keep_credentials(self, credential):
        """This method is used to write the credentials in .txt file"""
        file = open('credentials.txt', 'w')
        file.write(credential["user_name"] + "," + credential["user_password"])
        file.close()

    def registration(self, credential):
        "This method is used to enter the user data and accept the alert message"
        self.user_name.send_keys(credential["user_name"])
        self.user_password.send_keys(credential["user_password"])
        self.sign_up_button.click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        return credential
