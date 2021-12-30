from pytest_bdd import given
from constants.competethemes.constant import Constant


@given("The competethemes index page is displayed")
def get_login_page(driver):
    """This method is used get home page url"""
    driver.get(Constant.HOME_PAGE_URL)
    driver.switch_to.frame("iframe")
