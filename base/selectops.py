from selenium.common.exceptions import NoSuchElementException

from base.rootm import RootPage
from selenium.webdriver.support.select import Select


class SelectOps:

    def __init__(self, driver, element, sheet_name):
        self.root_obj = RootPage(driver)
        self.sel_obj = Select(self.root_obj.get_element(element, sheet_name))

    def select_option(self, value_or_visibletext="", index_value=None, all=False):
        if index_value is not None:
            try:
                self.sel_obj.select_by_visible_text(value_or_visibletext)
            except NoSuchElementException:
                self.sel_obj.select_by_value(value_or_visibletext)
        else:
            self.sel_obj.select_by_index(index_value)

    def select_option_for_multiple_dropdown_type(self):
        pass

    def deselect_option(self):
        pass

    def deselect_for_multiple_dropdown_type(self):
        pass
