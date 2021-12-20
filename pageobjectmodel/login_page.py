from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    user_name_loc = (By.XPATH, "//input[@id='loginusername']")
    password_loc = (By.XPATH, "//input[@id='loginpassword']")
    login_button_loc = (By.XPATH, "//button[normalize-space()='Log in']")

    @property
    def user_name(self):
        return self.driver.find_element(*self.user_name_loc)

    @property
    def user_password(self):
        return self.driver.find_element(*self.password_loc)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_loc)

    def login(self):
        "This method is used to login as a stored(credentials.txt) credentials"
        file = open("credentials.txt", "r")
        credentials = file.read().split(",")
        file.close()
        self.user_name.send_keys(credentials[0])
        self.user_password.send_keys(credentials[1])
        self.login_button.click()
