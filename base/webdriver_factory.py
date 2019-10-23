from selenium import webdriver


class WebDriverFactory:
    """Not used anymore"""
    def __init__(self, browser_name):
        self.browser = browser_name

    def open_browser(self):
        base_url = "http://192.168.92.128/dolibarr-3.3.1/htdocs/index.php"
        if self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(base_url)
        return driver
