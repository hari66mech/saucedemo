from selenium.webdriver.common.by import By
from constant.constant import Constant


class Collections:
    def __init__(self, driver):
        self.driver = driver

    course_loc = "//ul[@class='products__list']//li[{0}]//h3"
    course_list_loc = (By.XPATH, "//ul[@class='products__list']//li//h3")
    course_list_heading_loc = (By.XPATH, "//h3[@class='collections__heading']")

    @property
    def course_list_heading(self):
        return self.driver.find_element(*self.course_list_heading_loc)

    @property
    def course_list(self):
        return self.driver.find_elements(*self.course_list_loc)

    @property
    def total_courses(self):
        return len(self.course_list)

    def keep_courses(self):
        """This method is used to store the available courses in text file"""
        course_list = []
        for position in range(1, self.total_courses+1):
            course = self.course_loc.format(str(position))
            course_list.append(self.driver.find_element_by_xpath(course).text)
        file = open('courses.txt', 'w')
        for course_name in course_list:
            file.write(course_name+",")
        file.close()

    def validate_course_heading(self):
        """This method is used to validate the collection page"""
        assert self.course_list_heading.text == Constant.COURSES_LIST_HEADING
