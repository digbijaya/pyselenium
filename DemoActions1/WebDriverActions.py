from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type",0)
mydriver = webdriver.Firefox(profile)




mydriver.get("http://10.157.251.146:8078/auth/login/")
mydriver.implicitly_wait(10)

class findEle:
    def __init__(self, loc):
        self.loc = loc
    def waitAndFindElement(self):
        print("demo")
        try:
            self.element = WebDriverWait(mydriver, 10).until(
                EC.presence_of_element_located((self.loc))
            )

        except NoSuchElementException:
            print("element not found")
            import time
            time.sleep(2)
    # def type(self):
    #     self.element.send_keys("dj")


class TextBox(findEle):
    def __init__(self,loc):
        findEle.__init__(self,loc)
    def type(self, text):
        self.waitAndFindElement()
        self.element.send_keys(text)

class Button(findEle):
    def __init__(self,loc):
        findEle.__init__(self,loc)
    def click(self):
        self.waitAndFindElement()
        self.element.click()

