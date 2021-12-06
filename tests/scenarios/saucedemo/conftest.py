from pytest_bdd import given
from constants.saucedemo.constant import Constant


@given("The saucedemo login page is displayed")
def get_login_page(driver):
    """This method is used get login page url"""
    driver.get(Constant.LOGIN_PAGE_URL)

