import pytest


@pytest.mark.usefixtures("one_time_set_up")
class TestLogin:

    def test_valid_login(self):
        print("testing for valid login scenarios")

    def test_invalid_login(self):
        print("testing for invalid login")
