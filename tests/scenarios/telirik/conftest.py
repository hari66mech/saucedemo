from pytest_bdd import given
from constants.telirik.constant import Constant


@given("The telerik demos page is displayed")
def get_login_page(driver):
    """This method is used get demo page url"""
    driver.get(Constant.DEMO_PAGE_URL)
