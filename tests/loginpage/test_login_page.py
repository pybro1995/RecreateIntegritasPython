import pytest
import unittest
from base.webdriver_factory import WebDriverFactory
from pages.login_page import LoginPage


class TestLoginPage:

    @pytest.fixture(autouse=True)
    def classSetUp1(self, one_time_set_up):
        self.lp = LoginPage(one_time_set_up)

    def test_valid_login(self):
        self.lp.enter_email("Admin")
        self.lp.enter_password("admin")
        self.lp.click_on_connection_button()

    # @pytest.mark.parametrize("inv_email, inv_pwd", [("username1, pwd1"), ("usrnam2, pwd2)")])
    # def test_invalid_login(self, inv_email, inv_pwd):
    #     pass

