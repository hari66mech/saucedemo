from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    user_name_loc = (By.XPATH, "//input[@name='username']")
    password_loc = (By.XPATH, "//input[@name='password']")
    login_loc = (By.XPATH, "//input[@name='signon']")
    register_now_loc = (By.XPATH, "//a[normalize-space()='Register Now!']")

    @property
    def user_name(self):
        """This property used to find the user name XPath in signin page"""
        return self.driver.find_element(*self.user_name_loc)

    @property
    def password(self):
        """This property used to find the password XPath in signin page"""
        return self.driver.find_element(*self.password_loc)

    @property
    def login(self):
        """This property used to find the login button XPath in signin page"""
        return self.driver.find_element(*self.login_loc)

    @property
    def register_now(self):
        """This property used to find the 'register now' XPath"""
        return self.driver.find_element(*self.register_now_loc)

    def click_register_now(self):
        """This method used to click the 'register now'"""
        self.register_now.click()

    def log_in(self, credential):
        """This method is used to login with valid credential"""
        self.user_name.clear()
        self.user_name.send_keys(credential[0])
        self.password.clear()
        self.password.send_keys(credential[1])
        self.login.click()
