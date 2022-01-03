from selenium.webdriver.common.by import By
from pageobjectmodel.phptravels.home_page import Home


class DataMisMatchError(Exception):
    def __init__(self, value):
        self.value = value


class Features(Home):
    def __init__(self, driver):
        Home.__init__(self, driver)

    __features_loc = (By.XPATH, "//div[@class='wow fadeIn col-md-4 col-sm-6 animated']//h3[text()]")

    @property
    def features_list(self):
        return self.driver.find_elements(*self.__features_loc)

    @property
    def total_features(self):
        return len(self.features_list)

    def get_features(self):
        """This method is used to get features from the features_page"""
        global web_features_list
        web_features_list = []
        self.driver.execute_script("window.scrollTo(0, 1200)")
        for feature in range(0, self.total_features):
            web_features_list.append(self.features_list[feature].text)

    def get_txt_file_features(self):
        """This method is used to get features from the features_list.text file"""
        global products_summery
        file = open("C:/Users/harikrishna.manokara/PycharmProjects/demo/features_list.text", "r")
        products_summery = file.read().split("\n")
        file.close()

    def validate_features(self):
        """This method is used to compare text file data with web features"""
        for product in range(0, self.total_features):
            if web_features_list[product] == products_summery[product]:
                continue
            else:
                raise DataMisMatchError("Given text file data and Web features have not match")
