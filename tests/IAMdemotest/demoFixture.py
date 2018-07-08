import time
import pytest
from driver.democonfig import Driver
from selenium import webdriver



# In below way you can create a global variable for whole pytest session. they call it as pytest hook
def pytest_namespace():
    return {'test_driver': 0}
#can use scope="session"

@pytest.fixture(autouse=True,scope="module")
def setupAndTeardown():

    pytest.test_driver = Driver().initialise()
    time.sleep(5)

    yield setupAndTeardown
    pytest.test_driver.quit()
    pytest.test_driver = None
    # test_driver.quit()


