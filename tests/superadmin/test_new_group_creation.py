import time
import pytest

from pages.home_page import UsersAndGroupsPage
from pages.login_page import LoginPage


class TestNewGroupCreation:

    @pytest.fixture(autouse=True)
    def set_up(self, one_time_set_up):
        LoginPage(one_time_set_up).login_at_once("Admin", "admin")
        self.ug = UsersAndGroupsPage(one_time_set_up)

    def test_new_group_creation(self):
        self.ug.click_on_users_and_groups_tab()
        self.ug.click_on_new_group()
        self.ug.new_group_page_enter_group_name("Sales")
        self.ug.new_group_page_enter_note(
            "This group is responsible for the sales of all the products"
        )
        self.ug.new_group_page_click_on_create_group_button()
        self.ug.click_on_groups()
        assert "Sales" in self.ug.groups_page_groups_table_elements()
        print("creation of group successful")
        time.sleep(5)

    def test_group_creation_with_same_name(self):
        pass

    def test_functional_name_textbox(self):
        # not required
        pass

    def test_functional_note_textarea(self):
        # not required
        pass
