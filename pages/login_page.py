from base.rootm import get_element
from base.rootm import *
from utilities.util import read_data_from_excel


class LoginPage:

    def __init__(self, driver):
        sheet_name = "login_page"
        self.driver = driver

    def enter_email(self,  value):
        send_values(self.driver, "username_textbox", value)

    def enter_password(self, value):
        send_values(self.driver, "password_textbox", value)

    def click_on_connection_button(self):
        click_on_element(self.driver, "connection_button")

    def login_at_once(self, email="", password=""):
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_connection_button()

    # def validate_homepage(self):
    #