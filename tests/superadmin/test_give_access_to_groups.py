import time
import pytest

from pages.home_page import UsersAndGroupsPage
from pages.login_page import LoginPage


class TestGiveAccessToGroup:

    @pytest.fixture(autouse=True)
    def set_up(self, one_time_set_up):
        LoginPage(one_time_set_up).login_at_once("Admin", "admin")
        self.ug = UsersAndGroupsPage(one_time_set_up)

    def test_give_access_to_group(self):
        pass