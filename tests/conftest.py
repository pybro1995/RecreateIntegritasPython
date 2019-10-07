import pytest
from base.webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", help="choose wither one: firefox/chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def one_time_set_up(browser):
    print("running one time setup")
    wdf_obj = WebDriverFactory(browser)
    driver = wdf_obj.open_browser()
    yield driver
    driver.quit()
    print("running one time tear down")
