import os


class Config:
    os.chdir("..")
    USER_HOME = "C:" + os.path.sep + "Users" + os.path.sep + "harikrishna.manokara" + os.path.sep + "PycharmProjects" + os.path.sep + "demo" + os.path.sep
    CHROME_DRIVER_PATH = USER_HOME + 'driver' + os.path.sep + 'chromedriver.exe'
    FIREFOX_DRIVER_PATH = USER_HOME + 'driver' + os.path.sep + 'geckodriver.exe'
    MS_EDGE_DRIVER_PATH = USER_HOME + 'driver' + os.path.sep + 'msedgedriver.exe'
    # chrome, firefox, msedge
    DRIVER = "chrome"
