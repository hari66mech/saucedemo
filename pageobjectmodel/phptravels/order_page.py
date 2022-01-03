import random
from selenium.webdriver.common.by import By
from pageobjectmodel.phptravels.home_page import Home


class PlanMisMatchError(Exception):
    def __init__(self, value):
        self.value = value


class Order(Home):
    def __init__(self, driver):
        Home.__init__(self, driver)

    __platforms_loc = (By.XPATH, "//div[@class='col-md-9']//div[@class='row'][1]/div//h4")
    __features_loc = (By.XPATH, "//div[@class='col-md-9']//div[@class='row'][2]/div//h4")
    __modules_loc = (By.XPATH, "//div[@class='col-md-9']//div[@class='row'][3]/div//h4")
    __suppliers_loc = (By.XPATH, "//div[@class='col-md-9']//div[@class='row'][4]/div//h4")
    __payment_gateways_loc = (By.XPATH, "//div[@class='col-md-9']//div[@class='row'][5]/div//h4")
    __extras_loc = (By.XPATH, "//div[@class='col-md-9']//div[@class='row'][6]/div//h4")
    __buy_now_button_loc = (By.XPATH, "//button[@id='order_button']")
    __platform_loc = "//div[@class='col-md-9']//div[@class='row'][1]/div[{0}]//h4"
    __feature_loc = "//div[@class='col-md-9']//div[@class='row'][2]/div[{0}]//h4"
    __module_loc = "//div[@class='col-md-9']//div[@class='row'][3]/div[{0}]//h4"
    __supplier_loc = "//div[@class='col-md-9']//div[@class='row'][4]/div[{0}]//h4"
    __payment_gateway_loc = "//div[@class='col-md-9']//div[@class='row'][5]/div[{0}]//h4"
    __extra_loc = "//div[@class='col-md-9']//div[@class='row'][6]/div[{0}]//h4"

    @property
    def platforms(self):
        return self.driver.find_elements(*self.__platforms_loc)

    @property
    def total_platforms(self):
        return len(self.platforms)

    @property
    def features(self):
        return self.driver.find_elements(*self.__features_loc)

    @property
    def total_features(self):
        return len(self.features)

    @property
    def modules(self):
        return self.driver.find_elements(*self.__modules_loc)

    @property
    def total_modules(self):
        return len(self.modules)

    @property
    def suppliers(self):
        return self.driver.find_elements(*self.__suppliers_loc)

    @property
    def total_suppliers(self):
        return len(self.suppliers)

    @property
    def payment_gateways(self):
        return self.driver.find_elements(*self.__payment_gateways_loc)

    @property
    def total_payment_gateways(self):
        return len(self.payment_gateways)

    @property
    def extras(self):
        return self.driver.find_elements(*self.__extras_loc)

    @property
    def total_extras(self):
        return len(self.extras)

    @property
    def buy_now_button(self):
        return self.driver.find_element(*self.__buy_now_button_loc)

    def select_plan(self, plan):
        """This method is used to select the plan randomly"""
        global total_plans, particular_plan_loc
        if plan == "platform":
            total_plans = self.total_platforms
            particular_plan_loc = self.__platform_loc
        elif plan == "feature":
            total_plans = self.total_features
            particular_plan_loc = self.__feature_loc
        elif plan == "module":
            total_plans = self.total_modules
            particular_plan_loc = self.__module_loc
        elif plan == "supplier":
            total_plans = self.total_suppliers
            particular_plan_loc = self.__supplier_loc
        elif plan == "payment_gateway":
            total_plans = self.total_payment_gateways
            particular_plan_loc = self.__payment_gateway_loc
        elif plan == "extra":
            total_plans = self.total_extras
            particular_plan_loc = self.__extra_loc
        else:
            raise PlanMisMatchError("Plan heading is Wrong")
        particular_plan = random.randint(1, total_plans)
        self.driver.find_element_by_xpath(particular_plan_loc.format(str(particular_plan))).click()
