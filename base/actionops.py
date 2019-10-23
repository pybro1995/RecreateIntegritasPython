from selenium.webdriver import ActionChains

from base.rootm import RootPage


class ActionOps:

    def __init__(self, driver):
        self.root_obj = RootPage(driver)
        self.act_obj = ActionChains(driver)

    def right_click(self, element):
        self.act_obj.context_click(self.root_obj.get_element(element))

    def double_click(self, element):
        self.act_obj.double_click(self.root_obj.get_element(element))
