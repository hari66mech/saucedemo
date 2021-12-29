from selenium.webdriver.common.by import By
from constants.nextgenerationautomation.constant import Constant


class VideoLibrary:
    def __init__(self, driver):
        self.driver = driver

    video_library_loc = (By.XPATH, "//span[@class='color_24']//span[contains(text(),'Video Library')]")

    @property
    def video_library(self):
        return self.driver.find_element(*self.video_library_loc)

    def validate_video_library_title(self):
        """This method is used to validate video library page title"""
        assert self.video_library.text == Constant.VIDEO_LIBRARY_TEXT
