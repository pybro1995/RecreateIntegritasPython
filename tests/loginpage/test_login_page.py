import time
import pytest
from pages.login_page import LoginPage


class TestLoginPage:

    @pytest.fixture(autouse=True)
    def set_up(self, one_time_set_up):
        self.lp = LoginPage(one_time_set_up)

    def test_valid_login(self):
        self.lp.enter_email("Admin")
        self.lp.enter_password("admin")
        self.lp.click_on_connection_button()
        self.lp.verify_successful_login()
        time.sleep(5)

    @pytest.mark.parametrize("usrnme,pwd", [("Admin", "admin123"), ("_Admin", "admin")])
    def test_invalid_login(self, usrnme, pwd):
        print(usrnme)
        print(pwd)
        self.lp.login_at_once(usrnme, pwd)
        self.lp.verify_invalid_login()
        time.sleep(5)
