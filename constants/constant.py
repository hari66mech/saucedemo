import os


class Constant:
    os.chdir("..")
    USER_HOME = "C:" + os.path.sep + "Users" + os.path.sep + "harikrishna.manokara" + os.path.sep + "PycharmProjects" + os.path.sep + "saucedemo" + os.path.sep
    DRIVER_PATH = USER_HOME + 'driver' + os.path.sep + 'chromedriver.exe'
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    HOME_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"
    CART_PAGE_TITLE = "Swag Labs"
    ERROR_TEXT = "Epic sadface: Sorry, this user has been locked out."
    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PASSWORD = "secret_sauce"
