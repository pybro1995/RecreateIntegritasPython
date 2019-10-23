import pytest
# from base.webdriver_factory import WebDriverFactory
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", help="choose wither one: firefox/chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def one_time_set_up(browser):
    print("running one time setup")
    base_url = "http://192.168.92.128/dolibarr-3.3.1/htdocs/index.php"
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(base_url)
    # wdf_obj = WebDriverFactory(browser)
    # driver = wdf_obj.open_browser()
    yield driver
    driver.quit()
    print("running one time tear down")
