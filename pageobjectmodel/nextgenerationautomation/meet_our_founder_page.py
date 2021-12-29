from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.nextgenerationautomation.constant import Constant


class MeetOurFounder:
    def __init__(self, driver):
        self.driver = driver

    meet_our_founder_loc = (By.XPATH, "//div[@id='comp-k3929r25']//span[text()='Meet Our Founder']")

    @property
    def meet_our_founder(self):
        return self.driver.find_element(*self.meet_our_founder_loc)

    def validate_meet_our_founder_title(self):
        """This method is used to validate meet_our_founder page title"""
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.meet_our_founder_loc))
        assert self.meet_our_founder.text == Constant.MEET_OUR_FOUNDER_TEXT
