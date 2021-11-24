import os


class Constant:
    os.chdir("..")
    USER_HOME = "C:" + os.path.sep + "Users" + os.path.sep + "harikrishna.manokara" + os.path.sep + "PycharmProjects" + os.path.sep + "saucedemo" + os.path.sep
    DRIVER_PATH = USER_HOME + 'driver' + os.path.sep + 'chromedriver.exe'
    HOME_PAGE_URL = "https://www.saucedemo.com/"
    CARD_PAGE_URL = "https://www.saucedemo.com/cart.html"
    CARD_PAGE_TITLE = "Swag Labs"

