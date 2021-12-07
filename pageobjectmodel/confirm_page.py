from selenium.webdriver.common.by import By


class Confirm:
    def __init__(self, driver):
        self.driver = driver

    continue_button_loc = (By.XPATH, "//input[@name='newOrder']")
    confirm_button_loc = (By.XPATH, "//a[@class='Button']")
    total_bill_amount_loc = (By.XPATH, "//th[contains(text(),'Total:')]")
    thank_you_text_loc = (By.XPATH, "//li[normalize-space()='Thank you, your order has been submitted.']")

    @property
    def continue_button(self):
        """This property used to find the continue button XPath"""
        return self.driver.find_element(*self.continue_button_loc)

    @property
    def confirm_button(self):
        """This property used to find the confirm button XPath"""
        return self.driver.find_element(*self.confirm_button_loc)

    @property
    def thank_you_text(self):
        """This property used to find the thank you message text XPath"""
        return self.driver.find_element(*self.thank_you_text_loc)

    @property
    def total_bill_amount(self):
        """This property used to find the total bill XPath"""
        return self.driver.find_element(*self.total_bill_amount_loc)

    def click_continue_button(self):
        """This method is used to click the 'continue' button"""
        self.continue_button.click()

    def click_confirm_button(self):
        """This method is used to click the 'confirm' button"""
        self.confirm_button.click()

    def verify_confirmation_message(self):
        """This method is used to verify the confirmation message"""
        assert self.thank_you_text.is_displayed()

    def check_total_bill_amount(self):
        """This method is used to check the total bill amount is displayed in order page"""
        self.total_bill_amount.is_displayed()
