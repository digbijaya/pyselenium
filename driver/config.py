from selenium import webdriver
import json

# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.proxy.type",0)
# driver=webdriver.Firefox(profile)
# .set_preference("network.proxy.type", 1)
# driver = webdriver.Firefox()
# driver.get("http://10.157.251.146:8078/auth/login/")
# driver.quit()


class Config:

    def __init__(self, path="config/env.json"):
        config_data = json.load(open(path))#
        self.url = config_data["ooo_env_horizon_url"]
        self.userid = config_data["adminuser"]
        self.password = config_data["password"]
        self.browser = config_data["browser"]

driver = None

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
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type",0)
            global driver
            driver = webdriver.Firefox(profile)


        elif str(self.browser).lower() == "chrome":
            pass


        ''' Before starting your test development. the below method need to be overided to setup all the pages where 
        tests are going to navigate through '''

        def pageSetup(self):
            raise NotImplementedError("Please Implement this method and create OBJECTS of all the pages")

'''
if __name__ == "__main__":

    d = Driver()
    d.initialise()
    driver.get("http://10.157.251.146:8078/auth/login/")
    driver.implicitly_wait(5)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("workshop")
    driver.find_element_by_id("loginBtn").click()
    import time
    time.sleep(5)
    driver.quit()
'''


