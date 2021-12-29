from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from constants.nextgenerationautomation.constant import Constant


class Home:
    def __init__(self, driver):
        self.driver = driver

    sign_up_button_loc = (By.XPATH, "//span[normalize-space()='Log In / SignUp']")
    why_choose_us_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnf1label']")
    meet_our_founder_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnfmoreContainer0label']")
    our_services_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnf2label']")
    overseas_hiring_model_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnfmoreContainer0label']")
    placements_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnf3label']")
    apply_overseas_qa_job_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnfmoreContainer0label']")
    apply_indian_opening_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnfmoreContainer1label']")
    video_library_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnf5label']")
    blog_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnf6label']")
    book_bank_heading_loc = (By.XPATH, "//p[@id='comp-j6gqwjnf4label']")
    our_key_services_title_loc = (By.XPATH, "//span[contains(text(),'Our Key Services')]")

    @property
    def sign_up_button(self):
        return self.driver.find_element(*self.sign_up_button_loc)

    @property
    def why_choose_us_heading(self):
        return self.driver.find_element(*self.why_choose_us_heading_loc)

    @property
    def meet_our_founder_heading(self):
        return self.driver.find_element(*self.meet_our_founder_heading_loc)

    @property
    def our_services_heading(self):
        return self.driver.find_element(*self.our_services_heading_loc)

    @property
    def overseas_hiring_model_heading(self):
        return self.driver.find_element(*self.overseas_hiring_model_heading_loc)

    @property
    def placements_heading(self):
        return self.driver.find_element(*self.placements_heading_loc)

    @property
    def apply_overseas_qa_job_heading(self):
        return self.driver.find_element(*self.apply_overseas_qa_job_heading_loc)

    @property
    def apply_indian_opening_heading(self):
        return self.driver.find_element(*self.apply_indian_opening_heading_loc)

    @property
    def book_bank_heading(self):
        return self.driver.find_element(*self.book_bank_heading_loc)

    @property
    def video_library_heading(self):
        return self.driver.find_element(*self.video_library_heading_loc)

    @property
    def blog_heading(self):
        return self.driver.find_element(*self.blog_heading_loc)

    @property
    def our_key_services_title(self):
        return self.driver.find_element(*self.our_key_services_title_loc)

    def click_meet_our_founder(self):
        """This method is used to click meet_our_founder heading"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.why_choose_us_heading_loc))
        ActionChains(self.driver).move_to_element(self.why_choose_us_heading).perform()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.meet_our_founder_heading_loc))
        ActionChains(self.driver).move_to_element(self.meet_our_founder_heading).click().perform()

    def validate_our_key_services_title(self):
        """This method is used to validate our_key_services title"""
        assert self.our_key_services_title.text == Constant.OUR_KEY_SERVICES_TEXT

    def click_overseas_hiring_model(self):
        """This method is used to click overseas_hiring_model heading"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.our_services_heading_loc))
        ActionChains(self.driver).move_to_element(self.our_services_heading).perform()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.overseas_hiring_model_heading_loc))
        ActionChains(self.driver).move_to_element(self.overseas_hiring_model_heading).click().perform()

    def click_apply_overseas_qa_job(self):
        """This method is used to click apply_overseas_qa_job heading"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.placements_heading_loc))
        ActionChains(self.driver).move_to_element(self.placements_heading).perform()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.apply_overseas_qa_job_heading_loc))
        ActionChains(self.driver).move_to_element(self.apply_overseas_qa_job_heading).click().perform()

    def click_apply_india_opening(self):
        """This method is used to click apply_india_opening heading"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.placements_heading_loc))
        ActionChains(self.driver).move_to_element(self.placements_heading).perform()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.apply_indian_opening_heading_loc))
        ActionChains(self.driver).move_to_element(self.apply_indian_opening_heading).click().perform()
