
import pytest
from tests.IAMdemotest.demoFixture import *
from selenium import webdriver



@pytest.mark.usefixture("setupAndTeardown")
class Test_hirizon_login:
    from DemoPage.loginpage1 import loginpage
    loginpage = loginpage()

    @pytest.mark.dependency()
    def test_cloud_admin_role(self):
        Test_hirizon_login.loginpage.login("admin","workshop")
        assert True

    @pytest.mark.dependency(depends=["Test_hirizon_login::test_cloud_admin_role"])
    def test_cloud_admin_role1(self):
        # Test_hirizon_login.loginpage.login("admin","workshop")
        assert True
