import time
import pytest

from pages.home_page import UsersAndGroupsPage
from pages.login_page import LoginPage


class TestUserCreation:

    @pytest.fixture(autouse=True)
    def set_up(self, one_time_set_up):
        LoginPage(one_time_set_up).login_at_once("Admin", "admin")
        self.ug = UsersAndGroupsPage(one_time_set_up)

    def test_new_user_creation(self):
        self.ug.click_on_users_and_groups_tab()
        self.ug.click_on_new_user()
        self.ug.new_user_page_enter_last_name("Kumar")
        self.ug.new_user_page_enter_first_name("Pavan$")
        self.ug.new_user_page_enter_post_textbox("sales executive")
        self.ug.new_user_page_enter_login_textbox("pavan102")
        self.ug.new_user_page_enter_prof_phone("9005641234")
        self.ug.new_user_page_enter_mobile_number("45654475675")
        self.ug.new_user_page_enter_fax("43-435342")
        self.ug.new_user_page_enter_email("something@something.com")
        self.ug.new_user_page_enter_signature_textarea("signed")
        self.ug.new_group_page_enter_note("not note note1 note2")
        self.ug.new_user_page_click_on_create_user_button()
        self.ug.click_on_users()
        assert "pavan102" in self.ug.users_page_users_table_elements()
        time.sleep(5)

    def test_functional_last_name_textbox(self):
        pass

    def test_functional_first_name_textbox(self):
        pass

    def test_functional_post_textbox(self):
        pass
