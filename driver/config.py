import os


class Driver:
    os.chdir("..")
    USER_HOME = "C:" + os.path.sep + "Users" + os.path.sep + "harikrishna.manokara" + os.path.sep + "PycharmProjects" + os.path.sep + "pytest_bdd_training" + os.path.sep
    DRIVER_PATH = USER_HOME + 'driver' + os.path.sep + 'chromedriver.exe'