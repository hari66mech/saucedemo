from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class Blog:
    def __init__(self, driver):
        self.driver = driver

    blog_loc = (By.XPATH, "//div[@id='comp-kbv0rogq1']//span[text()]")

    @property
    def blog(self):
        return self.driver.find_element(*self.blog_loc)

    def validate_blog_title(self):
        """This method is used to validate blog page title"""
        assert self.blog.text == Constant.BLOG_SECTION_TEXT
