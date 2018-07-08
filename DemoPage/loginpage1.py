from DemoActions1.WebDriverActions1 import *

class loginpage:
    def __init__(self):
        self._uid_TextBox = TextBox((By.NAME, "username"))
        self._password_TextBox = TextBox((By.NAME, "password"))
        self._login_Button = Button((By.ID, "loginBtn"))

    def login(self, userid, password):
        self._uid_TextBox.type(userid)
        self._password_TextBox.type(password)
        self._login_Button.click()


