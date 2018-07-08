from selenium import webdriver
import json
from selenium.webdriver.firefox.options import Options
import os

class Config:

    def __init__(self, path="config/env.json"):
        config_data = json.load(open(path))#
        self.url = config_data["ooo_env_horizon_url"]
        self.userid = config_data["adminuser"]
        self.password = config_data["password"]
        self.browser = config_data["browser"]



class Driver(Config):


    def __init__(self):
        self.driver = None
        self.conf = Config()
        self.url = self.conf.url
        self.userid = self.conf.userid
        self.browser = self.conf.browser
        print(self.url)
        print(self.userid)
        print(self.browser)

    # to initial lize a driver object and lunch the browse(firefox/chrome)
    def initialise(self):

        if str(self.browser).lower() == "firefox":
            options = Options()
            #options.add_argument("--headless")
            driverPath=os.getcwd() + "/geckodriver"
            print(driverPath)
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type",0)
            global driver
            driver = webdriver.Firefox(firefox_options=options,firefox_profile=profile,executable_path=driverPath)
            driver.get(self.url)
            driver.implicitly_wait(10)
            return driver



        elif str(self.browser).lower() == "chrome":
            pass


        ''' Before starting your test development. the below method need to be overided to setup all the pages where 
        tests are going to navigate through '''

        def pageSetup(self):
            raise NotImplementedError("Please Implement this method and create OBJECTS of all the pages")
